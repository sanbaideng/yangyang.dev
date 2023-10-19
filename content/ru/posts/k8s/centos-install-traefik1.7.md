---
title: "[Cloud Native] Установка Traefik1.7 на CentOS"
date: 2023-02-20T14:01:39+08:00
черновик: false
tags: ["k8s"]
---
# Установка Traefik1.7 на CentOS
с сайта с документацией по Traefik:
kubectl apply -f https://raw.githubusercontent.com/containous/traefik/v1.7/examples/k8s/traefik-rbac.yaml
kubectl apply -f https://raw.githubusercontent.com/containous/traefik/v1.7/examples/k8s/traefik-ds.yaml

подробная информация о файле:

---


```
---
тип: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1beta1
метаданные:
имя: traefik-ingress-controller
правила:
- apiGroups:
- ""
ресурсы:
- сервисы
- конечные точки
- секреты
глаголы:
- получить
- список
- наблюдать
- apiGroups:
- расширения
ресурсы:
- ингрессии
глаголы:
- получить
- перечислять
- наблюдать
- apiGroups:
- расширения
ресурсы:
- ingresses/status
глаголы:
- update
---
тип: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1beta1
метаданные:
имя: traefik-ingress-controller
roleRef:
apiGroup: rbac.authorization.k8s.io
тип: ClusterRole
имя: traefik-ingress-controller
субъекты:
- вид: ServiceAccount
имя: traefik-ingress-controller
пространство имен: kube-system


```

```

---
apiVersion: v1
тип: ServiceAccount
метаданные:
имя: traefik-ingress-controller
пространство имен: kube-system
---
kind: DaemonSet
apiVersion: apps/v1
метаданные:
имя: traefik-ingress-controller
пространство имен: kube-system
метки:
k8s-app: traefik-ingress-lb
spec:
selector:
matchLabels:
k8s-app: traefik-ingress-lb
имя: traefik-ingress-lb
шаблон:
metadata:
метки:
k8s-app: traefik-ingress-lb
имя: traefik-ingress-lb
spec:
serviceAccountName: traefik-ingress-controller
terminationGracePeriodSeconds: 60
контейнеры:
- image: traefik:v1.7
имя: traefik-ingress-lb
порты:
- имя: http
containerPort: 80
hostPort: 80
- имя: admin
containerPort: 8080
hostPort: 8081
securityContext:
capabilities:
drop:
- ALL
добавить:
- NET_BIND_SERVICE
args:
--api
--kubernetes
--logLevel=INFO
---
тип: Сервис
apiVersion: v1
метаданные:
имя: traefik-ingress-service
пространство имен: kube-system
spec:
селектор:
k8s-app: traefik-ingress-lb
порты:
- протокол: TCP
порт: 80
имя: web
- протокол: TCP
порт: 8080
имя: admin

```

