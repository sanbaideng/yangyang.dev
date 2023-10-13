---
title: "创建 GPT 代理"
date: 2023-03-18T17:41:55+08:00
draft: false
tags: ["GPT","代理"]
---
# 创建 GPT 代理

在中国，OpenAI 被封锁了，因此我们需要创建一个代理来访问 OpenAI API。

## 1. AWS Lightsail 服务器
首先，在 AWS Lightsail 上创建一个 Ubuntu 20.04 LTS 服务器。

## 2. 安装 Node.js 和设置防火墙
请按以下步骤在 Ubuntu 服务器上安装 Node.js 并设置防火墙。

```shell
sudo apt update
cd ~
curl -sL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs

sudo npm install forever -g
sudo ufw allow 19030
sudo ufw reload
```

## 3. 启动代理服务器
在服务器上运行以下命令以启动代理服务器。

```shell
# 停止之前运行的应用程序（如果有）
forever stop app.js

# 清除日志文件
rm -f /home/ubuntu/.forever/forever.log

# 启动代理服务器
forever start -l forever.log -o out.log -e err.log app.js
```

## 4. 配置防火墙
按照以下步骤配置防火墙，确保已经开放了所需的端口。

```shell
# 查看已经开启的端口
sudo ufw status

# 打开端口 9123（根据需要替换为实际使用的端口）
sudo ufw allow 9123

# 开启防火墙
sudo ufw enable

# 重启防火墙
sudo ufw reload

# 再次查看已开放的端口，确认配置成功
```

请根据需要替换上述命令中的端口号。