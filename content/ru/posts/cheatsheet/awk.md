---
title: Awk
date: 2020-12-31 15:18:34
фон: bg-slate-600
теги:
    - bash
    - текст
    - скрипт
категории:
    - Linux Command
ввод: |
    Это одностраничная шпаргалка по [GNU awk](https://www.gnu.org/software/gawk/manual/gawk.html), в которой рассматриваются часто используемые выражения и команды awk.
плагины:
    - copyCode
---

Начало работы
---------------

### Попробуйте
``Шелл-скрипт {.wrap}
$ awk -F: '{print $1, $NF}' /etc/passwd
```
----
| - | - | - |
|---|---------------|---------------------------|
| | | `-F:` | Двоеточие как разделитель |
| | | `{...}` | Программа Awk |
| | | `print` | Печать текущей записи |
| | | `$1` | Первое поле |
| | | `$NF` | Последнее поле |
| | | `/etc/passwd` | Файл входных данных |
{.left-text}



### Программа Awk
```
BEGIN {<инициализации>}
   <шаблон 1> {<действия программы>}
   <шаблон 2> {<действия программы>}
   ...
END {< final actions >}
```
#### Пример
```
awk '
    BEGIN { print "\n>>>Start" }
    !/(login|shutdown)/ { print NR, $0 }
    END { print "<<<END\n" }
' /etc/passwd
```


### Переменные {.row-span-2}
``bash
          $1 $2/$(NF-1) $3/$NF
           ▼ ▼ ▼
        ┌──────┬──────────────────┬───────┐
$0/NR ▶ │ ID │ WEBSITE │ URI │
        ├──────┼──────────────────┼───────┤
$0/NR ▶ │ 1 │ cheatsheets.zip │ awk │
        ├──────┼──────────────────┼───────┤
$0/NR ▶ │ 2 │ google.com │ 25 │
        └──────┴──────────────────┴───────┘
```
---

```
# Первое и последнее поле
awk -F: '{print $1,$NF}' /etc/passwd

# С номером строки
awk -F: '{print NR, $0}' /etc/passwd

# Второе последнее поле
awk -F: '{print $(NF-1)}' /etc/passwd

# Пользовательская строка
awk -F: '{print $1 "=" $6}' /etc/passwd
```
См: [Переменные](#awk-variables)




### Примеры Awk-программ {.col-span-2 .row-span-2}
```
awk 'BEGIN {print "hello world"}'        # Печатает "hello world"
awk -F: '{print $1}' /etc/passwd # -F: Указать разделитель полей

# /pattern/ Выполнять действия только для совпадающего шаблона
awk -F: '/root/ {print $1}' /etc/passwd

# Блок BEGIN выполняется один раз при запуске
awk -F: 'BEGIN { print "uid"} { print $1 }' /etc/passwd

# Блок END выполняется один раз в конце
awk -F: '{print $1} END { print "-done-"}' /etc/passwd
```


### Условия
```
awk -F: '$3>30 {print $1}' /etc/passwd
```
См: [Условия](#awk-conditions)


### Генерировать 1000 пробелов
```
awk 'BEGIN{
    while (a++ < 1000)
        s=s " ";
    print s
}'
```
См: [Loops](#awk-loops)



### Массивы
```
awk 'BEGIN {
   fruits["mango"] = "желтый";
   fruits["orange"] = "orange"
   for(fruit in fruits) {
     print "Цвет " фрукта " равен " fruits[fruit]
   }
}'
```
См: [Массивы](#awk-arrays)



### Функции
```
# => 5
awk 'BEGIN{print length("hello")}'
# => HELLO
awk 'BEGIN{print toupper("hello")}'
# => hel
awk 'BEGIN{print substr("hello", 1, 3)}'
```
См: [Функции](#awk-functions)




Переменные Awk
---------


### Встроенные переменные
| - | - |
|----------------|-----------------------------------------------------|
| `$0` | Вся строка |
| `$1, $2...$NF` | Первое, второе... последнее поле |
| `NR` | `N` количество `R` записей |
| `NF` | `N` количество `F` полей |
| `OFS` | `O`ввод `F`поля `S`разделитель <br> _(по умолчанию " ")_ |
| `FS` | `Ввод `F`ield `S`eparator <br> _(по умолчанию " ")_ |
| `ORS` | `O`utput `R`ecord `S`eparator <br> _(по умолчанию "\n")_ |
| `RS` | входной `R`ecord `S`eparator <br> _(по умолчанию "\n")_ |
| `FILENAME` | Имя файла |



### Выражения
| - | - |
|---------------------|------------------------------------|
| `$1 == "root"` | Первое поле равно root |
| `{print $(NF-1)}` | Второе последнее поле |
| `NR!=1{print $0}` | Из второй записи |
| `NR > 3` | Из 4-й записи |
| `NR == 1` | Первая запись |
| `END{print NR}` | Всего записей |
| `BEGIN{print OFMT}` | Формат вывода |
| `{print NR, $0}` | Номер строки |
| `{print NR " " $0}` | Номер строки (табуляция) |
| `{$1 = NR; print}` | Заменить 1-е поле на номер строки |
| `$NF > 4` | Последнее поле > 4 |
| `NR % 2 == 0` | Четные записи |
| `NR==10, NR==20` | Записи с 10 по 20 |
| `BEGIN{print ARGC}` | Всего аргументов |
| `ORS=NR%5?",":"\n"` | Конкатенация записей |




### Примеры
Вывести сумму и среднее значение
```
awk -F: '{sum += $3}
     END { print sum, sum/NR }
' /etc/passwd
```
Печать параметров
```
awk 'BEGIN {
    for (i = 1; i < ARGC; i++)
        print ARGV[i] }' a b c
```
Вывод разделителя полей в виде запятой
```
awk 'BEGIN { FS=":";OFS=","}
    {print $1,$2,$3,$4}' /etc/passwd
```
Позиция совпадения
```
awk 'BEGIN {
    if (match("One Two Three", "Tw"))
        print RSTART }'
```
Длина совпадения
```
awk 'BEGIN {
    if (match("One Two Three", "re"))
        print RLENGTH }'
```





### Переменные окружения
| - | - |
|-----------|-----------------------------------------------------------|
| `ARGC` | Число или количество аргументов |
| `ARGV` | Массив аргументов |
| `FNR` | `F`ile `N`umber of `R`ecords |
| `OFMT` | Формат для чисел <br> _(по умолчанию "%.6g")_ |
| `RSTART` | Расположение в строке |
| `RLENGTH` | Длина совпадения |
| `SUBSEP` | Разделитель многомерных массивов <br> _(по умолчанию "\034")_ |
| `ARGIND` | Индекс аргумента |



### Только GNU awk
| - | - |
|---------------|-----------------------|
| `ENVIRON` | Переменные окружения |
| `IGNORECASE` | Игнорировать регистр |
| `CONVFMT` | Формат преобразования |
| `ERRNO` | Системные ошибки |
| `FIELDWIDTHS` | Поля фиксированной ширины |



### Определение переменной
```
awk -v var1="Hello" -v var2="Wold" '
    END {print var1, var2}
' </dev/null
```

#### Использование переменных оболочки
```
awk -v varName="$PWD" '
    END {print varName}' </dev/null
```



Операторы Awk
---------

### Операторы

| - | - |
|------------------|-------------|
| `{print $1}` | Первое поле |
| `$2 == "foo"` | Равно |
| `$2 != "foo"` | Не равно |
| `"foo" в массиве` | В массиве |
#### Регулярное выражение
| - | - |
|-----------------|-------------------|
| | `/regex/` | Совпадения строк |
| `!/regex/` | Строка не совпадает |
| `$1 ~ /regex/` | Полевые совпадения |
| `$1 !~ /regex/` | Поле не совпадает |
#### Дополнительные условия
| - | - |
|------------------------|-----|
| `($2 <= 4 || $3 < 20)` | | Или |
| `($1 == 4 && $3 < 20)` | | And |

### Операции
#### Арифметические операции
- `+`
- `-`
- `*`
- `/`
- `%`
- `++`
- `--`
{.cols-3 .marker-none}
#### Короткие присваивания
- `+=`
- `-=`
- `*=`
- `/=`
- `%=`
{.cols-3 .marker-none}
#### Операторы сравнения
- `==`
- `!=`
- `<`
- `>`
- `<=`
- `>=`
{.cols-3 .marker-none}



### Примеры
```
awk 'BEGIN {
    if ("foo" ~ "^fo+$")
        print "Fooey!";
}'
```
#### Не совпадает
```
awk 'BEGIN {
    if ("boo" !~ "^fo+$")
        print "Boo!";
}'
```
#### if in array
```
awk 'BEGIN {
    assoc["foo"] = "bar";
    assoc["bar"] = "baz";
    if ("foo" in assoc)
        print "Fooey!";
}'
```




Функции Awk
----------
### Общие функции {.col-span-2}
| Функция | Описание |
|-----------------------|---------------------------------------------------------------------------------|
| `index(s,t)` | Позиция в строке s, где встречается строка t, 0, если она не найдена |
| `length(s)` | Длина строки s (или $0, если аргумент отсутствует) |
| `rand` | Случайное число от 0 до 1 |
| `substr(s,index,len)` | Возврат len-char подстроки s, начинающейся с индекса (отсчитывается от 1) |
| `srand` | Установить семя для rand и вернуть предыдущее семя |
| `int(x)` | Усечение x до целочисленного значения |
| | `split(s,a,fs)` | Разделить строку s на массив a, разбитый на fs, с возвратом длины a |
| `match(s,r)` | Позиция в строке s, где встречается регекс r, или 0, если он не найден |
| `sub(r,t,s)` | Заменить t на первое вхождение регекса r в строке s (или $0, если s не задано) |
| `gsub(r,t,s)` | Заменить t на все вхождения регекса r в строку s |
| `system(cmd)` | Выполнить команду и вернуть статус выхода |
| `tolower(s)` | Перевести строку s в нижний регистр |
| `toupper(s)` | Перевести строку s в верхний регистр |
| `getline` | Установить $0 на следующую входную запись из текущего входного файла.                            |


### Функция, определяемая пользователем
```
awk ''
    # Возвращает минимальное число
    функция find_min(num1, num2){
       if (num1 < num2)
       return num1
       return num2
    }
    # Возвращает максимальное число
    function find_max(num1, num2){
       if (num1 > num2)
       return num1
       return num2
    }
    # Главная функция
    function main(num1, num2){
       result = find_min(num1, num2)
       print "Минимум =", result
      
       result = find_max(num1, num2)
       print "Maximum =", result
    }
    # Выполнение сценария начинается здесь
    BEGIN {
       main(10, 60)
    }
