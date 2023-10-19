---
Название: MATLAB
дата: 2023-01-03 09:51:44
фон: bg-[#692316]
теги:
категории:
  - Программирование
intro: |
    Эта шпаргалка содержит пример введения в использование языка научных вычислений [MATLAB](https://mathworks.cn/) для быстрого начала работы.
плагины:
    - copyCode
---

Начало работы
----

### Введение

MATLAB - это сокращение от `матричная лаборатория`.

----

- [Официальный сайт MATLAB](https://www.mathworks.com)
### Операции с матрицами и массивами {.row-span-3}

MATLAB позволяет использовать один арифметический оператор или функцию для работы со всеми значениями в матрице

``matlab
a + 10
```

MATLAB выполнит приведенный выше оператор и вернет следующие результаты:
```
ans = 3×3
    11 13 15
    12 14 16
    17 18 20
```

----

``matlab
sin(a)
```

MATLAB выполнит приведенный выше оператор и вернет следующие результаты:

```
ans = 3×3
    0.8415 0.1411 -0.9589
    0.9093 -0.7568 -0.2794
    0.6570 0.9894 -0.5440
```

Для транспонирования матрицы используйте одинарные кавычки (`'`)

``matlab
a'
```

----

```
ans = 3×3
     1 2 7
     3 4 8
     5 6 10
```

Выполните стандартное умножение матриц с помощью оператора `*`, который вычисляет внутреннее произведение между строками и столбцами

``matlab
p = a*inv(a)
```

----

```
p = 3×3
    1.0000 0 0
         0 1.0000 0
         0 0 1.0000
```

### конкатенация {.row-span-2}

Конкатенация - это процесс объединения массивов для получения более крупных массивов. Фактически, первый массив образуется путем конкатенации его элементов. Пары квадратных скобок `[]` являются операторами конкатенации.

``matlab
A = [a,a]
```

----

```
A = 3×6

     1 3 5 1 3 5
     2 4 6 2 4 6
     7 8 10 7 8 10
```

Объединение массивов, расположенных рядом друг с другом с использованием запятых, называется горизонтальным объединением. Каждый массив должен иметь одинаковое количество строк. Аналогично для вертикальной конкатенации можно использовать точку с запятой, если массивы имеют одинаковое количество столбцов.

``matlab
A = [a; a]
```

----

```
A = 6×3

     1 3 5
     2 4 6
     7 8 10
     1 3 5
     2 4 6
     7 8 10
```

### Матрицы и массивы{.row-span-3}

Чтобы создать массив с четырьмя элементами в строке, разделяйте элементы запятыми (`,`) или пробелами

``matlab
a = [1 2 3 4]
```

MATLAB выполнит приведенный выше оператор и вернет следующие результаты:

```
a = 1×4
     1 2 3 4
```

#### Создание матрицы с несколькими строками

``matlab
a = [1 3 5; 2 4 6; 7 8 10]
```

----

```
a = 3×3
     1 3 5
     2 4 6
     7 8 10
```

#### 5×1 столбцовый вектор нулей

``matlab
z = zeros(5,1)
```

----

```
z = 5×1
     0
     0
     0
     0
     0
```

### Комплексное число

Комплексное число имеет действительную и мнимую части, причем мнимой единицей является квадратный корень из -1.

``matlab
sqrt(-1)
```

----

```
ans = 0.0000 + 1.0000i
```

Для представления мнимой части комплексного числа используется символ i или j.

``matlab
c = [3+4i, 4+3j; -i, 10j]
```

----

```
c = 2×2 комплекс

   3.0000 + 4.0000i 4.0000 + 3.0000i
   0.0000 - 1.0000i 0.0000 +10.0000i
```

Базовые знания
----
### Введите команду

- | - | -
- | - | -
[ans](https://www.mathworks.com/help/matlab/ref/ans.html) | Последний вычисленный ответ
[clc](https://www.mathworks.com/help/matlab/ref/clc.html) | Очистить окно командной строки
[diary](https://www.mathworks.com/help/matlab/ref/diary.html) | Запись текста окна командной строки в файл журнала
[format](https://www.mathworks.com/help/matlab/ref/format.html) | Установить формат отображения выходных данных
[home](https://www.mathworks.com/help/matlab/ref/home.html) | Отправить сброс курсора
[iskeyword](https://www.mathworks.com/help/matlab/ref/iskeyword.html) | Определить, является ли вводимое слово <span class="trademark">MATLAB</span> ключевым словом
[more](https://www.mathworks.com/help/matlab/ref/more.html) | Управление выводом страниц в окне командной строки
[commandwindow](https://www.mathworks.com/help/matlab/ref/commandwindow.html) | Выбор окна командной строки
[commandhistory](https://www.mathworks.com/help/matlab/ref/commandhistory.html) | Открыть окно истории команд

#### Объекты

- | -
- | -
[DisplayFormatOptions](https://www.mathworks.com/help/matlab/ref/ans.html) | Вывод формата отображения в окне командной строки
### Матрицы и массивы {.row-span-5}

Создание и объединение массивов

- | - | -
- | - | -
[zeros](https://www.mathworks.com/help/matlab/ref/zeros.html) | Создать массив из всех нулей
[ones](https://www.mathworks.com/help/matlab/ref/ones.html) | Создать массив из всех единиц
[rand](https://www.mathworks.com/help/matlab/ref/rand.html) | Равномерно распределенные случайные числа
[true](https://www.mathworks.com/help/matlab/ref/true.html) | Логическое значение 1 (true)
[false](https://www.mathworks.com/help/matlab/ref/false.html) | Логический 0 (false)
[eye](https://www.mathworks.com/help/matlab/ref/eye.html) | матрица тождества
[diag](https://www.mathworks.com/help/matlab/ref/diag.html) | Создать диагональную матрицу или получить диагональные элементы матрицы
[blkdiag](https://www.mathworks.com/help/matlab/ref/blkdiag.html) | блочная диагональная матрица
[cat](https://www.mathworks.com/help/matlab/ref/double.cat.html) | Конкатенация массивов.
[horzcat](https://www.mathworks.com/help/matlab/ref/horzcat.html) | Конкатенация массивов по горизонтали
[vertcat](https://www.mathworks.com/help/matlab/ref/vertcat.html) | Конкатенировать массивы по вертикали
[repelem](https://www.mathworks.com/help/matlab/ref/repelem.html) | Повторить копию элемента массива
[repmat](https://www.mathworks.com/help/matlab/ref/repmat.html) | Повторное копирование массива

создать сетку

- | - | -
- | - | -
[linspace](https://www.mathworks.com/help/matlab/ref/linspace.html) | Генерировать линейно распределенные векторы
[logspace](https://www.mathworks.com/help/matlab/ref/logspace.html) | Генерировать логарифмически разнесенные векторы
[freqspace](https://www.mathworks.com/help/matlab/ref/freqspace.html) | Интервал между частотами частотной характеристики
[meshgrid](https://www.mathworks.com/help/matlab/ref/meshgrid.html) | Двумерные и трехмерные сетки
[ndgrid](https://www.mathworks.com/help/matlab/ref/ndgrid.html) | Прямоугольная сетка в N-мерном пространстве
Определение размера, формы и порядка

- | - | -
- | - | -
[length](https://www.mathworks.com/help/matlab/ref/length.html) | Длина наибольшей размерности массива
[size](https://www.mathworks.com/help/matlab/ref/size.html) | Размер массива
[ndims](https://www.mathworks.com/help/matlab/ref/double.ndims.html) | Количество размерностей массива
[numel](https://www.mathworks.com/help/matlab/ref/double.numel.html) | количество элементов массива
[isscalar](https://www.mathworks.com/help/matlab/ref/isscalar.html) | Определить, является ли входной сигнал скаляром
[issorted](https://www.mathworks.com/help/matlab/ref/issorted.html) | Определить, отсортирован ли массив
[issortedrows](https://www.mathworks.com/help/matlab/ref/issortedrows.html) | Определить, отсортированы ли строки матрицы или таблицы
[isvector](https://www.mathworks.com/help/matlab/ref/isvector.html) | Определить, является ли входной сигнал вектором
[ismatrix](https://www.mathworks.com/help/matlab/ref/ismatrix.html) | Определить, является ли входной сигнал матрицей
[isrow](https://www.mathworks.com/help/matlab/ref/isrow.html) | Определить, является ли входной сигнал вектором строк
[iscolumn](https://www.mathworks.com/help/matlab/ref/iscolumn.html) | Определить, является ли входной сигнал вектором-столбцом
[isempty](https://www.mathworks.com/help/matlab/ref/isempty.html) | Определить, является ли массив пустым

Рефакторинг и перестановка
- | - | -
- | - | -
[sort](https://www.mathworks.com/help/matlab/ref/sort.html) | Сортировка элементов массива
[sortrows](https://www.mathworks.com/help/matlab/ref/double.sortrows.html) | Сортировка строк матрицы или таблицы
[flip](https://www.mathworks.com/help/matlab/ref/flip.html) | Перевернуть порядок элементов
[fliplr](https://www.mathworks.com/help/matlab/ref/fliplr.html) | Перевернуть массив слева направо
[flipud](https://www.mathworks.com/help/matlab/ref/flipud.html) | Перевернуть массив сверху вниз
[rot90](https://www.mathworks.com/help/matlab/ref/rot90.html) | Поворот массива на 90 градусов
[transpose](https://www.mathworks.com/help/matlab/ref/transpose.html) | Транспонировать вектор или матрицу
[ctranspose](https://www.mathworks.com/help/matlab/ref/ctranspose.html) | транспонирование по комплексному сопряжению
[permute](https://www.mathworks.com/help/matlab/ref/permute.html) | перестановка размерности массива
[ipermute](https://www.mathworks.com/help/matlab/ref/ipermute.html) | обратная перестановка размерности массива.
[circshift](https://www.mathworks.com/help/matlab/ref/circshift.html) | Круговой сдвиг массива
[shiftdim](https://www.mathworks.com/help/matlab/ref/shiftdim.html) | сдвиг размерности массива
[reshape](https://www.mathworks.com/help/matlab/ref/reshape.html) | Изменение формы массива
[squeeze](https://www.mathworks.com/help/matlab/ref/squeeze.html) | Удалить размеры длины 1

индекс

- | - | -
- | - | -
[colon](https://www.mathworks.com/help/matlab/ref/colon.html) | Создание вектора, подзапись массива и итерация цикла <code class="literal">for</code>.
[end](https://www.mathworks.com/help/matlab/ref/end.html) | Завершение блока кода или указание максимального индекса массива
[ind2sub](https://www.mathworks.com/help/matlab/ref/ind2sub.html) | Преобразование линейного индекса в подстрочный индекс
[sub2ind](https://www.mathworks.com/help/matlab/ref/sub2ind.html) | Преобразование подстрочного индекса в линейный индекс

### Тип значения {.row-span-2}

Создание числовых переменных

- | - | -
- | - | -
[double](https://www.mathworks.com/help/matlab/ref/double.html) | массив двойной точности
[single](https://www.mathworks.com/help/matlab/ref/single.html) | массив одинарной точности
[int8](https://www.mathworks.com/help/matlab/ref/int8.html) | 8-разрядный знаковый целочисленный массив
[int16](https://www.mathworks.com/help/matlab/ref/int16.html) | 16-разрядный знаковый целочисленный массив
[int32](https://www.mathworks.com/help/matlab/ref/int32.html) | 32-разрядный знаковый целочисленный массив
[int64](https://www.mathworks.com/help/matlab/ref/int64.html) | 64-разрядный знаковый целочисленный массив
[uint8](https://www.mathworks.com/help/matlab/ref/uint8.html) | Массив 8-битных беззнаковых целых чисел
[uint16](https://www.mathworks.com/help/matlab/ref/uint16.html) | Массив 16-битных беззнаковых целых чисел
[uint32](https://www.mathworks.com/help/matlab/ref/uint32.html) | Массив 32-битных беззнаковых целых чисел
[uint64](https://www.mathworks.com/help/matlab/ref/uint64.html) | 64-битный массив целых беззнаковых чисел

Преобразование между числовыми типами

- | - | -
- | - | -
[cast](https://www.mathworks.com/help/matlab/ref/cast.html) | Преобразование переменных в различные типы данных
[typecast](https://www.mathworks.com/help/matlab/ref/typecast.html) | Преобразование типов данных без изменения базовых данных

тип и значение запроса

- | - | -
- | - | -
[allfinite](https://www.mathworks.com/help/matlab/ref/allfinite.html") | Определить, являются ли все элементы массива конечными
[anynan](https://www.mathworks.com/help/matlab/ref/anynan.html") | Определить, является ли любой элемент массива NaN
[isinteger](https://www.mathworks.com/help/matlab/ref/isinteger.html) | Определить, является ли входной массив целочисленным
[isfloat](https://www.mathworks.com/help/matlab/ref/isfloat.html) | Определить, является ли входной массив массивом с плавающей точкой
[isnumeric](https://www.mathworks.com/help/matlab/ref/isnumeric.html) | Определить, является ли входной сигнал числовым массивом
[isreal](https://www.mathworks.com/help/matlab/ref/isreal.html) | Определить, использует ли массив комплексное хранение
[isfinite](https://www.mathworks.com/help/matlab/ref/isfinite.html) | Определить, какие элементы массива являются конечными
[isinf](https://www.mathworks.com/help/matlab/ref/isinf.html) | Определить, какие элементы массива являются бесконечными
[isnan](https://www.mathworks.com/help/matlab/ref/isnan.html) | Определить, какие элементы массива являются NaN

Диапазон значений
- | - | -
- | - | -
[eps](https://www.mathworks.com/help/matlab/ref/eps.html) | Относительная точность с плавающей точкой
[flintmax](https://www.mathworks.com/help/matlab/ref/flintmax.html) | Наибольшее последовательное целое число в формате с плавающей точкой
[Inf](https://www.mathworks.com/help/matlab/ref/inf.html) | Создать массив со всеми значениями `Inf`
[intmax](https://www.mathworks.com/help/matlab/ref/intmax.html) | Максимальное значение конкретного целого типа
[intmin](https://www.mathworks.com/help/matlab/ref/intmin.html) | Минимальное значение конкретного целого типа
[NaN](https://www.mathworks.com/help/matlab/ref/nan.html) | Создать массив, в котором все значения <code class="literal">NaN</code>
[realmax](https://www.mathworks.com/help/matlab/ref/realmax.html) | Наибольшее положительное число с плавающей запятой
[realmin](https://www.mathworks.com/help/matlab/ref/realmin.html) | Минимальное стандартное число с плавающей точкой

### Циклы и условные операторы

- | -
- | -
[if, elseif, else](https://www.mathworks.com/help/matlab/ref/if.html) | Выполнение оператора при истинности условия
[switch, case, otherwise](https://www.mathworks.com/help/matlab/ref/switch.html) | Выполнение одного из нескольких наборов операторов
[for](https://www.mathworks.com/help/matlab/ref/for.html) | Цикл `for`, используемый для повторения заданного числа раз
[while](https://www.mathworks.com/help/matlab/ref/while.html) | Цикл `while`, который выполняется несколько раз, пока условие истинно
[try, catch](https://www.mathworks.com/help/matlab/ref/try.html) | Выполнение оператора и отслеживание возникшей ошибки
[break](https://www.mathworks.com/help/matlab/ref/break.html) | Прервать выполнение цикла for или while
[return](https://www.mathworks.com/help/matlab/ref/return.html) | Возврат управления вызывающему скрипту или функции
[continue](https://www.mathworks.com/help/matlab/ref/continue.html) | Передает управление на следующую итерацию цикла `for` или `while`.
[pause](https://www.mathworks.com/help/matlab/ref/pause.html) | Временно приостанавливает выполнение `MATLAB`.
[parfor](https://www.mathworks.com/help/matlab/ref/parfor.html) | Параллельный цикл for
[end](https://www.mathworks.com/help/matlab/ref/end.html) | Завершение блока кода или указание максимального индекса массива {.style-list}

### Массив строк

- | - | -
- | - | -
[string](https://www.mathworks.com/help/matlab/ref/string.html) | Массив строк
[strings](https://www.mathworks.com/help/matlab/ref/strings.html) | Создать массив строк, не содержащий символов
[join](https://www.mathworks.com/help/matlab/ref/join.html) | Объединение строк
[plus](https://www.mathworks.com/help/matlab/ref/plus.html) | Добавление чисел, добавление строк

### Массив символов

- | - | -
- | - | -
[char](https://www.mathworks.com/help/matlab/ref/char.html) | Массив символов
[cellstr](https://www.mathworks.com/help/matlab/ref/cellstr.html) | Преобразование в ячеистый массив векторов символов
[blanks](https://www.mathworks.com/help/matlab/ref/blanks.html) | Создать массив пустых символов
[newline](https://www.mathworks.com/help/matlab/ref/newline.html) | Создать новую строку

### Массив символов или строк

- | - | -
- | - | -
[compose](https://www.mathworks.com/help/matlab/ref/compose.html) | Форматирование данных в несколько строк
[sprintf](https://www.mathworks.com/help/matlab/ref/sprintf.html) | Форматирование данных в виде строки или вектора символов
[strcat](https://www.mathworks.com/help/matlab/ref/strcat.html) | Конкатенация строк по горизонтали
[append](https://www.mathworks.com/help/matlab/ref/append.html) | Объединение строк

### Преобразование входных аргументов в символы или строки

- | -
- | -
[convertCharsToStrings](https://www.mathworks.com/help/matlab/ref/convertcharstostrings.html) | Преобразование массива символов в массив строк, остальные массивы остаются неизменными
[convertStringsToChars](https://www.mathworks.com/help/matlab/ref/convertstringstochars.html) | Преобразование массива строк в массив символов, остальные массивы остаются без изменений
[convertContainedStringsToChars](https://www.mathworks.com/help/matlab/ref/convertcontainedstringstochars.html) | Преобразовать массив строк на любом уровне массива ячеек или структуры {.style-list}

### CHAR или STRING - преобразование между числовыми и строковыми значениями

- | - | -
- | - | -
[double](https://www.mathworks.com/help/matlab/ref/double.html) | массив двойной точности
[string](https://www.mathworks.com/help/matlab/ref/string.html) | Массив строк
[str2double](https://www.mathworks.com/help/matlab/ref/str2double.html) | Преобразование строки в двойное значение
[num2str](https://www.mathworks.com/help/matlab/ref/num2str.html) | Преобразование чисел в символьные массивы

### Символ или строка - определите тип и атрибуты {.row-span-2}

тип данных

- | - | -
- | - | -
[ischar](https://www.mathworks.com/help/matlab/ref/ischar.html) | Определяет, является ли входной сигнал символьным массивом
[iscellstr](https://www.mathworks.com/help/matlab/ref/iscellstr.html) | Определяет, является ли входной массив ячеек символьным вектором
[isstring](https://www.mathworks.com/help/matlab/ref/isstring.html) | Определяет, является ли входной сигнал массивом строк
[isStringScalar](https://www.mathworks.com/help/matlab/ref/isstringscalar.html) | Определяет, является ли входной сигнал строковым массивом, содержащим один элемент

атрибут text

- | - | -
- | - | -
[strlength](https://www.mathworks.com/help/matlab/ref/strlength.html) | Длина строки
[isstrprop](https://www.mathworks.com/help/matlab/ref/isstrprop.html) | Определить, какие символы во входной строке относятся к указанной категории
[isletter](https://www.mathworks.com/help/matlab/ref/isletter.html) | Определить, какие символы являются буквами
[isspace](https://www.mathworks.com/help/matlab/ref/isspace.html) | Определить, какие символы являются пробельными символами

### символ или строка - найти и заменить {.row-span-2}

искать

- | - | -
- | - | -
[contains](https://www.mathworks.com/help/matlab/ref/contains.html) | Определить наличие шаблона в строке
[matches](https://www.mathworks.com/help/matlab/ref/matches.html) | Определить, совпадает ли шаблон со строкой
[count](https://www.mathworks.com/help/matlab/ref/count.html) | Подсчитать количество вхождений шаблона в строку.
[endsWith](https://www.mathworks.com/help/matlab/ref/endswith.html) | Определить, заканчивается ли строка шаблоном
[startsWith](https://www.mathworks.com/help/matlab/ref/startswith.html) | Определить, начинается ли строка с шаблона
[strfind](https://www.mathworks.com/help/matlab/ref/strfind.html) | Найти строку в других строках
[sscanf](https://www.mathworks.com/help/matlab/ref/sscanf.html) | Чтение форматированных данных из строки

replace

- | - | -
- | - | -
[replace](https://www.mathworks.com/help/matlab/ref/replace.html) | Найти и заменить одну или несколько подстрок
[replaceBetween](https://www.mathworks.com/help/matlab/ref/replacebetween.html) | Заменить подстроку между началом и концом
[strrep](https://www.mathworks.com/help/matlab/ref/strrep.html) | Найти и заменить подстроку

### Шаблон совпадения строк - построить шаблон

- | - | -
- | - | -
[pattern](https://www.mathworks.com/help/matlab/ref/pattern.html) | шаблон для поиска и сопоставления текста

### Шаблон совпадения строк - Шаблон совпадения символов

- | - | -
- | - | -
[alphanumericsPattern](https://www.mathworks.com/help/matlab/ref/alphanumericspattern.html) | Соответствие алфавитно-цифровым символам
[characterListPattern](https://www.mathworks.com/help/matlab/ref/characterlistpattern.html) | совпадение символов в списке
[digitsPattern](https://www.mathworks.com/help/matlab/ref/digitspattern.html) | Соответствие символов цифрам
[lettersPattern](https://www.mathworks.com/help/matlab/ref/letterspattern.html) | Соответствие буквенным символам
[whitespacePattern](https://www.mathworks.com/help/matlab/ref/whitespacepattern.html) | Соответствие пробельным символам
[wildcardPattern](https://www.mathworks.com/help/matlab/ref/wildcardpattern.html) | Искать как можно меньше символов любого типа

### Правила поиска по шаблону -pattern
- | - | -
- | - | -
[optionalPattern](https://www.mathworks.com/help/matlab/ref/optionalpattern.html) | Сделать сопоставление шаблонов необязательным
[possessivePattern](https://www.mathworks.com/help/matlab/ref/possessivepattern.html) | Искать шаблон без обратного пути
[caseSensitivePattern](https://www.mathworks.com/help/matlab/ref/casesensitivepattern.html) | Сопоставлять шаблоны с учетом регистра.
[caseInsensitivePattern](https://www.mathworks.com/help/matlab/ref/caseinsensitivepattern.html) | Соответствие шаблонам без учета регистра.
[asFewOfPattern](https://www.mathworks.com/help/matlab/ref/asfewofpattern.html) | Количество совпадений шаблонов должно быть как можно меньше
[asManyOfPattern](https://www.mathworks.com/help/matlab/ref/asmanyofpattern.html) | Соответствие шаблону как можно большее количество раз

### Шаблон сопоставления строк -Граница шаблона {.row-span-2}

- | -
- | -
[alphanumericBoundary](https://www.mathworks.com/help/matlab/ref/alphanumericboundary.html) | Определяет границу между алфавитно-цифровыми и неалфавитными символами
[digitBoundary](https://www.mathworks.com/help/matlab/ref/digitboundary.html) | Определяет границу между цифровыми и нецифровыми символами
[letterBoundary](https://www.mathworks.com/help/matlab/ref/letterboundary.html) | Определяет границу между алфавитными и неалфавитными символами
[whitespaceBoundary](https://www.mathworks.com/help/matlab/ref/whitespaceboundary.html) | Определяет границу между пробельными и не пробельными символами
[lineBoundary](https://www.mathworks.com/help/matlab/ref/lineboundary.html) | совпадает с началом или концом строки
[textBoundary](https://www.mathworks.com/help/matlab/ref/textboundary.html) | совпадает с началом или концом текста
[lookAheadBoundary](https://www.mathworks.com/help/matlab/ref/lookaheadboundary.html) | поиск границы перед указанным шаблоном
[lookBehindBoundary](https://www.mathworks.com/help/matlab/ref/lookbehindboundary.html) | граница после совпадения с указанным образцом {.style-list}

### Шаблон сопоставления строк - отображение заданного шаблона

- | - | -
- | - | -
[maskedPattern](https://www.mathworks.com/help/matlab/ref/maskedpattern.html) | Шаблон с заданным отображаемым именем
[namedPattern](https://www.mathworks.com/help/matlab/ref/namedpattern.html) | Укажите именованный шаблон

### Шаблон сопоставления строк - регулярное выражение

- | - | -
- | - | -
[regexp](https://www.mathworks.com/help/matlab/ref/regexp.html) | Соответствие регулярному выражению (с учетом регистра)
[regexpi](https://www.mathworks.com/help/matlab/ref/regexpi.html) | Сопоставление регулярных выражений (без учета регистра)
[regexprep](https://www.mathworks.com/help/matlab/ref/regexprep.html) | Замена текста с помощью регулярных выражений
[regexptranslate](https://www.mathworks.com/help/matlab/ref/regexptranslate.html) | Преобразование текста в регулярные выражения
[regexpPattern](https://www.mathworks.com/help/matlab/ref/regexppattern.html) | Соответствие шаблону указанного регулярного выражения

### Шаблон сопоставления строк - объединение и разделение

- | - | -
- | - | -
[join](https://www.mathworks.com/help/matlab/ref/join.html) | Объединение строк
[plus](https://www.mathworks.com/help/matlab/ref/plus.html) | Добавление чисел, добавление строк
[split](https://www.mathworks.com/help/matlab/ref/split.html) | Разделить строку по разделителю
[splitlines](https://www.mathworks.com/help/matlab/ref/splitlines.html) | Разделить строку по новой строке
[strjoin](https://www.mathworks.com/help/matlab/ref/strjoin.html) | Объединить строки в массиве
[strsplit](https://www.mathworks.com/help/matlab/ref/strsplit.html) | Разделяет строку или вектор символов по указанному разделителю
[strtok](https://www.mathworks.com/help/matlab/ref/strtok.html) | Выделение части строки
[extract](https://www.mathworks.com/help/matlab/ref/extract.html) | Извлечение подстроки из строки
[extractAfter](https://www.mathworks.com/help/matlab/ref/extractafter.html) | Извлечение подстроки после указанной позиции
[extractBefore](https://www.mathworks.com/help/matlab/ref/extractbefore.html) | Извлечь подстроку до указанной позиции
[extractBetween](https://www.mathworks.com/help/matlab/ref/extractbetween.html) | Извлечение подстроки между начальной и конечной точками

### Редактирование строк {.row-span-2}

- | - | -
- | - | -
[erase](https://www.mathworks.com/help/matlab/ref/erase.html) | Удалить подстроку в строке
[eraseBetween](https://www.mathworks.com/help/matlab/ref/erasebetween.html) | Удалить подстроку между началом и концом
[extract](https://www.mathworks.com/help/matlab/ref/extract.html) | Извлечь подстроку из строки
[extractAfter](https://www.mathworks.com/help/matlab/ref/extractafter.html) | Извлечь подстроку после указанной позиции
[extractBefore](https://www.mathworks.com/help/matlab/ref/extractbefore.html) | Извлечение подстроки перед указанной позицией
[extractBetween](https://www.mathworks.com/help/matlab/ref/extractbetween.html) | Извлечение подстроки между начальной и конечной точками
[insertAfter](https://www.mathworks.com/help/matlab/ref/insertafter.html) | Вставить строку после указанной подстроки
[insertBefore](https://www.mathworks.com/help/matlab/ref/insertbefore.html) | Вставить строку перед указанной подстрокой
[pad](https://www.mathworks.com/help/matlab/ref/pad.html) | Добавление в строку ведущих или завершающих символов
[strip](https://www.mathworks.com/help/matlab/ref/strip.html) | Удаление ведущих и завершающих символов в строке
[lower](https://www.mathworks.com/help/matlab/ref/lower.html) | преобразовать строку в нижний регистр
[upper](https://www.mathworks.com/help/matlab/ref/upper.html) | преобразовать строку в верхний регистр
[reverse](https://www.mathworks.com/help/matlab/ref/reverse.html) | Изменить порядок следования символов в строке
[deblank](https://www.mathworks.com/help/matlab/ref/deblank.html) | Удаление пробелов в конце строки
[strtrim](https://www.mathworks.com/help/matlab/ref/strtrim.html) | Удалить из строки ведущие и ведомые пробелы
[strjust](https://www.mathworks.com/help/matlab/ref/strjust.html) | Выровнять строку

### Сравнение строк

- | - | -
- | - | -
[matches](https://www.mathworks.com/help/matlab/ref/matches.html) | Определить, соответствует ли шаблон строке
[strcmp](https://www.mathworks.com/help/matlab/ref/strcmp.html) | Сравнить строки
[strcmpi](https://www.mathworks.com/help/matlab/ref/strcmpi.html) | Сравнить строки (без учета регистра)
[strncmp](https://www.mathworks.com/help/matlab/ref/strncmp.html) | Сравнивает первые <code class="literal">n</code> символов строки (с учетом регистра)
[strncmpi](https://www.mathworks.com/help/matlab/ref/strncmpi.html) | Сравнивает первые <code class="literal">n</code> символов строки (без учета регистра )

### Базовая арифметика {.row-span-3}

#### Сложение
- [+](https://www.mathworks.com/help/matlab/ref/plus.html) Сложение чисел, добавление строк
- [sum](https://www.mathworks.com/help/matlab/ref/sum.html) сумма элементов массива
- [cumsum](https://www.mathworks.com/help/matlab/ref/cumsum.html) кумулятивная сумма
- [movsum](https://www.mathworks.com/help/matlab/ref/movsum.html) перемещение суммы {.cols-2 style-none}

#### Вычитание

- [-](https://www.mathworks.com/help/matlab/ref/minus.html) вычитание
- [diff](https://www.mathworks.com/help/matlab/ref/diff.html) разность и приближенная производная {.cols-2 style-none}

#### Умножение

- | - | -
- | - | -
[.*](https://www.mathworks.com/help/matlab/ref/times.html) | Умножение
[*](https://www.mathworks.com/help/matlab/ref/mtimes.html) | Матричное умножение
[prod](https://www.mathworks.com/help/matlab/ref/prod.html) | произведение элементов массива
[cumprod](https://www.mathworks.com/help/matlab/ref/cumprod.html) | кумулятивное произведение
[pagemtimes](https://www.mathworks.com/help/matlab/ref/pagemtimes.html) | умножение матрицы на страницу
[tensorprod](https://www.mathworks.com/help/matlab/ref/tensorprod.html) | Тензорное произведение двух тензоров

#### Деление

- | - | -
- | - | -
[./](https://www.mathworks.com/help/matlab/ref/rdivide.html) | Правое деление массива
[.\\\](https://www.mathworks.com/help/matlab/ref/ldivide.html) | Деление массива налево
[/](https://www.mathworks.com/help/matlab/ref/mrdivide.html) | Решить систему линейных уравнений xA = B относительно x
[\\\](https://www.mathworks.com/help/matlab/ref/mldivide.html) | Решить систему линейных уравнений Ax = B относительно x

#### Мощность

- [.^](https://www.mathworks.com/help/matlab/ref/power.html) Поэлементное экспонирование
- [^](https://www.mathworks.com/help/matlab/ref/mpower.html) Мощность матрицы {.cols-2}

#### Транспонирование

- | - | -
- | - | -
[.'](https://www.mathworks.com/help/matlab/ref/transpose.html) | Транспонировать вектор или матрицу
['](https://www.mathworks.com/help/matlab/ref/ctranspose.html) | транспонирование по комплексному сопряжению
[pagetranspose](https://www.mathworks.com/help/matlab/ref/pagetranspose.html) | Транспонирование по страницам
[pagectranspose](https://www.mathworks.com/help/matlab/ref/pagectranspose.html) | Транспонирование по комплексному сопряжению на страницу

#### Условные обозначения массивов

- [uminus](https://www.mathworks.com/help/matlab/ref/uminus.html) унарное вычитание
- [uplus](https://www.mathworks.com/help/matlab/ref/uplus.html) унарное сложение {.cols-2}

### Модульное деление и округление

- | - | -
- | - | -
[mod](https://www.mathworks.com/help/matlab/ref/mod.html) | Остаток после деления (операция модуло)
[rem](https://www.mathworks.com/help/matlab/ref/rem.html) | Остаток после деления
[idivide](https://www.mathworks.com/help/matlab/ref/idivide.html) | Делимость с возможностью округления
[ceil](https://www.mathworks.com/help/matlab/ref/ceil.html) | Округление в сторону положительной бесконечности
[fix](https://www.mathworks.com/help/matlab/ref/fix.html) | округление в сторону нуля
[floor](https://www.mathworks.com/help/matlab/ref/floor.html) | округление в сторону отрицательной бесконечности
[round](https://www.mathworks.com/help/matlab/ref/round.html) | округлить до ближайшего десятичного или целого числа

### Пользовательские двоичные функции

- | - | -
- | - | -
[bsxfun](https://www.mathworks.com/help/matlab/ref/bsxfun.html) | Применение операций "по элементам" к двум массивам (с включенным неявным расширением)

### Реляционные операции

сравнение значений

- | - | -
- | - | -
[==](https://www.mathworks.com/help/matlab/ref/eq.html) | Определить равенство
[>=](https://www.mathworks.com/help/matlab/ref/ge.html) | Определить больше или равно
[>](https://www.mathworks.com/help/matlab/ref/gt.html) | Определить больше, чем
[<=](https://www.mathworks.com/help/matlab/ref/le.html) | Определить меньше или равно
[<](https://www.mathworks.com/help/matlab/ref/lt.html) | Определить меньше, чем
[~=](https://www.mathworks.com/help/matlab/ref/ne.html) | Определить неравенство
[isequal](https://www.mathworks.com/help/matlab/ref/isequal.html) | Определить равенство массивов
[isequaln](https://www.mathworks.com/help/matlab/ref/isequaln.html) | Проверка равенства массивов, значения `NaN` рассматриваются как равные

### Логические (булевы) операции

условие истинности или ложности

- | - | -
- | - | -
[Замыкание &&, \|\|](https://www.mathworks.com/help/matlab/ref/logicaloperatorsshortcircuit.html) | Логические операторы с функцией замыкания
[&](https://www.mathworks.com/help/matlab/ref/and.html) | Вычислительная логика `AND`
[~](https://www.mathworks.com/help/matlab/ref/not.html) | Вычислительная логика `NOT`
[\|](https://www.mathworks.com/help/matlab/ref/or.html) | Вычислительная логика `OR`
[xor](https://www.mathworks.com/help/matlab/ref/xor.html) | Вычислительная логика `OR`
[all](https://www.mathworks.com/help/matlab/ref/all.html) | Определить, являются ли все элементы массива ненулевыми или `истинными`
[any](https://www.mathworks.com/help/matlab/ref/any.html) | Определить, являются ли все элементы массива ненулевыми
[false](https://www.mathworks.com/help/matlab/ref/false.html) | Логическое `0` (false)
[find](https://www.mathworks.com/help/matlab/ref/find.html) | Найти индекс и значение ненулевых элементов
[islogical](https://www.mathworks.com/help/matlab/ref/islogical.html) | Определить, является ли входной массив логическим
[logical](https://www.mathworks.com/help/matlab/ref/logical.html) | Преобразование числовых значений в логические
[true](https://www.mathworks.com/help/matlab/ref/true.html) | Логическое значение `1` (true)

### Операция установки

объединение, пересечение, отношение множества

- | - | -
- | - | -
[intersect](https://www.mathworks.com/help/matlab/ref/double.intersect.html) | Установить пересечение двух массивов
[ismember](https://www.mathworks.com/help/matlab/ref/double.ismember.html) | Определить, является ли элемент массива членом массива set
[setdiff](https://www.mathworks.com/help/matlab/ref/double.setdiff.html) | Установить разность между двумя массивами
[setxor](https://www.mathworks.com/help/matlab/ref/double.setxor.html) | Установить XOR двух массивов
[union](https://www.mathworks.com/help/matlab/ref/double.union.html) | Установить объединение двух массивов
[unique](https://www.mathworks.com/help/matlab/ref/double.unique.html) | Уникальное значение в массиве
[ismembertol](https://www.mathworks.com/help/matlab/ref/ismembertol.html) | Установка членства в пределах допуска
[uniquetol](https://www.mathworks.com/help/matlab/ref/uniquetol.html) | уникальные значения в пределах допуска
[join](https://www.mathworks.com/help/matlab/ref/table.join.html) | Объединить две таблицы или расписания строка за строкой с использованием ключевой переменной
[innerjoin](https://www.mathworks.com/help/matlab/ref/innerjoin.html) | Внутреннее соединение между двумя таблицами или расписаниями
[outerjoin](https://www.mathworks.com/help/matlab/ref/outerjoin.html) | Внешнее соединение двух таблиц или расписаний
### Побитовые операции

установка, смещение или сравнение определенных битовых полей

- | - | -
- | - | -
[bitand](https://www.mathworks.com/help/matlab/ref/bitand.html) | Побитовое `AND`
[bitor](https://www.mathworks.com/help/matlab/ref/bitor.html) | Побитовое `OR`
[bitxor](https://www.mathworks.com/help/matlab/ref/bitxor.html) | Побитовое `XOR`
[bitcmp](https://www.mathworks.com/help/matlab/ref/bitcmp.html) | Побитовое дополнение
[bitget](https://www.mathworks.com/help/matlab/ref/bitget.html) | Получить бит в указанной позиции
[bitset](https://www.mathworks.com/help/matlab/ref/bitset.html) | Установить бит в указанную позицию
[bitshift](https://www.mathworks.com/help/matlab/ref/bitshift.html) | Сдвиг битов на указанное количество бит
[swapbytes](https://www.mathworks.com/help/matlab/ref/swapbytes.html) | Поменять порядок следования байтов

Импорт и экспорт данных
---

### текстовый файл - чтение и запись таблицы или расписания {.row-span-2}

#### Базовый импорт и экспорт

- | - | -
- | - | -
[readtable](https://www.mathworks.com/help/matlab/ref/readtable.html) | Создание таблицы на основе файла
[writetable](https://www.mathworks.com/help/matlab/ref/writetable.html) | Запись таблицы в файл
[readtimetable](https://www.mathworks.com/help/matlab/ref/readtimetable.html) | Создать расписание на основе файла
[writetimetable](https://www.mathworks.com/help/matlab/ref/writetimetable.html) | Запись расписания в файл

#### Определение правил импорта

- | -
- | -
[detectImportOptions](https://www.mathworks.com/help/matlab/ref/detectimportoptions.html) | Генерировать параметры импорта на основе содержимого файла
[delimitedTextImportOptions](https://www.mathworks.com/help/matlab/ref/matlab.io.text.delimitedtextimportoptions.html) | Объект опций импорта для разделенного текста
[fixedWidthImportOptions](https://www.mathworks.com/help/matlab/ref/matlab.io.text.fixedwidthimportoptions.html) | Объект опций импорта для текстовых файлов фиксированной ширины
[xmlImportOptions](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.xmlimportoptions.html) | Объект опций импорта для XML-файла
[htmlImportOptions](https://www.mathworks.com/help/matlab/ref/matlab.io.html.htmlimportoptions.html) | Объект опций импорта для HTML-файлов
[wordDocumentImportOptions](https://www.mathworks.com/help/matlab/ref/matlab.io.word.worddocumentimportoptions.html) | Объект параметров импорта файлов `Microsoft Word`
[getvaropts](https://www.mathworks.com/help/matlab/ref/matlab.io.text.delimitedtextimportoptions.getvaropts.html) | Получить параметры импорта переменных
[setvaropts](https://www.mathworks.com/help/matlab/ref/matlab.io.text.delimitedtextimportoptions.setvaropts.html) | Установить параметры импорта переменных
[setvartype](https://www.mathworks.com/help/matlab/ref/matlab.io.text.delimitedtextimportoptions.setvartype.html) | Установить тип данных переменной
[preview](https://www.mathworks.com/help/matlab/ref/matlab.io.text.delimitedtextimportoptions.preview.html) | Предварительный просмотр восьми строк данных в файле с опциями импорта
{.style-list}
### Текстовые файлы - чтение и запись матриц и массивов
- | - | -
- | - | -
[readmatrix](https://www.mathworks.com/help/matlab/ref/readmatrix.html) | Чтение матрицы из файла
[writematrix](https://www.mathworks.com/help/matlab/ref/writematrix.html) | Запись матрицы в файл
[readcell](https://www.mathworks.com/help/matlab/ref/readcell.html) | Чтение массива ячеек из файла
[writecell](https://www.mathworks.com/help/matlab/ref/writecell.html) | Запись массива ячеек в файл
[readvars](https://www.mathworks.com/help/matlab/ref/readvars.html) | Чтение переменных из файла
[textscan](https://www.mathworks.com/help/matlab/ref/textscan.html) | Чтение форматированных данных из текстового файла или строки
[type](https://www.mathworks.com/help/matlab/ref/type.html) | Отображение содержимого файла
[fileread](https://www.mathworks.com/help/matlab/ref/fileread.html) | Чтение содержимого файла в текстовом формате
[readlines](https://www.mathworks.com/help/matlab/ref/readlines.html) | Чтение строк файла в виде массива строк
[writelines](https://www.mathworks.com/help/matlab/ref/writelines.html) | Запись текста в файл

### Электронная таблица - чтение и запись таблицы или расписания {.row-span-2}

Базовый импорт и экспорт

- | - | -
- | - | -
[readtable](https://www.mathworks.com/help/matlab/ref/readtable.html) | Создание таблицы из файла
[writetable](https://www.mathworks.com/help/matlab/ref/writetable.html) | Записать таблицу в файл
[readtimetable](https://www.mathworks.com/help/matlab/ref/readtimetable.html) | Создать расписание из файла
[writetimetable](https://www.mathworks.com/help/matlab/ref/writetimetable.html) | Запись расписания в файл
[sheetnames](https://www.mathworks.com/help/matlab/ref/sheetnames.html) | Получить имена листов из файла электронной таблицы
{.style-list}

Определение правил импорта

- | -
- | -
[detectImportOptions](https://www.mathworks.com/help/matlab/ref/detectimportoptions.html) | Генерировать параметры импорта на основе содержимого файла
[spreadsheetImportOptions](https://www.mathworks.com/help/matlab/ref/matlab.io.spreadsheet.spreadsheetimportoptions.html) | Объект опций импорта электронных таблиц
[getvaropts](https://www.mathworks.com/help/matlab/ref/matlab.io.text.delimitedtextimportoptions.getvaropts.html) | Получить параметры импорта переменных
[setvaropts](https://www.mathworks.com/help/matlab/ref/matlab.io.text.delimitedtextimportoptions.setvaropts.html) | Установить параметры импорта переменных
[setvartype](https://www.mathworks.com/help/matlab/ref/matlab.io.text.delimitedtextimportoptions.setvartype.html) | Установить тип данных переменной
[preview](https://www.mathworks.com/help/matlab/ref/matlab.io.text.delimitedtextimportoptions.preview.html) | Предварительный просмотр восьми строк данных в файле с опциями импорта {.style-list}

### Электронная таблица - Чтение и запись матриц и массивов

- | - | -
- | - | -
[readmatrix](https://www.mathworks.com/help/matlab/ref/readmatrix.html) | Чтение матрицы из файла
[writematrix](https://www.mathworks.com/help/matlab/ref/writematrix.html) | Запись матрицы в файл
[readcell](https://www.mathworks.com/help/matlab/ref/readcell.html) | Чтение массива ячеек из файла
[writecell](https://www.mathworks.com/help/matlab/ref/writecell.html) | Запись массива ячеек в файл
[readvars](https://www.mathworks.com/help/matlab/ref/readvars.html) | Чтение переменных из файла
[importdata](https://www.mathworks.com/help/matlab/ref/importdata.html) | Загрузка данных из файла

### изображения

- | - | -
- | - | -
[imfinfo](https://www.mathworks.com/help/matlab/ref/imfinfo.html) | Информация о графических файлах
[imread](https://www.mathworks.com/help/matlab/ref/imread.html) | Считывание изображения из графического файла
[imwrite](https://www.mathworks.com/help/matlab/ref/imwrite.html) | Запись изображения в графический файл
[Tiff](https://www.mathworks.com/help/matlab/ref/tiff.html) | Вход в MATLAB для подпрограмм библиотеки LibTIFF

### Чтение или запись NetCDF-файла {.row-span-2}

- | - | -
- | - | -
[nccreate](https://www.mathworks.com/help/matlab/ref/nccreate.html) | Создание переменных в NetCDF-файле
[ncdisp](https://www.mathworks.com/help/matlab/ref/ncdisp.html) | Отображает содержимое источника данных NetCDF в окне командной строки
[ncinfo](https://www.mathworks.com/help/matlab/ref/ncinfo.html) | Возвращает информацию об источнике данных NetCDF
[ncread](https://www.mathworks.com/help/matlab/ref/ncread.html) | Чтение данных переменных из источника данных NetCDF
[ncreadatt](https://www.mathworks.com/help/matlab/ref/ncreadatt.html) | Чтение значений атрибутов в источнике данных NetCDF
[ncwrite](https://www.mathworks.com/help/matlab/ref/ncwrite.html) | Запись данных в NetCDF-файл
[ncwriteatt](https://www.mathworks.com/help/matlab/ref/ncwriteatt.html) | Запись атрибутов в NetCDF-файл
[ncwriteschema](https://www.mathworks.com/help/matlab/ref/ncwriteschema.html) | Добавляет определение схемы NetCDF в NetCDF-файл

### Пакет библиотек NetCDF - Библиотечные функции

- | -
- | -
[netcdf.getChunkCache](https://www.mathworks.com/help/matlab/ref/netcdf.getchunkcache.html) | Получает настройки кэша чанков для библиотеки NetCDF
[netcdf.inqLibVers](https://www.mathworks.com/help/matlab/ref/netcdf.inqlibvers.html) | Возвращает информацию о версии библиотеки NetCDF
[netcdf.setChunkCache](https://www.mathworks.com/help/matlab/ref/netcdf.setchunkcache.html) | Устанавливает стандартные настройки кэш-памяти для библиотеки NetCDF
[netcdf.setDefaultFormat](https://www.mathworks.com/help/matlab/ref/netcdf.setdefaultformat.html) | Изменение формата файла netCDF по умолчанию {.style-list}

### Пакет библиотеки NetCDF -file operations {.row-span-2}

- | -
- | -
[netcdf.abort](https://www.mathworks.com/help/matlab/ref/netcdf.abort.html) | восстанавливает последнее определение файла netCDF
[netcdf.close](https://www.mathworks.com/help/matlab/ref/netcdf.close.html) | закрывает файл netCDF
[netcdf.create](https://www.mathworks.com/help/matlab/ref/netcdf.create.html) | Создание нового набора данных NetCDF
[netcdf.endDef](https://www.mathworks.com/help/matlab/ref/netcdf.enddef.html) | Завершить режим определения файла netCDF
[netcdf.inq](https://www.mathworks.com/help/matlab/ref/netcdf.inq.html) | Возвращает информацию о файле netCDF
[netcdf.inqFormat](https://www.mathworks.com/help/matlab/ref/netcdf.inqformat.html) | Определяет формат NetCDF-файла
[netcdf.inqGrps](https://www.mathworks.com/help/matlab/ref/netcdf.inqgrps.html) | Получает массив идентификаторов подгрупп
[netcdf.inqUnlimDims](https://www.mathworks.com/help/matlab/ref/netcdf.inqunlimdims.html) | Получает список бесконечных размерностей в группе
[netcdf.open](https://www.mathworks.com/help/matlab/ref/netcdf.open.html) | Открыть источник данных NetCDF
[netcdf.reDef](https://www.mathworks.com/help/matlab/ref/netcdf.redef.html) | Переводит открытый netCDF-файл в режим определения
[netcdf.setFill](https://www.mathworks.com/help/matlab/ref/netcdf.setfill.html) | Установить режим заполнения netCDF-файла
[netcdf.sync](https://www.mathworks.com/help/matlab/ref/netcdf.sync.html) | Синхронизация файлов netCDF на диске

### Пакет библиотек NetCDF -Размеры

- | - | -
- | - | -
[netcdf.defdim](https://www.mathworks.com/help/matlab/ref/netcdf.defdim.html) | Создание размерностей netCDF
[netcdf.inqDim](https://www.mathworks.com/help/matlab/ref/netcdf.inqdim.html) | Возвращает имена и длины размерностей netCDF
[netcdf.inqDimID](https://www.mathworks.com/help/matlab/ref/netcdf.inqdimid.html) | Возвращает идентификатор размерности
[netcdf.renameDim](https://www.mathworks.com/help/matlab/ref/netcdf.renamedim.html) | Изменение имен размеров netCDF

### Пакет библиотек NetCDF -group

- | - | -
- | - | -
[netcdf.defGrp](https://www.mathworks.com/help/matlab/ref/netcdf.defgrp.html) | Создание групп в NetCDF-файле
[netcdf.inqDimIDs](https://www.mathworks.com/help/matlab/ref/netcdf.inqdimids.html) | Получает список идентификаторов измерений в группе
[netcdf.inqGrpName](https://www.mathworks.com/help/matlab/ref/netcdf.inqgrpname.html) | Получение имени группы
[netcdf.inqGrpNameFull](https://www.mathworks.com/help/matlab/ref/netcdf.inqgrpnamefull.html) | полное имя пути к группе
[netcdf.inqGrpParent](https://www.mathworks.com/help/matlab/ref/netcdf.inqgrpparent.html) | Получение идентификатора родительской группы.
[netcdf.inqNcid](https://www.mathworks.com/help/matlab/ref/netcdf.inqncid.html) | Возвращает идентификатор именованной группы
[netcdf.inqVarIDs](https://www.mathworks.com/help/matlab/ref/netcdf.inqvarids.html) | Идентификаторы всех переменных в группе

### Пакет библиотеки NetCDF -variable {.row-span-3}

- | -
- | -
[netcdf.defVarFill](https://www.mathworks.com/help/matlab/ref/netcdf.defvarfill.html) | Определяет параметр заполнения для переменной NetCDF
[netcdf.defVar](https://www.mathworks.com/help/matlab/ref/netcdf.defvar.html) | Создание NetCDF-переменной
[netcdf.defVarChunking](https://www.mathworks.com/help/matlab/ref/netcdf.defvarchunking.html) | Определяет поведение кусков для NetCDF-переменных
[netcdf.defVarDeflate](https://www.mathworks.com/help/matlab/ref/netcdf.defvardeflate.html) | Определяет параметры сжатия для переменных NetCDF
[netcdf.defVarFletcher32](https://www.mathworks.com/help/matlab/ref/netcdf.defvarfletcher32.html) | Определяет параметры валидации для переменных NetCDF
[netcdf.getVar](https://www.mathworks.com/help/matlab/ref/netcdf.getvar.html) | Чтение данных из переменной NetCDF
[netcdf.inqVar](https://www.mathworks.com/help/matlab/ref/netcdf.inqvar.html) | Информация о переменных
[netcdf.inqVarChunking](https://www.mathworks.com/help/matlab/ref/netcdf.inqvarchunking.html) | Определяет настройки разбиения на куски для переменных NetCDF
[netcdf.inqVarDeflate](https://www.mathworks.com/help/matlab/ref/netcdf.inqvardeflate.html) | Определяет настройки сжатия для переменных NetCDF
[netcdf.inqVarFill](https://www.mathworks.com/help/matlab/ref/netcdf.inqvarfill.html) | Определяет значение параметра заполнения для переменной NetCDF
[netcdf.inqVarFletcher32](https://www.mathworks.com/help/matlab/ref/netcdf.inqvarfletcher32.html) | О настройках контрольной суммы Fletcher32 для переменных NetCDF
[netcdf.inqVarID](https://www.mathworks.com/help/matlab/ref/netcdf.inqvarid.html) | Возвращает идентификатор, связанный с именем переменной
[netcdf.putVar](https://www.mathworks.com/help/matlab/ref/netcdf.putvar.html) | Запись данных в переменную NetCDF
[netcdf.renameVar](https://www.mathworks.com/help/matlab/ref/netcdf.renamevar.html) | Изменение имени переменной netCDF {.style-list}

### Пакет библиотеки NetCDF -properties

- | - | -
- | - | -
[netcdf.copyAtt](https://www.mathworks.com/help/matlab/ref/netcdf.copyatt.html) | Скопировать атрибут в новое место.
[netcdf.delAtt](https://www.mathworks.com/help/matlab/ref/netcdf.delatt.html) | Удалить атрибут netCDF
[netcdf.getAtt](https://www.mathworks.com/help/matlab/ref/netcdf.getatt.html) | Возвращает атрибут NetCDF
[netcdf.inqAtt](https://www.mathworks.com/help/matlab/ref/netcdf.inqatt.html) | Возвращает информацию об атрибутах NetCDF
[netcdf.inqAttID](https://www.mathworks.com/help/matlab/ref/netcdf.inqattid.html) | Возвращает идентификатор атрибута netCDF
[netcdf.inqAttName](https://www.mathworks.com/help/matlab/ref/netcdf.inqattname.html) | Возвращает имя атрибута netCDF
[netcdf.putAtt](https://www.mathworks.com/help/matlab/ref/netcdf.putatt.html) | Запись атрибутов netCDF
[netcdf.renameAtt](https://www.mathworks.com/help/matlab/ref/netcdf.renameatt.html) | Изменить имя атрибута

### Пакет библиотеки NetCDF - определяемые пользователем типы
:- | :-
:- | :-
[netcdf.defVlen](https://www.mathworks.com/help/matlab/ref/netcdf.defvlen.html) | Определение типа массива переменной длины, определяемого пользователем (NC_VLEN)
[netcdf.inqUserType](https://www.mathworks.com/help/matlab/ref/netcdf.inqusertype.html) | Возврат информации о типе, определяемом пользователем
[netcdf.inqVlen](https://www.mathworks.com/help/matlab/ref/netcdf.inqvlen.html) | Возврат информации о типе `NC_VLEN`, определяемом пользователем {.style-list}
### Пакет библиотеки NetCDF -Utilities

- | -
- | -
[netcdf.getConstant](https://www.mathworks.com/help/matlab/ref/netcdf.getconstant.html) | Возвращает значение именованной константы
[netcdf.getConstantNames](https://www.mathworks.com/help/matlab/ref/netcdf.getconstantnames.html) | возвращает список констант, известных библиотеке netCDF {.style-list}

### Чтение или запись файлов HDF5

- | - | -
- | - | -
[h5create](https://www.mathworks.com/help/matlab/ref/h5create.html) | Создать набор данных HDF5
[h5disp](https://www.mathworks.com/help/matlab/ref/h5disp.html) | Отображение содержимого файлов HDF5
[h5info](https://www.mathworks.com/help/matlab/ref/h5info.html) | Информация о файлах HDF5
[h5read](https://www.mathworks.com/help/matlab/ref/h5read.html) | Чтение данных из набора данных HDF5
[h5readatt](https://www.mathworks.com/help/matlab/ref/h5readatt.html) | Чтение атрибутов из файлов HDF5
[h5write](https://www.mathworks.com/help/matlab/ref/h5write.html) | Запись набора данных HDF5
[h5writeatt](https://www.mathworks.com/help/matlab/ref/h5writeatt.html) | Запись атрибутов HDF5

### Пакет библиотек HDF5 {.row-span-4}

- | -
- | -
[Библиотека (H5)](https://www.mathworks.com/help/matlab/ref/libraryh5.html) | Функции общего назначения для использования со всей библиотекой HDF5
[Атрибут (H5A)](https://www.mathworks.com/help/matlab/ref/attributeh5a.html) | Метаданные, связанные с наборами или группами данных
[Dataset (H5D)](https://www.mathworks.com/help/matlab/ref/dataseth5d.html) | Многомерные массивы элементов данных и вспомогательные метаданные
[Dimension Scale (H5DS)](https://www.mathworks.com/help/matlab/ref/dimensionscaleh5ds.html) | Шкала размерности, связанная с размерами набора данных
[Error (H5E)](https://www.mathworks.com/help/matlab/ref/errorh5e.html) | Обработка ошибок
[File (H5F)](https://www.mathworks.com/help/matlab/ref/fileh5f.html) | Доступ к файлам HDF5
[Group (H5G)](https://www.mathworks.com/help/matlab/ref/grouph5g.html) | Организация объектов в файле
[Идентификатор (H5I)](https://www.mathworks.com/help/matlab/ref/identifierh5i.html) | Идентификаторы объектов HDF5
[Link (H5L)](https://www.mathworks.com/help/matlab/ref/linkh5l.html) | Ссылки в файле HDF5
[MATLAB (H5ML)](https://www.mathworks.com/help/matlab/ref/matlabh5ml.html) | Утилитные функции `MATLAB`, не входящие в состав библиотеки HDF5 C
[Object (H5O)](https://www.mathworks.com/help/matlab/ref/objecth5o.html) | Объекты в файле
[Property (H5P)](https://www.mathworks.com/help/matlab/ref/propertyh5p.html) | Списки свойств объектов
[Reference (H5R)](https://www.mathworks.com/help/matlab/ref/referenceh5r.html) | Ссылки на HDF5
[Dataspace (H5S)](https://www.mathworks.com/help/matlab/ref/dataspaceh5s.html) | Размерность набора данных
[Datatype (H5T)](https://www.mathworks.com/help/matlab/ref/datatypeh5t.html) | Тип данных элементов в наборе данных {.style-list}

### Файлы HDF4 - Дополнительные функции

- | -
- | -
[hdfinfo](https://www.mathworks.com/help/matlab/ref/hdfinfo.html) | Информация о файлах HDF4 или HDF-EOS
[hdfread](https://www.mathworks.com/help/matlab/ref/hdfread.html) | Чтение данных из файлов HDF4 или HDF-EOS
[imread](https://www.mathworks.com/help/matlab/ref/imread.html) | Чтение изображения из графического файла
[imwrite](https://www.mathworks.com/help/matlab/ref/imwrite.html) | Запись изображения в графический файл

### Низкоуровневые функции -package {.row-span-3}

- | -
- | -
[matlab.io.hdf4.sd](https://www.mathworks.com/help/matlab/ref/matlab.io.hdf4.sd.html) | Прямое взаимодействие с интерфейсом многофайловых наборов научных данных (SD) HDF4
[matlab.io.hdfeos.gd](https://www.mathworks.com/help/matlab/ref/matlab.io.hdfeos.gd.html) | Низкоуровневый доступ к данным сетки HDF-EOS
[matlab.io.hdfeos.sw](https://www.mathworks.com/help/matlab/ref/matlab.io.hdfeos.sw.html) | Низкоуровневый доступ к сегментированным файлам HDF-EOS

#### Функции низкого уровня -Функции

- | -
- | -
[hdfan](https://www.mathworks.com/help/matlab/ref/hdfan.html) | Ввод интерфейса многофайловой аннотации HDF (AN)
[hdfhx](https://www.mathworks.com/help/matlab/ref/hdfhx.html) | Вход в интерфейс внешних данных HDF (HX)
[hdfh](https://www.mathworks.com/help/matlab/ref/hdfh.html) | Вход в интерфейс HDF H
[hdfhd](https://www.mathworks.com/help/matlab/ref/hdfhd.html) | Вход в интерфейс HDF HD
[hdfhe](https://www.mathworks.com/help/matlab/ref/hdfhe.html) | Вход в интерфейс HDF HE
[hdfml](https://www.mathworks.com/help/matlab/ref/hdfml.html) | Утилиты для работы с функциями ввода HDF в `MATLAB`
[hdfpt](https://www.mathworks.com/help/matlab/ref/hdfpt.html) | Интерфейс точечного объекта HDF-EOS
[hdfv](https://www.mathworks.com/help/matlab/ref/hdfv.html) | Интерфейс входа в HDF Vgroup (V)
[hdfvf](https://www.mathworks.com/help/matlab/ref/hdfvf.html) | Вход функции VF в интерфейс HDF Vdata
[hdfvh](https://www.mathworks.com/help/matlab/ref/hdfvh.html) | Запись функции VH в интерфейсе HDF Vdata
[hdfvs](https://www.mathworks.com/help/matlab/ref/hdfvs.html) | Запись функции VS в интерфейсе HDF Vdata
[hdfdf24](https://www.mathworks.com/help/matlab/ref/hdfdf24.html) | Запись интерфейса 24-битного растрового изображения HDF (DF24)
[hdfdfr8](https://www.mathworks.com/help/matlab/ref/hdfdfr8.html) | Запись интерфейса 8-битного растрового изображения HDF (DFR8)

### FITS-файл -функция

- | -
- | -
[fitsdisp](https://www.mathworks.com/help/matlab/ref/fitsdisp.html) | Отображение метаданных FITS-файла
[fitsinfo](https://www.mathworks.com/help/matlab/ref/fitsinfo.html) | Информация о файлах FITS
[fitsread](https://www.mathworks.com/help/matlab/ref/fitsread.html) | Чтение данных из файлов FITS
[fitswrite](https://www.mathworks.com/help/matlab/ref/fitswrite.html) | Запись изображения в FITS-файл

### Файлы FITS - доступ к файлам

- | -
- | -
[createFile](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.createfile.html) | Создать FITS-файл
[openFile](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.openfile.html) | Открыть FITS-файл
[openDiskFile](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.opendiskfile.html) | Открыть FITS-файл
[closeFile](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.closefile.html) | Закрыть FITS-файл
[deleteFile](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.deletefile.html) | Удалить FITS-файл
[fileName](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.filename.html) | Имя FITS-файла
[fileMode](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.filemode.html) | Режим ввода/вывода для FITS-файлов
### FITS-файлы - обработка изображений

- | -
- | -
[createImg](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.createimg.html) | Создание FITS-изображения
[getImgSize](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.getimgsize.html) | Размер изображения
[getImgType](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.getimgtype.html) | Тип данных изображения
[insertImg](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.insertimg.html) | Вставить FITS-изображение после текущего изображения
[readImg](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.readimg.html) | Чтение данных изображения
[setBscale](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.setbscale.html) | Сброс масштаба изображения
[writeImg](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.writeimg.html) | запись FITS-изображения

### FITS-файл - ключевое слово {.row-span-2}

- | -
- | -
[readCard](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.readcard.html) | Заглавная запись ключевых слов
[readKey](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.readkey.html) | Ключевое слово
[readKeyCmplx](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.readkeycmplx.html) | Ключевое слово в виде комплексного скалярного значения
[readKeyDbl](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.readkeydbl.html) | Ключевое слово в виде значения двойной точности
[readKeyLongLong](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.readkeylonglong.html) | Ключевое слово в виде `int64`
[readKeyLongStr](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.readkeylongstr.html) | Значение длинной строки
[readKeyUnit](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.readkeyunit.html) | Строка единиц измерения в ключе
[readRecord](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.readrecord.html) | Запись заголовка, заданная номером
[writeComment](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.writecomment.html) | Запись или добавление ключевого слова COMMENT к CHU
[writeDate](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.writedate.html) | Запись ключевого слова DATE в CHU
[writeKey](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.writekey.html) | Обновление или добавление новых ключевых слов в текущий HDU
[writeKeyUnit](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.writekeyunit.html) | Записать строку физических единиц измерения
[writeHistory](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.writehistory.html) | Запись или добавление ключевого слова HISTORY в CHU
[deleteKey](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.deletekey.html) | Удаление ключа по имени
[deleteRecord](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.deleterecord.html) | Удаление ключевых слов по номеру записи
[getHdrSpace](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.gethdrspace.html) | Количество ключевых слов в заголовке

### Файлы FITS - доступ к блоку данных заголовка (HDU)

- | -
- | -
[copyHDU](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.copyhdu.html) | Копирование текущего HDU из одного файла в другой
[getHDUnum](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.gethdunum.html) | Номер текущего HDU в файле FITS
[getHDUtype](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.gethdutype.html) | Тип текущего HDU
[getNumHDUs](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.getnumhdus.html) | Общее количество HDU в файле FITS
[movAbsHDU](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.movabshdu.html) | Переход к абсолютной нумерации HDU
[movNamHDU](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.movnamhdu.html) | Переход к первому HDU, содержащему определенный тип и значение ключевого слова
[movRelHDU](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.movrelhdu.html) | Перемещение относительного количества HDU из текущего HDU
[writeChecksum](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.writechecksum.html) | Вычисление и запись контрольной суммы текущего HDU
[deleteHDU](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.deletehdu.html) | Удалить текущий HDU в FITS-файле

### Файлы FITS - сжатие изображений

- | -
- | -
[imgCompress](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.imgcompress.html) | Сжатие HDU из одного файла в другой
[isCompressedImg](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.iscompressedimg.html) | Определить, сжато ли текущее изображение
[setCompressionType](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.setcompressiontype.html) | Установить тип сжатия изображения
[setHCompScale](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.sethcompscale.html) | Установка параметров масштабирования алгоритма HCOMPRESS
[setHCompSmooth](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.sethcompsmooth.html) | Устанавливает сглаживание для изображений, сжатых с помощью алгоритма HCOMPRESS
[setTileDim](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.settiledim.html) | Установка размеров плитки

### FITS-файл - таблица в формате ASCII и двоичная таблица {.row-span-3}

- | -
- | -
[createTbl](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.createtbl.html) | Создать новое расширение таблицы ASCII или бинарной таблицы
[insertCol](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.insertcol.html) | Вставить столбец в таблицу
[insertRows](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.insertrows.html) | Вставить строки в таблицу
[insertATbl](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.insertatbl.html) | Вставить ASCII-таблицу после текущего HDU
[insertBTbl](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.insertbtbl.html) | Вставить двоичную таблицу за текущим HDU
[deleteCol](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.deletecol.html) | Удалить столбец из таблицы
[deleteRows](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.deleterows.html) | Удалить строки из таблицы
[getAColParms](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.getacolparms.html) | Информация о таблице в формате ASCII
[getBColParms](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.getbcolparms.html) | Информация о бинарной таблице
[getColName](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.getcolname.html) | имя столбца таблицы
[getColType](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.getcoltype.html) | Тип данных, значение повтора, ширина масштабируемого столбца
[getEqColType](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.geteqcoltype.html) | Тип данных столбца, повторяющееся значение, ширина
[getNumCols](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.getnumcols.html) | Количество столбцов в таблице
[getNumRows](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.getnumrows.html) | количество строк в таблице
[readATblHdr](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.readatblhdr.html) | Чтение заголовочной информации из текущей ASCII-таблицы
[readBTblHdr](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.readbtblhdr.html) | Чтение заголовочной информации из текущей двоичной таблицы
[readCol](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.readcol.html) | Считывает строки столбцов ASCII- или бинарной таблицы
[setTscale](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.settscale.html) | Сброс масштаба изображения
[writeCol](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.writecol.html) | Запись элементов в столбец ASCII или двоичной таблицы

### FITS-файлы -Утилиты

- | -
- | -
[getConstantValue](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.getconstantvalue.html) | Указать значение константы
[getVersion](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.getversion.html) | номер ревизии библиотеки CFITSIO
[getOpenFiles](https://www.mathworks.com/help/matlab/ref/matlab.io.fits.getopenfiles.html) | список открытых FITS-файлов

### Файл с чередованием полос

- | -
- | -
[multibandread](https://www.mathworks.com/help/matlab/ref/multibandread.html) | Чтение чередующегося файла с чередованием полос из двоичного файла
[multibandwrite](https://www.mathworks.com/help/matlab/ref/multibandwrite.html) | Запись данных с чередованием полос в файл

### Общий формат данных (CDF)

- | -
- | -
[cdfinfo](https://www.mathworks.com/help/matlab/ref/cdfinfo.html) | Информация о файлах Common Data Format (CDF)
[cdfread](https://www.mathworks.com/help/matlab/ref/cdfread.html) | Чтение данных из файлов Common Data Format (CDF)
[cdfepoch](https://www.mathworks.com/help/matlab/ref/cdfepoch.html) | Преобразование литерала даты или значения последовательности дат в дату в формате CDF
[todatenum](https://www.mathworks.com/help/matlab/ref/todatenum.html) | Преобразование объектов эпохи CDF в последовательные значения даты в `MATLAB`.

#### Bag

- | -
- | -
[cdflib](https://www.mathworks.com/help/matlab/ref/cdflib.html) | Прямое взаимодействие с библиотекой CDF

### Чтение видеоданных

- | -
- | -
[VideoReader](https://www.mathworks.com/help/matlab/ref/videoreader.html) | Создать объект для чтения видеофайла
[read](https://www.mathworks.com/help/matlab/ref/videoreader.read.html) | Считывание одного или нескольких видеокадров
[readFrame](https://www.mathworks.com/help/matlab/ref/videoreader.readframe.html) | Считать следующий видеокадр
[hasFrame](https://www.mathworks.com/help/matlab/ref/videoreader.hasframe.html) | Определить, есть ли кадры видео, доступные для чтения
[getFileFormats](https://www.mathworks.com/help/matlab/ref/videoreader.getfileformats.html) | Форматы файлов, поддерживаемые `VideoReader`
[mmfileinfo](https://www.mathworks.com/help/matlab/ref/mmfileinfo.html) | Информация о мультимедийных файлах

### Запись видеоданных

- | -
- | -
[VideoWriter](https://www.mathworks.com/help/matlab/ref/videowriter.html) | Создать объект для записи видеофайла
[open](https://www.mathworks.com/help/matlab/ref/videowriter.open.html) | Открыть файл для записи видеоданных
[writeVideo](https://www.mathworks.com/help/matlab/ref/videowriter.writevideo.html) | Записать видеоданные в файл
[close](https://www.mathworks.com/help/matlab/ref/videowriter.close.html) | Закрыть файл после записи видеоданных
[getProfiles](https://www.mathworks.com/help/matlab/ref/videowriter.getprofiles.html) | Описание файлов и форматов, поддерживаемых `VideoWriter`.

### Чтение или запись звука

- | -
- | -
[audioread](https://www.mathworks.com/help/matlab/ref/audioread.html) | Чтение аудиофайлов
[audiowrite](https://www.mathworks.com/help/matlab/ref/audiowrite.html) | Запись аудиофайлов
[lin2mu](https://www.mathworks.com/help/matlab/ref/lin2mu.html) | Преобразование линейного аудиосигнала в mu-law
[mu2lin](https://www.mathworks.com/help/matlab/ref/mu2lin.html) | Преобразование mu-law аудиосигнала в линейный формат
[audioinfo](https://www.mathworks.com/help/matlab/ref/audioinfo.html) | Информация об аудиофайлах

### Воспроизведение аудио

- | -
- | -
[audioplayer](https://www.mathworks.com/help/matlab/ref/audioplayer.html) | Объект для воспроизведения звука
[isplaying](https://www.mathworks.com/help/matlab/ref/audioplayer.isplaying.html) | Определить, идет ли воспроизведение.
[pause](https://www.mathworks.com/help/matlab/ref/audioplayer.pause.html) | Приостановить воспроизведение или запись
[play](https://www.mathworks.com/help/matlab/ref/audioplayer.play.html) | Воспроизведение звука из объекта `audioplayer`.
[playblocking](https://www.mathworks.com/help/matlab/ref/audioplayer.playblocking.html) | Воспроизведение звука в объекте `audioplayer`, сохранение контроля до завершения воспроизведения
[resume](https://www.mathworks.com/help/matlab/ref/audioplayer.resume.html) | Возобновить воспроизведение или запись из состояния паузы
[stop](https://www.mathworks.com/help/matlab/ref/audioplayer.stop.html) | Остановить воспроизведение или запись

### Запись звука

- | -
- | -
[audiorecorder](https://www.mathworks.com/help/matlab/ref/audiorecorder.html) | Объект для записи звука
[getaudiodata](https://www.mathworks.com/help/matlab/ref/audiorecorder.getaudiodata.html) | Хранить записанный аудиосигнал в числовом массиве
[getplayer](https://www.mathworks.com/help/matlab/ref/audiorecorder.getplayer.html) | Создать связанный объект `audioplayer`.
[isrecording](https://www.mathworks.com/help/matlab/ref/audiorecorder.isrecording.html) | Определить, идет ли запись
[record](https://www.mathworks.com/help/matlab/ref/audiorecorder.record.html) | Запись звука в объект `audiorecorder`.
[recordblocking](https://www.mathworks.com/help/matlab/ref/audiorecorder.recordblocking.html) | Запись звука в объект `audiorecorder`, сохранение контроля до завершения записи

### Воспроизведение звука

- | -
- | -
[audiodevinfo](https://www.mathworks.com/help/matlab/ref/audiodevinfo.html) | Информация об аудиоустройствах
[audiodevreset](https://www.mathworks.com/help/matlab/ref/audiodevreset.html) | Обновление списка доступных аудиоустройств
[sound](https://www.mathworks.com/help/matlab/ref/sound.html) | Преобразование матрицы данных сигнала в звук
[soundsc](https://www.mathworks.com/help/matlab/ref/soundsc.html) | Масштабировать данные и воспроизвести их как звук
[beep](https://www.mathworks.com/help/matlab/ref/beep.html) | Генерировать звуковой сигнал операционной системы

### Чтение и запись XML-документов

- | -
- | -
[matlab.io.xml.dom.DOMWriter](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.domwriter-class.html) | Запись сериализованных XML-документов Инжектор
[matlab.io.xml.dom.EntityResolver](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.entityresolver-class.html) | Абстрактный базовый класс распознавателя сущностей
[matlab.io.xml.dom.FileWriter](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.filewriter-class.html) | Писатель для создания текстовых файлов
[matlab.io.xml.dom.Locator](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.locator-class.html) | Местоположение элемента в XML-файле
[matlab.io.xml.dom.Parser](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.parser-class.html) | Парсер XML-разметки
[matlab.io.xml.dom.ParserConfiguration](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.parserconfiguration-class.html) | Параметры парсера XML
[matlab.io.xml.dom.ParseError](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.parseerror-class.html) | Ошибка разбора указанного XML-тега
[matlab.io.xml.dom.ParseErrorHandler](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.parseerrorhandler-class.html) | Абстрактный базовый класс для обработчиков ошибок разбора
[matlab.io.xml.dom.ParseErrorLocator](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.parseerrorlocator-class.html) | Определяет местоположение ошибки разбора
[matlab.io.xml.dom.ParseErrorSeverity](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.parseerrorseverity-class.html) | Указывает степень серьезности ошибок разбора XML-тегов enum class
[matlab.io.xml.dom.ResourceIdentifier](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.resourceidentifier-class.html) | Идентификатор XML-ресурса
[matlab.io.xml.dom.ResourceIdentifierType](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.resourceidentifiertype-class.html) | Тип идентификатора XML-ресурса
[matlab.io.xml.dom.WriterConfiguration](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.writerconfiguration-class.html) | Параметры писателя XML DOM
{.style-list-arrow}

### W3C DOM

- | -
- | -
[matlab.io.xml.dom.Attr](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.attr-class.html) | Атрибуты элементов XML
[matlab.io.xml.dom.CDATASection](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.cdatasection-class.html) | Секция CDATA
[matlab.io.xml.dom.Comment](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.comment-class.html) | Комментарии в XML-документах
[matlab.io.xml.dom.Document](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.document-class.html) | XML-документ
[matlab.io.xml.dom.DocumentFragment](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.documentfragment-class.html) | Группа узлов документа
[matlab.io.xml.dom.DocumentType](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.documenttype-class.html) | тип документа
[matlab.io.xml.dom.Element](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.element-class.html) | элемент XML-документа
[matlab.io.xml.dom.Entity](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.entity-class.html) | Сущность, определенная типом документа
[matlab.io.xml.dom.NamedNodeMap](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.namednodemap-class.html) | Набор узлов документа с именами
[matlab.io.xml.dom.NodeList](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.nodelist-class.html) | Список узлов документа
[matlab.io.xml.dom.Notation](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.notation-class.html) | Нотация в определении типа документа
[matlab.io.xml.dom.ProcessingInstruction](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.processinginstruction-class.html) | Инструкция по обработке XML
[matlab.io.xml.dom.Text](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.text-class.html) | Текст в XML-документе
[matlab.io.xml.dom.TypeInfo](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.dom.typeinfo-class.html) | Информация о типе схемы
{.style-list-arrow}

### Трансформация XML

- | -
- | -
[matlab.io.xml.transform.CompiledStylesheet](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.transform.compiledstylesheet-class.html) | Скомпилированная таблица стилей
[matlab.io.xml.transform.ResultDocument](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.transform.resultdocument-class.html) | Сохранить результат преобразования в виде документа
[matlab.io.xml.transform.ResultString](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.transform.resultstring-class.html) | Сохранить результат преобразования в виде строки
[matlab.io.xml.transform.ResultFile](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.transform.resultfile-class.html) | Сохранить результат преобразования в виде файла
[matlab.io.xml.transform.SourceDocument](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.transform.sourcedocument-class.html) | Исходный документ XML для преобразования
[matlab.io.xml.transform.SourceFile](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.transform.sourcefile-class.html) | Исходный файл XML для преобразования
[matlab.io.xml.transform.SourceString](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.transform.sourcestring-class.html) | Исходная строка XML для строки преобразования
[matlab.io.xml.transform.StylesheetSourceDocument](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.transform.stylesheetsourcedocument-class.html) | Источник таблицы стилей для документа преобразования
[matlab.io.xml.transform.StylesheetSourceFile](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.transform.stylesheetsourcefile-class.html) | Источник таблицы стилей для документа преобразования
[matlab.io.xml.transform.StylesheetSourceString](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.transform.stylesheetsourcestring-class.html) | Строка-источник XSL для строки преобразования
[matlab.io.xml.transform.Tracer](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.transform.tracer-class.html) | Трассировка выполнения таблицы стилей
{.style-list-arrow}

### XPath запрос

- | -
- | -
[matlab.io.xml.xpath.CompiledExpression](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.xpath.compiledexpression-class.html) | Скомпилированное выражение XPath
[matlab.io.xml.xpath.EvalResultType](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.xpath.evalresulttype-class.html) | Тип результата вычисления выражения XPath
[matlab.io.xml.xpath.Evaluator](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.xpath.evaluator-class.html) | Оценщик выражений XPath
[matlab.io.xml.xpath.PrefixResolver](https://www.mathworks.com/help/matlab/ref/matlab.io.xml.xpath.prefixresolver-class.html) | Абстрактный базовый класс для разрешения префиксов пространств имен
{.style-list-arrow}

### Формат JSON

- | -
- | -
[jsondecode](https://www.mathworks.com/help/matlab/ref/jsondecode.html) | Декодирование текста в формат JSON
[jsonencode](https://www.mathworks.com/help/matlab/ref/jsonencode.html) | Создание JSON-формата текста {.style-list} из структурированных данных `MATLAB`.

### Переменные рабочей области и MAT-файл {.row-span-2}

- | -
- | -
[load](https://www.mathworks.com/help/matlab/ref/load.html) | Загрузить переменные файла в рабочую область
[save](https://www.mathworks.com/help/matlab/ref/save.html) | Сохранить переменные рабочей области в файл
[matfile](https://www.mathworks.com/help/matlab/ref/matlab.io.matfile.html) | Доступ и изменение переменных в MAT-файле без загрузки файла в память
[disp](https://www.mathworks.com/help/matlab/ref/disp.html) | Вывести на экран значение переменной
[formattedDisplayText](https://www.mathworks.com/help/matlab/ref/formatteddisplaytext.html) | Захват вывода на экран в виде строки
[who](https://www.mathworks.com/help/matlab/ref/who.html) | Список переменных в рабочей области
[whos](https://www.mathworks.com/help/matlab/ref/whos.html) | Список переменных в рабочей области с указанием их размера и типа
[clear](https://www.mathworks.com/help/matlab/ref/clear.html) | Удаление элементов из рабочей области и освобождение системной памяти
[clearvars](https://www.mathworks.com/help/matlab/ref/clearvars.html) | Очистить переменные в памяти
[openvar](https://www.mathworks.com/help/matlab/ref/openvar.html) | Открыть переменную рабочей области в редакторе переменных или других средствах графического редактирования
[Workspace Browser](https://www.mathworks.com/help/matlab/ref/workspace.html) | Открытие браузера рабочей области для управления рабочей областью

### Низкоуровневый файловый ввод-вывод {.row-span-2}

- | -
- | -
[fclose](https://www.mathworks.com/help/matlab/ref/fclose.html) | Закрыть один или все открытые файлы
[feof](https://www.mathworks.com/help/matlab/ref/feof.html) | Определить конец файла
[ferror](https://www.mathworks.com/help/matlab/ref/ferror.html) | Сообщение об ошибке ввода/вывода файла
[fgetl](https://www.mathworks.com/help/matlab/ref/fgetl.html) | Чтение строк из файла и удаление переносов строк
[fgets](https://www.mathworks.com/help/matlab/ref/fgets.html) | Чтение строк из файла с сохранением новых строк
[fileread](https://www.mathworks.com/help/matlab/ref/fileread.html) | Чтение содержимого файла в текстовом формате
[fopen](https://www.mathworks.com/help/matlab/ref/fopen.html) | Открыть файл или получить информацию об открытии файла
[fprintf](https://www.mathworks.com/help/matlab/ref/fprintf.html) | Запись данных в текстовый файл
[fread](https://www.mathworks.com/help/matlab/ref/fread.html) | Чтение данных в двоичных файлах
[frewind](https://www.mathworks.com/help/matlab/ref/frewind.html) | Переместить индикатор позиции файла в начало открытого файла
[fscanf](https://www.mathworks.com/help/matlab/ref/fscanf.html) | Чтение данных в текстовом файле
[fseek](https://www.mathworks.com/help/matlab/ref/fseek.html) | Перемещение на указанную позицию в файле
[ftell](https://www.mathworks.com/help/matlab/ref/ftell.html) | Текущее местоположение
[fwrite](https://www.mathworks.com/help/matlab/ref/fwrite.html) | Запись данных в двоичный файл

### Последовательная и USB-связь - подключение и настройка

- | -
- | -
[serialportlist](https://www.mathworks.com/help/matlab/ref/serialportlist.html) | Список последовательных портов, подключенных к системе
[serialport](https://www.mathworks.com/help/matlab/ref/serialport.html) | Подключение к последовательному порту
[configureTerminator](https://www.mathworks.com/help/matlab/ref/serialport.configureterminator.html) | Установка терминатора для обмена ASCII-строками с последовательным портом
[configureCallback](https://www.mathworks.com/help/matlab/ref/serialport.configurecallback.html) | Установка функции обратного вызова и условий срабатывания для связи с устройствами последовательного порта

### Последовательная и USB-связь - чтение и запись

- | -
- | -
[read](https://www.mathworks.com/help/matlab/ref/serialport.read.html) | Чтение данных из последовательного порта
[readline](https://www.mathworks.com/help/matlab/ref/serialport.readline.html) | Чтение строки данных ASCII-строки из последовательного порта
[write](https://www.mathworks.com/help/matlab/ref/serialport.write.html) | Запись данных в последовательный порт
[writeline](https://www.mathworks.com/help/matlab/ref/serialport.writeline.html) | Запись строки данных ASCII в последовательный порт

### Последовательная и USB-связь - управляющие контакты и память

- | -
- | -
[flush](https://www.mathworks.com/help/matlab/ref/serialport.flush.html) | Очистить буфер устройства последовательного порта
[getpinstatus](https://www.mathworks.com/help/matlab/ref/serialport.getpinstatus.html) | Получить статус последовательного порта
[setRTS](https://www.mathworks.com/help/matlab/ref/serialport.setrts.html) | Установить контакт RTS последовательного порта
[setDTR](https://www.mathworks.com/help/matlab/ref/serialport.setdtr.html) | Установить вывод DTR последовательного порта

### TCP/IP связь - подключение и настройка

- | -
- | -
[tcpclient](https://www.mathworks.com/help/matlab/ref/tcpclient.html) | Создание соединения клиента TCP/IP с сервером TCP/IP
[echotcpip](https://www.mathworks.com/help/matlab/ref/echotcpip.html) | Запуск или остановка эхо-сервера TCP/IP
[configureTerminator](https://www.mathworks.com/help/matlab/ref/tcpclient.configureterminator.html) | Установка терминатора для обмена ASCII-строками с удаленным хостом по TCP/IP
[configureCallback](https://www.mathworks.com/help/matlab/ref/tcpclient.configurecallback.html) | Установка функции обратного вызова и условия срабатывания для связи с удаленным хостом по TCP/IP {.style-list}

### Связь по TCP/IP - чтение и запись

- | -
- | -
[read](https://www.mathworks.com/help/matlab/ref/tcpclient.read.html) | Чтение данных на удаленном хосте через TCP/IP
[readline](https://www.mathworks.com/help/matlab/ref/tcpclient.readline.html) | Чтение строки данных ASCII-строки с удаленного хоста через TCP/IP
[write](https://www.mathworks.com/help/matlab/ref/tcpclient.write.html) | Запись данных на удаленный хост через TCP/IP
[writeline](https://www.mathworks.com/help/matlab/ref/tcpclient.writeline.html) | Запись ASCII-строки данных на удаленный хост по TCP/IP
[flush](https://www.mathworks.com/help/matlab/ref/tcpclient.flush.html) | Промывка буферов для связи с удаленными хостами по TCP/IP {.style-list}

### Связь по Bluetooth - подключение и настройка

- | -
- | -
[bluetoothlist](https://www.mathworks.com/help/matlab/ref/bluetoothlist.html) | Сканирование на наличие близлежащих классических устройств `Bluetooth`
[bluetooth](https://www.mathworks.com/help/matlab/ref/bluetooth.html) | Подключение к `Bluetooth` классическому устройству
[configureTerminator](https://www.mathworks.com/help/matlab/ref/bluetooth.configureterminator.html) | Установка терминатора для обмена ASCII-строками с устройством `Bluetooth`
[configureCallback](https://www.mathworks.com/help/matlab/ref/bluetooth.configurecallback.html) | Установить функцию обратного вызова и условие срабатывания для связи с устройством `Bluetooth` {.style-list}

### Связь по Bluetooth - чтение и запись {.row-span-2}

- | -
- | -
[read](https://www.mathworks.com/help/matlab/ref/bluetooth.read.html) | Чтение данных с устройства `Bluetooth`.
[readline](https://www.mathworks.com/help/matlab/ref/bluetooth.readline.html) | Считать строку данных ASCII-строки с устройства `Bluetooth`.
[write](https://www.mathworks.com/help/matlab/ref/bluetooth.write.html) | Запись данных на `Bluetooth` устройство
[writeline](https://www.mathworks.com/help/matlab/ref/bluetooth.writeline.html) | Записать строку данных в формате ASCII на устройство `Bluetooth`.
[flush](https://www.mathworks.com/help/matlab/ref/bluetooth.flush.html) | Очистить буфер устройства `Bluetooth` {.style-list}

### Связь Bluetooth Low Energy {.row-span-2}

- | -
- | -
[blelist](https://www.mathworks.com/help/matlab/ref/blelist.html) | Сканирование на наличие близлежащих периферийных устройств с низким энергопотреблением `Bluetooth
[ble](https://www.mathworks.com/help/matlab/ref/ble.html) | Подключение к периферийным устройствам с низким энергопотреблением `Bluetooth`
[characteristic](https://www.mathworks.com/help/matlab/ref/matlabshared.blelib.characteristic.html) | Доступ к характеристикам периферийных устройств `Bluetooth` с низким энергопотреблением
[дескриптор](https://www.mathworks.com/help/matlab/ref/matlabshared.blelib.descriptor.html) | Доступ к дескрипторам периферийных устройств с низким энергопотреблением `Bluetooth`
[read](https://www.mathworks.com/help/matlab/ref/matlabshared.blelib.characteristic.read.html) | Чтение характеристик или дескрипторов периферийного устройства с низким уровнем энергии `Bluetooth`
[write](https://www.mathworks.com/help/matlab/ref/matlabshared.blelib.characteristic.write.html) | Запись данных в характеристику или дескриптор периферийного устройства `Bluetooth` с низким энергопотреблением
[subscribe](https://www.mathworks.com/help/matlab/ref/matlabshared.blelib.characteristic.subscribe.html) | Подписаться на уведомления о характеристиках или инструкциях
[unsubscribe](https://www.mathworks.com/help/matlab/ref/matlabshared.blelib.characteristic.unsubscribe.html) | Отменить подписку на уведомления и инструкции по характеристикам {.style-list}
### Веб-сервисы

- | -
- | -
[webread](https://www.mathworks.com/help/matlab/ref/webread.html) | Чтение содержимого из RESTful веб-сервисов
[webwrite](https://www.mathworks.com/help/matlab/ref/webwrite.html) | Запись данных в REST-сервис
[websave](https://www.mathworks.com/help/matlab/ref/websave.html) | Сохранить содержимое REST-сервиса в файл
[weboptions](https://www.mathworks.com/help/matlab/ref/weboptions.html) | Задание параметров для REST-сервисов
[web](https://www.mathworks.com/help/matlab/ref/web.html) | Открыть веб-страницу или файл в браузере
[sendmail](https://www.mathworks.com/help/matlab/ref/sendmail.html) | Отправить письмо по списку адресов

### Файловые операции FTP {.row-span-2}

- | -
- | -
[ftp](https://www.mathworks.com/help/matlab/ref/ftp.html) | Подключение к FTP-серверу для доступа к его файлам
[sftp](https://www.mathworks.com/help/matlab/ref/sftp.html) | Подключение к SFTP-серверу для доступа к его файлам
[ascii](https://www.mathworks.com/help/matlab/ref/ftp.ascii.html) | Установить режим передачи данных по FTP на ASCII
[binary](https://www.mathworks.com/help/matlab/ref/ftp.binary.html) | Установить режим передачи данных по FTP в двоичном виде
[cd](https://www.mathworks.com/help/matlab/ref/ftp.cd.html) | Изменение или просмотр текущей папки на SFTP- или FTP-сервере
[close](https://www.mathworks.com/help/matlab/ref/ftp.close.html) | Закрыть соединение с SFTP- или FTP-сервером
[delete](https://www.mathworks.com/help/matlab/ref/ftp.delete.html) | Удаление файлов на SFTP- или FTP-сервере
[dir](https://www.mathworks.com/help/matlab/ref/ftp.dir.html) | Список содержимого папок на SFTP или FTP-сервере
[mget](https://www.mathworks.com/help/matlab/ref/ftp.mget.html) | Загрузить файлы с SFTP или FTP-сервера
[mkdir](https://www.mathworks.com/help/matlab/ref/ftp.mkdir.html) | Создать новую папку на SFTP или FTP-сервере
[mput](https://www.mathworks.com/help/matlab/ref/ftp.mput.html) | Загрузить файлы или папки на SFTP или FTP-сервер
[rename](https://www.mathworks.com/help/matlab/ref/ftp.rename.html) | Переименовать файл на SFTP или FTP-сервере
[rmdir](https://www.mathworks.com/help/matlab/ref/ftp.rmdir.html) | Удалить папку на SFTP или FTP-сервере

### Данные Интернета вещей (IoT)

- | -
- | -
[thingSpeakRead](https://www.mathworks.com/help/matlab/ref/thingspeakread.html) | Чтение данных, хранящихся в канале `ThingSpeak`.
[thingSpeakWrite](https://www.mathworks.com/help/matlab/ref/thingspeakwrite.html) | запись данных в канал `ThingSpeak`.
