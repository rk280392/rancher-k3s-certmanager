### deploy argocd

$ kubectl create ns argocd

$ kubectl apply -f externalSecretDexConfig.yaml

$ helm upgrade --install argo -n argo argo/argo-cd --values argocd/values.yaml

$ kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d | xargs

https://github.com/argoproj/argo-cd/blob/master/docs/faq.md

### Enable Auth0 with github

1 - Create github oAuth app and get clientId and secret. ( Hint: settings --> Developer options --> oAuth)

2 - Create a secret named `argocd-secret` in `argocd` namespace.

3 - Include the client and secret id variable from the secret to argocd-cm config-map. (https://argo-cd.readthedocs.io/en/stable/operator-manual/user-management/)

4 - Update the argocd-rbac-cm with new role and policies for this github user. (https://argo-cd.readthedocs.io/en/stable/operator-manual/rbac/)