'
```




Массивы Awk
---------



### Массив с индексом
```
awk 'BEGIN {
    arr[0] = "foo";
    arr[1] = "bar";
    print(arr[0]); # => foo
    удалить arr[0];
    print(arr[0]); # => ""
}'
```

### Массив с ключом
```
awk 'BEGIN {
    assoc["foo"] = "bar";
    assoc["bar"] = "baz";
    print("baz" в assoc); # => 0
    print("foo" in assoc); # => 1
}'
```


### Массив с разбиением
```
awk 'BEGIN {
    split("foo:bar:baz", arr, ":");
    for (key in arr)
        print arr[key];
}'
```

### Массив с асортом
```
awk 'BEGIN {
    arr[0] = 3
    arr[1] = 2
    arr[2] = 4
    n = asort(arr)
    for (i = 1; i <= n ; i++)
        print(arr[i])
}'
```



### Многомерность
```
awk 'BEGIN {
    multidim[0,0] = "foo";
    multidim[0,1] = "bar";
    multidim[1,0] = "baz";
    multidim[1,1] = "boo";
}'
```

### Многомерная итерация
```
awk 'BEGIN {
    array[1,2]=3;
    array[2,3]=5;
    for (comb in array) {
        split(comb,sep,SUBSEP);
        print sep[1], sep[2],
        array[sep[1],sep[2]]
    }
}'
```



Условия Awk
----------

### оператор if-else
```
awk -v count=2 'BEGIN {
    if (count == 1)
        выведите "Да";
    else
        print "Huh?";
}'
```
#### Тернарный оператор
```
awk -v count=2 'BEGIN {
    print (count==1) ? "Yes" : "Huh?";
}'
```


### Exists
```
awk 'BEGIN {
    assoc["foo"] = "bar";
    assoc["bar"] = "baz";
    if ("foo" in assoc)
        print "Fooey!";
}'
```
#### Не существует
```
awk 'BEGIN {
    assoc["foo"] = "bar";
    assoc["bar"] = "baz";
    if ("Huh" в assoc == 0 )
        print "Huh!";
}'
```


### switch
```
awk -F: '{
    switch (NR * 2 + 1) {
        case 3:
        case "11":
            print NR - 1
            break
        
        case /2[[:digit:]]+/:
            print NR
        
        по умолчанию:
            print NR + 1
        
        case -1:
            print NR * -1
    }
}' /etc/passwd
```


Циклы Awk
----------

### for...i
```
awk 'BEGIN {
    for (i = 0; i < 10; i++)
        print "i=" i;
}'
```
#### Коэффициенты двойки от 1 до 100
```
awk 'BEGIN {
    for (i = 1; i <= 100; i *= 2)
        print i
}'
```


### for...in
```
awk 'BEGIN {
    assoc["key1"] = "val1"
    assoc["key2"] = "val2"
    for (key in assoc)
        print assoc[key];
}'
```
#### Аргументы
```
awk 'BEGIN {
    for (argnum in ARGV)
        print ARGV[argnum];
}' a b c
```



### Примеры {.row-span-3}
#### Обратные записи
```
awk -F: '{ x[NR] = $0 }
    END {
        for (i = NR; i > 0; i--)
        print x[i]
    }
