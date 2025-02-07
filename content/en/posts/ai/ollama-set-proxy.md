---
title: ollama set proxy
date: 2025-02-07 14:56:31.702312  
tags: ["ollama","ai"]
---
# ollama set proxy
To set proxy in ollama, you can use the following command:

- vim /etc/systemd/system/ollama.service

```
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/local/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

Environment="https_proxy=http://mycorporateproxy.local:8080"  #                             <---------------- 

[Install]
WantedBy=default.target
```

sudo systemctl daemon-reload
sudo systemctl restart ollama.service