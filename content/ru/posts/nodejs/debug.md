---
title: "nodejs error infos"
date: 2023-08-05T17:20:12+08:00
tags: ["nodejs", "error info"]
---
# React Native Error: ENOSPC: System limit for number of file watchers reached
```
//https://stackoverflow.com/questions/55763428/react-native-error-enospc-system-limit-for-number-of-file-watchers-reached
# вставить новое значение в системный конфиг
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p

# проверить, что новое значение было применено
cat /proc/sys/fs/inotify/max_user_watches

```