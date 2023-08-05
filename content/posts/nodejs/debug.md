---
title: "nodejs error infos"
date: 2023-08-05T17:20:12+08:00
draft: false
tags: ["nodejs", "error info"]
---
# React Native Error: ENOSPC: System limit for number of file watchers reached
```
//https://stackoverflow.com/questions/55763428/react-native-error-enospc-system-limit-for-number-of-file-watchers-reached
# insert the new value into the system config
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p

# check that the new value was applied
cat /proc/sys/fs/inotify/max_user_watches

```