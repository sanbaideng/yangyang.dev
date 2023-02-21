---
title: "Centos Install Helm2.x"
date: 2023-02-20T14:04:44+08:00
draft: true
---

```

mkdir -pv helm && cd helm
wget https://storage.googleapis.com/kubernetes-helm/helm-v2.9.1-linux-amd64.tar.gz
tar xf helm-v2.9.1-linux-amd64.tar.gz
sudo mv linux-amd64/helm /usr/local/sbin
rm -rf linux-amd64
helm init --upgrade -i ghcr.io/helm/tiller:v2.16.7 --stable-repo-url https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
wget https://raw.githubusercontent.com/Azure/helm-charts/master/docs/prerequisities/helm-rbac-config.yaml

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