' /etc/passwd
```

#### Обратные поля
```
awk -F: '{
    for (i = NF; i > 0; i--)
        printf("%s ",$i);
    print ""
}' /etc/passwd
```

#### Сумма по записи
```
awk -F: '{
    s=0;
    for (i = 1; i <= NF; i++)
        s += $i;
    print s
}' /etc/passwd
```


#### Сумма всего файла
```
awk -F: '
    {for (i = 1; i <= NF; i++)
        s += $i;
    };
    END{print s}
' /etc/passwd
```



### while {.row-span-2}
```
awk 'BEGIN {
    while (a < 10) {
        print "- " " конкатенация: " a
        a++;
    }
}'
```
#### do...while
```
awk '{
    i = 1
    do {
        вывести $0
        i++
    } while (i <= 5)
}' /etc/passwd
```



### Break
```
awk 'BEGIN {
    break_num = 5
    for (i = 0; i < 10; i++) {
        вывести i
        if (i == break_num)
            break
    }
}'
```



### Продолжение
```
awk 'BEGIN {
    for (x = 0; x <= 10; x++) {
        if (x == 5 || x == 6)
            продолжить
        printf "%d ", x
    }
    print ""
}'
```



Форматированная печать Awk
---------

### Использование
#### Выравнивание по правому краю
```
awk 'BEGIN{printf "|%10s|\n", "hello"}'

