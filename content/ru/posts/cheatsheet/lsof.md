---
title: Lsof
date: 2021-02-05 16:12:47
фон: bg-blue-400
теги:
    - порт
    - процессы
    - утилита
категории:
    - Linux Command
ввод: |
     В этой краткой шпаргалке представлены различные варианты использования команды lsof.
плагины:
    - copyCode
---

Начало работы
--------------

### Введение
**lsof**, означающее `L`i`S`t `O`pen `F`iles, используется для выяснения того, какие файлы открыты каким процессом.

Шелл-скрипт
$ lsof
$ sudo lsof -u root
```

### Порт-специфичен

```Шелл-скрипт
$ lsof -i :8080
$ lsof -i :80 -i :22
$ lsof -i TCP:22
$ lsof -i TCP:1-1024
$ lsof -i UDP
$ lsof -i @192.168.1.5
```



### Процесс-специфический
```Основной сценарий
$ lsof -c mysql
$ lsof -c java
$ lsof -c ssh
$ lsof -c nginx
$ lsof -c ssh -c httpd
```


### Специфические для пользователя

``` Сценарий командной строки
$ lsof -u www-data
$ lsof -u www-data -u ubuntu
$ lsof -i -u ^root # За исключением определенного пользователя
```


### Сетевая специфика
```Шелл-скрипт
$ lsof -i 4 # только IPv4
$ lsof -i 6 # только IPv6
```

### PID-специфичный
```Шелл-скрипт
$ lsof -p 1753
$ lsof -p ^3 # Исключение определенных пидов
```

### Скрипт, зависящий от имени файла
```Шелл-скрипт
$ lsof /var/log/messages
$ lsof /etc/passwd
```


### Directory-specific
```Шелл-скрипт
$ lsof +D /var/log # Внутри каталога
```


### Kill
``Шелл-скрипт
$ kill -9 `lsof -t -u apache`
$ kill -9 $(lsof -t -i :8080)
```



