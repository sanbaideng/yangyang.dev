---
title: MySQL
date: 2020-12-16 18:28:43
фон: bg-[#2a6387]
тэги:
    - РСУБД
    - БД
категории:
    - Базы данных
intro: Шпаргалка по SQL содержит наиболее часто используемые операторы SQL для справки.
плагины:
    - подсказка
    - copyCode
---


Начало работы {.cols-2}
---------------


### Подключение MySQL
```
mysql -u <user> -p

mysql [имя_базы]

mysql -h <host> -P <port> -u <user> -p [db_name]

mysql -h <host> -u <user> -p [db_name]
```



### Commons {.row-span-2}

#### База данных

| - | - |
|--------------------------|-----------------|
| `CREATE DATABASE` db `;` | Создать базу данных |
| `SHOW DATABASES;` | Список баз данных |
| `USE` db`;` | Переключиться на базу данных |
| `CONNECT` db`;` | Переключиться на db |
| `DROP DATABASE` db`;` | Удалить db |

#### Таблица

| - | - |
|--------------------------|----------------------------|
| `SHOW TABLES;` | Список таблиц для текущей базы данных |
| `SHOW FIELDS FROM` t`;` | Список полей для таблицы |
| `DESC` t`;` | Показать структуру таблицы |
| `SHOW CREATE TABLE `t`;` | Показать sql создания таблицы |
| `TRUNCATE TABLE `t`;` | Удалить все данные в таблице |
| `DROP TABLE `t`;` | Удалить таблицу |

#### Процесс

| - | - |
|---------------------|----------------|
| `show processlist;` | Список процессов |
| `kill` pid`;` | kill process |
#### Другое

| - | - |
|----------------|--------------------|
| `exit` или `\q` | Выход из сеанса MySQL |

### Резервное копирование

Создайте резервную копию
```ql
mysqldump -u user -p db_name > db.sql
```

Экспорт db без схемы
``` {.wrap}
mysqldump -u user -p db_name --no-data=true --add-drop-table=false > db.sql
```

Восстановление резервной копии
```
mysql -u user -p db_name < db.sql
```




Примеры MySQL
--------------


### Управление таблицами
Создайте новую таблицу с тремя столбцами

``ql
CREATE TABLE t (
     id INT,
     name VARCHAR DEFAULT NOT NULL,
     цена INT DEFAULT 0
     PRIMARY KEY(id)
);
```

Удаление таблицы из базы данных
```ql
DROP TABLE t ;
```

Добавить в таблицу новый столбец
```sql
ALTER TABLE t ADD column;
```

Удалить столбец c из таблицы
```ql
ALTER TABLE t DROP COLUMN c ;
```

Добавить ограничение
```sql
ALTER TABLE t ADD constraint;
```

Удалить ограничение
```ql
ALTER TABLE t DROP constraint;
```

Переименование таблицы из t1 в t2
```sql
ALTER TABLE t1 RENAME TO t2;
```

Переименовать столбец c1 в c2
```sql
ALTER TABLE t1 RENAME c1 TO c2 ;
```

Удалить все данные в таблице
```sql
TRUNCATE TABLE t;
```



### Запрос данных из таблицы
Запрос данных в столбцах c1, c2 из таблицы

```ql
SELECT c1, c2 FROM t
```


Запрос всех строк и столбцов из таблицы

```ql
SELECT * FROM t
```


Запрос данных и фильтрация строк с помощью условия

```ql
SELECT c1, c2 FROM t
ГДЕ условие
```


Запрос отдельных строк из таблицы

```ql
SELECT DISTINCT c1 FROM t
WHERE условие
```


Отсортировать набор результатов в порядке возрастания или убывания

```ql
SELECT c1, c2 FROM t
ORDER BY c1 ASC [DESC]
```


Пропустить смещение строк и вернуть следующие n строк

```ql
SELECT c1, c2 FROM t
ORDER BY c1
LIMIT n OFFSET offset
```


Группировка строк с помощью агрегатной функции

```ql
SELECT c1, aggregate(c2)
FROM t
GROUP BY c1
```


Фильтр групп с помощью предложения HAVING

```ql
SELECT c1, aggregate(c2)
FROM t
GROUP BY c1
условие HAVING
```


### Запрос из нескольких таблиц {.row-span-2}
Внутреннее соединение t1 и t2

``ql
SELECT c1, c2
из t1
INNER JOIN t2 ON condition
```


Левое соединение t1 и t1

```ql
SELECT c1, c2
из t1
LEFT JOIN t2 ON condition
```


Правое соединение t1 и t2

```ql
SELECT c1, c2
из t1
RIGHT JOIN t2 ON condition
```


Выполнить полное внешнее объединение

```ql
SELECT c1, c2
из t1
FULL OUTER JOIN t2 ON condition
```


Произвести декартово произведение строк в таблицах

```ql
SELECT c1, c2
из t1
CROSS JOIN t2
```


Другой способ выполнения перекрестного соединения

```ql
SELECT c1, c2
FROM t1, t2
```


Присоединим t1 к самому себе с помощью предложения INNER JOIN

```ql
SELECT c1, c2
FROM t1 A
INNER JOIN t1 B ON condition
```


Использование операторов SQL
Объединение строк из двух запросов

``ql
SELECT c1, c2 FROM t1
UNION [ALL]
SELECT c1, c2 FROM t2
```


Возвращает пересечение двух запросов

```ql
SELECT c1, c2 FROM t1
INTERSECT
SELECT c1, c2 FROM t2
```


Вычитание набора результатов из другого набора результатов

```ql
SELECT c1, c2 FROM t1
МИНУС
SELECT c1, c2 FROM t2
```


Запрос строк с использованием сопоставления шаблонов %, _

```ql
SELECT c1, c2 FROM t1
WHERE c1 [NOT] LIKE pattern
```


Запрос строк в списке

```ql
SELECT c1, c2 FROM t
WHERE c1 [NOT] IN value_list
```


Запрос строк между двумя значениями

```ql
SELECT c1, c2 FROM t
WHERE c1 BETWEEN low AND high
```


Проверка того, являются ли значения в таблице NULL или нет

```ql
SELECT c1, c2 FROM t
WHERE c1 IS [NOT] NULL
```


### Использование ограничений SQL


Установите c1 и c2 в качестве первичного ключа

``ql
CREATE TABLE t(
    c1 INT, c2 INT, c3 VARCHAR,
    PRIMARY KEY (c1,c2)
);
```


Установить столбец c2 в качестве внешнего ключа

```ql
CREATE TABLE t1(
    c1 INT PRIMARY KEY,
    c2 INT,
    FOREIGN KEY (c2) REFERENCES t2(c2)
);
```


Сделаем значения в c1 и c2 уникальными

``ql
CREATE TABLE t(
    c1 INT, c1 INT,
    UNIQUE(c2,c3)
);
```


Убедиться, что c1 > 0 и значения в c1 >= c2

```ql
CREATE TABLE t(
  c1 INT, c2 INT,
  CHECK(c1> 0 AND c1 >= c2)
);
```

Установить значения в столбце c2 не NULL

```ql
CREATE TABLE t(
     c1 INT PRIMARY KEY,
     c2 VARCHAR NOT NULL
);
```


### Модификация данных


Вставка одной строки в таблицу

``ql
INSERT INTO t(список_столбцов)
VALUES(value_list);
```


Вставка нескольких строк в таблицу

```ql
INSERT INTO t(список_столбцов)
VALUES (список_значений),
       (список_значений), ...;
```


Вставка строк из t2 в t1

```ql
INSERT INTO t1(список_колонок)
SELECT column_list
FROM t2;
```


Обновить новое значение в столбце c1 для всех строк

```ql
UPDATE t
SET c1 = new_value;
```


Обновление значений в столбцах c1, c2, соответствующих условию

```ql
UPDATE t
SET c1 = new_value,
        c2 = new_value
WHERE условие;
```


Удаление всех данных в таблице

```ql
DELETE FROM t;
```


Удаление подмножества строк в таблице

```ql
DELETE FROM t
WHERE условие;
```


### Управление представлениями


Создайте новое представление, состоящее из c1 и c2

``ql
CREATE VIEW v(c1,c2)
AS
SELECT c1, c2
FROM t;
```


Создайте новое представление с опцией проверки

``ql
CREATE VIEW v(c1,c2)
AS
SELECT c1, c2
FROM t;
С ОПЦИЕЙ ПРОВЕРКИ [CASCADED | LOCAL];
```


Создание рекурсивного представления

```ql
CREATE RECURSIVE VIEW v
AS
select-statement -- якорная часть
UNION [ALL]
select-statement; -- рекурсивная часть
```


Создайте временное представление

```ql
CREATE TEMPORARY VIEW v
AS
SELECT c1, c2
FROM t;
```


Удаление представления

```ql
DROP VIEW view_name;
```


### Управление триггерами


Создание или изменение триггера

```ql
CREATE OR MODIFY TRIGGER trigger_name
КОГДА СОБЫТИЕ
ON table_name TRIGGER_TYPE
EXECUTE stored_procedure;
```
#### WHEN

| - | - |
|----------|--------------------------------|
| `BEFORE` | вызов до наступления события |
| `AFTER` | вызов после наступления события |

#### СОБЫТИЕ

| - | - |
|----------|-------------------|
| `INSERT` | вызов для INSERT |
| `UPDATE` | вызов UPDATE |
| `DELETE` | вызов DELETE |

#### TRIGGER_TYPE

| - | - |
|----------------------|---|
| `ДЛЯ КАЖДОЙ СТРОКИ` | |
| `ДЛЯ КАЖДОГО ОПЕРАТОРА` | |




### Управление индексами

Создайте индекс на c1 и c2 таблицы t

``ql
CREATE INDEX idx_name
ON t(c1,c2);
```


Создадим уникальный индекс на c3, c4 таблицы t

```ql
CREATE UNIQUE INDEX idx_name
ON t(c3,c4)
```


Удаление индекса

```ql
DROP INDEX idx_name;
```


Типы данных MySQL
---------


### Строки

| - | - |
|--------------|-----------------------------|
| `CHAR` | Строка (0 - 255)|
| `VARCHAR` | Строка (0 - 255) |
| `TINYTEXT` | Строка (0 - 255)|
| `TEXT` | Строка (0 - 65535)|
| `BLOB` | String (0 - 65535) |
| `MEDIUMTEXT` | Строка (0 - 16777215)|
| `MEDIUMBLOB` | String (0 - 16777215) |
| `LONGTEXT` | String (0 - 4294967295)|
| `LONGBLOB` | String (0 - 4294967295)|
| `ENUM` | Один из предустановленных вариантов |
| `SET` | Выбор опций предустановки |


### Дата и время
| Тип данных | Формат |
|-------------|---------------------|
| `DATE` | yyyy-MM-dd |
| `TIME` | hh:mm:ss |
| `DATETIME` | yyyy-MM-dd hh:mm:ss |
| `TIMESTAMP` | yyyy-MM-dd hh:mm:ss |
| `YEAR` | yyyy |


### Числовой

| - | - |
|---------------|---------------------------------------------------------------|
| `TINYINT x` | Целое число (от -128 до 127)|
| `SMALLINT x` | Целое число (от -32768 до 32767)|
| `MEDIUMINT x` | Целое число (от -8388608 до 8388607)|
| `INT x` | Целое число (от -2147483648 до 2147483647)|
| `BIGINT x` | Целое число (от -9223372036854775808 до 9223372036854775807)|
| `FLOAT` | Десятичная система счисления (с точностью до 23 цифр) |
| `DOUBLE` | Десятичная дробь (от 24 до 53 цифр)|
| `DECIMAL` | "DOUBLE" хранится как строка |




Функции и операторы MySQL
---------


### Строки {.row-span-2}
- [ASCII()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_ascii){data-tooltip="Возвращает числовое значение крайнего левого символа"}
- [BIN()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_bin){data-tooltip="Возвращает строку, содержащую двоичное представление числа"}
- [BIT_LENGTH()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_bit-length){data-tooltip="Возвращает длину аргумента в битах"}
- [CHAR()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_char){data-tooltip="Возвращает символ для каждого переданного целого числа"}
- [CHARACTER_LENGTH()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_character-length){data-tooltip="Синоним CHAR_LENGTH()"}
- [CHAR_LENGTH()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_char-length){data-tooltip="Возвращает количество символов в аргументе"}
- [CONCAT()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_concat){data-tooltip="Возвращает конкатенированную строку"}
- [CONCAT_WS()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_concat-ws){data-tooltip="Возвращает конкатенацию с разделителем"}
- [ELT()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_elt){data-tooltip="Возвращает строку по номеру индекса"}
- [EXPORT_SET()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_export-set){data-tooltip="Возвращается строка, в которой для каждого установленного бита значения получается строка on, а для каждого неустановленного бита - строка off"}
- [FIELD()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_field){data-tooltip="Индекс (позиция) первого аргумента в последующих аргументах"}
- [FIND_IN_SET()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_find-in-set){data-tooltip="Индекс (позиция) первого аргумента внутри второго аргумента"}
- [FORMAT()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_format){data-tooltip="Возвращает число, отформатированное до указанного количества знаков после запятой"}
- [FROM_BASE64()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_from-base64){data-tooltip="Декодировать строку в кодировке base64 и вернуть результат"}
- [HEX()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_hex){data-tooltip="Шестнадцатеричное представление десятичного или строкового значения"}
- [INSERT()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_insert){data-tooltip="Вставить подстроку в указанную позицию до указанного количества символов"}
- [INSTR()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_instr){data-tooltip="Вернуть индекс первого вхождения подстроки"}
- [LCASE()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_lcase){data-tooltip="Синоним LOWER()"}
- [LEFT()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_left){data-tooltip="Возвращает крайнее левое число символов, как указано"}
- [LENGTH()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_length){data-tooltip="Возвращает длину строки в байтах"}
- [LIKE](https://dev.mysql.com/doc/refman/8.0/en/string-comparison-functions.html#operator_like){data-tooltip="Простое сопоставление шаблонов"}
- [LOAD_FILE()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_load-file){data-tooltip="Загрузить именованный файл"}
- [LOCATE()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_locate){data-tooltip="Возвращает позицию первого вхождения подстроки"}
- [LOWER()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_lower){data-tooltip="Вернуть аргумент в нижнем регистре"}
- [LPAD()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_lpad){data-tooltip="Возвращает строковый аргумент, дополненный слева указанной строкой"}
- [LTRIM()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_ltrim){data-tooltip="Удалить ведущие пробелы"}
- [MAKE_SET()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_make-set){data-tooltip="Возвращает набор разделенных запятыми строк, у которых установлен соответствующий бит в битах"}
- [MATCH](https://dev.mysql.com/doc/refman/8.0/en/fulltext-search.html#function_match){data-tooltip="Выполнить полнотекстовый поиск"}
- [MID()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_mid){data-tooltip="Возвращает подстроку, начиная с указанной позиции"}
- [NOT LIKE](https://dev.mysql.com/doc/refman/8.0/en/string-comparison-functions.html#operator_not-like){data-tooltip="Отрицание простого сопоставления с образцом"}
- [NOT REGEXP](https://dev.mysql.com/doc/refman/8.0/en/regexp.html#operator_not-regexp){data-tooltip="Отрицание REGEXP"}
- [OCT()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_oct){data-tooltip="Возвращает строку, содержащую восьмеричное представление числа"}
- [OCTET_LENGTH()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_octet-length){data-tooltip="Синоним LENGTH()"}
- [ORD()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_ord){data-tooltip="Возвращает символьный код крайнего левого символа аргумента"}
- [POSITION()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_position){data-tooltip="Синоним LOCATE()"}
- [QUOTE()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_quote){data-tooltip="Вывод аргумента для использования в операторе SQL"}
- [REGEXP](https://dev.mysql.com/doc/refman/8.0/en/regexp.html#operator_regexp){data-tooltip="Соответствует ли строка регулярному выражению"}
- [REGEXP_INSTR()](https://dev.mysql.com/doc/refman/8.0/en/regexp.html#function_regexp-instr){data-tooltip="Начальный индекс подстроки, соответствующей регулярному выражению"}
- [REGEXP_LIKE()](https://dev.mysql.com/doc/refman/8.0/en/regexp.html#function_regexp-like){data-tooltip="Соответствует ли строка регулярному выражению"}
- [REGEXP_REPLACE()](https://dev.mysql.com/doc/refman/8.0/en/regexp.html#function_regexp-replace){data-tooltip="Заменить подстроку, соответствующую регулярному выражению"}
- [REGEXP_SUBSTR()](https://dev.mysql.com/doc/refman/8.0/en/regexp.html#function_regexp-substr){data-tooltip="Возвращает подстроку, соответствующую регулярному выражению"}
- [REPEAT()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_repeat){data-tooltip="Повторять строку указанное количество раз"}
- [REPLACE()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_replace){data-tooltip="Заменить вхождения указанной строки"}
- [REVERSE()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_reverse){data-tooltip="Поменять местами символы в строке"}
- [RIGHT()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_right){data-tooltip="Вернуть указанное крайнее правое число символов"}
- [RLIKE](https://dev.mysql.com/doc/refman/8.0/en/regexp.html#operator_regexp){data-tooltip="Соответствует ли строка регулярному выражению"}
- [RPAD()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_rpad){data-tooltip="Добавить строку указанное количество раз"}
- [RTRIM()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_rtrim){data-tooltip="Удалить пробелы в конце строки"}
- [SOUNDEX()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_soundex){data-tooltip="Вернуть строку саундекса"}
- [SOUNDS LIKE](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#operator_sounds-like){data-tooltip="Сравнить звуки"}
- [SPACE()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_space){data-tooltip="Вернуть строку с указанным количеством пробелов"}
- [STRCMP()](https://dev.mysql.com/doc/refman/8.0/en/string-comparison-functions.html#function_strcmp){data-tooltip="Сравнить две строки"}
- [SUBSTR()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_substr){data-tooltip="Возвращает указанную подстроку"}
- [SUBSTRING()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_substring){data-tooltip="Вернуть указанную подстроку"}
- [SUBSTRING_INDEX()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_substring-index){data-tooltip="Возвращает подстроку из строки до указанного количества вхождений разделителя"}
- [TO_BASE64()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_to-base64){data-tooltip="Возвращает аргумент, преобразованный в строку base-64"}
- [TRIM()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_trim){data-tooltip="Удаление ведущих и завершающих пробелов"}
- [UCASE()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_ucase){data-tooltip="Синоним UPPER()"}
- [UNHEX()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_unhex){data-tooltip="Возвращает строку, содержащую шестнадцатеричное представление числа"}
- [UPPER()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_upper){data-tooltip="Преобразовать в верхний регистр"}
- [WEIGHT_STRING()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_weight-string){data-tooltip="Возвращает строку веса для строки"}
{.cols-2}



### Дата и время {.row-span-2}
- [ADDDATE()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_adddate){data-tooltip="Добавить значения времени (интервалы) к значению даты"}
- [ADDTIME()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_addtime){data-tooltip="Добавить время"}
- [CONVERT_TZ()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_convert-tz){data-tooltip="Перевести из одного часового пояса в другой"}
- [CURDATE()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_curdate){data-tooltip="Вернуть текущую дату"}
- [CURRENT_DATE()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-date){data-tooltip="Синонимы для CURDATE()"}
- [CURRENT_TIME()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-time){data-tooltip="Синонимы для CURTIME()"}
- [CURRENT_TIMESTAMP()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp){data-tooltip="Синонимы для NOW()"}
- [CURTIME()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_curtime){data-tooltip="Возврат текущего времени"}
- [DATE()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date){data-tooltip="Извлечение части даты из выражения date или datetime"}
- [DATE_ADD()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-add){data-tooltip="Добавить значения времени (интервалы) к значению даты"}
- [DATE_FORMAT()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-format){data-tooltip="Форматировать дату в соответствии с указаниями"}
- [DATE_SUB()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-sub){data-tooltip="Вычесть из даты значение времени (интервал)"}
- [DATEDIFF()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_datediff){data-tooltip="Вычесть две даты"}
- [DAY()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_day){data-tooltip="Синоним DAYOFMONTH()"}
- [DAYNAME()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_dayname){data-tooltip="Возвращает название дня недели"}
- [DAYOFMONTH()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_dayofmonth){data-tooltip="Возвращает день месяца (0-31)"}
- [DAYOFWEEK()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_dayofweek){data-tooltip="Возвращает индекс дня недели аргумента"}
- [DAYOFYEAR()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_dayofyear){data-tooltip="Возвращает день года (1-366)"}
- [EXTRACT()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_extract){data-tooltip="Извлечь часть даты"}
- [FROM_DAYS()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_from-days){data-tooltip="Преобразовать номер дня в дату"}
- [FROM_UNIXTIME()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_from-unixtime){data-tooltip="Форматировать временную метку Unix в дату"}
- [GET_FORMAT()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_get-format){data-tooltip="Возвращает строку формата даты"}
- [HOUR()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_hour){data-tooltip="Извлечь час"}
- [LAST_DAY](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_last-day){data-tooltip="Возвращает последний день месяца для аргумента"}
- [LOCALTIME()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_localtime){data-tooltip="Синоним NOW()"}
- [LOCALTIMESTAMP()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_localtimestamp){data-tooltip="Синоним NOW()"}
- [MAKEDATE()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_makedate){data-tooltip="Создать дату из года и дня года"}
- [MAKETIME()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_maketime){data-tooltip="Создать время из часа, минуты, секунды"}
- [MICROSECOND()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_microsecond){data-tooltip="Возвращает микросекунды из аргумента"}
- [MINUTE()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_minute){data-tooltip="Вернуть минуту из аргумента"}
- [MONTH()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_month){data-tooltip="Вернуть месяц из переданной даты"}
- [MONTHNAME()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_monthname){data-tooltip="Вернуть название месяца"}
- [NOW()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_now){data-tooltip="Возвращает текущую дату и время"}
- [PERIOD_ADD()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_period-add){data-tooltip="Добавить период к году-месяцу"}
- [PERIOD_DIFF()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_period-diff){data-tooltip="Возвращает количество месяцев между периодами"}
- [QUARTER()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_quarter){data-tooltip="Вернуть квартал из аргумента даты"}
- [SEC_TO_TIME()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_sec-to-time){data-tooltip="Преобразовывает секунды в формат 'hh:mm:ss'"}
- [SECOND()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_second){data-tooltip="Возвращает секунду (0-59)"}
- [STR_TO_DATE()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_str-to-date){data-tooltip="Преобразовать строку в дату"}
- [SUBDATE()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_subdate){data-tooltip="Синоним функции DATE_SUB() при вызове с тремя аргументами"}
- [SUBTIME()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_subtime){data-tooltip="Вычитание времени"}
- [SYSDATE()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_sysdate){data-tooltip="Возвращает время, в которое выполняется функция"}
- [TIME()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_time){data-tooltip="Извлечь временную часть переданного выражения"}
- [TIME_FORMAT()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_time-format){data-tooltip="Форматировать как время"}
- [TIME_TO_SEC()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_time-to-sec){data-tooltip="Возвращает аргумент, преобразованный в секунды"}
- [TIMEDIFF()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_timediff){data-tooltip="Вычесть время"}
- [TIMESTAMP()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_timestamp){data-tooltip="При одном аргументе эта функция возвращает выражение даты или времени; при двух аргументах - сумму аргументов"}
- [TIMESTAMPADD()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_timestampadd){data-tooltip="Добавить интервал к выражению времени-даты"}
- [TIMESTAMPDIFF()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_timestampdiff){data-tooltip="Вычесть интервал из выражения времени"}
- [TO_DAYS()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_to-days){data-tooltip="Возвращает аргумент даты, преобразованный в дни"}
- [TO_SECONDS()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_to-seconds){data-tooltip="Возвращает аргумент даты или datetime, преобразованный в секунды, начиная с года 0"}
- [UNIX_TIMESTAMP()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_unix-timestamp){data-tooltip="Возвращает временную метку Unix"}
- [UTC_DATE()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_utc-date){data-tooltip="Возвращает текущую дату по Гринвичу"}
- [UTC_TIME()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_utc-time){data-tooltip="Вернуть текущее время UTC"}
- [UTC_TIMESTAMP()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_utc-timestamp){data-tooltip="Возврат текущей даты и времени по Гринвичу"}
- [WEEK()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_week){data-tooltip="Вернуть номер недели"}
- [WEEKDAY()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_weekday){data-tooltip="Возвращает индекс дня недели"}
- [WEEKOFYEAR()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_weekofyear){data-tooltip="Возвращает календарную неделю даты (1-53)"}
- [YEAR()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_year){data-tooltip="Вернуть год"}
- [YEARWEEK()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_yearweek){data-tooltip="Возвращает год и неделю"}
- [GET_FORMAT()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_get-format){data-tooltip="'%m.%d.%Y'"}
{.cols-2}




### Числовой
- [%, MOD](https://dev.mysql.com/doc/refman/8.0/en/arithmetic-functions.html#operator_mod){data-tooltip="Оператор модуляции"}
- [*](https://dev.mysql.com/doc/refman/8.0/en/arithmetic-functions.html#operator_times){data-tooltip="Оператор умножения"}
- [+](https://dev.mysql.com/doc/refman/8.0/en/arithmetic-functions.html#operator_plus){data-tooltip="Оператор сложения"}
- [-](https://dev.mysql.com/doc/refman/8.0/en/arithmetic-functions.html#operator_minus){data-tooltip="Оператор минуса"}
- [-](https://dev.mysql.com/doc/refman/8.0/en/arithmetic-functions.html#operator_unary-minus){data-tooltip="Изменить знак аргумента"}
- [/](https://dev.mysql.com/doc/refman/8.0/en/arithmetic-functions.html#operator_divide){data-tooltip="Оператор деления"}
- [ABS()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_abs){data-tooltip="Возврат абсолютного значения"}
- [ACOS()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_acos){data-tooltip="Возврат косинуса дуги"}
- [ASIN()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_asin){data-tooltip="Вернуть синус дуги"}
- [ATAN()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_atan){data-tooltip="Вернуть тангенс дуги"}
- [ATAN2(), ATAN()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_atan2){data-tooltip="Возвращает тангенс дуги двух аргументов"}
- [CEIL()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_ceil){data-tooltip="Возвращает наименьшее целое значение, не меньшее аргумента"}
- [CEILING()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_ceiling){data-tooltip="Вернуть наименьшее целое значение, не меньшее аргумента"}
- [CONV()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_conv){data-tooltip="Преобразование чисел между различными основаниями чисел"}
- [COS()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_cos){data-tooltip="Вернуть косинус"}
- [COT()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_cot){data-tooltip="Вернуть котангенс"}
- [CRC32()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_crc32){data-tooltip="Вычислить значение проверки циклической избыточности"}
- [DEGREES()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_degrees){data-tooltip="Преобразование радианов в градусы"}
- [DIV](https://dev.mysql.com/doc/refman/8.0/en/arithmetic-functions.html#operator_div){data-tooltip="Целочисленное деление"}
- [EXP()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_exp){data-tooltip="Возведение в степень"}
- [FLOOR()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_floor){data-tooltip="Возвращает наибольшее целое значение, не превышающее аргумент"}
- [LN()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_ln){data-tooltip="Возвращает натуральный логарифм аргумента"}
- [LOG()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_log){data-tooltip="Возвращает натуральный логарифм первого аргумента"}
- [LOG10()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_log10){data-tooltip="Возвращает логарифм аргумента по основанию 10"}
- [LOG2()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_log2){data-tooltip="Возвращает логарифм аргумента по основанию 2"}
- [MOD()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_mod){data-tooltip="Вернуть остаток"}
- [PI()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_pi){data-tooltip="Вернуть значение числа pi"}
- [POW()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_pow){data-tooltip="Возвращает аргумент, возведенный в указанную степень"}
- [POWER()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_power){data-tooltip="Возвращает аргумент, возведенный в указанную степень"}
- [RADIANS()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_radians){data-tooltip="Возвращает аргумент, пересчитанный в радианы"}
- [RAND()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_rand){data-tooltip="Возвращает случайное значение с плавающей точкой"}
- [ROUND()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_round){data-tooltip="Округлить аргумент"}
- [SIGN()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_sign){data-tooltip="Вернуть знак аргумента"}
- [SIN()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_sin){data-tooltip="Вернуть синус аргумента"}
- [SQRT()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_sqrt){data-tooltip="Вернуть квадратный корень из аргумента"}
- [TAN()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_tan){data-tooltip="Вернуть тангенс аргумента"}
- [TRUNCATE()](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html#function_truncate){data-tooltip="Усечение до заданного количества десятичных знаков"}
{.cols-2}



### Агрегат
- [AVG()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_avg){data-tooltip="Возвращает среднее значение аргумента"}
- [BIT_AND()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_bit-and){data-tooltip="Возвращает побитовое AND"}
- [BIT_OR()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_bit-or){data-tooltip="Возвращает побитовое ИЛИ"}
- [BIT_XOR()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_bit-xor){data-tooltip="Возврат побитового XOR"}
- [COUNT()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_count){data-tooltip="Возвращает счетчик количества возвращенных строк"}
- [COUNT(DISTINCT)](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_count-distinct){data-tooltip="Возвращает подсчет количества различных значений"}
- [GROUP_CONCAT()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_group-concat){data-tooltip="Возвращает конкатенированную строку"}
- [JSON_ARRAYAGG()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_json-arrayagg){data-tooltip="Возвращает набор результатов в виде одного JSON-массива"}
- [JSON_OBJECTAGG()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_json-objectagg){data-tooltip="Возвращает набор результатов в виде одного JSON-объекта"}
- [MAX()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_max){data-tooltip="Возвращает максимальное значение"}
- [MIN()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_min){data-tooltip="Вернуть минимальное значение"}
- [STD()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_std){data-tooltip="Возврат стандартного отклонения популяции"}
- [STDDEV()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_stddev){data-tooltip="Вернуть стандартное отклонение популяции"}
- [STDDEV_POP()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_stddev-pop){data-tooltip="Вернуть стандартное отклонение популяции"}
- [STDDEV_SAMP()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_stddev-samp){data-tooltip="Вернуть выборочное стандартное отклонение"}
- [SUM()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_sum){data-tooltip="Вернуть сумму"}
- [VAR_POP()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_var-pop){data-tooltip="Вернуть стандартную дисперсию популяции"}
- [VAR_SAMP()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_var-samp){data-tooltip="Вернуть выборочную дисперсию"}
- [VARIANCE()](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_variance){data-tooltip="Вернуть стандартную дисперсию популяции"}
{.cols-2}




### JSON {.row-span-4}
- [->](https://dev.mysql.com/doc/refman/8.0/en/json-search-functions.html#operator_json-column-path){data-tooltip="Возвращаем значение из столбца JSON после вычисления пути; эквивалентно JSON_EXTRACT()."}
- [->>](https://dev.mysql.com/doc/refman/8.0/en/json-search-functions.html#operator_json-inline-path){data-tooltip="Возвращаем значение из столбца JSON после оценки пути и снятия кавычек с результата; эквивалентно JSON_UNQUOTE(JSON_EXTRACT())."}
- [JSON_ARRAY()](https://dev.mysql.com/doc/refman/8.0/en/json-creation-functions.html#function_json-array){data-tooltip="Создать массив JSON"}
- [JSON_ARRAY_APPEND()](https://dev.mysql.com/doc/refman/8.0/en/json-modification-functions.html#function_json-array-append){data-tooltip="Добавить данные в JSON-документ"}
- [JSON_ARRAY_INSERT()](https://dev.mysql.com/doc/refman/8.0/en/json-modification-functions.html#function_json-array-insert){data-tooltip="Вставить в массив JSON"}
- [JSON_CONTAINS()](https://dev.mysql.com/doc/refman/8.0/en/json-search-functions.html#function_json-contains){data-tooltip="Содержит ли JSON-документ определенный объект по пути"}
- [JSON_CONTAINS_PATH()](https://dev.mysql.com/doc/refman/8.0/en/json-search-functions.html#function_json-contains-path){data-tooltip="Содержит ли JSON-документ какие-либо данные по пути"}
- [JSON_DEPTH()](https://dev.mysql.com/doc/refman/8.0/en/json-attribute-functions.html#function_json-depth){data-tooltip="Максимальная глубина JSON-документа"}
- [JSON_EXTRACT()](https://dev.mysql.com/doc/refman/8.0/en/json-search-functions.html#function_json-extract){data-tooltip="Возврат данных из JSON-документа"}
- [JSON_INSERT()](https://dev.mysql.com/doc/refman/8.0/en/json-modification-functions.html#function_json-insert){data-tooltip="Вставить данные в JSON-документ"}
- [JSON_KEYS()](https://dev.mysql.com/doc/refman/8.0/en/json-search-functions.html#function_json-keys){data-tooltip="Массив ключей из JSON-документа"}
- [JSON_LENGTH()](https://dev.mysql.com/doc/refman/8.0/en/json-attribute-functions.html#function_json-length){data-tooltip="Количество элементов в JSON-документе"}
- [JSON_MERGE() (deprecated)](https://dev.mysql.com/doc/refman/8.0/en/json-modification-functions.html#function_json-merge){data-tooltip="Слияние JSON-документов с сохранением дублирующихся ключей". Утраченный синоним для JSON_MERGE_PRESERVE()"}
- [JSON_MERGE_PATCH()](https://dev.mysql.com/doc/refman/8.0/en/json-modification-functions.html#function_json-merge-patch){data-tooltip="Объединять JSON-документы, заменяя значения дублирующихся ключей"}
- [JSON_MERGE_PRESERVE()](https://dev.mysql.com/doc/refman/8.0/en/json-modification-functions.html#function_json-merge-preserve){data-tooltip="Объединять JSON-документы, сохраняя значения дублирующихся ключей"}
- [JSON_OBJECT()](https://dev.mysql.com/doc/refman/8.0/en/json-creation-functions.html#function_json-object){data-tooltip="Создать JSON-объект"}
- [JSON_OVERLAPS() (введена в 8.0.17)](https://dev.mysql.com/doc/refman/8.0/en/json-search-functions.html#function_json-overlaps){data-tooltip="Сравнивает два JSON-документа, возвращает TRUE (1), если в них есть общие пары ключ-значение или элементы массива, иначе FALSE (0)"}
- [JSON_PRETTY()](https://dev.mysql.com/doc/refman/8.0/en/json-utility-functions.html#function_json-pretty){data-tooltip="Вывести JSON-документ в человекочитаемом формате"}
- [JSON_QUOTE()](https://dev.mysql.com/doc/refman/8.0/en/json-creation-functions.html#function_json-quote){data-tooltip="Цитировать JSON-документ"}
- [JSON_REMOVE()](https://dev.mysql.com/doc/refman/8.0/en/json-modification-functions.html#function_json-remove){data-tooltip="Удалить данные из JSON-документа"}
- [JSON_REPLACE()](https://dev.mysql.com/doc/refman/8.0/en/json-modification-functions.html#function_json-replace){data-tooltip="Заменить значения в JSON-документе"}
- [JSON_SCHEMA_VALID() (введена в 8.0.17)](https://dev.mysql.com/doc/refman/8.0/en/json-validation-functions.html#function_json-schema-valid){data-tooltip="Проверка соответствия JSON-документа схеме JSON; возвращает TRUE/1, если документ соответствует схеме, или FALSE/0, если не соответствует"}
- [JSON_SCHEMA_VALIDATION_REPORT() (введена в 8.0.17)](https://dev.mysql.com/doc/refman/8.0/en/json-validation-functions.html#function_json-schema-validation-report){data-tooltip="Проверка JSON-документа на соответствие JSON-схеме; возвращает отчет в формате JSON о результатах проверки, включая успех или неудачу и причины неудачи"}
- [JSON_SEARCH()](https://dev.mysql.com/doc/refman/8.0/en/json-search-functions.html#function_json-search){data-tooltip="Путь к значению в JSON-документе"}
- [JSON_SET()](https://dev.mysql.com/doc/refman/8.0/en/json-modification-functions.html#function_json-set){data-tooltip="Вставить данные в JSON-документ"}
- [JSON_STORAGE_FREE()](https://dev.mysql.com/doc/refman/8.0/en/json-utility-functions.html#function_json-storage-free){data-tooltip="Освобождение места в двоичном представлении значения столбца JSON после частичного обновления"}
- [JSON_STORAGE_SIZE()](https://dev.mysql.com/doc/refman/8.0/en/json-utility-functions.html#function_json-storage-size){data-tooltip="Место, используемое для хранения двоичного представления JSON-документа"}
- [JSON_TABLE()](https://dev.mysql.com/doc/refman/8.0/en/json-table-functions.html#function_json-table){data-tooltip="Возвращать данные из JSON-выражения в виде реляционной таблицы"}
- [JSON_TYPE()](https://dev.mysql.com/doc/refman/8.0/en/json-attribute-functions.html#function_json-type){data-tooltip="Тип JSON-значения"}
- [JSON_UNQUOTE()](https://dev.mysql.com/doc/refman/8.0/en/json-modification-functions.html#function_json-unquote){data-tooltip="Значение JSON без кавычек"}
- [JSON_VALID()](https://dev.mysql.com/doc/refman/8.0/en/json-attribute-functions.html#function_json-valid){data-tooltip="Является ли JSON-значение действительным"}
- [JSON_VALUE() (введена в 8.0.21)](https://dev.mysql.com/doc/refman/8.0/en/json-search-functions.html#function_json-value){data-tooltip="Извлечь значение из JSON-документа в место, на которое указывает указанный путь; вернуть это значение в виде VARCHAR(512) или указанного типа"}
- [MEMBER OF() (введено в 8.0.17)](https://dev.mysql.com/doc/refman/8.0/en/json-search-functions.html#operator_member-of){data-tooltip="Возвращает true (1), если первый операнд совпадает с любым элементом массива JSON, переданного в качестве второго операнда, в противном случае возвращает false (0)"}
{.cols-1}


### Cast
- [BINARY](https://dev.mysql.com/doc/refman/8.0/en/cast-functions.html#operator_binary){data-tooltip="Приведение строки к двоичной строке"}
- [CAST()](https://dev.mysql.com/doc/refman/8.0/en/cast-functions.html#function_cast){data-tooltip="Приведение значения к определенному типу"}
- [CONVERT()](https://dev.mysql.com/doc/refman/8.0/en/cast-functions.html#function_convert){data-tooltip="Приведение значения к определенному типу"}
{.cols-2}


### Управление потоком
- [CASE](https://dev.mysql.com/doc/refman/8.0/en/flow-control-functions.html#operator_case){data-tooltip="Оператор Case"}
- [IF()](https://dev.mysql.com/doc/refman/8.0/en/flow-control-functions.html#function_if){data-tooltip="Конструкция If/else"}
- [IFNULL()](https://dev.mysql.com/doc/refman/8.0/en/flow-control-functions.html#function_ifnull){data-tooltip="Нулевая конструкция if/else"}
- [NULLIF()](https://dev.mysql.com/doc/refman/8.0/en/flow-control-functions.html#function_nullif){data-tooltip="Возвращает NULL, если expr1 = expr2"}
{.cols-2}


### Информация
- [BENCHMARK()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_benchmark){data-tooltip="Повторное выполнение выражения"}
- [CHARSET()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_charset){data-tooltip="Возвращает набор символов аргумента"}
- [COERCIBILITY()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_coercibility){data-tooltip="Возвращает значение когерентности collation для строкового аргумента"}
- [COLLATION()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_collation){data-tooltip="Возвращает значение collation строкового аргумента"}
- [CONNECTION_ID()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_connection-id){data-tooltip="Возвращает идентификатор соединения (идентификатор потока) для данного соединения"}
- [CURRENT_ROLE()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_current-role){data-tooltip="Возвращает текущие активные роли"}
- [CURRENT_USER()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_current-user){data-tooltip="Аутентифицированное имя пользователя и имя хоста"}
- [DATABASE()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_database){data-tooltip="Возвращает имя базы данных по умолчанию (текущее)"}
- [FOUND_ROWS()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_found-rows){data-tooltip="Для SELECT с предложением LIMIT количество строк, которое было бы возвращено, если бы не было предложения LIMIT"}
- [ICU_VERSION()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_icu-version){data-tooltip="Версия библиотеки ICU"}
- [LAST_INSERT_ID()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_last-insert-id){data-tooltip="Значение столбца AUTOINCREMENT для последнего INSERT"}
- [ROLES_GRAPHML()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_roles-graphml){data-tooltip="Возвращает документ GraphML, представляющий подграфы ролей памяти"}
- [ROW_COUNT()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_row-count){data-tooltip="Количество обновленных строк"}
- [SCHEMA()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_schema){data-tooltip="Синоним DATABASE()"}
- [SESSION_USER()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_session-user){data-tooltip="Синоним USER()"}
- [SYSTEM_USER()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_system-user){data-tooltip="Синоним USER()"}
- [USER()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_user){data-tooltip="Имя пользователя и имя хоста, предоставленные клиентом"}
- [VERSION()](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html#function_version){data-tooltip="Возвращает строку, указывающую на версию сервера MySQL"}
{.cols-2}


### Шифрование и сжатие
- [AES_DECRYPT()](https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html#function_aes-decrypt){data-tooltip="Расшифровать с помощью AES"}
- [AES_ENCRYPT()](https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html#function_aes-encrypt){data-tooltip="Шифрование с использованием AES"}
- [COMPRESS()](https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html#function_compress){data-tooltip="Возвращать результат в виде двоичной строки"}
- [MD5()](https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html#function_md5){data-tooltip="Вычислить контрольную сумму MD5"}
- [RANDOM_BYTES()](https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html#function_random-bytes){data-tooltip="Возвращает вектор случайных байтов"}
- [SHA1(), SHA()](https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html#function_sha1){data-tooltip="Вычислить 160-битную контрольную сумму SHA-1"}
- [SHA2()](https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html#function_sha2){data-tooltip="Вычислить контрольную сумму SHA-2"}
- [STATEMENT_DIGEST()](https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html#function_statement-digest){data-tooltip="Вычислить хэш-значение statement digest"}
- [STATEMENT_DIGEST_TEXT()](https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html#function_statement-digest-text){data-tooltip="Вычислить нормализованный дайджест выписки"}
- [UNCOMPRESS()](https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html#function_uncompress){data-tooltip="Распаковать сжатую строку"}
- [UNCOMPRESSED_LENGTH()](https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html#function_uncompressed-length){data-tooltip="Возврат длины строки до сжатия"}
- [VALIDATE_PASSWORD_STRENGTH()](https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html#function_validate-password-strength){data-tooltip="Определить силу пароля"}
{.cols-1}



### Блокировка
- [GET_LOCK()](https://dev.mysql.com/doc/refman/8.0/en/locking-functions.html#function_get-lock){data-tooltip="Получить именованную блокировку"}
- [IS_FREE_LOCK()](https://dev.mysql.com/doc/refman/8.0/en/locking-functions.html#function_is-free-lock){data-tooltip="Свободна ли именованная блокировка"}
- [IS_USED_LOCK()](https://dev.mysql.com/doc/refman/8.0/en/locking-functions.html#function_is-used-lock){data-tooltip="Используется ли именованная блокировка; если true, то возвращается идентификатор соединения"}
- [RELEASE_ALL_LOCKS()](https://dev.mysql.com/doc/refman/8.0/en/locking-functions.html#function_release-all-locks){data-tooltip="Освободить все текущие именованные блокировки"}
- [RELEASE_LOCK()](https://dev.mysql.com/doc/refman/8.0/en/locking-functions.html#function_release-lock){data-tooltip="Освободить именованную блокировку"}
{.cols-1}



### Бит
- [&](https://dev.mysql.com/doc/refman/8.0/en/bit-functions.html#operator_bitwise-and){data-tooltip="Побитовое И"}
- [>>](https://dev.mysql.com/doc/refman/8.0/en/bit-functions.html#operator_right-shift){data-tooltip="Сдвиг вправо"}
- [<<](https://dev.mysql.com/doc/refman/8.0/en/bit-functions.html#operator_left-shift){data-tooltip="Сдвиг влево"}
- [^](https://dev.mysql.com/doc/refman/8.0/en/bit-functions.html#operator_bitwise-xor){data-tooltip="Побитовый XOR"}
- [BIT_COUNT()](https://dev.mysql.com/doc/refman/8.0/en/bit-functions.html#function_bit-count){data-tooltip="Возврат количества установленных битов"}
- [|](https://dev.mysql.com/doc/refman/8.0/en/bit-functions.html#operator_bitwise-or){data-tooltip="Побитовое ИЛИ"}
- [~](https://dev.mysql.com/doc/refman/8.0/en/bit-functions.html#operator_bitwise-invert){data-tooltip="Побитовая инверсия"}
{.cols-2}



### Разное
- [ANY_VALUE()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_any-value){data-tooltip="Подавлять отбраковку значения ONLY_FULL_GROUP_BY"}
- [BIN_TO_UUID()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_bin-to-uuid){data-tooltip="Преобразование двоичного UUID в строку"}
- [DEFAULT()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_default){data-tooltip="Возвращает значение по умолчанию для столбца таблицы"}
- [GROUPING()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_grouping){data-tooltip="Отличить супер-агрегатные строки ROLLUP от обычных строк"}
- [INET_ATON()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_inet-aton){data-tooltip="Возвращает числовое значение IP-адреса"}
- [INET_NTOA()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_inet-ntoa){data-tooltip="Вернуть IP-адрес из числового значения"}
- [INET6_ATON()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_inet6-aton){data-tooltip="Вернуть числовое значение IPv6-адреса"}
- [INET6_NTOA()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_inet6-ntoa){data-tooltip="Вернуть IPv6-адрес из числового значения"}
- [IS_IPV4()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_is-ipv4){data-tooltip="Является ли аргумент IPv4-адресом"}
- [IS_IPV4_COMPAT()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_is-ipv4-compat){data-tooltip="Является ли аргумент IPv4-совместимым адресом"}
- [IS_IPV4_MAPPED()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_is-ipv4-mapped){data-tooltip="Является ли аргумент адресом, сопоставленным с IPv4"}
- [IS_IPV6()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_is-ipv6){data-tooltip="Является ли аргумент IPv6-адресом"}
- [IS_UUID()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_is-uuid){data-tooltip="Является ли аргумент действительным UUID"}
- [MASTER_POS_WAIT()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_master-pos-wait){data-tooltip="Блокировать до тех пор, пока реплика не прочитает и не применит все обновления до указанной позиции"}
- [NAME_CONST()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_name-const){data-tooltip="Причинить столбцу заданное имя"}
- [SLEEP()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_sleep){data-tooltip="Спать в течение определенного количества секунд"}
- [UUID()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_uuid){data-tooltip="Вернуть универсальный уникальный идентификатор (UUID)"}
- [UUID_SHORT()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_uuid-short){data-tooltip="Возвращает универсальный идентификатор с целочисленным значением"}
- [UUID_TO_BIN()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_uuid-to-bin){data-tooltip="Преобразование строкового UUID в двоичный"}
- [VALUES()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html#function_values){data-tooltip="Определите значения, которые будут использоваться при INSERT"}
{.cols-2}


См. также {.cols-1}
--------
- [Regex in MySQL](/regex#regex-in-mysql) _(cheatsheets.zip)_
