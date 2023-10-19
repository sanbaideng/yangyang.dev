---
title: Kubernetes
date: 2023-01-09 10:26:55
фон: bg-[#416cde]
теги:
   - config
   - формат
категории:
   - Программирование
intro: |
    На этой странице приведен список часто используемых команд и флагов kubectl.

плагины:
    - copyCode
---


# Kubernetes
---



### Узлы


``bash
kubectl get no # Показать всю информацию об узлах
kubectl get no -o wide # Показать дополнительную информацию обо всех узлах
kubectl describe no # Показать подробную информацию об узле
kubectl get no -o yaml # Показать подробную информацию об узле в формате yaml
kubectl get node --selector=[имя_метки] # Отфильтровать узлы с указанной меткой
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type="ExternalIP")].address}'
# Вывести информацию о поле, заданную выражением jsonpath
kubectl top node [имя_узла] # Отображение использования узла (процессор/память/хранилище)
```

Имя ресурса: nodes, сокращение: no



### Узлы


``bash
kubectl get po # Отображение информации обо всех группах контейнеров
kubectl get po -o wide
kubectl describe po
kubectl get po --show-labels # Просмотр меток группы контейнеров
kubectl get po -l app=nginx
kubectl get po -o yaml
kubectl get pod [pod_name] -o yaml --export
kubectl get pod [pod_name] -o yaml --export > nameoffile.yaml
# Экспорт информации о группе контейнеров в файл в формате yaml
kubectl get pods --field-selector status.phase=Running
# Используйте селектор полей для фильтрации информации о группах контейнеров
```

Имя ресурса: pods, сокращение: po



### Пространства имен


``bash
kubectl get ns
kubectl get ns -o yaml
kubectl describe ns
```

Имя ресурса: пространства имен, сокращение: ns



### Развертывания


``bash
kubectl get deploy
kubectl describe deploy
kubectl get deploy -o wide
kubectl get deploy -o yaml
```
Имя ресурса: deployments, сокращение: deploy



### Услуги


``bash
kubectl get svc
kubectl describe svc
kubectl get svc -o wide
kubectl get svc -o yaml
kubectl get svc --show-labels
```
Имя ресурса: services, сокращение: svc



### Наборы демонов


``bash
kubectl get ds
kubectl describe ds --all-namespaces
kubectl describe ds [имя_демона] -n [имя_пространства_имен]
kubectl get ds [ds_name] -n [ns_name] -o yaml
```
Имя ресурса: daemonsets, сокращение: ds



### События


``bash
kubectl get events
kubectl get events -n kube-system
kubectl get events -w
```

Имя ресурса: events, сокращение: ev



### Журналы

``bash
kubectl logs [pod_name]
kubectl logs --since=1h [pod_name]
kubectl logs --tail=20 [pod_name]
kubectl logs -f -c [имя_контейнера] [имя_пода]
kubectl logs [pod_name] > pod.log
```



### Учетные записи служб


``bash
kubectl get sa
kubectl get sa -o yaml
kubectl get serviceaccounts default -o yaml >./sa.yaml
kubectl replace serviceaccounts default -f ./sa.yaml
```
Имя ресурса: serviceaccounts, сокращение: ev



### Наборы реплик


``bash
kubectl get rs
kubectl describe rs
kubectl get rs -o wide
kubectl get rs -o yaml
```

Имя ресурса: replicasets, сокращение: rs



### Роли

``bash
kubectl get roles --all-namespaces
kubectl get roles --all-namespaces -o yaml
```



### Секреты

``bash
kubectl get secrets
kubectl get secrets --all-namespaces
kubectl get secrets -o yaml
```



### Карты конфигурации

Имя ресурса: configmaps, сокращение: cm

``bash
kubectl get cm
kubectl get cm --all-namespaces
kubectl get cm --all-namespaces -o yaml
```



### Ингрессы

Название ресурса: ingresses, сокращение: ing

``bash
kubectl get ing
kubectl get ing --all-namespaces
```



### Постоянные тома

Имя ресурса: persistentvolumes, сокращение: pv

``bash
kubectl get pv
kubectl describe pv
```



### Объявление постоянного тома

Имя ресурса: persistentvolumeclaims, сокращение: pvc

``bash
kubectl get pvc
kubectl describe pvc
```



### класс хранилища

Имя ресурса: storageclasses, Сокращение: sc

``bash
kubectl get sc
kubectl get sc -o yaml
```



### Множественные ресурсы

``bash
kubectl get svc, po
kubectl get deploy, no
kubectl get all
kubectl get all --all-namespaces
```

Обновление ресурсов
---



### Taint

``bash
kubectl taint [node_name] [taint_name]
```



### Label

``bash
kubectl label [имя_узла] disktype=ssd
kubectl label [pod_name] env=prod
```



### Поддерживаемые/настраиваемые

``bash
kubectl cordon [имя_узла] # обслуживание узла
kubectl uncordon [имя_узла] # узел доступен для планирования
```



### clear

``bash
kubectl drain [имя_узла] # очистить узел
```



### Node/Pod {.row-span-2}

``bash
kubectl delete node [имя_узла]
kubectl delete pod [pod_name]
kubectl edit node [node_name]
kubectl edit pod [pod_name]
```



### Stateless/Namespaced {.row-span-2}

``bash
kubectl edit deploy [deploy_name]
kubectl delete deploy [deploy_name]
kubectl expose deploy [deploy_name] --port=80 --type=NodePort
kubectl scale deploy [deploy_name] --replicas=5
kubectl delete ns
kubectl edit ns [ns_name]
```



### Сервис

``bash
kubectl edit svc [svc_name]
kubectl delete svc [svc_name]
```



### Набор демонов
``bash
kubectl edit ds [ds_name] -n kube-system
kubectl delete ds [ds_name]
```



### Учетная запись службы

``bash
kubectl edit sa [sa_name]
kubectl delete sa [sa_name]
```



### Примечания

``bash
kubectl annotate po [pod_name] [annotation]
kubectl annotateno [имя_узла]
```

Создание ресурсов
---



### Создать капсулу

``bash
kubectl create -f [имя_of_файла]
kubectl apply -f [имя_of_файла]
kubectl run [pod_name] --image=nginx --restart=Never
kubectl run [pod_name] --generator=run-pod/v1 --image=nginx
kubectl run [pod_name] --image=nginx --restart=Never
```



### Создать службу

``bash
kubectl create svc nodeport [svc_name] --tcp=8080:80
```



### Создание приложения без статического состояния

``bash
kubectl create -f [имя_of_файла]
kubectl apply -f [имя_of_файла]
kubectl create deploy [имя_развертывания] --image=nginx
```



### взаимодействие

``bash
kubectl run [pod_name] --image=busybox --rm -it --restart=Never --sh
```



### Выходной YAML

``bash
kubectl create deploy [deploy_name] --image=nginx --dry-run -o yaml > deploy.yaml
kubectl get po [имя_под] -o yaml --export > pod.yaml
```



### Справка

``bash
kubectl -h
kubectl create -h
kubectl run -h
kubectl explain deploy.spec
```


Разное
---



### API

``bash
kubectl get --raw /apis/metrics.k8s.io/
```



### Информация

``bash
kubectl config
kubectl cluster-info
kubectl get componentstatus
```

Также см.
---

- [Kubernetes Official Documentation](https://kubernetes.io/zh-cn/docs/reference/kubectl/) _(kubernetes.io)_
