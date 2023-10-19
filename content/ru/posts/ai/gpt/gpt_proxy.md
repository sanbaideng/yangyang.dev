---
title: "создание прокси для gpt"
date: 2023-03-18T17:41:55+08:00
tags: ["GPT", "proxy"]
---
создание прокси для gpt

В Китае openai запрещен.
Поэтому нам нужно создать прокси для посещения openai api.

1.сервер aws lightsail
2.создать сервер ubuntu Ubuntu 20.04 LTS

```
https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-22-04
sudo apt update
cd ~
curl -sL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs


sudo npm install forever -g
sudo ufw allow 19030
 sudo ufw reload

 
forever останавливает app.js
rm -f /home/ubuntu/.forever/forever.log
forever start -l forever.log -o out.log -e err.log app.js
```



```
１.查看已经开启的端口

$ sudo ufw status

2.打开端口

$ sudo ufw allow 9123

3.开启防火墙

$ sudo ufw enable

４.重启防火墙

$ sudo ufw reload

5.再次查看一下端口是否已开放
```