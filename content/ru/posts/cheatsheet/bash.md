---
название: Bash
дата: 2020-11-25 18:28:43
фон: bg-[#3e4548]
тэги:
    - shell
    - sh
    - эхо
    - скрипт
    - linux
категории:
    - Программирование
    - Операционная система
intro: Это краткая шпаргалка для начала работы со сценариями оболочки linux bash.
плагины:
    - copyCode
---

Начало работы
---------------

### hello.sh

``bash
#!/bin/bash

VAR="world"
echo "Hello $VAR!" # => Hello world!
```
Выполнить скрипт
``Основной сценарий
$ bash hello.sh
```


### Переменные

``bash
NAME="John"

echo ${NAME}    # => Джон (переменные)
echo $NAME # => Джон (Переменные)
echo "$NAME"    # => Джон (переменные)
echo '$NAME' # => $NAME (Точная строка)
echo "${NAME}!" # => John! (Переменные)

NAME = "John" # => Ошибка (о пробеле)
```



### Комментарии

``bash
# Это встроенный комментарий Bash.
```

``bash
: '
Это
очень аккуратный комментарий
в bash
'
```
В многострочных комментариях используется `:'` для открытия и `'` для закрытия




### Аргументы {.row-span-2}

| Выражение | Описание |
|-------------|---------------------------------------|
| `$1` ... `$9` | Параметр 1 ... 9 |
| `$0` | Имя самого скрипта |
| `$1` | Первый аргумент |
| | `${10}` | Позиционный параметр 10 |
| | `$#` | Количество аргументов |
| `$$` | Идентификатор процесса оболочки |
| `$*` | Все аргументы |
| | `$@` | Все аргументы, начиная с первого |
| `$-` | Текущие опции |
| `$_` | Последний аргумент предыдущей команды |

См: [Специальные параметры](http://wiki.bash-hackers.org/syntax/shellvars#special_parameters_and_shell_variables)


### Функции

``bash
get_name() {
    echo "John"
}

echo "Вы - $(get_name)"
```

См: [Функции](#bash-functions)

### Условные обозначения {#conditionals-example}

``bash
if [[ -z "$string" ]]; then
    echo "Строка пуста"
elif [[ -n "$string" ]]; then
    echo "Строка не пуста"
fi
```

См: [Conditionals](#bash-conditionals)

### Расширение скобок

``bash
echo {A,B}.js
```
---

| Выражение | Описание |
|------------|---------------------|
| `{A,B}` | То же, что `A B` |
| `{A,B}.js` | То же, что `A.js B.js` |
| `{1..5}` | То же, что `1 2 3 4 5` |

См: [Brace expansion](http://wiki.bash-hackers.org/syntax/expansion/brace)

### Выполнение оболочки

``bash
# => Я нахожусь в /path/of/current
echo "I'm in $(PWD)"

# То же самое, что:
echo "I'm in `pwd`"
```

См: [Подстановка команд](http://wiki.bash-hackers.org/syntax/expansion/cmdsubst)



Расширения параметров Bash
--------------------



### Синтаксис {.row-span-2}

| Код | Описание |
|-------------------|---------------------|
| `${FOO%suffix}` | Удалить суффикс |
| `${FOO#prefix}` | Удалить префикс |
| `${FOO%suffix}` | Удалить длинный суффикс |
| `${FOO##prefix}` | Удалить длинный префикс |
| `${FOO/from/to}` | Заменить первое совпадение |
| `${FOO//from/to}` | Заменить все |
| `${FOO/%from/to}` | Заменить суффикс |
| `${FOO/#from/to}` | Заменить префикс |
#### Подстроки
| Выражение | Описание |
|-----------------|--------------------------------|
| `${FOO:0:3}` | Substring _(position, length)_ |
| `${FOO:(-3):3}` | Подстрока справа |
#### Длина
| Выражение | Описание |
|------------|------------------|
| `${#FOO}` | Длина `$FOO` |
#### Значения по умолчанию
| Выражение | Описание |
|-------------------|------------------------------------------|
| | `${FOO:-val}` | `$FOO`, или `val`, если не задано |
| `${FOO:=val}` | Установить `$FOO` в `val`, если не установлено |
| `${FOO:+val}` | `val`, если `$FOO` установлен |
| `${FOO:?message}` | Показать сообщение и выйти, если `$FOO` не установлено |



### Подстановка

``bash
echo ${food:-Cake}  #=> $food или "Cake"
```


``bash
STR="/path/to/foo.cpp"
echo ${STR%.cpp}    # /path/to/foo
echo ${STR%.cpp}.o # /path/to/foo.o
echo ${STR%/*}      # /path/to

echo ${STR##*.}     # cpp (расширение)
echo ${STR##*/}     # foo.cpp (basepath)

echo ${STR#*/}      # path/to/foo.cpp
echo ${STR##*/}     # foo.cpp

echo ${STR/foo/bar} # /path/to/bar.cpp
```


### Нарезка

``bash
name="John"
echo ${name}           # => John
echo ${name:0:2}       # => Jo
echo ${name::2}        # => Jo
echo ${name::-1} # => Joh
echo ${name:(-1)} # => n
echo ${name:(-2)} # => hn
echo ${name:(-2):2}    # => hn

длина=2
echo ${name:0:length}  # => Jo
```
См: [Расширение параметров](http://wiki.bash-hackers.org/syntax/pe)



### basepath & dirpath
``bash
SRC="/path/to/foo.cpp"
```

``bash
BASEPATH=${SRC##*/}   
echo $BASEPATH # => "foo.cpp"


DIRPATH=${SRC%$BASEPATH}
echo $DIRPATH # => "/path/to/"
```






### Трансформация

``bash
STR="HELLO WORLD!"
echo ${STR,}   # => hELLO WORLD!
echo ${STR,,}  # => hello world!

STR="hello world!"
echo ${STR^}   # => Hello world!
echo ${STR^^}  # => HELLO WORLD!

ARR=(hello World)
echo "${ARR[@],}" # => hello world
echo "${ARR[@]^}" # => Hello World
```




Массивы Bash
------

### Определение массивов

``bash
Fruits=('Apple' 'Banana' 'Orange')

Fruits[0]="Apple"
Fruits[1]="Банан"
Fruits[2]="Orange"

ARRAY1=(foo{1..2}) # => foo1 foo2
ARRAY2=({A..D}) # => A B C D

# Объединение => foo1 foo2 A B C D
ARRAY3=(${ARRAY1[@]} ${ARRAY2[@]})

# объявить конструкцию
declare -a Numbers=(1 2 3)
Numbers+=(4 5) # Append => 1 2 3 4 5
```



### Индексирование

| - | - |
|--------------------|---------------|
| `${Фрукты[0]}` | Первый элемент |
| `${Fruits[-1]}` | Последний элемент |
| `${Fruits[*]}` | Все элементы |
| `${Fruits[@]}` | Все элементы |
| | `${#Fruits[@]}` | Количество всех |
| | `${#Fruits}` | Длина 1-го |
| | `${#Fruits[3]}` | Длина n-го |
| `${Фрукты[@]:3:2}` | Диапазон |
| `${!Fruits[@]}` | Ключи всех |



### Итерация

``bash
Fruits=('Apple' 'Banana' 'Orange')

for e in "${Фрукты[@]}"; do
    echo $e
done
```
#### С индексом
``bash
for i in "${!Fruits[@]}"; do
  printf "%s\t%s\n" "$i" "${Фрукты[$i]}"
done

```


### Операции {.col-span-2}

``bash
Fruits=("${Fruits[@]}" "Арбуз") # Push
Fruits+=('Арбуз') # Также Push
Fruits=( ${Fruits[@]/Ap*/} ) # Удалить по совпадению с regex
unset Fruits[2] # Удалить один элемент
Fruits=("${Fruits[@]}") # Дублировать
Fruits=("${Fruits[@]}" "${Veggies[@]}") # Конкатенация
lines=(`cat "logfile"`) # Чтение из файла
```

### Массивы в качестве аргументов
``bash
function extract()
{
    local -n myarray=$1
    local idx=$2
    echo "${myarray[$idx]}"
}
Fruits=('Apple' 'Banana' 'Orange')
извлечь Фрукты 2 # => Апельсин
```





Словари Bash
------------

### Определение

``bash
declare -A sounds
```

``bash
звуки[собака]="лай"
звуки[корова]="му"
звуки[птица]="чирикать"
звуки[волк]="вой"
```


### Работа со словарями

``bash
echo ${sounds[dog]} # Звук собаки
echo ${sounds[@]}   # Все значения
echo ${!sounds[@]}  # Все ключи
echo ${#sounds[@]}  # Количество элементов
unset sounds[dog] # Удалить собаку
```

### Итерация

``bash
for val in "${sounds[@]}"; do
    echo $val
done
```
---
``bash
for key in "${!sounds[@]}"; do
    echo $key
done
```





Условные обозначения Bash
------------

### Целочисленные условия

| Условие | Описание |
|---------------------|---------------------------------------------|
| `[[ NUM -eq NUM ]]` | <yel>Eq</yel>ual |
| `[[ NUM -ne NUM ]]` | <yel>N</yel>ot <yel>e</yel>qual |
| `[[ NUM -lt NUM ]]` | <yel>L</yel>ess <yel>t</yel>han |
| `[[ NUM -le NUM ]]` | <yel>L</yel>ess than or <yel>e</yel>qual |
| `[[ NUM -gt NUM ]]` | <yel>G</yel> больше <yel>t</yel>han |
| `[[ NUM -ge NUM ]]` | <yel>G</yel> больше или <yel>e</yel>равно |
| `(( NUM < NUM ))` | Меньше, чем |
| `(( NUM <= NUM ))` | Меньше или равно |
| `(( NUM > NUM ))` | Больше, чем |
| `(( NUM >= NUM ))` | Больше или равно |


### Строковые условия

| Условие | Описание |
|--------------------|-----------------------------|
| `[[ -z STR ]]` | Пустая строка |
| `[[ -n STR ]]` | <yel>N</yel> не пустая строка |
| `[[ STR == STR ]]` | Равно |
| `[[ STR = STR ]]` | Равно (то же, что и выше) |
| `[[ STR < STR ]]` | Меньше _(ASCII)_ |
| `[[ STR > STR ]]` | Больше _(ASCII)_ |
| `[[ STR != STR ]` | Не равно |
| `[[ STR =~ STR ]]` | Regexp |






### Пример {.row-span-3}

#### Строка
``bash
if [[ -z "$string" ]]; then
    echo "Строка пуста"
elif [[ -n "$string" ]]; then
    echo "Строка не пуста"
else
    echo "Такого не бывает"
fi
```

#### Комбинации
``bash
if [[ X && Y ]]; then
    ...
fi
```

#### Equal
``bash
if [[ "$A" == "$B" ]]; then
    ...
fi
```

#### Regex
``bash
if [[ '1. abc' =~ ([a-z]+) ]]; then
    echo ${BASH_REMATCH[1]}
fi
```

#### Меньше
``bash
if (( $a < $b )); then
   echo "$a меньше, чем $b"
fi
```

#### Exists
``bash
if [[ -e "file.txt" ]]; then
    echo "файл существует"
fi
```





### Условия файла {.row-span-2}

| Условие | Описание |
|-------------------|----------------------------------------|
| `[[ -e FILE ]]` | <yel>E</yel>xists |
| `[[ -d FILE ]` | <yel>D</yel>irectory |
| `[[ -f FILE ]]` | <yel>F</yel>ile |
| `[[ -h FILE ]]` | Symlink |
| | `[[ -s FILE ]]` | Размер > 0 байт |
| `[[ -r FILE ]]` | <yel>R</yel>eadable |
| `[[ -w FILE ]` | <yel>W</yel>ritable |
| `[[ -x FILE ]]` | Исполняемый |
| `[[ f1 -nt f2 ]` | f1 <yel>n</yel>ewer <yel>t</yel>han f2 |
| `[[ f1 -ot f2 ]` | f2 <yel>o</yel>lder <yel>t</yel>han f1 |
| `[[ f1 -ef f2 ]]` | Те же файлы |


### Дополнительные условия

| Условие | Описание |
|----------------------|----------------------|
| `[[ -o noclobber ]]` | Если OPTION включен |
| `[[ ! EXPR ]]` | Не |
| `[[ X && Y ]]` | И |
| `[[ X || Y ]]` | Или |


### логическое и, или
``bash
if [ "$1" = 'y' -a $2 -gt 0 ]; then
    echo "yes"
fi

if [ "$1" = 'n' -o $2 -lt 0 ]; then
    echo "no"
fi
```



Циклы Bash
-----

### Базовый цикл for

``bash
for i in /etc/rc.*; do
    echo $i
done
```

### C-подобный цикл for

``bash
for ((i = 0 ; i < 100 ; i++)); do
    echo $i
done
```

### Диапазоны {.row-span-2}

``bash
for i in {1..5}; do
    echo "Добро пожаловать $i"
done
```


#### С размером шага

``bash
for i in {5..50..5}; do
    echo "Добро пожаловать $i"
done
```



### Автоинкремент

``bash
i=1
while [[ $i -lt 4 ]]; do
    echo "Число: $i"
    ((i++))
done
```

### Автоматический декремент

```bash
i=3
while [[ $i -gt 0 ]]; do
    echo "Число: $i"
    ((i--))
done
```


### Продолжение

```bash {data=3,5}
for number in $(seq 1 3); do
    if [[ $number == 2 ]]; then
        продолжить;
    fi
    echo "$number"
done
```


### Break

``bash
for number in $(seq 1 3); do
    if [[ $number == 2 ]]; then
        # Пропустить всю оставшуюся часть цикла.
        break;
    fi
    # В результате будет выведено только 1
    echo "$number"
done
```

### До
```bash
count=0
until [ $count -gt 10 ]; do
    echo "$count"
    ((count++))
done
```


### Forever

``bash
while true; do
    # здесь находится некоторый код.
done
```

### Forever (сокращение)
``bash
while :; do
    # здесь находится некоторый код.
done
```


### Чтение строк

``bash
cat file.txt | while read line; do
    echo $line
done
```





Функции Bash
---------

### Определение функций

``bash
myfunc() {
    echo "hello $1"
}
```

``bash
# То же, что и выше (альтернативный синтаксис)
function myfunc() {
    echo "hello $1"
}
```

``bash
myfunc "John"
```

### Возврат значений

``bash
myfunc() {
    local myresult='некоторое значение'
    echo $myresult
}
```

``bash
result="$(myfunc)"
```

### Возбуждение ошибок

``bash
myfunc() {
    return 1
}
```

``bash
if myfunc; then
    echo "success"
else
    echo "failure"
fi
```



Опции Bash {.cols-2}
-------

### Опции

``bash
# Избегать наложения файлов
# (echo "hi" > foo)
set -o noclobber

# Используется для выхода при ошибке
# избегая каскадных ошибок
set -o errexit

# Выявляет скрытые сбои
set -o pipefail

# Выявляет незаданные переменные
set -o nounset
```

### Глобальные опции

``bash
# Несоответствующие глобусы удаляются
# ('*.foo' => '')
shopt -s nullglob

# Несовпадающие глобусы выбрасывают ошибки
shopt -s failglob

# Нечувствительные к регистру глобусы
shopt -s nocaseglob

# Wildcards match dotfiles
# ("*.sh" => ".foo.sh")
shopt -s dotglob

# Разрешить ** для рекурсивных совпадений
# ('lib/**/*.rb' => 'lib/a/b/c.rb')
shopt -s globstar
```


История Bash {.cols-2}
-------

### Команды

| Команда | Описание |
|-----------------------|-------------------------------------------|
| `history` | Показать историю |
| `sudo !!!` | Выполнить предыдущую команду с помощью sudo |
| `shopt -s histverify` | Не выполнять расширенный результат немедленно |

### Расширения

| Выражение | Описание |
|--------------|------------------------------------------------------|
| `!$` | Развернуть последний параметр последней команды |
| `!*` | Развернуть все параметры последней команды |
| `!-n` | Развернуть `n`-ю последнюю команду |
| `!n` | Развернуть `n`-ю команду в истории |
| `!<команда>` | Раскрыть последний вызов команды `<команда>` |

### Операции

Код | Код | Описание |
|----------------------|-----------------------------------------------------------------------|
| `!!` | Выполнить последнюю команду еще раз | |
| `!!!:s/<FROM>/<TO>/` | Заменить первое вхождение `<FROM>` на `<TO>` в последней команде |
| `!!:gs/<FROM>/<TO>/` | Заменить все вхождения `<FROM>` на `<TO>` в последней команде |
| `!$:t` | Расширить только базовое имя из последнего параметра последней команды |
| `!$:h` | Расширять только директорию из последнего параметра последней команды |

`!!!` и `!$` могут быть заменены любым допустимым расширением.

### Ломтики

| Код | Описание |
|----------|------------------------------------------------------------------------------------------|
| `!!!:n` | Развернуть только `n`-ю лексему из последней команды (команда - `0`; первый аргумент - `1`)|
| `!^` | Развернуть первый аргумент из последней команды |
| `!$` | Развернуть последнюю лексему из последней команды |
| | `!!:n-m` | Расширение диапазона лексем из последней команды |
| `!!!:n-$` | Развернуть `n`-ый токен до последнего из последней команды |

`!!!` может быть заменено любым допустимым расширением, например, `!cat`, `!-2`, `!42` и т.д.


Разное
-------------

### Числовые вычисления

``bash
$((a + 200))      # Прибавить 200 к $a
```

``bash
$(($RANDOM%200))  # Случайное число 0..199
```

### Под-оболочки

``bash
(cd somedir; echo "I'm now in $PWD")
pwd # все еще в первой директории
```


### Проверка команд

``bash
command -V cd
#=> "cd - это функция/алиас/что угодно"
```


### Перенаправление {.row-span-2 .col-span-2}

``bash
python hello.py > output.txt # stdout to (file)
python hello.py >> output.txt # stdout to (file), append
python hello.py 2> error.log # stderr в (файл)
python hello.py 2>&1 # stderr в stdout
python hello.py 2>/dev/null # stderr в (null)
python hello.py &>/dev/null # stdout и stderr в (null)
```

``bash
python hello.py < foo.txt # передать foo.txt на stdin для python
```


### Источник относительный

``bash
source "${0%/*}/../share/foo.sh"
```

### Каталог скрипта

``bash
DIR="${0%/*}"
```

### Case/switch

``bash
case "$1" in
    start | up)
    vagrant up
    ;;

    *)
    echo "Usage: $0 {start|stop|ssh}"
    ;;
esac
```


### Отлавливать ошибки {.col-span-2}

``bash
trap 'echo Error at about $LINENO' ERR
```

или

``bash
traperr() {
    echo "ERROR: ${BASH_SOURCE[1]} at about ${BASH_LINENO[0]}"
}

set -o errtrace
trap traperr ERR
```


### printf

``bash
printf "Hello %s, I'm %s" Sven Olga
#=> "Hello Sven, I'm Olga

printf "1 + 1 = %d" 2
#=> "1 + 1 = 2"

printf "Print a float: %f" 2
#=> "Print a float: 2.000000"
```

### Получение опций {.col-span-2}

``bash
while [[ "$1" =~ ^- && !"$1" == "--" ]]; do case $1 in
    -V | --version )
    echo $version
    exit
    ;;
    -s | --string )
    shift; string=$1
    ;;
    -f | --flag )
    flag=1
    ;;
esac; shift; done
if [[ "$1" == '--' ]]; then shift; fi
```

### Проверка результата выполнения команды {.col-span-2}

``bash
if ping -c 1 google.com; then
    echo "Похоже, что у вас есть рабочее подключение к Интернету"
fi
```


### Специальные переменные {.row-span-2}

| Выражение | Описание |
|------------|------------------------------|
| `$?` | Статус выхода из последней задачи |
| `$!` | PID последней фоновой задачи |
| `$$` | PID оболочки |
| `$0` | Имя файла сценария оболочки |

См. раздел [Специальные параметры](http://wiki.bash-hackers.org/syntax/shellvars#special_parameters_and_shell_variables).


### Проверка Grep {.col-span-2}

``bash
if grep -q 'foo' ~/.bash_history; then
    echo "Похоже, что в прошлом вы набирали 'foo'"
fi
```


### Обратные косые черты {.row-span-2}

- &nbsp;
- \!
- \"
- \#
- \&
- \'
- \(
- \)
- \,
- \;
- \<
- \>
- \[
- \|
- \\
- \]
- \^
- \{
- \}
- \`
- \$
- \*
- \?
{.cols-4 .marker-none}


Экранируйте эти специальные символы с помощью `\`.




### Heredoc

``sh
cat <<END
здравствуй мир
END
```


### Переход в предыдущий каталог

``bash
pwd # /home/user/foo
cd bar/
pwd # /home/user/foo/bar
cd -
pwd # /home/user/foo
```


### Чтение входных данных

``bash
echo -n "Proceed? [y/n]: "
прочитать ans
echo $ans
```

``bash
read -n 1 ans # Только один символ
```


### Условное выполнение

``bash
git commit && git push
git commit || echo "Commit failed"
```


### Строгий режим

``bash
set -euo pipefail
IFS=$'\n\t'
```

См: [Неофициальный строгий режим bash](http://redsymbol.net/articles/unofficial-bash-strict-mode/)


### Необязательные аргументы

``bash
args=("$@")
args+=(foo)
args+=(bar)
echo "${args[@]}"
```

Поместите аргументы в массив, а затем добавьте



## Также смотрите {.cols-1}
* [Devhints](https://devhints.io/bash) _(devhints.io)_
* [Bash-hackers wiki](http://wiki.bash-hackers.org/) _(bash-hackers.org)_
* [Shell vars](http://wiki.bash-hackers.org/syntax/shellvars) _(bash-hackers.org)_
* [Learn bash in y minutes](https://learnxinyminutes.com/docs/bash/) _(learnxinyminutes.com)_
* [Bash Guide](http://mywiki.wooledge.org/BashGuide) _(mywiki.wooledge.org)_
* [ShellCheck](https://www.shellcheck.net/) _(shellcheck.net)_
* [shell - Standard Shell](https://devmanual.gentoo.org/tools-reference/bash/index.html) _(devmanual.gentoo.org)_
