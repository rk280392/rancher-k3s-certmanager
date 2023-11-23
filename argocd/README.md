### Deploy ArgoCD

$ kubectl create ns argo

$ kubectl apply -f externalSecretDexConfig.yaml

$ helm upgrade --install argo -n argo argo/argo-cd --values argocd/values.yaml

$ kubectl -n argo get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d | xargs

https://github.com/argoproj/argo-cd/blob/master/docs/faq.md

### Enable Auth0 with github

1 - Create github oAuth app and get clientId and secret. ( Hint: settings --> Developer options --> oAuth)

2 - Create a secret named `argocd-secret` in `argo` namespace.

3 - Include the client and secret id variable from the secret to argocd-cm config-map. (https://argo-cd.readthedocs.io/en/stable/operator-manual/user-management/)

4 - Update the argocd-rbac-cm with new role and policies for this github user. (https://argo-cd.readthedocs.io/en/stable/operator-manual/rbac/)


For multi Rancher cluster see this : https://gist.github.com/janeczku/b16154194f7f03f772645303af8e9f80

kubectl apply -f rancher-master/argocd-multi-rancher-cluster-secret.yaml
