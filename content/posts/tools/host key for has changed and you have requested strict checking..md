---
title: "host key for xx has changed and you have requested strict checking."
date: 2024-01-11T09:20:14+08:00
draft: false
keywords: ssh

tags: ["ssh"]
---
# vscode 远程连接ssh，报错："could not establish connection to XHR failed"

## 现象

```
[user@hostname ~]$ ssh root@ping
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
6e:45:f9:a8:af:38:3d:a1:a5:c7:76:1d:02:f8:77:00.
Please contact your system administrator.
Add correct host key in /home/hostname /.ssh/known_hosts to get rid of this message.
Offending RSA key in /var/lib/sss/pubconf/known_hosts:4
RSA host key for ping has changed and you have requested strict checking.
Host key verification failed.
```

## 解决办法

Here is the simplest solution:
```
ssh-keygen -R <host>
```
For example,
```
ssh-keygen -R 192.168.3.10
```

