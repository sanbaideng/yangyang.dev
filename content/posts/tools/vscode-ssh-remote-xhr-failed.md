---
title: "vscode remote ssh would report XHR FAILED"
date: 2024-01-10T11:15:14+08:00
draft: false
keywords: XHR

tags: ["vscode", "ssh"]
---
# vscode 远程连接ssh，报错："could not establish connection to XHR failed"

## 现象

terminal ssh 可以连接到服务器，vscode远程连接时，报错"could not establish connection to XHR failed"

## 解决办法

登录到服务器，进入目录，~/.vscode-server/bin

```
cd ~/.vscode-server/bin
找到日期最新的目录，进入，如果有vscode-remote-lock文件，如：vscode-remote-lock.root.af28b32d7e553898b2a91af498b1fb666fdebe0c
则将整个目录备份，
再重连即可
```

