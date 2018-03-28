package keystonetoken

import (
	"fmt"
	"net/http"
	"github.com/openshift/origin/pkg/auth/authenticator/password/keystonetoken"

	"github.com/openshift/origin/pkg/auth/api"
	"k8s.io/apiserver/pkg/authentication/user"
	"strings"
)

const token = "3b04c178a71d450187be1237c7f0c40a"
const auth_url = "http://172.16.92.30:5000"

type TestUserIdentityMapper struct{}

func (m *TestUserIdentityMapper) UserFor(identityInfo api.UserIdentityInfo) (user.Info, error) {
	return &user.DefaultInfo{Name: identityInfo.GetProviderUserName()}, nil
}

func main() {
	cred := "http://172.16.92.30:5000/v2.0:4c1313665a0f4fa9a4092ce47454bb6c"
	idx := strings.LastIndex(cred, ":")
	fmt.Println(cred[:idx], cred[idx+1:])

	cli := keystonetoken.New("t2cloud", "", http.DefaultTransport, &TestUserIdentityMapper{})
	fmt.Println(cli)

	fmt.Println(cli.AuthenticatePassword(auth_url, token))
}
