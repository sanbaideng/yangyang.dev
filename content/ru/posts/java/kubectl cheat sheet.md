# Kubectl Command Cheatsheet

Kubectl - это инструмент командной строки для настройки Kubernetes, который взаимодействует с сервером Kubernetes API. Использование Kubectl позволяет создавать, проверять, обновлять и удалять объекты Kubernetes. Эта шпаргалка послужит кратким руководством по выполнению команд для многих распространенных компонентов и ресурсов Kubernetes. Вы можете использовать полную команду для объекта, например, pod(s) или варианты шорткодов, упомянутые в заголовке каждого раздела. Все они приведут к одному и тому же результату. Кроме того, в большинстве команд необходимо указывать конкретное <имя> ресурса, которым вы управляете.

## Управление кластером

Отображение информации о конечных точках мастера и сервисов в кластере

``json
kubectl cluster-info
```

 

Отображение версии Kubernetes, запущенной на клиенте и сервере

``json
версия kubectl
```

 Получение конфигурации кластера

``json
kubectl config view
```

 Список доступных ресурсов API

``json
kubectl api-resources
```

 Список доступных версий API

``json
kubectl api-versions
```

 Перечислить все

``json
kubectl get all --all-namespaces
```

 

## Наборы демонов

**Shortcode = ds**

Перечислить один или несколько наборов демонов

``json
kubectl get daemonset
```

 

Редактирование и обновление определения одного или нескольких наборов демонов

``json
kubectl edit daemonset <имя_даемонсета>
```

 

Удалить демонстрационный набор

``json
kubectl delete daemonset <имя_даемонсета>
```

 

Создать новый демонстрационный набор

``json
kubectl create daemonset <имя_даемонсета>
```

 

Управление развертыванием демонстрационного набора

``json
kubectl rollout daemonset
```

 

Отображение подробного состояния демонстрационных наборов в пространстве имен

``json
kubectl describe ds <имя_демосета> -n <имя_пространства_имен>
```

 

## Развертывания

**Shortcode = deploy**

Список одного или нескольких развертываний

``json
kubectl get deployment
```

 

Отображение подробной информации о состоянии одного или нескольких развертываний

``json
kubectl describe deployment <имя_развертывания>
```

 

Редактирование и обновление определения одного или нескольких развертываний на сервере

``json
kubectl edit deployment <deployment_name>
```

 

Создание нового развертывания

``json
kubectl create deployment <имя_развертывания>
```

 

Удаление развертываний

``json
kubectl delete deployment <имя_развертывания>
```

 

Просмотр статуса разворачивания развертывания

``json
kubectl rollout status deployment <deployment_name>
```

 

## События

**Shortcode = ev**

Список последних событий для всех ресурсов в системе

``json
kubectl get events
```

 

Список только предупреждений

``json
kubectl get events --field-selector type=Warning
```

 

Вывести список событий, но исключить события Pod

``json
kubectl get events --field-selector involvedObject.kind!=Pod
```

 

Извлечение событий для одного узла с определенным именем

``json
kubectl get events --field-selector involvedObject.kind=Node, involvedObject.name=<имя_узла>
```

 

Отфильтровать обычные события из списка событий

``json
kubectl get events --field-selector type!=Normal
```

 

## Журналы

Печать журналов для капсулы

``json
kubectl logs <имя_под>
```

 

Печать журналов за последний час для стручка

``json
kubectl logs --since=1h <имя_под>
```

 

Получить последние 20 строк журналов

``json
kubectl logs --tail=20 <имя_под>
```

 

Получить журналы из сервиса и опционально выбрать контейнер

``json
kubectl logs -f <имя_сервиса> [-c <$container>]
```

 

Печать журналов для стручка и отслеживание новых журналов

``json
kubectl logs -f <имя_под>
```

 

Печать журналов для контейнера в стручке

``json
kubectl logs -c <имя_контейнера> <имя_под>
```

 

Вывод журналов для капсулы в файл с именем 'pod.log'

``json
kubectl logs <имя_под> pod.log
```

 

Просмотр журналов для ранее отказавшего pod

``json
kubectl logs --previous <pod_name>
```

 

Для работы с журналами мы также рекомендуем использовать инструмент, разработанный Йоханом Халеби, под названием Kubetail. Это bash-скрипт, позволяющий получать журналы из нескольких подсистем одновременно. Подробнее о нем можно узнать на его [Github-репозитории](https://github.com/johanhaleby/kubetail). Здесь приведены примеры команд, использующих Kubetail.

 

Получить журналы для всех подсистем с именем pod_prefix

``json
kubetail <pod_prefix>
```

 

Включить последние 5 минут журналов

``json
kubetail <pod_prefix> -s 5m
```

 

## Файлы манифеста

Другой вариант модификации объектов - через Manifest Files. Мы настоятельно рекомендуем использовать этот метод. Для этого используются yaml-файлы, в которых заданы все необходимые опции для объектов. Наши yaml-файлы хранятся в git-репозитории, что позволяет отслеживать изменения и оптимизировать их.

 

Применение конфигурации к объекту по имени файла или stdin. Заменяет существующую конфигурацию.

``json
kubectl apply -f manifest_file.yaml
```

 

Создание объектов

``json
kubectl create -f manifest_file.yaml
```

 

Создание объектов во всех файлах манифеста в каталоге

``json
kubectl create -f ./dir
```

 

Создание объектов по URL-адресу

``json
kubectl create -f 'url'
```

 

Удаление объекта

``json
kubectl delete -f manifest_file.yaml
```

 

## Пространства имен

**Шорткод = ns**

