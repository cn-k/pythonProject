#!/bin/bash
sshpass -p 'server' scp -r /Users/cenkakdeniz/Desktop/projects/python/pythonProject root@172.12.2.63:/root/sadedegel
sshpass -p 'server' ssh root@172.12.2.63 docker build -t registry.172.12.2.63.nip.io/docker-metrics:latest /root/sadedegel/pythonProject
kubectl delete -f /Users/cenkakdeniz/Desktop/projects/python/pythonProject/test_deployment.yaml
sshpass -p 'server' ssh root@172.12.2.63 docker push registry.172.12.2.63.nip.io/docker-metrics:latest
kubectl apply -f /Users/cenkakdeniz/Desktop/projects/python/pythonProject/test_deployment.yaml