## Rancher Local cluster Deployment

Install k3s
- curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.26.7+k3s1 INSTALL_K3S_EXEC="server" sh -

SSH to the NODE and copy the k3s.yaml to interact with the cluster
- cat /etc/rancher/k3s/k3s.yaml 

Paste the k3s.yaml in your local system and export as KUBECONFIG.

Steps:

- kubectl create ns cattle-system
- helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --version v1.13.1 --set installCRDs=true
- helm install rancher rancher-latest/rancher -n cattle-system -f rancher-helm-values.yaml --create-namespace
- kubectl -n cattle-system get certificaterequest
- kubectl -n cattle-system get issuer
- kubectl -n cattle-system get certificate
- kubectl -n cattle-system get order
- kubectl -n cattle-system get secret
- kubectl -n cattle-system get pods
- cd ../
- kubectl get secret --namespace cattle-system bootstrap-secret -o go-template='{{.data.bootstrapPassword|base64decode}}'
- echo https://rancher.rajesh-kumar.in/dashboard/?setup=$(kubectl get secret --namespace cattle-system bootstrap-secret -o go-template='{{.data.bootstrapPassword|base64decode}}')
- kubectl apply -f ingresses/rancher-ingress.yaml
- kubectl -n cert-manager get secret rancher-tls-cert -o yaml | yq 'del(.metadata.creationTimestamp, .metadata.resourceVersion, .metadata.selfLink, .metadata.uid, .metadata.managedFields, .metadata.namespace, .metadata.annotations)' | kubectl apply -n cattle-system -f -
- helm repo add hashicorp https://helm.releases.hashicorp.com
- helm install vault hashicorp/vault
- kubectl exec -it vault-0 vault operator init
- kubectl exec -it vault-0 -- vault login $INITIAL_ROOT_TOKEN
- kubectl apply -f vaults/vaultTokenSecret.yaml
- kubectl apply -f ingresses/vault-ingress.yaml
- kubectl apply -f clusterSecretStore.yaml

Deploy Argo in master and add practice cluster to deploy apps in practice cluster. See argocd/README.

To add monitoring:

- Deploy monitoring through UI 
	- Disable grafana
	- Add remoteWrite configs
	- Add additionalScrapeConfig to scrape argo
- create Thanos receive secret to push prometheus scrapes to central Thanos server. See home-cluster/prom-thanos-receive-demo.yaml.
