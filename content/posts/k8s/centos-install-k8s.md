---
title: "[Cloud Native] Install K8s on CentOS"
date: 2023-02-20T13:53:16+08:00
draft: false
---

建议配置docker 加速器

https://www.jianshu.com/p/1a4025c5f186

本文参考网址：

https://www.techrepublic.com/article/how-to-install-a-kubernetes-cluster-on-centos-7/

# 关闭防火墙 
```
systemctl stop firewalld
systemctl disable firewalld 
```
# 禁用SELINUX 
```
setenforce 0
sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux
```
# 关闭swap
```
swapoff -a
```
## 或永久关闭
```
vi  /etc/fstab
``` 
comment this line
```
# /dev/mapper/centos-swap swap swap defaults 0 0
```

# 设置br_netfilter
```
modprobe br_netfilter
echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables
```
# 添加yum源
```
vi   /etc/yum.repos.d/kubernetes.repo
```
添加内容如下-建议从本文参考网址拷贝如下内容，防止格式差异(本文第四行)：
```
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
```
阿里云源20191230更新
```
[kubernetes]
name=Kubernetes
baseurl=http://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=http://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg
       http://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
```

# 查看可用版本
```
yum list kubelet --showduplicate
```
# 然后安装 then install
```
yum install -y kubelet kubeadm kubectl
yum install -y kubelet-1.17.13-0 kubeadm-1.17.13-0 kubectl-1.17.13-0
yum install -y kubelet-1.13.5-0 kubeadm-1.13.5-0 kubectl-1.13.5-0  --skip-broken

systemctl daemon-reload 
systemctl enable kubelet
systemctl restart kubelet
```

# kubeadm init启动，参考

https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/
```
echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables
sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'
echo 1 > /proc/sys/net/bridge/bridge-nf-call-ip6tables
echo 1 > /proc/sys/net/bridge/bridge-nf-call-iptables
```
用阿里云的镜像启动
建立一个配置文件
#cat init-config.yaml
apiVersion: kubeadm.k8s.io/v1beta1
kind: ClusterConfiguration
kubernetesVersion: v1.16.4
imageRepository: registry.aliyuncs.com/google_containers

kubeadm config images pull --config=init-config.yaml

---
### kubadm init:
```
calico:作为网络组件 --pod-network-cidr=192.168.0.0/16
kubeadm init --pod-network-cidr=192.168.0.0/16 --kubernetes-version=v1.17.13 --image-repository=registry.cn-hangzhou.aliyuncs.com/google_containers
kubeadm init  --kubernetes-version=v1.17.13 --image-repository=registry.cn-hangzhou.aliyuncs.com/google_containers
kubeadm init --pod-network-cidr=192.168.0.0/17 --service-cidr=192.168.128.0/17  --kubernetes-version=v1.17.13 --image-repository=registry.cn-hangzhou.aliyuncs.com/google_containers


kubeadm init --pod-network-cidr=192.168.0.0/16  --kubernetes-version=v1.17.13 --image-repository=registry.aliyuncs.com/google_containers
kubeadm init  --network-plugin=cni  --kubernetes-version=v1.17.13 --image-repository=registry.aliyuncs.com/google_containers
kubeadm init   --kubernetes-version=v1.17.13 --image-repository=registry.aliyuncs.com/google_containers

calico：  kubectl apply -f  https://docs.projectcalico.org/archive/v3.14/manifests/calico.yaml

kubectl taint nodes --all node-role.kubernetes.io/master-

重新生成join语句
kubeadm token create --print-join-command --ttl=0

kubeadm join 172.16.20.199:6443 --token jncgw9.7bbex0rp5hah979y --discovery-token-ca-cert-hash sha256:a80e18efa6f775291373ba56142a9bc27514fd3917a0508ec429238a6e85e23d
常用命令：
kubectl get pod --namespace=kube-system
kubectl describe po kubernetes-dashboard-77fd78f978-kkffb --namespace=kube-system



The link to the Calico docs I used to install Calico v3.14.0 is:
kubectl apply -f https://docs.projectcalico.org/v3.14.0/manifests/calico-typha.yaml
kubectl apply -f https://docs.projectcalico.org/v3.14.0/manifests/calicoctl.yaml
```

---


### 查看集群信息
```
kubectl cluster-info
kubectl get pods --all-namespaces

sudo journalctl -u kubelet --all | tail
kubectl logs 99a04cab33e1 -n=istio-system

kubectl --kubeconfig=/home/linux/.kube/kubeconfig.yaml get svc -n ingress-nginx

watch kubectl get pods --all-namespaces

kubectl taint nodes --all node-role.kubernetes.io/master-

iptables -S -t nat

kubectl get cs,node,svc,pods,ingress --all-namespaces -o wide 
```

---

### 卸载
```
yum remove kubelet kubeadm kubectl
```
### 安装指定版本
```
yum install -y kubelet-1.13.5-0.x86_64 
yum install -y kubectl-1.13.5-0.x86_64
yum install -y kubeadm-1.13.5-0.x86_64

20191230更新
yum install -y kubelet-1.21.8-0 kubectl-1.21.8-0 kubeadm-1.21.8-0
yum install -y kubelet-1.17.8-0 kubectl-1.17.8-0 kubeadm-1.17.8-0
yum install -y kubeadm-1.14.6-0 kubelet-1.14.6-0 kubectl-1.14.6-0 --disableexcludes=kubernetes
```
### 查看日志
```
journalctl -f -u kubelet
```


编辑应用，不需要yaml文件 ： 
```
kubectl edit deployment/my-nginx
```

---
管理组件 
```
https://kuboard.cn/install/install-k8s.html#%E6%96%87%E6%A1%A3%E7%89%B9%E7%82%B9
```
---