Создать пространство имен <имя>

``json
kubectl create namespace <имя_пространства_имен>
```

 

Перечислить одно или несколько пространств имен

``json
kubectl get namespace <имя_пространства_имен>
```

 

Вывод подробной информации о состоянии одного или нескольких пространств имен

``json
kubectl describe namespace <имя_пространства_имен>
```

 

Удаление пространства имен

``json
kubectl delete namespace <имя_пространства_имен>
```

 

Редактирование и обновление определения пространства имен

``json
kubectl edit namespace <имя_пространства_имен>
```

 

Отображение использования ресурсов (процессор/память/хранилище) для пространства имен

``json
kubectl top namespace <имя_пространства_имен>
```

 

## Узлы

**Шорткод = нет**

Обновление пятен на одном или нескольких узлах

``json
kubectl taint node <node_name>
```

 

Перечислить один или несколько узлов

``json
kubectl get node
```

 

Удаление узла или нескольких узлов

``json
kubectl delete node <node_name>
```

 

Отображение использования ресурсов (CPU/Memory/Storage) для узлов

``json
kubectl top node
```

 

Распределение ресурсов на узел

``json
kubectl describe nodes | grep Allocated -A 5
```

 

Подсистемы, запущенные на узле

``json
kubectl get pods -o wide | grep <имя_узла>
```

 

Аннотирование узла

``json
kubectl annotate node <имя_узла>
```

 

Пометить узел как не планируемый

``json
kubectl cordon node <node_name>
```

 

Пометить узел как планируемый

``json
kubectl uncordon node <node_name>
```

 

Слить узел для подготовки к обслуживанию

``json
kubectl drain node <node_name>
```

 

Добавить или обновить метки одного или нескольких узлов

``json
kubectl label node
```

 

## Pods

**Shortcode = po**

Перечислите одну или несколько подсистем

``json
kubectl get pod
```

 

Удаление стручка

``json
kubectl delete pod <имя_под>
```

 

Отображение подробного состояния подсистемы

``json
kubectl describe pod <pod_name>
```

 

Создание стручка

``json
kubectl create pod <имя_под>
```

 

Выполнение команды над контейнером в стручке

``json
kubectl exec <имя_под> -c <имя_контейнера> <команда>
```

 

Получение интерактивной оболочки для одноконтейнерного стручка

``json
kubectl exec -it <имя_пода> /bin/sh
```

 

Отображение использования ресурсов (CPU/Memory/Storage) для подсистем

``json
kubectl top pod
```

 

Добавление или обновление аннотаций стручка

``json
kubectl annotate pod <pod_name> <annotation>
```

 

Добавляет или обновляет метку капсулы

``json
kubectl label pod <pod_name>
```

 

## Контроллеры репликации

**Shortcode = rc**

Список контроллеров репликации

``json
kubectl get rc
```

 

Список контроллеров репликации по пространству имен

``json
kubectl get rc --namespace="<имя_пространства_имен>"
```

 

## ReplicaSets

**Shortcode = rs**

Список ReplicaSets

``json
kubectl get replicasets
```

 

Отображение подробного состояния одного или нескольких наборов реплик

``json
kubectl describe replicasets <имя_репликасета>
```

 

Масштабирование набора реплик

``json
kubectl scale --replicas=[x]
```

 

## Секреты

Создать секрет

``json
kubectl create secret
```

 

Список секретов

``json
kubectl get secrets
```

 

Вывод подробной информации о секретах

``json
kubectl describe secrets
```

 

Удалить секрет

``json
kubectl delete secret <secret_name>
```

 

## Услуги

**Shortcode = svc**

Перечислите одну или несколько услуг

``json
kubectl get services
```

 

Отображение подробного состояния сервиса

``json
kubectl describe services
```

 

Раскрытие контроллера репликации, сервиса, развертывания или стручка в качестве нового сервиса Kubernetes

``json
kubectl expose deployment [deployment_name]
```

 

Редактирование и обновление определения одного или нескольких сервисов

``json
kubectl edit services
```

 

## Учетные записи служб

**Shortcode = sa**

Список счетов обслуживания

``json
kubectl get serviceaccounts
```

 

Отображение подробного состояния одной или нескольких учетных записей сервисов

``json
kubectl describe serviceaccounts
```

 

Замена учетной записи сервиса

``json
kubectl replace serviceaccount
```

 

Удаление учетной записи сервиса

``json
kubectl delete serviceaccount <имя_сервисного_аккаунта>
```

 

## StatefulSet

**Shortcode = sts**

Список StatefulSet

``json
kubectl get statefulset
```

 

Удаление только набора StatefulSet (не стручков)

``json
kubectl delete statefulset/[stateful_set_name] --cascade=false
```

 

## Общие параметры

В Kubectl можно указывать необязательные флаги в командах. Ниже приведены некоторые из наиболее распространенных и полезных.

 

-o Формат вывода. Например, если вы хотите вывести список всех капсул в формате ps с дополнительной информацией.

``json
kubectl get pods -o wide
```

 

-n Сокращение от --namespace. Например, если вы хотите получить список всех модулей в определенном пространстве имен, то выполните следующую команду:

``json
kubectl get pods --namespace=[имя_пространства_имен]
```

 

``json
kubectl get pods -n=[имя_пространства_имени]
```

 

-f Имя файла, директория или URL-адрес файлов для использования при создании ресурса. Например, при создании капсулы с использованием данных в файле с именем newpod.json.

``json
kubectl create -f ./newpod.json
```

 

-l Селектор для фильтрации, поддерживает '=', '==' и '!='.

 

Справка по kubectl

-h