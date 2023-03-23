---
title: "create a proxy for gpt"
date: 2023-03-18T17:41:55+08:00
draft: false
tags: ["GPT","proxy"]
---
create a proxy for gpt

in china , openai is banned .
so we need to create a proxy to visit the openai api.

1.aws lightsail server
2.create a ubuntu server Ubuntu 20.04 LTS
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

 
forever stop app.js 
rm -f /home/ubuntu/.forever/forever.log
forever start -l forever.log -o out.log -e err.log app.js 
```
