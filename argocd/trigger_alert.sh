#!/bin/bash


# port-forward alertmanager service first

url='http://localhost:9093/api/v1/alerts'
echo "Firing up alert"
curl -XPOST $url -d '[{"status": "firing","labels": {"alertname": "personal-setup"}}]'
echo ""

echo "press enter to resolve alert"
read

echo "sending resolve"
curl -XPOST $url -d '[{"status": "resolved","labels": {"alertname": "personal-setup"},"endsAt": "2020-07-23T01:05:38+00:00"}]'
echo ""

