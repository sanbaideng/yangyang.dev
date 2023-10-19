---
title: Git
date: 2020-11-25 18:28:43
фон: bg-[#d7593e]
теги:
    - github
    - gitlab
    - версия
    - VCS
категории:
    - Linux Command
Введение: Эта шпаргалка содержит краткое описание часто используемых команд командной строки Git для быстрого ознакомления.
плагины:
    - copyCode
---

Начало работы
---------------

### Создание репозитория
Создайте новый локальный репозиторий
``Сценарий оболочки
$ git init [имя проекта]
```

Клонировать репозиторий
``Скрипт оболочки
$ git clone git_url
```

Клонирование репозитория в указанную директорию
``` shell script
$ git clone git_url my_directory
```




### Внести изменения {.row-span-2}
Показать измененные файлы в рабочем каталоге, поставленные для следующей фиксации
``Сценарий оболочки
$ git status
```

Ставит файл в состояние готовности к фиксации
``Скрипт оболочки
$ git add [file]
```

Ставит все измененные файлы, готовые к фиксации
``Сценарий оболочки
$ git add .
```

Зафиксировать все поэтапные файлы в истории версий
``Скрипт оболочки
$ git commit -m "commit message"
```

Зафиксировать все отслеживаемые файлы в истории версий
``` сценарий оболочки
$ git commit -am "commit message"
```
Отбросить изменения в рабочем каталоге, который не является ступенчатым
``Скрипт оболочки
$ git restore [file]
```
Снять с хранения ступенчатый файл или файл, который является ступенчатым
``Скрипт оболочки
$ git restore --staged [file]
```

Снять файл с сохранением изменений в файле
``сценарий оболочки
$ git reset [file]
```

Вернуть все к последнему коммиту
``Скрипт оболочки
$ git reset --hard
```

Diff того, что изменено, но не поставлено
``Скрипт оболочки
$ git diff
```

Дифф того, что поставлено, но еще не зафиксировано
``Скрипт оболочки
$ git diff --staged
```

Применить все коммиты текущей ветки вперед указанной
``Скрипт оболочки
$ git rebase [branch]
```


### Конфигурация

Задайте имя, которое будет прикрепляться к вашим коммитам и тегам
``Сценарий оболочки
$ git config --global user.name "name"
```

Установка адреса электронной почты, который будет прикрепляться к вашим коммитам и тегам
``` сценарий оболочки
$ git config --global user.email "email"
```

Включить некоторую раскраску вывода Git'а
``` сценарий оболочки
$ git config --global color.ui auto
```

Редактирование файла глобальной конфигурации в текстовом редакторе
``` сценарий оболочки
$ git config --global --edit
```



### Работа с ветвями

Список всех локальных ветвей
``Сценарий оболочки
$ git branch
```

Список всех ветвей, локальных и удаленных
``` сценарий оболочки
$ git branch -av
```

Переключение на ветку my_branch и обновление рабочего каталога
``Скрипт оболочки
$ git checkout my_branch
```

Создать новую ветку с именем new_branch
``Скрипт оболочки
$ git checkout -b new_branch
```

Удалить ветку с именем my_branch
``` сценарий оболочки
$ git branch -d my_branch
```

Объединить веткуА с веткойВ
``` сценарий оболочки
$ git checkout branchB
$ git merge branchA
```

Пометить текущий коммит
``Сценарий оболочки
$ git tag my_tag
```



### Наблюдение за вашим репозиторием
Показать историю коммитов для активной в данный момент ветки
``Сценарий оболочки
$ git log
```
Показать коммиты на веткеА, которых нет на веткеВ
``` сценарий оболочки
$ git log branchB..branchA
```
Показать коммиты, изменившие файл, даже при переименовании
``` shell script
$ git log --follow [file]
```
Показать разницу между тем, что есть в веткеА, и тем, чего нет в веткеВ
``` сценарий оболочки
$ git diff branchB...branchA
```
Показать любой объект в Git в человекочитаемом формате
``Сценарий оболочки
$ git show [SHA]
```



### Синхронизация

Получить все ветки с данного Git-узла
``Сценарий оболочки
$ git fetch [alias]
```

Слияние удаленной ветки с текущей веткой для приведения ее в актуальное состояние
``Скрипт оболочки
$ git merge [alias]/[branch]
# Без перемотки вперед
$ git merge --no-ff [alias]/[branch]
# Только быстрая перемотка
$ git merge --ff-only [alias]/[branch]
```

Передача коммитов локальной ветки в ветку удаленного репозитория
``Сценарий оболочки
$ git push [alias] [branch]
```

Получить и объединить все коммиты из отслеживаемой удаленной ветки
``Сценарий оболочки
$ git pull
```

Слияние только одного конкретного коммита из другой ветки в вашу текущую ветку
``Скрипт оболочки
$ git cherry-pick [commit_id]
```




### Удаленный
Добавление URL-адреса git в качестве псевдонима
``Сценарий оболочки
$ git remote add [alias] [url]
```

Показать имена настроенных удаленных репозиториев
``` сценарий оболочки
$ git remote
```

Показать имена и URL-адреса удаленных репозиториев
``Сценарий оболочки
$ git remote -v
```

Удалить удаленный репозиторий
``` сценарий оболочки
$ git remote rm [имя удаленного репозитория]
```

Изменить URL-адрес git-репозитория
``` сценарий оболочки
$ git remote set-url origin [git_url]
```






### Временные фиксации

Сохранение модифицированных и поэтапных изменений
``Сценарий оболочки
$ git stash
```

Перечислить порядок хранения изменений в файлах
``Сценарий оболочки
$ git stash list
```

Запись работы с вершины стека хранения
``Скрипт оболочки
$ git stash pop
```

Удаление изменений из верхней части стека stash
``сценарий оболочки
$ git stash drop
```




### Отслеживание изменений пути
Удаление файла из проекта и постановка удаления на фиксацию
``Сценарий оболочки
$ git rm [file]
```

Изменение пути к существующему файлу и постановка перемещения
``Сценарий оболочки
$ git mv [existing-path] [new-path]
```

Показать все журналы фиксации с указанием путей, которые были перемещены
``` сценарий оболочки
$ git log --stat -M
```


### Игнорирование файлов

```
/logs/*

# "!" означает не игнорировать
!logs/.gitkeep

/# Игнорировать системные файлы Mac
.DS_store

# Игнорировать папку node_modules
node_modules

# Игнорировать файлы конфигурации SASS
.sass-cache
```
Файл `.gitignore` задает намеренно неотслеживаемые файлы, которые Git должен игнорировать



Трюки Git
------

### Переименование ветки
- #### **Переименована** в `new_name`.
    командный сценарий
    $ git branch -m <new_name>
    ```
- #### **Толкаем** и сбрасываем.
    ``Шелл-скрипт
    $ git push origin -u <new_name>
    ```
- #### **Удаление** удаленной ветки
    ```Шелл-скрипт
    $ git push origin --delete <old>
    ```
{.marker-timeline}


### Журнал
Поиск изменений по содержимому
командный сценарий
$ git log -S'<a термин в источнике>'
```
Показать изменения во времени для конкретного файла
``Шелл-скрипт
$ git log -p <имя_файла>
```
Вывести классную визуализацию вашего журнала
```Шелл-скрипт {.wrap}
$ git log --pretty=oneline --graph --decorate --all
```

### Ветви {.row-span-2}
Список всех ветвей и их восходящих потоков
``` Шелл-скрипт
$ git branch -vv
```
Быстрый переход к предыдущей ветке
```Шелл-скрипт
$ git checkout -vv
```
Получение только удаленных веток
```Шелл-скрипт
$ git branch -r
```
Проверка одного файла из другой ветки
```Шелл-скрипт
$ git checkout <branch> -- <file>
```



### Переписывание истории
Переписать последнее сообщение о фиксации
командный сценарий
$ git commit --amend -m "new message"
```

Внесение изменений в последний коммит без изменения сообщения коммита.
``Основной сценарий
$ git commit --amend --no-edit
```


См. также: [Переписывание истории](https://www.atlassian.com/git/tutorials/rewriting-history)


### Псевдонимы Git
``cmd
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
```
См. также: [Другие псевдонимы](https://gist.github.com/johnpolacek/69604a1f6861129ef088)


Расширенный Git
------------

### Субмодули

Создайте новый подмодуль в вашем репозитории:
``шелл-скрипт
$ git submodule add <repository_url> <path>
```

Клонирование репозитория и инициализация его субмодулей:
```шелл-скрипт
$ git clone --recursive <repository_url>
```
Обновите все подмодули в репозитории до последней фиксации соответствующих веток:
``шелл-скрипт
$ git submodule update
```

Извлеките последние изменения из удаленных репозиториев подмодулей и обновите их в своем основном репозитории:
``Основной скрипт
$ git submodule update --remote
```

Удалить подмодуль из репозитория:
``шелл-скрипт
$ git submodule deinit <path>
$ git rm <путь>
$ git commit -m "Удален субмодуль"
```

### Cherry-picking
Cherry-picking позволяет применить определенный коммит из одной ветки к другой ветке.

``` Шелл-скрипт
$ git cherry-pick <commit_hash>
```

### Рефлог

Отображение рефлога, показывающего историю перемещений HEAD и ветки:
``Основной сценарий
$ git reflog
```

Найдите хэш потерянного коммита или ветки с помощью reflog и выполните checkout на этот хэш для его восстановления:
``шелл-скрипт
$ git checkout <хэш_коммита_или_ветви>
```