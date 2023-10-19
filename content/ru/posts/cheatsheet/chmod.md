---
title: Chmod
дата: 2021-07-01 10:51:44
фон: bg-emerald-600
теги:
    - разрешение
категории:
    - Linux Command
ввод: |
    Эта краткая шпаргалка содержит краткий обзор разрешений файлов и работы команды chmod
плагины:
    - copyCode
---


Начало работы
--------


### Синтаксис
Шелл-скрипт
$ chmod [options] <permissions> <file>
```
#### Пример
```Шелл
$ chmod 755 foo.txt
$ chmod +x cheatsheets.py
$ chmod u-x cheatsheets.py
$ chmod u=rwx,g=rx,o= cheatsheets.sh
```
#### Рекурсивное изменение файлов и каталогов
``hell
$ chmod -R 755 my_directory
```
Команда `chmod` означает "режим изменения".


### Генератор Chmod
<widget name="chmod"/>

Chmod Generator позволяет быстро и наглядно генерировать права доступа в числовом и символьном виде.


### Общие разрешения
| Команда | s | Значение |
|---------|-----------|------------------------------|
| `400` | r-------- | Доступно только для чтения владельцем |
| `500` | r-x------ | Не изменять |
| `600` | rw------- | Изменять может пользователь |
| `644` | rw-r--r-- | Чтение и изменение пользователем |
| `660` | rw-rw---- | Изменять может пользователь и группа |
| `700` | rwx------ | Только пользователь имеет полный доступ |
| `755` | rwxr-xr-x | Изменять может только пользователь |
| `775` | rwxrwxr-x | Режим совместного доступа для группы |
| `777` | rwxrwxrwx | Все могут делать все |


### Пояснения
``hell
$ ls -l
-rw-r--r-- 1 root root 3 Jun 29 15:35 a.log
drwxr-xr-x 2 root root 2 Jun 30 18:06 dir
```
#### Анализ разрешений для "dir"
``текст
d rwx r-x r-x
┬ ─┬─ ─┬─ ─┬─
│ │ │ │
│ │ │ └─ 4. Другое｜5 (4+0+1)
│ │ └────── 3. Группа｜5 (4+0+1)
│ └─────────── 2. Пользователь ｜7 (4+2+1)
└─────────────── 1. Тип файла | каталог
```


### Режимы разрешения {.col-span-2}
| Permission | Description | Octal | Decimal | Decimal
|------------|-------------------------|-------|-----------|
| `---` | Нет разрешения | 000 | 0 (0+0+0) |
| `--x` | Выполнить | 001 | 1 (0+0+1) |
| `-w-` | Запись | 010 | 2 (0+2+0) |
| `-wx` | Выполнить и записать | 011 | 3 (0+2+1) |
| `r--` | Чтение | 100 | 4 (4+0+0) |
| `r-x` | Чтение и выполнение | 101 | 5 (4+0+1) |
| `rw-` | Чтение и запись | 110 | 6 (4+2+0) |
| | `rwx` | Чтение, запись и выполнение | 111 | 7 (4+2+1) |
{.show-header}



### Объекты
| Кто (abbr.) | Значение |
|-------------|--------------------|
| `u` | `U`ser |
| `g` | `G`roup |
| `o` | `O`thers |
| `a` | `A`ll, то же, что ugo |
{.show-header}


### Разрешения
| Аббревиатура | Разрешение | Значение |
|--------------|---------------|-------|
| `r` | `R`ead | 4 |
| `w` | `W`rite | 2 |
| `x` | E`x`ecute | 1 | |
| `-` | Нет разрешения | 0 |
{.show-header}


### Типы файлов
| Аббревиатура | Тип файла |
|--------------|-----------------|
| `d` | `D` директория |
| `-` | Обычный файл |
| `l` | Символическая `L`ссылка |
{.show-header}



Примеры Chmod
--------


### Операторы
| Символ | Описание |
|--------|-------------|
| `+` | Добавить |
| `-` | Удалить |
| `=` | Установить |


### chmod 600
``hell
$ chmod 600 example.txt
$ chmod u=rw,g=,o= example.txt
$ chmod a+rwx,u-x,g-rwx,o-rwx example.txt
```


### chmod 664
``hell
$ chmod 664 example.txt
$ chmod u=rw,g=rw,o=r example.txt
$ chmod a+rwx,u-x,g-x,o-wx example.txt
```

### chmod 777
```hell
$ chmod 777 example.txt
$ chmod u=rwx,g=rwx,o=rwx example.txt
$ chmod a=rwx example.txt
```


### Символьный режим {.row-span-3}
Запретить разрешение на выполнение всем.
``hell
$ chmod a-x chmodExampleFile.txt
```
Разрешить чтение всем.
```hell
$ chmod a+r chmodExampleFile.txt
```
Сделать файл доступным для чтения и записи для группы и других.
```hell
$ chmod go+rw chmodExampleFile.txt
```
Сделать сценарий оболочки исполняемым пользователем/владельцем.
```hell
$ chmod u+x chmodExampleScript.sh
```
Разрешить всем читать, писать и исполнять файл и включить заданный group-ID.
```hell
$ chmod =rwx,g+s chmodExampleScript.sh
```

### Удаление разрешений {.row-span-3}
Для снятия разрешений на чтение-запись, предоставленных файлу, используйте следующий синтаксис:
``hell
$ chmod o-rw example.txt
```
Для нашего файла example.txt мы можем снять разрешения на чтение-запись с помощью chmod for group, выполнив следующую команду:
```hell
$ chmod g-rx example.txt
```
Для удаления прав чтения-записи chmod для группы и добавления прав чтения-записи для public/others можно использовать следующую команду:
``hell
$ chmod g-rx, o+rx example.txt
```
Если же необходимо удалить все разрешения для группы и других, то можно воспользоваться командой go=:
```hell
$ chmod go= example.txt
```

### Исполняемый файл
```hell
$ chmod +x ~/example.py
$ chmod u+x ~/example.py
$ chmod a+x ~/example.py
```

### chmod 754
``Шелл
$ chmod 754 foo.sh
$ chmod u=rwx,g=rx,o=r foo.sh
```



Chmod Практика
---------------

### Разрешения SSH
Шелковый сценарий
$ chmod 700 ~/.ssh
$ chmod 600 ~/.ssh/authorized_keys
$ chmod 600 ~/.ssh/id_rsa
$ chmod 600 ~/.ssh/id_rsa.pub
$ chmod 400 /path/to/access_key.pem
```

### Веб-разрешения
``` Шелл-скрипт
$ chmod -R 644 /var/www/html/
$ chmod 644 .htaccess
$ chmod 644 robots.txt
$ chmod 755 /var/www/uploads/
$ find /var/www/html -type d -exec chmod 755 {} \;
```

### Пакетное изменение
``Шелл-скрипт
$ chmod -R 644 /ваш_путь
$ find /path -type d -exec chmod 755 {} \;
$ find /path -type f -exec chmod 644 {} \;
```
См: [Замена команд](https://tldp.org/LDP/abs/html/commandsub.html)


## Также см.
* [Изменение разрешений файлов с помощью chmod](https://www.linode.com/docs/guides/modify-file-permissions-with-chmod/) _(linode.com)_
