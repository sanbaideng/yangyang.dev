---
title: "[Cloud Native] Install Docker on CentOS"
date: 2023-02-20T13:48:58+08:00
draft: false
---

centos安装docker

```
sudo yum install -y yum-utils \
device-mapper-persistent-data \
lvm2
```

添加阿里云源
```
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo 
```

如果yum-config-manager: command not found
执行：
``` 
yum -y install yum-utils 
```

列出列表：
yum list docker --showduplicates |sort -r
yum -v list docker-ce --show-duplicates
安装18.06版本 
```
sudo yum install -y docker-ce-18.06.1.ce-3.el7
systemctl enable docker
systemctl start docker
```


docker 设置代理
10.在为docker设置代理，完成后， 测试命令：docker pull k8s.gcr.io/kube-proxy:v1.12.2
10.1
``` 
mkdir -p /etc/systemd/system/docker.service.d
```
10.2
``` 
vi /etc/systemd/system/docker.service.d/http-proxy.conf
```

```
[Service]
Environment="HTTP_PROXY=http://10.0.20.44:1081/"
Environment="HTTPS_PROXY=http://10.0.20.44:1081/"
Environment="NO_PROXY=localhost,127.0.0.1,5aw91zix.mirror.aliyuncs.com,docker.io,registry.cn-hangzhou.aliyuncs.com,reg.cecii.cn"
```

```
sudo systemctl daemon-reload
sudo systemctl restart docker

systemctl show --property=Environment docker
```
