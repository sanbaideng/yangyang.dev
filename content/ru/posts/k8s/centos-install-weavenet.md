---
title: "[Cloud Native] Установка Weavenet на CentOS"
date: 2023-02-21T10:16:19+08:00
tags: ["k8s"]
---
# Установка Weavenet на CentOS
```
kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"
```