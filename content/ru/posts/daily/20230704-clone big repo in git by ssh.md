---
title: "Клонирование большого репо в gitlab по ssh"
date: 2023-07-04T09:54:12+08:00
черновик: false
tags: ["git"].

---
1. Генерация новой пары ключей SSH 生成ssh key
    > http://gitlab.test/help/ssh/README#locating-an-existing-ssh-key-pair

    > https://docs.gitlab.com/ee/user/ssh.html

    ```ssh-keygen -o -t rsa -C "your.email@example.com" -b 4096``

2. Добавьте SSH-ключи (открытый ключ) в Настройки пользователя. 在用户设置中配置ssh keys 公钥

3. Если не удается войти по ssh через домен, настройте его в файле hosts.如果不能通过域名登录ssh，在hosts文件中配置域名与ip的映射,
   файл windows hosts находится в ``C:\Windows\System32\drivers\etc``.
   конфигурация будет выглядеть следующим образом:
   ``` 172.27.xx.xxx gitlab.test ```
4. Затем протестируйте вход по ssh в cmd
   ``` ssh -T gitlab.test ```
   В случае успеха будет выдано эхо ``Добро пожаловать в GitLab, @username!``

5. Затем выполните клонирование:
   ``` git clone git@gitlab.test:relative/repo.git``.

