---
title: "Creating a Proxy for GPT"
date: 2023-03-18T17:41:55+08:00
draft: false
tags: ["GPT","proxy"]
---
# Creating a Proxy for GPT

In China, OpenAI is banned, so we need to create a proxy to access the OpenAI API.

## Setting up an AWS Lightsail server

1. Create an Ubuntu 20.04 LTS server on AWS Lightsail.

## Installing Node.js on Ubuntu server

Follow the steps below to install Node.js on your Ubuntu server:

1. Update the system:
```bash
sudo apt update
```

2. Download the Node.js setup script:
```bash
cd ~
curl -sL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh
```

3. Run the setup script to install Node.js:
```bash
sudo bash nodesource_setup.sh
sudo apt install nodejs
```

## Configuring the firewall

To ensure that our proxy server is accessible, we need to configure the firewall. Follow the steps below:

1. Allow incoming connections to port 19030:
```bash
sudo ufw allow 19030
```

2. Reload the firewall:
```bash
sudo ufw reload
```

## Starting and managing the proxy server

To start and manage our proxy server, follow the steps below:

1. Stop any existing running instances of the proxy:
```bash
forever stop app.js
```

2. Remove the log files of the previous session (if any):
```bash
rm -f /home/ubuntu/.forever/forever.log
```

3. Start the proxy server and save the output logs:
```bash
forever start -l forever.log -o out.log -e err.log app.js
```

## Checking the firewall status

To verify if the firewall is properly configured and the required ports are open, follow the steps below:

1. Check the status of the firewall:
```bash
sudo ufw status
```

2. Verify that port 9123 is open:
```bash
sudo ufw allow 9123
```

3. Enable the firewall (if not enabled already):
```bash
sudo ufw enable
```

4. Reload the firewall:
```bash
sudo ufw reload
```

5. Verify the opened ports:
```bash
sudo ufw status
```

By following these steps, you will be able to create a proxy for GPT and access the OpenAI API even in China where it is banned.