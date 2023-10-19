--- 
title: "[Cloud Native] Install Helm2.x on CentOS" 
date: 2023-02-20T14:04:44+08:00
tags: ["k8s"] 
--- 
# Установка Helm2.x на CentOS

Что такое Helm?

    Helm - это инструмент, помогающий определять, устанавливать и обновлять приложения, работающие на Kubernetes. 
    По своей сути Helm - это шаблонизатор, создающий манифесты Kubernetes. Но в отличие от него Helm может также обновлять и масштабировать приложения.

Почему это важно?

    Эта возможность особенно важна при работе с большими и сложными приложениями; приложение может содержать десятки объектов Kubernetes, которые необходимо настраивать и изменять при обновлении. Это также актуально при многократном развертывании одного и того же приложения. Использование метода find-and-replace в нескольких манифестах - это рецепт катастрофы. Helm может сделать этот процесс простым и повторяемым.
    
    Именно поэтому экземпляр графика, запущенный на кластере Kubernetes, называется релизом. Если вам нужны три разные установки веб-сервера, то каждая из них - это отдельный релиз. В документации Helm релизы рассматриваются как одно из трех важных понятий:

Как работает Helm?

    Helm комбинирует шаблоны и значения по умолчанию в диаграмме с предоставленными вами значениями, а также с информацией из вашего кластера для развертывания и обновления приложений. Вы можете использовать графики непосредственно из репозиториев, загруженные или созданные самостоятельно. Helm использует шаблонизатор Go, поэтому если вы знакомы с ним, то поймете, как работают диаграммы.

    Начиная с Helm 3, все необходимые данные хранятся локально в конфигурации вашего клиента Helm или в кластере, где установлены релизы. В предыдущих версиях Helm для этого требовался компонент tiller, установленный на кластере. Теперь этот компонент не нужен, поэтому Helm стал проще в установке и использовании.

Как установить helm2 в CentOS?

``` mkdir -pv helm && cd helm wget https://storage.googleapis.com/kubernetes-helm/helm-v2.9.1-linux-amd64.tar.gz tar xf helm-v2.9.1-linux-amd64.tar.gz sudo mv linux-amd64/helm /usr/local/sbin rm -rf linux-amd64 helm init --upgrade -i ghcr.io/helm/tiller:v2.16.7 --stable-repo-url https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts wget https://raw.githubusercontent.com/Azure/helm-charts/master/docs/prerequisities/helm-rbac-config.yaml ``` ``` helm init --upgrade -i reg.cecii.cn/pub/tiller:v2.16.7 --stable-repo-url https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts helm init --upgrade -i reg.cecii.cn/pub/tiller:v2.16.7 kubectl create -f helm-rbac-config.yaml kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount": "tiller"}}}}' kubectl create serviceaccount --namespace kube-system tiller kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller

kubectl create clusterrolebinding add-on-cluster-admin --clusterrole=cluster-admin --serviceaccount=kube-system:default

#在每个节点运行 echo "###warn:yum install -y socat at every node" yum install -y socat ```

helm 删除某个命名空间的所有应用

`` helm delete --purge $(helm list --all --namespace 203 |awk '{if (NR>1){print $1}}') ```

按日期排序

`` helm list -d

kubectl get pod --sort-by='{.status.startTime}' -n 203 ```