package keystonetoken

import (
	"os"
	"fmt"
	"net/http"
	"runtime/debug"

	"github.com/golang/glog"
	"github.com/rackspace/gophercloud"
	"github.com/rackspace/gophercloud/openstack"

	authapi "github.com/openshift/origin/pkg/auth/api"
	"github.com/openshift/origin/pkg/auth/authenticator"
	utilruntime "k8s.io/apimachinery/pkg/util/runtime"
	"k8s.io/apiserver/pkg/authentication/user"

	tokens2 "github.com/rackspace/gophercloud/openstack/identity/v2/tokens"
)

// keystoneTokenAuthenticator uses OpenStack keystone to authenticate a user by password
type keystoneTokenAuthenticator struct {
	providerName   string
	url            string
	client         *http.Client
	identityMapper authapi.UserIdentityMapper
}

func v2auth(client *gophercloud.ProviderClient, endpoint string, options gophercloud.AuthOptions) (*tokens2.User, error) {
	v2Client := openstack.NewIdentityV2(client)
	if endpoint != "" {
		v2Client.Endpoint = endpoint
	}

	result := tokens2.GetResult{tokens2.Create(v2Client, tokens2.AuthOptions{AuthOptions: options})}

	username, err := result.ExtractUser()
	if err != nil {
		return nil, err
	}

	return username, nil
}

// New creates a new password authenticator that uses OpenStack keystone to authenticate a user by password
// A custom transport can be provided (typically to customize TLS options like trusted roots or present a client certificate).
// If no transport is provided, http.DefaultTransport is used
func New(providerName string, url string, transport http.RoundTripper, identityMapper authapi.UserIdentityMapper) authenticator.Password {
	if transport == nil {
		transport = http.DefaultTransport
	}
	client := &http.Client{Transport: transport}
	return &keystoneTokenAuthenticator{providerName, url, client,identityMapper}
}

// AuthenticatePassword approves any login attempt which is successfully validated with Keystone
func (a keystoneTokenAuthenticator) AuthenticatePassword(username, token string) (user.Info, bool, error) {
	defer func() {
		if e := recover(); e != nil {
			utilruntime.HandleError(fmt.Errorf("Recovered panic: %v, %s", e, debug.Stack()))
		}
	}()

	// if token is missing, fail authentication immediately
	if len(token) == 0 {
		return nil, false, nil
	}

	if len(a.url) == 0 {
		// 没有配置则从环境变量里取
		a.url = os.Getenv("OS_AUTH_URL")
		if len(a.url) == 0 {
			return nil, false, nil
		}
	}

	opts := gophercloud.AuthOptions{
		IdentityEndpoint: a.url,
		TokenID: token,
	}

	// Calling NewClient/Authenticate manually rather than simply calling AuthenticatedClient
	// in order to pass in a transport object that supports SSL
	client, err := openstack.NewClient(opts.IdentityEndpoint)
	if err != nil {
		glog.Warningf("Failed: Initializing openstack authentication client: %v", err)
		return nil, false, err
	}

	client.HTTPClient = *a.client
	info, err := v2auth(client, "", opts)
	if err != nil {
		if responseErr, ok := err.(*gophercloud.UnexpectedResponseCodeError); ok {
			if responseErr.Actual == 401 {
				return nil, false, nil
			}
		}
		glog.Warningf("Failed: Calling openstack AuthenticateV3: %v", err)
		return nil, false, err
	}

	identity := authapi.NewDefaultUserIdentityInfo(a.providerName, info.Name)
	user, err := a.identityMapper.UserFor(identity)
	if err != nil {
		glog.Warningf("Error creating or updating mapping for: %#v due to %v", identity, err)
		return nil, false, err
	}
	glog.V(4).Infof("Got userIdentityMapping: %#v", user)

	return user, true, nil
}
