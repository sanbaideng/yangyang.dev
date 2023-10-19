---
title: PostgreSQL
фон: bg-[#3d6488]
теги:
    - БД
    - РСУБД
категории:
  - Базы данных
date: 2021-01-11 14:19:24
intro: |
    Шпаргалка [PostgreSQL](https://www.postgresql.org/docs/current/) знакомит с общими командами и операторами PostgreSQL.
плагины:
    - copyCode
---



Начало работы
---------------

### Начало работы
Переключение и подключение
``Сценарий оболочки
$ sudo -u postgres psql
```

Вывести список всех баз данных
```Основной скрипт
postgres=# \l
```

Подключение к базе данных с именем postgres
```Шелл-скрипт
postgres=# \c postgres
```

Отключить
```Шелл-скрипт
postgres=# \q
postgres=# \!
```


### Команды psql {.col-span-2}
| Опция | Пример | Описание |
|---------------------|----------------------------------------------|--------------------------------|
| `[-d] <база данных>` | psql -d mydb | Подключение к базе данных |
| `-U` | psql -U john mydb | Подключение от имени конкретного пользователя |
| `-h` `-p` | psql -h localhost -p 5432 mydb | Подключение к хосту/порту |
| `-U` `-h` `-p` `-d` | psql -U admin -h 192.168.1.5 -p 2506 -d mydb | Подключение удаленного PostgreSQL |
| `-W` | psql -W mydb | Принудительный ввод пароля |
| `-c` | psql -c '\c postgres' -c '\dt' | Выполнить SQL-запрос или команду |
| `-H` | psql -c "\l+" -H postgres > database.html | Создать HTML-отчет |
| `-l` | psql -l | Вывести список всех баз данных |
| `-f` | psql mydb -f file.sql | Выполнение команд из файла |
| `-V` | psql -V | Вывести версию psql |
{.show-header}


### Получение справки

| - | - |
|-------------|--------------------------------|
| `\h` | Справка по синтаксису команд SQL |
| `\h` DELETE | Синтаксис SQL-запроса DELETE |
| `\?` | Список команд PostgreSQL |

Запуск в консоли PostgreSQL



Работа с PostgreSQL
-------

### Recon
Показать версию
```
SHOW SERVER_VERSION;
```
Показать состояние системы
```sql {.wrap}
\conninfo
```
Показать переменные окружения
```sql {.wrap}
SHOW ALL;
```
Показать список пользователей
```sql {.wrap}
SELECT rolname FROM pg_roles;
```
Показать текущего пользователя
```sql {.wrap}
SELECT current_user;
```
Показать права доступа текущего пользователя
```
\du
```
Показать текущую базу данных
```ql {.wrap}
SELECT current_database();
```
Показать все таблицы в базе данных
```sql {.wrap}
\dt
```
Перечислить функции
```sql {.wrap}
\df <schema>
```



### Базы данных

Список баз данных
```ql {.wrap}
\l
```
Подключиться к базе данных
```sql {.wrap}
\c <имя_базы_данных>
```
Показать текущую базу данных
```sql {.wrap}
SELECT current_database();
```
[Создать базу данных](http://www.postgresql.org/docs/current/static/sql-createdatabase.html)
```sql {.wrap}
CREATE DATABASE <имя_базы_данных> WITH OWNER <имя_пользователя>;
```
[Drop database](http://www.postgresql.org/docs/current/static/sql-dropdatabase.html)
```sql {.wrap}
DROP DATABASE IF EXISTS <database_name>;
```
[Переименовать базу данных](http://www.postgresql.org/docs/current/static/sql-alterdatabase.html)
```sql {.wrap}
ALTER DATABASE <old_name> RENAME TO <new_name>;
```



### Таблицы

Список таблиц в текущей базе данных
```ql {.wrap}
\dt

SELECT table_schema,table_name FROM information_schema.tables ORDER BY table_schema,table_name;
```
Перечислить таблицы в глобальном порядке
```sql {.wrap}
\dt *.*.

SELECT * FROM pg_catalog.pg_tables
```
Перечислить схему таблицы
```sql {.wrap}
\d <имя_таблицы>
\d+ <имя_таблицы>

SELECT имя_колонки, тип_данных, максимальная_длина_символа
ИЗ INFORMATION_SCHEMA.COLUMNS
WHERE имя_таблицы = '<имя_таблицы>';
```
[Создать таблицу](http://www.postgresql.org/docs/current/static/sql-createtable.html)
```sql {.wrap}
CREATE TABLE <table_name>(
  <column_name> <column_type>,
  <имя_столбца> <тип_столбца>
);
```
Создание таблицы с автоинкрементным первичным ключом
```sql {.wrap}
CREATE TABLE <table_name> (
  <имя_столбца> SERIAL PRIMARY KEY
);
```
[Удалить таблицу](http://www.postgresql.org/docs/current/static/sql-droptable.html)
```sql {.wrap}
DROP TABLE IF EXISTS <table_name> CASCADE;
```



### Разрешения
Станьте пользователем postgres, если у вас есть ошибки в правах
``hell
sudo su - postgres
psql
```
[Grant](http://www.postgresql.org/docs/current/static/sql-grant.html) все разрешения на базу данных
```sql {.wrap}
GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <user_name>;
```
Предоставление прав на подключение к базе данных
```sql {.wrap}
GRANT CONNECT ON DATABASE <db_name> TO <user_name>;
```
Предоставление прав на схему
```sql {.wrap}
GRANT USAGE ON SCHEMA public TO <user_name>;
```
Предоставление прав на функции
```sql {.wrap}
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO <user_name>;
```
Предоставление прав на выборку, обновление, вставку, удаление для всех таблиц
```sql {.wrap}
GRANT SELECT, UPDATE, INSERT ON ALL TABLES IN SCHEMA public TO <user_name>;
```
Предоставление прав доступа к таблице
```ql {.wrap}
GRANT SELECT, UPDATE, INSERT ON <table_name> TO <user_name>;
```
Предоставление прав на выборку в таблице
```sql {.wrap}
GRANT SELECT ON ALL TABLES IN SCHEMA public TO <user_name>;
```






### Колонки

[Добавить колонку](http://www.postgresql.org/docs/current/static/sql-altertable.html)
```ql {.wrap}
ALTER TABLE <table_name> IF EXISTS
ADD <column_name> <data_type> [<constraints>];
```
Обновление столбца
```sql {.wrap}
ALTER TABLE <table_name> IF EXISTS
ALTER <имя_колонки> TYPE <data_type> [<constraints>];
```
Удаление столбца
```sql {.wrap}
ALTER TABLE <table_name> IF EXISTS
DROP <column_name>;
```
Обновить столбец, сделав его автоинкрементным первичным ключом
```sql {.wrap}
ALTER TABLE <table_name>
ADD COLUMN <column_name> SERIAL PRIMARY KEY;
```
Вставка в таблицу с автоинкрементным первичным ключом
```sql {.wrap}
INSERT INTO <имя_таблицы>
VALUES (DEFAULT, <value1>);


INSERT INTO <table_name> (<column1_name>,<column2_name>)
VALUES ( <value1>,<value2> );
```



### Данные
[Select](http://www.postgresql.org/docs/current/static/sql-select.html) all data
```ql {.wrap}
SELECT * FROM <имя_таблицы>;
```
Чтение одного ряда данных
```sql {.wrap}
SELECT * FROM <имя_таблицы> LIMIT 1;
```
Поиск данных
```sql {.wrap}
SELECT * FROM <table_name> WHERE <column_name> = <value>;
```
[Вставка](http://www.postgresql.org/docs/current/static/sql-insert.html) данных
```sql {.wrap}
INSERT INTO <table_name> VALUES( <value_1>, <value_2> );
```
[Update](http://www.postgresql.org/docs/current/static/sql-update.html) данные
```sql {.wrap}
UPDATE <table_name>
SET <column_1> = <value_1>, <column_2> = <value_2>
WHERE <column_1> = <value>;
```
[Удалить](http://www.postgresql.org/docs/current/static/sql-delete.html) все данные
```sql {.wrap}
DELETE FROM <имя_таблицы>;
```
Удалить конкретные данные
```sql {.wrap}
DELETE FROM <имя_таблицы>
WHERE <column_name> = <value>;
```





### Пользователи

Список ролей
```ql {.wrap}
SELECT rolname FROM pg_roles;
```
[Создать пользователя](http://www.postgresql.org/docs/current/static/sql-createuser.html)
```sql {.wrap}
CREATE USER <имя_пользователя> WITH PASSWORD '<пароль>';
```
[Drop user](http://www.postgresql.org/docs/current/static/sql-dropuser.html)
```sql {.wrap}
DROP USER IF EXISTS <user_name>;
```
[Alter](http://www.postgresql.org/docs/current/static/sql-alterrole.html) пароль пользователя
```sql {.wrap}
ALTER ROLE <имя_пользователя> WITH PASSWORD '<пароль>';
```


### Схема
Список схем
```sql {.wrap}
\dn

SELECT schema_name FROM information_schema.schemata;

SELECT nspname FROM pg_catalog.pg_namespace;
```
[Create schema](http://www.postgresql.org/docs/current/static/sql-createschema.html)
```sql {.wrap}
CREATE SCHEMA IF NOT EXISTS <schema_name>;
```
[Drop schema](http://www.postgresql.org/docs/current/static/sql-dropschema.html)
```sql {.wrap}
DROP SCHEMA IF EXISTS <schema_name> CASCADE;
```


### Даты

Показать [текущую дату](https://www.postgresql.org/docs/15/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT) ГГГГ-ММ-ДД
```ql {.wrap}
SELECT current_date;
```
Вычислить [возраст](https://www.postgresql.org/docs/15/functions-datetime.html#:~:text=age%20(%20timestamp%2C%20timestamp%20)%20%E2%86%92%20интервал) между двумя датами
```ql {.wrap}
SELECT age(timestamp, timestamp);
```
Показать [текущее время](https://www.postgresql.org/docs/15/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT) с учетом часового пояса
```sql {.wrap}
SELECT current_time;
```
[Make](https://www.postgresql.org/docs/15/functions-datetime.html#:~:text=make_date%20(%20year%20int%2C%20month%20int%2C%20day%20int%20)%20%E2%86%92%20date) даты с использованием целых чисел
```ql {.wrap}
SELECT make_date(2021,03,25);
```



Команды PostgreSQL
-----------

### Таблицы
| - | - |
|------------------|---------------------------------|
| `\d <table>` | Описать таблицу |
| `\d+ <table>` | Описать таблицу с подробностями |
| `\dt` | Список таблиц из текущей схемы |
| `\dt *.*` | Список таблиц из всех схем |
| `\dt <schema>.*` | Список таблиц для схемы |
| `\dp` | Список привилегий доступа к таблицам |
| `\det[+]` | Список иностранных таблиц |



### Буфер запросов
| - | - |
|--------------|------------------------------------|
| `\e [FILE]` | Редактировать буфер запроса (или файл) |
| `\ef [FUNC]` | Редактировать определение функции |
| `\p` | Показать содержимое |
| `\r` | Сбросить (очистить) буфер запроса |
| `\s [FILE]` | Показать историю или сохранить ее в файл |
| `\w FILE` | Записать буфер запроса в файл |



### Информационный {.row-span-4}
| - | - |
|-----------------|---------------------------------|
| `\l[+]` | Список всех баз данных |
| `\dn[S+]` | Список схем |
| `\di[S+]` | Список индексов |
| `\du[+]` | Список ролей |
| `\ds[S+]` | Список последовательностей |
| `\df[antw][S+]` | Список функций |
| `\deu[+]` | Список отображений пользователей |
| `\dv[S+]` | Список представлений |
| `\dl` | Список больших объектов |
| `\dT[S+]` | Список типов данных |
| `\da[S]` | Список агрегатов |
| `\db[+]` | Список табличных пространств |
| `\dc[S+]` | Список преобразований |
| `\dC[+]` | Приведение к списку |
| `\ddp` | Список привилегий по умолчанию |
| `\dd[S]` | Показать описания объектов |
| `\dD[S+]` | Список доменов |
| `\des[+]` | Список иностранных серверов |
| `\dew[+]` | Список обёрток для иностранных данных |
| `\dF[+]` | Список конфигураций текстового поиска |
| `\dFd[+]` | Список словарей для поиска текста |
| `\dFp[+]` | Список парсеров для поиска текста |
| `\dFt[+]` | Список шаблонов текстового поиска |
| `\dL[S+]` | Список процедурных языков |
| `\do[S]` | Список операторов |
| `\dO[S+]` | Список колаций |
| `\drds` | Список ролевых настроек для каждой базы данных |
| `\dx[+]` | Список расширений |

`S`: показать системные объекты, `+`: дополнительная детализация


### Соединение
| - | - |
|------------------------|-----------------------------|
| `\c [DBNAME]` | Подключение к новой базе данных |
| `\encoding [ENCODING]` | Показать или установить кодировку клиента |
| `\password [USER]` | Изменить пароль |
| `\conninfo` | Показать информацию |


### Форматирование
| - | - |
|---------------|--------------------------------------------|
| `\a` | Переключение между выравниванием и выравниванием |
| `\C [STRING]` | Установить заголовок таблицы или снять его, если он отсутствует |
| `\f [STRING]` | Показать или установить разделитель полей для невыровненных |
| `\H` | Переключение режима вывода HTML |
| `\t [on|off]` | Показать только строки |
| `\T [STRING]` | Установить или снять атрибуты тега HTML \<table\> |
| `\x [on|off]` | Включить расширенный вывод |



### Ввод/вывод
| - | - |
|-------------------|----------------------------------------------------------------|
| `\copy ...` | Импорт/экспорт таблицы<br> _См. также:_ [copy](#import-export-csv)|
| `\echo [STRING]` | Вывести строку |
| `\i FILE` | Выполнить файл |
| `\o [FILE]` | Экспорт всех результатов в файл |
| `\qecho [STRING]` | Вывести строку в выходной поток |


### Переменные
| - | - |
|-----------------------|-----------------------------------------------|
| `\prompt [TEXT] NAME` | Установить переменную |
| `\set [NAME [VALUE]]` | Установить переменную _(или перечислить все, если нет параметров)_ |
| `\unset NAME` | Удалить переменную |


### Misc
| - | - |
|--------------------|----------------------|
| `\cd [DIR]` | Изменить каталог |
| `\timing [on|off]` | Переключение синхронизации |
| `\! [COMMAND]` | Выполнить в оболочке |
| `\! ls -l` | Перечислить все в оболочке |


### Большие объекты
- `\lo_export LOBOID FILE`
- `\lo_import FILE [COMMENT]`
- `\lo_list`
- `\lo_unlink LOBOID`





Разное
-------------


### Резервное копирование
Используйте pg_dumpall для резервного копирования всех баз данных
'''shell-скрипт
$ pg_dumpall -U postgres > all.sql
```
Использование pg_dump для резервного копирования базы данных
командный сценарий
$ pg_dump -d mydb -f mydb_backup.sql
```

- &nbsp; `-a` &nbsp; Выгружать только данные, но не схему
- &nbsp; `-s` &nbsp; Дамп только схемы, без данных
- &nbsp; `-c` &nbsp; Сбросить базу данных перед воссозданием
- &nbsp; `-C` &nbsp; Создать базу данных перед восстановлением
- &nbsp; `-t` &nbsp; Дамп только именованной таблицы (таблиц)
- &nbsp; `-F` &nbsp; Формат (`c`: custom, `d`: directory, `t`: tar)
{.marker-none}

Для получения полного списка опций используйте команду `pg_dump -?`.



### Восстановление
Восстановление базы данных с помощью psql
командный сценарий
$ psql -U user mydb < mydb_backup.sql
```
Восстановление базы данных с помощью pg_restore
``Основной сценарий
$ pg_restore -d mydb mydb_backup.sql -c
```

- &nbsp; `-U` &nbsp; Укажите пользователя базы данных
- &nbsp; `-c` &nbsp; Сбросить базу данных перед воссозданием
- &nbsp; `-C` &nbsp; Создать базу данных перед восстановлением
- &nbsp; `-e` &nbsp; Выход при возникновении ошибки
- &nbsp; `-F` &nbsp; Format (`c`: custom, `d`: directory, `t`: tar, `p`: plain text sql(default))
{.marker-none}

Используйте `pg_restore -?` для получения полного списка опций



### Удаленный доступ
Получение местоположения файла postgresql.conf
'''shell-скрипт
$ psql -U postgres -c 'SHOW config_file'
```
Добавить в postgresql.conf
```Шелл-скрипт
listen_addresses = '*'
```
Добавьте в pg_hba.conf (в том же месте, что и postgresql.conf)
```shell script
host all all 0.0.0.0/0 md5
host all all ::/0 md5
```
Перезапустите сервер PostgreSQL
```Шелл-скрипт
$ sudo systemctl restart postgresql
```


### Импорт/экспорт CSV
Экспорт таблицы в CSV-файл
```Основной сценарий
\copy table TO '<path>' CSV
\copy table(col1,col1) TO '<path>' CSV
\copy (SELECT...) TO '<path>' CSV
```
Импорт CSV-файла в таблицу
``Основной сценарий
\copy table FROM '<path>' CSV
\copy table(col1,col1) FROM '<path>' CSV
```
См. также: [Copy](https://www.postgresql.org/docs/current/sql-copy.html)

Также см.
--------
- [Posgres-cheatsheet](https://gist.github.com/apolloclark/ea5466d5929e63043dcf#posgres-cheatsheet) _(gist.github.com)_
