---
title: "[Cloud Native] Install Helm2.x on CentOS"
date: 2023-02-20T14:04:44+08:00
draft: false
tags: ["k8s"]
---
What Is Helm?

    Helm is a tool to help you define, install, and upgrade applications running on Kubernetes. 
    At its most basic, Helm is a templating engine that creates Kubernetes manifests. What makes Helm more than that is it can upgrade and scale applications as well.

Why Is It Important?

    This capability really stands out when you have a large, complex application; your app may contain dozens of Kubernetes objects that need to be configured and changed during upgrades. It also applies if you’re deploying the same app multiple times. Using find-and-replace in multiple manifests is a recipe for disaster. Helm can make the process easy and repeatable.
    
    It’s why an instance of a chart running on a Kubernetes cluster is called a release. If you need three different installs of a web server, each one is its own release. The Helm docs includes releases as one of three important concepts:

How Does Helm Work?

    Helm combines the templates and default values in a chart with values you’ve supplied, along with information from your cluster to deploy and update applications. You can use charts directly from repos, charts you’ve downloaded, or charts you’ve created yourself. Helm uses the Go templating engine, so if you’re familiar with that, you’ll understand how the charts work.

    As of Helm 3, all of the necessary data is stored locally in your Helm client config or in the cluster where the releases are installed. In previous versions of Helm, it required a component called tiller installed on the cluster. That component is no longer needed so Helm is now easier to install and use.

How to install helm2 in CentOS?

```
mkdir -pv helm && cd helm
wget https://storage.googleapis.com/kubernetes-helm/helm-v2.9.1-linux-amd64.tar.gz
tar xf helm-v2.9.1-linux-amd64.tar.gz
sudo mv linux-amd64/helm /usr/local/sbin
rm -rf linux-amd64
helm init --upgrade -i ghcr.io/helm/tiller:v2.16.7 --stable-repo-url https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
wget https://raw.githubusercontent.com/Azure/helm-charts/master/docs/prerequisities/helm-rbac-config.yaml
```
```
helm init --upgrade -i reg.cecii.cn/pub/tiller:v2.16.7 --stable-repo-url https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
helm init --upgrade -i reg.cecii.cn/pub/tiller:v2.16.7
kubectl create -f helm-rbac-config.yaml
kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'
kubectl create serviceaccount --namespace kube-system tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller

kubectl create clusterrolebinding add-on-cluster-admin --clusterrole=cluster-admin --serviceaccount=kube-system:default

#在每个节点运行
echo "###warn:yum install -y socat at every node"
yum install -y socat
```

helm 删除某个命名空间的所有应用

```
helm delete --purge $(helm list --all  --namespace 203 |awk '{if (NR>1){print $1}}')
```

按日期排序

```
helm list -d 

kubectl get pod --sort-by='{.status.startTime}' -n 203
```