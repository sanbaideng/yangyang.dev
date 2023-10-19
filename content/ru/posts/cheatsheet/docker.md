---
Название: Docker
дата: 2020-12-30 10:55:24
фон: bg-[#488fdf]
теги:
    - контейнер
    - виртуальный
категории:
    - Программирование
intro: |
    Это краткая справочная шпаргалка по [Docker](https://docs.docker.com/get-started/). Здесь вы найдете наиболее распространенные команды Docker.
плагины:
    - copyCode
---

Начало работы {.cols-2}
---------------

### Начало работы
Создание и запуск контейнера в фоновом режиме

Шелл-скрипт
$ docker run -d -p 80:80 docker/getting-started
```

----

- `-d` - Запуск контейнера в отсоединенном режиме
- `-p 80:80` - Сопоставить порт 80 с портом 80 в контейнере
- `docker/getting-started` - Образ для использования
{.marker-none}


Создание и запуск контейнера на переднем плане
``Шелл-скрипт
$ docker run -it -p 8001:8080 --name my-nginx nginx
```

----

- `-it` - Интерактивный режим bash
- `-p 8001:8080` - Сопоставить порт 8001 с портом 8080 в контейнере
- `--name my-nginx` - Указать имя
- `nginx` - Используемый образ
{.marker-none}



### Общие команды
| Пример | Описание |
|-------------------------------------|--------------------------------------------------|
| `docker ps` | Список запущенных контейнеров |
| `docker ps -a` | Список всех контейнеров |
| `docker ps -s` | Список запущенных контейнеров<br>_(с CPU / памятью)_ |
| `docker images` | Список всех изображений |
| `docker exec -it <container> bash` | Подключение к контейнеру |
| `docker logs <container>` | Показывает консольный журнал контейнера |
| `docker stop <container>` | Остановить контейнер |
| `docker restart <container>` | Перезапустить контейнер |
| `docker rm <container>` | Удалить контейнер |
| `docker port <container>` | Показывает сопоставление портов контейнера |
| `docker top <container>` | Список процессов |
| `docker kill <container>` | Убить контейнер |

Параметр `<контейнер>` может быть идентификатором или именем контейнера




Контейнеры Docker {.cols-2}
----------


### Запуск и остановка
| Описание | Пример |
|-------------------------------|-------------------------------------|
| `docker start my-nginx` | Запуск |
| `docker stop my-nginx` | Остановка |
| `docker restart my-nginx` | Перезапуск |
| `docker pause my-nginx` | Пауза |
| `docker unpause my-nginx` | Снять паузу |
| `docker wait my-nginx` | Блокирование контейнера |
| `docker kill my-nginx` | Отправка сообщения SIGKILL |
| `docker attach my-nginx` | Подключение к существующему контейнеру |



### Информация

| Пример | Описание |
|-------------------------------|----------------------------------------|
| `docker ps` | Список запущенных контейнеров |
| `docker ps -a` | Список всех контейнеров |
| `docker logs my-nginx` | Журналы контейнеров |
| `docker inspect my-nginx` | Проверка контейнеров |
| `docker events my-nginx` | События контейнеров |
| `docker port my-nginx` | Публичные порты |
| `docker top my-nginx` | Запущенные процессы |
| `docker stats my-nginx` | Использование ресурсов контейнера |
| `docker diff my-nginx` | Список изменений, внесенных в контейнер. |


### Создание

``yaml
docker create [options] IMAGE
  -a, --attach # присоединить stdout/err
  -i, --interactive # присоединить stdin (интерактивный)
  -t, --tty # псевдо-tty
      --name NAME # дать имя вашему изображению
  -p, --publish 5000:5000 # карта портов (хост:контейнер)
      --expose 5432 # открыть порт для контейнеров
  -P, --publish-all # опубликовать все порты
      --link container:alias # связывание
  -v, --volume `pwd`:/app # монтирование (необходимы абсолютные пути)
  -e, --env NAME=hello # env vars
```
#### Пример
сценарий оболочки
$ docker create --name my_redis --expose 6379 redis:3.0.2
```


### Манипулирование
Переименование контейнера
``Сценарий командной строки
docker rename my-nginx my-nginx
```
Удаление контейнера
Шелл-скрипт
docker rm my-nginx
```
Обновление контейнера
сценарий
docker update --cpu-shares 512 -m 300M my-nginx
```




Образы Docker {.cols-2}
------

### Манипулирование
| `Example` | Description |
|------------------------------------|---------------------------------|
| `docker images` | Listing images |
| `docker rmi nginx` | Удаление изображения |
| `docker load < ubuntu.tar.gz` | Загрузка репозитория в tar-архиве |
| `docker load --input ubuntu.tar` | Загрузка репозитория в tar-архиве |
| `docker save busybox > ubuntu.tar` | Сохранение изображения в tar-архиве |
| `docker history` | Отображение истории образа |
| `docker commit nginx` | Сохранение контейнера в виде образа.   |
| `docker tag nginx eon01/nginx` | Пометить образ |
| `docker push eon01/nginx` | Размещение образа |


### Создание образов
Шелл-скрипт
$ docker build .
$ docker build github.com/creack/docker-firefox
$ docker build - < Dockerfile
$ docker build - < context.tar.gz
$ docker build -t eon/my-nginx .
$ docker build -f myOtherDockerfile .
$ curl example.com/remote/Dockerfile | docker build -f - .
```



Docker Networking {.cols-2}
----------




### Манипулирование

Удаление сети
Шелл-скрипт
docker network rm MyOverlayNetwork
```
Вывод сетей в список
сценарий командной строки
docker network ls
```
Получение информации о сети
```ll-скрипт
docker network inspect MyOverlayNetwork
```
Подключение запущенного контейнера к сети
``Шелл-скрипт
docker network connect MyOverlayNetwork nginx
```
Подключение контейнера к сети при его запуске
``Шелл-скрипт
docker run -it -d --network=MyOverlayNetwork nginx
```
Отключение контейнера от сети
```Шелл-скрипт
docker network disconnect MyOverlayNetwork nginx
```



### Создание сетей
``Сценарий командной строки
docker network create -d overlay MyOverlayNetwork

docker network create -d bridge MyBridgeNetwork

docker network create -d overlay \
  --subnet=192.168.0.0/16 \
  --subnet=192.170.0.0/16 \
  --gateway=192.168.0.100 \
  --gateway=192.170.0.100 \
  --ip-range=192.168.1.0/24 \
  --aux-address="my-router=192.168.1.5" \
  --aux-address="my-switch=192.168.1.6" \
  --aux-address="my-printer=192.170.1.5" \
  --aux-address="my-nas=192.170.1.6" \
  MyOverlayNetwork
```



Очистка {.cols-2}
-------------


### Clean All
Очищает висящие образы, контейнеры, тома и сети (т.е. не связанные с контейнером)
``hell
docker system prune
```

-------

Кроме того, удалите все остановленные контейнеры и все неиспользуемые образы (не только висящие)

``hell
docker system prune -a
```



### Контейнеры

Остановите все работающие контейнеры
``hell
docker stop $(docker ps -a -q)
```

Удалить остановленные контейнеры
```hell
docker container prune
```

### Изображения

Удалите все болтающиеся (не помеченные и не связанные с контейнером) изображения:
``hell
docker image prune
```

Удалить все образы, которые не используются существующими контейнерами
```hell
docker image prune -a
```


### Тома

```hell
docker volume prune
```
Удалить все тома, не используемые хотя бы одним контейнером



Разное {.cols-2}
-------------


### Docker Hub
| Синтаксис | Описание | Docker.
|-----------------------------|-------------------------------------|
| `docker search search_word` | Поиск изображений на хабе docker.       |
| `docker pull user/image` | Загрузка образа с хаба docker. |
| `docker login` | Аутентификация на хабе docker |
| `docker push user/image` | Загружает изображение на хаб docker.     |





### Команды реестра {.row-span-3}

Вход в реестр

Шелл-скрипт
$ docker login
$ docker login localhost:8080
```

Выход из реестра

``Шелл-скрипт
$ docker logout
$ docker logout localhost:8080
```

Поиск изображения

``Шелл-скрипт
$ docker search nginx
$ docker search nginx --stars=3 --no-trunc busybox
```

Извлечение изображения

``Шелл-скрипт
$ docker pull nginx
$ docker pull eon01/nginx localhost:5000/myadmin/nginx
```

Передача изображения

Шелл-скрипт
$ docker push eon01/nginx
$ docker push eon01/nginx localhost:5000/myadmin/nginx
```



### Пакетная очистка
| Пример | Описание |
|-------------|---------------------------------------------|
`docker stop -f $(docker ps -a -q)` | Остановка всех контейнеров
`docker rm -f $(docker ps -a -q)` | Удаление всех контейнеров
`docker rmi -f $(docker images -q)` | Удаление всех образов





### Объемы

Проверка томов
Шелевой сценарий
$ docker volume ls
```
Очистка неиспользуемых томов
```Шелл-скрипт
$ docker volume prune
```
