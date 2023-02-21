---
title: "[Cloud Native] Install Weavenet on CentOS"
date: 2023-02-21T10:16:19+08:00
draft: true
---
kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"
