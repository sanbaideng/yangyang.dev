---
title: Vim
date: 2020-11-25 18:28:43
фон: bg-[#46933f]
теги:
    - vi
    - текст
    - редактор
    - терминал
    - ярлык
категории:
    - Набор инструментов
введение: |
    Полезная коллекция шпаргалок по [Vim](http://www.vim.org/) 8.2, которая поможет вам быстрее освоить редактор vim.
плагины:
    - copyCode
---

Начало работы
---------------

### Диаграммы движения {.row-span-2}

``bash
▼/▶ Курсор ▽/▷ Цель
```
#### Движения влево-вправо
``баш
┌───────────── |
├───────────── 0 $ ──────────────┐
│ ┌────────── ^ fe ────────┐ │
│ │ │ ┌─────── Fo te ───────┐│ │ │ │ │ │
│ │ │ │┌────── To 30| ───┐ │ ││ │ │ │ │ │
│ │ │ ││ ┌──── ge w ──┐ │ │ │ ││ │ │ │ │
│ │ ││ │ ┌──── b e ─┐ │ │ ││ ││ │ ││ │ │ │
│ │ │ ││ │ │ ┌h l┐ │ │ ││ │ ││ │ ││ │ │ │
▽ ▽ ▽▽ ▽ ▽ ▽▼ ▼▽ ▽ ▽ ▽ ▽▽ ▽
   echo "Шпаргалка от quickref.me"
```
#### Движения вверх-вниз
````bash
                 - ЗАПУСК ЭКРАНА 1
   ┌─┬─────────▷ #!/usr/bin/python
   │ │ ┌───▷
   │ │ │ │ │ print("Hello")
   │ │ { } ▶ print("Vim")
   │ │ │ │ │ print("!")
   │ │ └─▷
   │ │ ┌───┬───▷ print("Welcome")
G gg H M L k j ▶ print("to")
│ │ └─▷ print("cheatsheets.zip")
│ │ print("/vim")
│ │
│ └─────▷
│ - ЭКРАН 1 КОНЕЦ
└──────────────▷ print("SCREEN 2")
```

### Движения {.row-span-2}

| Shortcut | Description |
|--------------------------------|-------------------|
| `h` _|_ `j` _|_ `k` _|_ `l` | Клавиши со стрелками |
| `<C-u>` _/_ `<C-d>` | Переход на полстраницы вверх/вниз |
| `<C-b>` _/_ `<C-f>` | Страница вверх/вниз |
{.shortcuts}

#### Words{.left-text}
| Shortcut | Description
|--------------|---------------------------|
| `b` _/_ `w` | Предыдущее/Следующее слово |
| `ge` _/_ `e` | Предыдущий/Следующий конец слова |
{.shortcuts}

#### Строка

| Ярлык | Описание
|----------------------|-----------------------------|
| `0` _(ноль)_ _/_ `$` | Начало/конец строки |
| `^` | Начало строки _(непустой)_ |
{.shortcuts}

#### Символ

| Ярлык | Описание
|---------------|-------------------------------------|
| `Fe` _/_ `fe` | Перемещение на предыдущее/следующее `e` |
| `To` _/_ `to` | Перемещение до/после предыдущего/следующего `o` |
| `|` _/_ `n|` | Переход к первому/`n`-му столбцу |
{.shortcuts}

#### Документ

| Shortcut | Description
|----------------|--------------------------|
| `gg` _/_ `G` | Первая/Последняя строка |
| `:n` _||_ `nG` | Переход к строке `n` ||.
| `}` _/_ `{` | Следующая/предыдущая пустая строка |
{.shortcuts}

#### Окно

| Ярлык | Описание
|-------------------------|-----------------------------|
| `H` _/_ `M` _/_ `L` | Верхний/Средний/Нижний экран |
| `zt` _/_ `zz` _/_ `zb` | Верхняя/Центральная/Нижняя строка |
{.shortcuts}


### Режим вставки
| Ярлык | Описание
|------------------------|-------------------------------|
| `i` _/_ `a` | Вставить до/после курсора |
| `I` _/_ `A` | Вставить начало/конец строки ||.
| `o` _/_ `O` _(буква)_ | Вставить новую строку ниже/выше |
| `s` _/_ `S` | Удалить символ/строку и вставить |
| | `C` _/_ `cc` | Переход к концу/текущей строки |
| `gi` | Вставить в последнюю точку вставки |
| `Esc` _|_ `<C-[>` | Выход из режима вставки |
{.shortcuts}



### Сохранение и выход
| Ярлык | Описание
|---------------------------|-------------------------|
| `:w` | Сохранить
| `:q` | Закрыть файл | | file
| `:wq` _|_ `:x` _|_ `ZZ` | | | Сохранить и выйти
| `:wqa` | Сохранить и выйти из всех файлов | `:wqa
| `:q!
| | `:qa` | Закрыть все файлы | | | | все файлы.
| | | `:qa!` | Принудительный выход из всех файлов
| `:w` now.txt | Запись в `now.txt` | `:sav` new.txt
| `:sav` new.txt | Сохранить и отредактировать `new.txt` | `:w` !
| `:w` !sudo tee % | Запись в файл, доступный для чтения ||.
{.shortcuts}



### Нормальный режим
| Ярлык | Описание
|-----------------------|------------------------------|
| `r` | Заменить один символ |
| `R` | Войти в режим замены |
| `u` _/_ `3u` | Отменить изменения `1` / `3` раза ||.
| `U` | Отменить изменения в одной строке
| `J` | Присоединить к следующей строке
| `<C-r>` _/_ 5 `<C-r>` | Повторить изменения `1` / `5` раз |
{.shortcuts}


### Вырезать и вставить {.row-span-2}
| Shortcut | Description |
|------------------|-------------------------------|
| `x` | Удалить символ _(Вырезать)_ |
| `p` _/_ `P` | Вставить после/перед |
| `xp` | Поменять два символа местами |
| `D` | Удалить до конца строки _(Вырезать)_ |
| `dw` | Удалить слово _(Вырезать)_ |
| `dd` | Удалить строку _(Cut)_ | Поменять два символа местами
| `ddp` | Поменять местами две строки
| `yy` | Выдернуть строку _(Копировать)_ |
| `"*p` _|_ `"+p` | Вставить из системного буфера обмена |
| `"*y` _||_ `"+y` | Вставить в системный буфер обмена | {.shortcuts}
{.shortcuts}


#### В визуальном режиме
| Ярлык | Описание
|--------------|---------------------------|
| `d` _|_ `x` | Удалить выделение _(Вырезать)_ |
| `s` | Заменить выделение |
| `y` | Снять выделение _(Копировать)_ |
{.shortcuts}



### Повтор
| Shortcut | Description
|----------|---------------------------------------------|
| `.` | Повторить последнюю команду |
| `;` | Повторить последние `f`, `t`, `F` или `T` |
| `;` | Повторять последние `f`, `t`, `F` или `T` в обратном порядке |
| | `&` | Повторять последние `:s` |
| `@:` | Повторить команду командной строки |
{.shortcuts}



### Визуальный режим
| Shortcut | Description
|-------------|-------------------------|
| `v` | Ввести визуальный режим
| `V` | Вход в режим визуальной строки |
| `<C-v>` | Вход в режим визуального блока | | Визуальный режим
| `ggVG` | Выделить весь текст | | Режим визуального блока
| `>` _/_ `<` | Сдвиг текста вправо/влево |

{.shortcuts}



### Макросы
| - | - |
|-------|-----------------------|
| `qi` | Запись макроса `i` |
| `q` | Остановить запись макроса |
| `@i` | Запустить макрос `i` |
| `7@i` | Запустить макрос `i` 7 раз
| `@@` | Повторить последний макрос
{.shortcuts}

Вы можете сохранять макросы для любых букв, а не только для `i`.


Операторы Vim
---------

### Использование {.secondary}

| Shortcut | Description
|----------|--------------|
| `d` | <yel>w</yel> |
| Оператор | Движение

Объедините [операторы](#available-operators) с [движениями](#motions), чтобы использовать их




### Доступные операторы {.row-span-2}
| Shortcut | Description
|----------|---------------------------------|
| `d` | Удалить
| `y` | Yank _(copy)_ |
| `c` | Изменить _(удалить, затем вставить)_ |
| `p` | Вставить
| `=` | Форматирует код |
| `g~` | Переключение регистра |
| `gU` | Верхний регистр |
| `gu` | строчный
| `>` | Отступ вправо |
| `<` | Отступ слева
| Фильтр через внешнюю программу


### Примеры {.row-span-2}

| Комбинация | Описание |
|----------------------|---------------------------------------|
| `d`<yel>d</yel> | Удалить текущую строку |
| `d`<yel>j</yel> | Удалить две строки |
| `d`<yel>w</yel> | Удаление до следующего слова |
| `d`<yel>b</yel> | Удалить до начала слова |
| `d`<yel>fa</yel> | Удаление до символа `a` |
| `d`<yel>/hello</yel> | Удалить до `hello` |
| `c`<yel>c</yel> | Изменить текущую строку, синоним `S` |
| `y`<yel>y</yel> | Копировать текущую строку
| `>`<yel>j</yel> | Отступ на 2 строки |
| gg`d`<yel>G</yel> | Удалить весь документ |
| gg`=`<yel>G</yel> | Отступ от всего документа |
| gg`y`<yel>G</yel> | Скопировать весь документ |
{.show-header}



### Подсчеты
```
[count] <оператор> <движение>
<оператор> [count] <motion>
```
---

| Комбинация | Описание
|------------------|----------------------------|
| 2`d`<yel>d</yel> | Удалить `2` строки |
| 6`y`<yel>y</yel> | Скопировать `6` строк |
| `d`3<yel>w</yel> | Удалить `3` слова |
| `d`5<yel>j</yel> | Удалить `5` строк вниз ||.
| `>`4<yel>k</yel> | Отступ на `4` строки вверх |



Текстовые объекты Vim
------------

### Использование {.secondary}

| Shortcut | Description | - |
|----------|-----------------------------------------------------------|--------------|
| `v` | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <pur>i</pur> _/_ <pur>a</pur> | <yel>p</yel> |
| Оператор | <pur>i</pur>nner _/_ <pur>a</pur>round | Текстовый объект |

Оперировать с [оператором](#available-operators) внутри или вокруг текстовых блоков




### Текстовые объекты {.row-span-2}

| Shortcut | Description
|------------------------------------------------------|----------------------------------------|
| <yel>p</yel> | Paragraph |
| <yel>w</yel> | Word |
| <yel>W</yel> | СЛОВО <br/>_(окруженное пробелами)_ | | <yel>s</yel> | Слово
| <yel>s</yel> | Sentence |
| <yel>[</yel> <yel>(</yel> <yel>{</yel> <yel><</yel> | A [], (), или {} блок |
| <yel>]</yel> <yel>)</yel> <yel></yel> <yel> <yel> <yel> | A [], (), или {} block | |'</yel>.
| <yel>'</yel> <yel>"</yel> <yel> <yel></yel> | Строка, заключенная в кавычки |
| <yel>b</yel> | Блок [( | | <yel>B</yel>)

| | <yel>t</yel> | Блок HTML-тегов |

См. `:help text-objects`.



### Удалить

| Shortcut | Description
|-----------------------------|---------------------------------------|
| `d`<pur>i</pur><yel>w</yel> | Удалить внутреннее слово |
| `d`<pur>i</pur><yel>s</yel> | Удалить внутреннее предложение |
| `d`<pur>i</pur><yel>"</yel> | Удалить внутренние кавычки |
| `d`<pur>a</pur><yel>"</yel> | Удалить в кавычках _(включая кавычки)_ |
| `d`<pur>i</pur><yel>p</yel> | Удалить абзац |



### Выделения
| Ярлык | Описание
|-----------------------------------------------------|-------------------------------------------|
| `v`<pur>i</pur><yel>"</yel> | Выделить внутренние кавычки "`...`{.underline}"   |
| `v`<pur>a</pur><yel>"</yel> | Выделить кавычки `"...`{.underline}"|
| `v`<pur>i</pur><yel>[</yel> | Выберите внутренние скобки [`...`{.underline}]|
| `v`<pur>a</pur><yel>[</yel> | Выберите скобки `[...]`{.underline} |.
| | `v`<pur>i</pur><yel>w</yel> | Выделите внутреннее слово |
| `v`<pur>i</pur><yel>p</yel> | Выделить внутренний абзац |.
| `v`<pur>i</pur><yel>p</yel><pur>i</pur><yel>p</yel> | Выберите дополнительный абзац |


### Misc

| Shortcut | Description
|-----------------------------|--------------------------------------|
| | `c`<pur>i</pur><yel>w</yel> | Изменить внутреннее слово |
| | `c`<pur>i</pur><yel>"</yel> | Изменить внутренние кавычки
| | `c`<pur>i</pur><yel>t</yel> | Изменить внутренние теги (HTML) | | | `c`<pur>i</pur><yel>"</yel>.
| | `c`<pur>i</pur><yel>p</yel> | Изменить внутренний абзац
| `y`<pur>i</pur><yel>p</yel> | Выдернуть внутренний абзац |
| `y`<pur>a</pur><yel>p</yel> | Отменить абзац _(включая новую строку)_ |




Vim Множественные файлы
-------------



### Буферы
| - | - |
|------------|----------------------------------|
| `:e file` | Редактирование файла в новом буфере | | | |.
| `:bn` | Переход к следующему буферу | | | Переход к следующему буферу
| `:bp` | Переход к предыдущему буферу | | | | к следующему буферу.
| `:bd` | Удалить файл из списка буферов
| `:b 5` | Открыть буфер #5
| `:b file` | Перейти к буферу по файлу | | | | List all
| `:ls` | Список всех открытых буферов | | Открыть буфер №5
| | | | | | sp file` | Открыть и разделить окно
| `:vs file` | Открыть и разделить окно по вертикали
| | | | hid` | Скрыть этот буфер
| | `:wn` | Записать файл и перейти к следующему | | файлу.
| `:tab ba` | Редактирование всех буферов в виде вкладок



### Windows
| - | - |
|----------------------|-----------------------------|
| `<C-w>` `S` | Разделить окно |
| `<C-w>` `v` | Разделить окно по вертикали |
| `<C-w>` `w` | Переключение окон |
| `<C-w>` `q` | Выход из окна |
| `<C-w>` `T` | Переход на новую вкладку |
| `<C-w>` `x` | Поменять текущее окно на следующее |
| `<C-w>` `-` _/_ `+` | Уменьшить/Увеличить высоту |
| `<C-w>` `<` _/_ `>` | Уменьшить/Увеличить ширину |
| `<C-w>` `|` | Уменьшить ширину |
| `<C-w>` `=` | Одинаково высокая и широкая |
| `<C-w>` `h` _/_ `l` | | Переход к окну слева/справа |
| `<C-w>` `j` _/_ `k` | Переход к окну вверх/вниз |
{.shortcuts}



### Вкладки
| Ярлык | Описание
|----------------|-----------------------------------|
| | `:tabe [file]` | <yel>Э</yel>тот файл в новой вкладке ||.
| | | `:tabf [файл]` | открыть, если существует, в новой вкладке
| | `:tabc` | <yel>C</yel> закрыть текущую вкладку |
| `:tabo` | Закрыть <yel>о</yel> другие вкладки ||.
| | `:tabs` | Список всех <yel>вкладок</yel> ||.
| | `:tabr` | Перейти на fi<yel>r</yel>-ю вкладку ||.
| `:tabl` | Переход к <yel>l</yel> последней вкладке |
| `:tabm 0` | <yel>M</yel> Переход к позиции `0` |.
| | `:tabn` | Переход на <yel>n</yel> последнюю вкладку |
| `:tabp` | <yel>p</yel> предыдущая вкладка ||.


#### Обычный режим
| Ярлык | Описание
|----------|-------------------------------|
| `gt` | Переход на <yel>n</yel> последнюю вкладку |
| `gT` | Переход на <yel>p</yel> предыдущую вкладку |
| `2gt` | Переход на вкладку с номером `2` |
{.shortcuts}





Поиск и замена в Vim
------------------

### Поиск
| - | - |
|----------|-------------------------------------|
| `/foo` | Поиск вперед |
| `/foo` | Поиск вперед _(без учета регистра)_ |
| `?foo` | Поиск в обратном направлении ||.
| | `/foov\d+` | Поиск с помощью [regex](/regex) |
| | `n` | Следующее совпадение |
| `N` | Предыдущее совпадение |
| | `*` | Поиск текущего слова вперед |
| `#` | Поиск текущего слова назад |
{.shortcuts}



### Заменить строку
``vim
:[range]s/{pattern}/{str}/[flags]
```

---

| | |
|-------------------|----------------------------------|
| `:s/old/new` | Заменить первый | | | все
| | `:s/old/new/g` | Заменить все
| | | `:s/old/new/g` | Заменить все на [regex](/regex) |
| | `:s/old/new/gc` | Заменить все _(Confirm)_ |
| | | `:s/old/new/i` | Игнорировать замену первого регистра
| | `:2.6s/old/new/g` | Заменить между строками `2`-`6` |

### Замена ФАЙЛА
``vim
:%s/{pattern}/{str}/[flags]
```

---

| | |
|-------------------|----------------------------------|
| | `:%s/old/new` | Заменить первым
| | `:%s/old/new/g` | Заменить все
| | `:%s/old/new/gc` | Заменить все _(подтвердить)_ | | `:%s/old/new/gc` | Заменить все _(подтвердить)_
| | `:%s/old/new/gi` | Заменить все _(игнорировать случай)_ | | `:%s/old/new/g` | Заменить все _(игнорировать случай)_
| | | `:%s/old/new/g` | Заменить все на [regex](/regex) |



### Диапазоны {.row-span-2}
| - | - |
|---------|-------------------|
| `%` | Весь файл |
| `'<,'>` | Текущее выделение |
| `5` | Строка `5` | Строки
| | | Строки `5,10` | Строки с `5` по `10` |
| `$` | Последняя строка
| Строки `2,$` | Строки от `2` до последней
| `.` | Текущая строка
| `,3` | Следующие `3` строки
| `3,` | Следующие `3` строки ||.




### Глобальная команда {.row-span-2}
``vim
:[range]g/{pattern}/[command]
```
---

| | |
|--------------|------------------------------------|
| | `:g/foo/d` | Удаление строк, содержащих `foo` | | |.
| | `:g!/foo/d` | Удаление строк, не содержащих `foo` | | `:g/^{s*$/d`
| | `:g/^{s*$/d` | Удаление всех пустых строк ||.
| | `:g/foo/t$` | Скопировать строки, содержащие `foo`, в EOF
| `:g/foo/m$` | Переместить строки, содержащие `foo`, в EOF ||.
| `:g/^/m0` | Обратный ход файла |
| `:g/^/t.` | Дублировать каждую строку |



### Инверсия :g
``vim
:[range]v/{pattern}/[command]
```
---

| | |
|------------|------------------------------------------------------------|
| `:v/foo/d` | Удалить строки, не содержащие `foo`<br/>_(также `:g!/foo/d`)_ |




### Флаги

| - | - |
|-----|---------------------------|
| `g` | Заменить все вхождения |
| `i` | Игнорировать регистр |
| `I` | Не игнорировать регистр
| `c` | Подтверждать каждую замену



### Подставляем выражение (магическое)
| - | - |
|---------------|----------------------------------|
| `&` _\|_ ``0`` | Заменить на все совпадающие |
| ``1`...``9`` | Заменить на группу 0-9 | | |.
| `U` | Верхний регистр следующей буквы |
| `U` | Верхний регистр следующих букв |
| строчная следующая буква | строчные следующие символы
| `L` | Следующая буква в нижнем регистре | следующая буква в нижнем регистре.
| `E` | Конец ``U`, ``U`, ``L` и ``L`.
| `E` | Конец ``u`, ``U`, ``L` и ``L` |



### Примеры {.col-span-2}
``c {.wrap}
:s/a|b/xxx xxxx/g # Модифицирует "a b" в "xxxaxxx xxxbxxx"
:s/test/U& file/ # Модифицирует "test" в "TEST FILE"
:s/test/U& file/ # Модифицирует "test" в "TEST file"
:s// еfv([abc])([efg])/efg # Модифицирует "af fa bg" в "fa fa gb"

:s/\v([ab])|([cd])/\1x/g # Модифицирует "a b c d" в "ax bx x x"
:%s/.*/\L&/ # Модифицирует "HTML" в "html"
:s/^}(*)(*)// # Делает каждую первую букву слова прописной
:%s/^}(.*) # Удаляет дублирующиеся строки
:%s/<pattern/s/ # Преобразование HTML-тегов в верхний регистр
:g/^pattern/s/$/mytext # Найти и добавить текст в конец
:g/pattern/norm! @i # Запустить макрос на совпадающих строках
# Просмотр дубликатов строк
/\:v/./,/.*)(r/.1) +$ # Просмотр дубликатов строк (очень волшебно)
:v/./,/./-j # Сжать пустые строки в пустую строку
:g/<p1>/,/<p2>/d # Удалять включительно от <p1> до <p2>
```



Vimdiff
-------


### Использование {.secondary}

``шелл-скрипт

$ vimdiff file1 file2 [file3]
$ vim -d file1 file2 [file3]
```



### Редактирование {.row-span-2}
```
:[range]diffget[bufspec]
:[range]diffput [bufspec]
```
---
| Shortcut | Description
|---------------------|-------------------------|
| `do` _/_ `:diffget` | Получить (получить) разницу |
| `dp` _/_ `:diffput` | Поместить разницу
| `:dif` | Повторное сканирование различий
| `:diffo` | Выключить режим дифференцирования
| `:1,$+1diffget` | Получить все разности | | |EUR.
| `ZQ` | Выход без изменений
{.shortcuts}

См.: [Ranges](#ranges)



### Складки {.row-span-2}

| Shortcut | Description
|---------------|------------------------------|
| `zo` _/_ `zO` | Открыть
| `zc` _/_ `zC` | Закрыть |
| `za` _/_ `zA` | Toggle |
| `zv` | Открыть складки для этой строки |
| `zM` | Закрыть все
| `zR` | Открыть все
| `zm` | Складывать больше _(foldlevel += 1)_ |
| `zr` | Сложить меньше _(foldlevel -= 1)_ | }
| `zx` | Обновить складки |
{.shortcuts}



### Переход
<>

| Shortcut | Description
|----------|---------------------|
| `]c` | Следующая разница |
| `[c` | Предыдущая разница |
{.shortcuts}






Разное
-------------


### Case {.row-span-2}

| Shortcut | Description
|----------------|-------------------------|
| `vU` | _Прописной_ символ |
| `vu` | _Нижний регистр_ символов |
| `~` | _Толковый регистр_ символов |
| | `viw` `U` | _Прописное_ слово |
| `viw` `u` | _Нижний регистр_ слова |
| | `viw` `~` | _Толковый регистр_ слова |
| | `VU` _/_ `gUU` | _Прописная_ строка |
| `Vu` _/_ `guu` | _Lowercase_ line |
| `V~` _/_ `g~~` | _Тогге case_ line |
| `gggUG` | _Прописной_ весь текст |
| `ggguG` | _Нижний регистр_ всего текста |
| `gggg~G` | _Toggle case_ all text |
{.shortcuts}




### Прыжки

| Shortcut | Description
|----------|--------------------------|
| `<C-o>` | Вернуться к предыдущему |
| `<C-i>` | Переход вперед
| `gf` | Переход к файлу в курсоре |
| `ga` | Отображение шестнадцатеричного или ascii значения |
{.shortcuts}




### Командные строки {.row-span-2}
| - | - |
|----------------|--------------------------------------------|
| | | `:h` | Справка открыть вид справки |
| | `:edit!` | Перезагрузить текущий файл
| | `:2,8m0` | Переместить строки `2`-`8` в `0` | }
| | `:noh` | Очистить основные моменты поиска
| `:sort` | Сортировать строки
| | | Открыть окно терминала | | | |.
| | set paste` | Включить подрежим "Вставить-вставить" |
| `:set nopaste` | Отключить подрежим вставки | | | `:cq` | Выполнить подрежим вставки
| | `:cq` | Выход с ошибкой<br/>_(прерывание Git)_ |


### Навигация

| Shortcut | Description
|--------------------------|---------------------------|
| `%` | Ближайшее/подходящее `{[()]}` |
| `[(` _||_ `[{` | Предыдущая `(` или `{` | |]
| `])` _||_ `]{` | Следующий `)` или `}` | `` или `}` | `[m]| | Предыдущий метод.
| `[m` | Начало предыдущего метода |
| `[M` | Конец предыдущего метода |
{.shortcuts}


### Счетчики

| Shortcut | Description
|----------|-----------------|
| `<C-a>` | Увеличить число |
| `<C-x>` | Уменьшить число |
{.shortcuts}


### Теги {.row-span-2 .col-span-2}

| Shortcut | Description
|----------------------|-------------------------------------------------|
| | `:tag Classname` | Перейти к первому определению Classname | |.
| | | `<C-]>` | Перейти к определению | ||.
| | `g]` | Посмотреть все определения
| | `<C-t>` | Вернуться к последнему тегу |
| `<C-o> <C-i>` | Назад/вперед | | `:tselect Classname
| | | `:tselect Classname` | Поиск определений Classname | | |.
| | `:tjump Classname` | Поиск определений Classname (автовыбор 1-го) | | | {.shortcuts}
{.shortcuts}


### Форматирование
| - | - |
|---------|----------------------------------|
| `:ce 8` | Выравнивание строк по центру между `8` колонками ||.
| `:ri 4` | Выравнивание строк вправо по `4` столбцам
| `:le` | Выравнивание строк по левому краю | | Выравнивание строк по левому краю

См. `:справка по форматированию`.




### Марки {.col-span-2 .row-span-4}

| Shortcut | Description
| --- | --- |
| <code>`^</code> | Последняя позиция курсора в режиме вставки.
| Последнее изменение в текущем буфере.
| <code>"</code> | Последний выход из текущего буфера.
| <code>`0</code> | В последнем отредактированном файле |
| <code>''</code> | Возврат к строке в текущем буфере, с которой произошел переход |
| <code>``</code> | Возврат к позиции в текущем буфере, из которой был совершен переход |
| <code>]</code> | К началу ранее измененного или выдернутого текста |
| <code>``]</code> | К концу ранее измененного или выдернутого текста |
| <code>|&lt;</code> | К началу последнего визуального выделения | <code>`&gt;</code>.
| <code>`&gt;</code> | К концу последнего визуального выделения |

| `ma` | Пометить эту позицию курсора как `a` |
| <code>`a</code> | Перейти к позиции курсора `a` |
| `'a` | Переход к началу строки с позицией `a` |
| <code>d'a</code> | Удалить с текущей строки до строки с отметкой `a` |
| <code>d'a</code> | Удалить из текущей позиции в позицию метки `a` |
| <code>c'a</code> | Изменить текст с текущей строки на строку отметки `a` |
| <code>y'a</code> | Выдернуть текст из текущей позиции в позицию `a` |

| `:marks` | Список всех текущих меток | | | a</code>.
| | `:delm a` | Удалить метку `a` | | | текущую метку.
| | | `:delm a-d` | Удалить метки `a`, `b`, `c`, `d` | | | `:delm abc`
| | | `:delm abc` | Удалить метки `a`, `b`, `c` |.
{.shortcuts}



### Калькулятор

| Shortcut | Description
|------------------|------------------|
| `<C-r>` `=` 7*7 | Показывает результат |
| `<C-r>` `=` 10/2 | Показывает результат |
{.shortcuts}

Выполните это в режиме INSERT




### Shell
| - | - |
|--------------|--------------------------------|
| `:!<shell>` | Интерпретировать команду оболочки |
| `:r!<shell>` | Считать вывод команды Shell |
| `:r!date` | Вставить дату |
| `:!date` | Заменить текущую строку на дату




### Командная строка

| Shortcut | Description
|--------------|-------------------------------------------|
| `<C-r><C-w>` | Вставить текущее слово в командную строку |
| `<C-r>` | Вставить из регистра " |
| `<C-x><C-f>` | Автодополнение пути в режиме вставки |
{.shortcuts}


### Трюки
Удаление дублирующихся строк
``Шелл-скрипт
:sort | %!uniq -u
```
Пронумеровать строки в файле
```Шелл-скрипт
:%!cat -n
```
Скопировать весь документ в буфер обмена
```Шелл-скрипт
:%w !pbcopy # Mac OS X
:%w !xclip -i -sel c # GNU/Linux
:%w !xsel -i -b # GNU/Linux
```


Также см.
--------

- Devhints](https://devhints.io/vim) _(devhints.io)_
- Vim cheatsheet](https://vim.rtorr.com/) _(vim.rotrr.com)_
- Документация по Vim](http://vimdoc.sourceforge.net/htmldoc/) _(vimdoc.sourceforge.net)_
- Интерактивный учебник по Vim](http://openvim.com/) _(openvim.com)_
