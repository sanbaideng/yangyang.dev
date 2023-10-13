---
title: "criar um proxy para gpt"
date: 2023-03-18T17:41:55+08:00
draft: false
tags: ["GPT","proxy"]
---
## Criar um proxy para GPT

Na China, o OpenAI está proibido.
Portanto, precisamos criar um proxy para acessar a API da OpenAI.

1. Servidor AWS Lightsail
2. Criar um servidor Ubuntu 20.04 LTS

```bash
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


```bash
1. Verifique as portas abertas

$ sudo ufw status

2. Abra a porta

$ sudo ufw allow 9123

3. Ative o firewall

$ sudo ufw enable

4. Reinicie o firewall

$ sudo ufw reload

5. Verifique novamente se a porta está aberta
```