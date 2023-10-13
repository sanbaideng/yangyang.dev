---
title: "Erstellen Sie einen Proxy für GPT"
date: 2023-03-18T17:41:55+08:00
draft: false
tags: ["GPT", "Proxy"]
---
# Erstellen Sie einen Proxy für GPT

In China ist OpenAI gesperrt. Daher müssen wir einen Proxy erstellen, um die OpenAI API zu besuchen.

## 1. AWS Lightsail Server
## 2. Erstellen Sie einen Ubuntu Server Ubuntu 20.04 LTS

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

```
1. Überprüfen Sie die geöffneten Ports:

$ sudo ufw status

2. Öffnen Sie den Port:

$ sudo ufw allow 9123

3. Aktivieren Sie die Firewall:

$ sudo ufw enable

4. Firewall neustarten:

$ sudo ufw reload

5. Überprüfen Sie erneut, ob der Port geöffnet ist.
```

Bitte beachten Sie, dass Sie Ihren Proxy gemäß lokalen oder globalen Vorschriften und Bestimmungen einrichten sollten.