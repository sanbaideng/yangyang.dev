---
title: "Clone big repo in gitlab by ssh"
date: 2023-07-04T09:54:12+08:00
draft: false
tags: ["git"]

---
1. Generating a new SSH key pair  生成ssh key
    > http://gitlab.test/help/ssh/README#locating-an-existing-ssh-key-pair

    > https://docs.gitlab.com/ee/user/ssh.html

    ```ssh-keygen -o -t rsa -C "your.email@example.com" -b 4096```

2. Add SSH Keys (public key) in User Settings. 在用户设置中配置ssh keys 公钥

3. IF  can't ssh login via Domain, config it in the hosts file.如果不能通过域名登录ssh，在hosts文件中配置域名与ip的映射,
   windows hosts file located in ``` C:\Windows\System32\drivers\etc```
   config will like this:
   ``` 172.27.xx.xxx gitlab.test ```
4. Then test ssh login in cmd
   ``` ssh -T gitlab.test ```
   if succeed, it will echo  ``` Welcome to GitLab, @username!```

5. Then clone:
   ```  git clone git@gitlab.test:relative/repo.git```

