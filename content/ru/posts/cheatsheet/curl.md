---
title: Curl
date: 2023-01-03 15:18:34
фон: bg-slate-600
tags:
    - url
    - запрос
категории:
    - Linux Command
ввод: |
    Эта шпаргалка [Curl](https://github.com/curl/curl) содержит команды и примеры некоторых распространенных приемов работы с Curl.
плагины:
    - copyCode
---

Начало работы
---------------


### Введение

`Curl` - это инструмент для передачи данных между серверами, поддерживающий протоколы, в том числе:
- HTTP
- HTTPS
- FTP
- IMAP
- LDAP
- POP3
- SCP
- SFTP
- SMB
- SMTP
- и т.д.
{.cols-3 .marker-none}

----------------------------------------------------------------

- [Репозиторий исходных текстов Curl GitHub](https://github.com/curl/curl) _(github.com)_
- [Официальный сайт Curl](https://curl.se/) _(curl.se)_


### Опции {.col-span-2 row-span-2}

``bash
-o <file> # --output: запись в файл
-u user:pass # --user: аутентификация
```

---

``bash
-v # --verbose: Сделать curl многословным во время работы
-vv # еще более многословным
-s # --silent: не показывать счетчик выполнения или ошибки
-S # --show-error: При использовании с --silent (-sS) показывать ошибки, но не показывать счетчик выполнения
```

---

``bash
-i # --include: включать в вывод HTTP-заголовки
-I # --head: только заголовки
```



### Запрос

``bash
-X POST # --request
-L # Если страница перенаправляет, перейдите по ссылке
-F # --form: HTTP POST-данные для multipart/form-data
```
<!--rehype:className=wrap-text -->



### данные

``bash
# --data: Данные HTTP-поста
# кодировка URL (например, status="Hello")
-d 'data'

# --data pass file
-d @file

# --get: передать -d data через get
-G
```



### Информация о заголовках Заголовки

``bash
-A <str> # --user-agent

-b name=val # --cookie

-b, --cookie FILE # Загрузка cookies из указанного файла для URL
-c, --cookie-jar FILE # Сохранить cookies в указанный файл из URL

-H "X-Foo: y" # --header

--compressed # использовать deflate/gzip
```



### SSL

``bash
    --cacert <file>
    --capath <dir>
```

``bash
-E, --cert <cert> # --cert: файл сертификата клиента
    --cert-type # der/pem/eng
-k, --insecure # Для самоподписанных сертификатов
```



#### Установить

``bash
apk add --update curl # установка в alpine linux
```

Пример {.cols-6}
----
<!--rehype:body-class=cols-6-->


### CURL GET/HEAD {.col-span-4 .row-span-2}

команда | описание
:-| :-
`curl -I https://cheatsheets.zip` | `curl` отправляет запрос
`curl -v -I https://cheatsheets.zip` | `curl` отправляет запрос с деталями
`curl -X GET https://cheatsheets.zip` | использовать явный метод http для `curl`
`curl --noproxy 127.0.0.1 http://www.stackoverflow.com` | `curl` без http-прокси
`curl --connect-timeout 10 -I -k https://cheatsheets.zip` | `curl` по умолчанию не имеет таймаута
`curl --verbose --header "Host: www.mytest.com:8182" cheatsheets.zip` | `curl` получает дополнительный заголовок
`curl -k -v https://www.google.com` | `curl` получить ответ с заголовками
<!--rehype:class=auto-wrap-->



### Многократная загрузка файлов {.col-span-2}

``bash
$ curl -v --include \
--form key1=value1 \
    --form upload=@localfilename URL
```



### Претенциозный вывод json для ответа curl {.col-span-2}

``bash
$ curl -XGET http://${elasticsearch_ip}:9200/_cluster/nodes | python -m json.tool
```
<!--rehype:className=wrap-text -->



### CURL POST {.col-span-4}

команда | описание
:-| :-
`curl -d "name=username&password=123456" <URL>` | `curl` отправить запрос
`curl <URL> -H "content-type: application/json" -d "{ \"гав\": \"bark\"}"` | `curl` отправляет json
<!--rehype:class=auto-wrap-->
### CURL-скрипт install rvm {.col-span-2}

``шелл
curl -sSL https://get.rvm.io | bash
```



### CURL Advanced {.col-span-6}

команда | описание
:-| :-
`curl -L -s http://ipecho.net/plain, curl -L -s http://whatismijnip.nl` | Получить мой публичный `IP`
`curl -u $username:$password http://repo.dennyzhang.com/README.txt` | `curl` с учетными данными
`curl -v -F key1=value1 -F upload=@localfilename <URL>` | `curl` upload
`curl -k -v --http2 https://www.google.com/` | использовать http2 curl
`curl -T cryptopp552.zip -u test:test ftp://10.32.99.187/` | curl `ftp` upload
`curl -u test:test ftp://10.32.99.187/cryptopp552.zip -o cryptopp552.zip` | curl `ftp` download
`curl -v -u admin:admin123 --upload-file package1.zip http://mysever:8081/dir/package1.zip` | upload with credentials `curl`.
<!--rehype:class=auto-wrap-->



### Проверить время отклика сайта {.col-span-4}

``hell
curl -s -w \
'\nLookup time:\t%{time_namelookup}\nConnect time:\t%{time_connect}\nAppCon time:\t%{time_appconnect}\nRedirect time:\t%{time_redirect}\nPreXfer time:\t%{time_pretransfer}\nStartXfer time:\t%{time_starttransfer}\n\nTotal time:\t%{time_total}\n' \n
     -o /dev/null https://www.google.com
```
<!--rehype:className=wrap-text -->



### Используйте Curl для проверки доступности удаленного ресурса {.col-span-2}

``bash
curl -o /dev/null --silent -Iw "%{http_code}" https://example.com/my.remote.tarball.gz
```
<!--rehype:className=wrap-text -->



### Загрузка файла {.col-span-3}

``bash
curl https://example.com | \
grep --only-matching 'src="[^"]*.[png]"'' | \
cut -d \" -f2 | \
while read i; do curl https://example.com/"${i}" \
-o "${i##*/}"; done
```

Загрузите все PNG-файлы с сайта (используя GNU grep)



### Скачайте файл, сохраните его, не меняя имени {.col-span-3}

``bash
curl --remote-name "https://example.com/linux-distro.iso"
```

переименовать файл

``bash
curl --remote-name "http://example.com/index.html" --output foo.html
```



### продолжить частичную загрузку {.col-span-3}

``bash
curl --remote-name --continue-at - "https://example.com/linux-distro.iso"
```
<!--rehype:className=wrap-text -->



### Загрузка файлов с нескольких доменов {.col-span-3}

``bash
curl "https://www.{example,w3,iana}.org/index.html" --output "file_#1.html"
```
<!--rehype:className=wrap-text -->



### Скачать серию файлов {.col-span-3}

``bash
curl "https://{foo,bar}.com/file_[1-4].webp" --output "#1_#2.webp"
```
<!--rehype:className=wrap-text -->

Загрузить серию файлов (вывод `foo_file1.webp`, `foo_file2.webp...bar_file1_webp` и т.д.)
### Перенаправить вывод в файл {.col-span-3}

``bash
$ curl http://url/file > file
```



### Базовая аутентификация {.col-span-3}

``bash
$ curl --user username:password http://example.com/
$ curl -u username:password http://example.com/
```



### Запись в файл вместо stdout {.col-span-2}

``bash
$ curl -o file http://url/file
$ curl --output file http://url/file
```



### Загрузка заголовочной информации

``bash
$ curl -I url
# отобразить информацию о заголовке
```



### Запись вывода в файл с именем remote_file {.col-span-2}

``bash
$ curl -o file http://url/file
$ curl --output file http://url/file
```
### Выполнение удаленного скрипта {.col-span-2}

``bash
$ curl -s http://url/myscript.sh
```



### Конфигурационный файл {.col-span-2}

``bash
curl -K file
# чтение конфигурации из файла
curl --config файл
$HOME/.curlrc # файл конфигурации по умолчанию в UNIX-подобных системах
```
