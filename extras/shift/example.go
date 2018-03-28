package main

import (
	"github.com/openshift/origin/pkg/cmd/util/clientcmd"
	PI "github.com/openshift/origin/pkg/project/generated/internalclientset/typed/project/internalversion"
	UI "github.com/openshift/origin/pkg/user/generated/internalclientset/typed/user/internalversion"
	"github.com/spf13/pflag"
	v1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"log"
)

func main() {
	flags := pflag.FlagSet{}
	f := clientcmd.New(&flags)

	p, _ := f.OpenshiftInternalProjectClient()
	pc := PI.New(p.Project().RESTClient())
	pl, _ := pc.Projects().List(v1.ListOptions{})
	for _, i := range pl.Items {
		log.Print(i.Name)
	}

	log.Println("----------")

	u, _ := f.OpenshiftInternalUserClient()
	uc := UI.New(u.User().RESTClient())
	ul, _ := uc.Users().List(v1.ListOptions{})
	for _, i := range ul.Items {
		log.Print(i.Name)
	}
}