| hello|
```
#### Выравнивание по левому краю
```
awk 'BEGIN{printf "|%-10s|\n", "hello"}'

|hello |
```

### Общие спецификаторы
| Характер | Описание |
|---------------|-----------------------|
| `c` | ASCII-символ |
| `d` | Десятичное целое число |
| `e`, `E`, `f` | Формат с плавающей точкой |
| `o` | Беззнаковое восьмеричное значение |
| ``S`` | Строка |
| `%` | Литерал % |




### Пространство
```
awk -F: '{
    printf "%-10s %s\n", $1, $(NF-1)
}' /etc/passwd | head -n 3
```
Выходные данные
``Сценарий командной строки
root /root
bin /bin
демон /sbin
```



### Заголовок
```
awk -F: 'BEGIN {
    printf "%-10s %s\n", "User", "Home"
    printf "%-10s %s\n", "----", "----"}
    { printf "%-10s %s\n", $1, $(NF-1) }
' /etc/passwd | head -n 5
```
Выводит
```
Дом пользователя
---- ----
root /root
bin /bin
демон /sbin
```



Разное
-------------

### Метасимволы Regex
- `\`
- `^`
- `$`
- `.`
- `[`
- `]`
- `|`
- `(`
- `)`
- `*`
- `+`
- `?`
{.cols-3 .marker-none}

### Escape Sequences
| - | - |
|------|---------------------|
| `\b` | Backspace |
| `\f` | Form feed |
| `\n` | Новая строка (перевод строки) |
| `\r` | Возврат каретки |
| `\t` | Горизонтальная табуляция |
| `\v` | Вертикальная табуляция |


### Запуск скрипта
``Основной сценарий
$ cat demo.awk
#!/usr/bin/awk -f
BEGIN { x = 23 }
      { x += 2 }
END { print x }
$ awk -f demo.awk /etc/passwd
69
```


Также см.
--------

- [The GNU Awk User's Guide](https://www-zeuthen.desy.de/dv/documentation/unixguide/infohtml/gawk/gawk.html) _(www-zeuthen.desy.de)_
- [AWK cheatsheet](https://gist.github.com/Rafe/3102414) _(gist.github.com)_


