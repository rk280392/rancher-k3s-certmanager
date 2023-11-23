## Secure Thanos receive endpoint with proxy config

1. Use the htpasswd utility to create a file containing username and password pairs. This file will be used for basic authentication.

`htpasswd -cB /path/to/htpasswdfile username`

2. Configure Traefik Middleware for Basic Authentication and use the middleware in ingressroute config 

`kubectl apply -f ../../../ingresses/thanos-ingress.yaml`

