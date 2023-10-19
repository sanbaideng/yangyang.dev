---
Название: Python
дата: 2020-12-23 18:41:20
фон: bg-[#436b97]
теги:
    - скрипт
    - интерпретировать
категории:
    - Программирование
intro: |
    Шпаргалка [Python](https://www.python.org/) - это одностраничный справочник по языку программирования Python 3.
плагины:
    - copyCode
---



Начало работы
---------------


### Введение
- [Python](https://www.python.org/) _(python.org)_
- [Python Document](https://docs.python.org/3/index.html) _(docs.python.org)_
- [Learn X in Y minutes](https://learnxinyminutes.com/docs/python/) _(learnxinyminutes.com)_
- [Regex в python](/regex#regex-in-python) _(cheatsheets.zip)_



### Hello World

``python
>>> print("Hello, World!")
Hello, World!
```

Знаменитая программа "Hello World" на языке Python


### Переменные
``python
age = 18 # возраст имеет тип int
name = "John" # имя теперь имеет тип str
print(name)
```

Python не может объявить переменную без присваивания.



### Типы данных {.row-span-2}
| | |
|------------------------------------|----------|
| `str` | Text |
| `int`, `float`, `complex` | Numeric |
| `list`, `tuple`, `range` | Sequence |
| `dict` | Mapping |
| `set`, `frozenset` | Набор |
| `bool` | Boolean |
| `bytes`, `bytearray`, `memoryview` | Двоичный файл | `Binary`.
См: [Типы данных](#python-data-types)


### Нарезка строк

``python
>>> msg = "Hello, World!"
>>> print(msg[2:5])
llo
```

См: [Strings](#python-strings)

### Списки
``python
mylist = []
mylist.append(1)
mylist.append(2)
for item in mylist:
    print(item) # выводит 1,2
```

См: [Lists](#python-lists)


### If Else
``python
num = 200
if num > 0:
    print("num больше 0")
else:
    print("num не больше 0")
```
См: [Управление потоком](#python-flow-control)

### Циклы
``python
for item in range(6):
    if item == 3: break
    print(item)
else:
    print("Наконец-то закончили!")
```
См: [Loops](#python-loops)


### Функции
``python
>>> def my_function():
... print("Привет от функции")
...
>>> my_function()
Привет от функции
```

См: [Функции](#python-functions)


### Обработка файлов {.col-span-2}
``python
with open("myfile.txt", "r", encoding='utf8') as file:
    for line in file:
        print(line)
```

См: [Обработка файлов](#python-file-handling)



### Арифметика
``python
результат = 10 + 30 # => 40
результат = 40 - 10 # => 30
результат = 50 * 5 # => 250
результат = 16 / 4 # => 4.0 (Деление с плавающей запятой)
result = 16 // 4 # => 4 (целочисленное деление)
результат = 25 % 2 # => 1
результат = 5 ** 3 # => 125
```
Символ `/` означает коэффициент x и y, а символ `//` - floated quotient of x and y, см. также [StackOverflow](https://stackoverflow.com/a/183870/13192320)

### Plus-Equals
``python
счётчик = 0
counter += 10 # => 10
счётчик = 0
счетчик = счетчик + 10 # => 10

message = "Часть 1".

# => Часть 1.Часть 2.
message += "Часть 2."   
```

### f-Strings (Python 3.6+)
``python
>>> website = 'Quickref.ME'
>>> f "Hello, {website}"
"Hello, Quickref.ME"

>>> num = 10
>>> f'{num} + 10 = {num + 10}'
'10 + 10 = 20'
```
См: [Python F-Strings](#python-f-strings-since-python-3-6)



Встроенные типы данных Python
---------------



### Строки

``python
hello = "Hello World"
hello = "Hello World

multi_string = ``Многострочные строки
Lorem ipsum dolor sit amet,
consectetur adipiscing elit """
```
См: [Strings](#python-strings)



### Числа
``python
x = 1 # int
y = 2.8 # float
z = 1j # complex

>>> print(type(x))
<class 'int'>
```



### Булевы
``python
my_bool = True
my_bool = False

bool(0) # => False
bool(1) # => True
```



### Списки
``python
list1 = ["яблоко", "банан", "вишня"]
list2 = [True, False, False]
list3 = [1, 5, 7, 9, 3]
list4 = list((1, 5, 7, 9, 3))
```
См: [Lists](#python-lists)


### Кортеж
``python
my_tuple = (1, 2, 3)
my_tuple = tuple((1, 2, 3))
```
Аналогично List, но неизменяемый


### Набор
``python
set1 = {"a", "b", "c"}   
set2 = set((("a", "b", "c"))
```
Набор уникальных элементов/объектов



### Словарь
``python {.wrap}
>>> empty_dict = {}
>>> a = {"один": 1, "2": 2, "3": 3}
>>> a["one"]
1
>>> a.keys()
dict_keys(['one', 'two', 'three'])
>>> a.values()
dict_values([1, 2, 3])
>>> a.update({"четыре": 4})
>>> a.keys()
dict_keys(['one', 'two', 'three', 'four'])
>>> a['four']
4
```
Ключ: Пара значений, JSON как объект


### Кастинг

#### Целые числа
``python
x = int(1) # x будет равно 1
y = int(2.8) # y будет равно 2
z = int("3") # z будет равно 3
```

#### Floats
``python
x = float(1) # x будет равно 1,0
y = float(2.8) # y будет равно 2.8
z = float("3") # z будет равно 3,0
w = float("4.2") # w будет равно 4.2
```

#### Строки
``python
x = str("s1") # x будет 's1'
y = str(2) # y будет '2'
z = str(3.0) # z будет '3.0'
```

Расширенные типы данных Python
-----------------------
### Кучи {.col-span-2 .row-span-3}
``python
import heapq

myList = [9, 5, 4, 1, 3, 2]
heapq.heapify(myList) # превращаем myList в Min Heap
print(myList) # => [1, 3, 2, 5, 9, 4]
print(myList[0]) # первое значение всегда наименьшее в куче

heapq.heappush(myList, 10) # вставляем 10
x = heapq.heappop(myList) # извлечение и возврат наименьшего элемента
print(x) # => 1
```
#### Отрицание всех значений для использования Min Heap в качестве Max Heap
``python
myList = [9, 5, 4, 1, 3, 2]
myList = [-val for val in myList] # умножение на -1 для отрицания
heapq.heapify(myList)

x = heapq.heappop(myList)
print(-x) # => 9 (не забыв еще раз умножить на -1)
```
Кучи - это двоичные деревья, для которых каждый родительский узел имеет значение меньше или равное любому из своих дочерних узлов. Полезны для быстрого доступа к минимальному/максимальному значению. Временная сложность: O(n) для heapify, O(log n) push и pop. См: [Heapq](https://docs.python.org/3/library/heapq.html)

### Стеки и очереди {.row-span-3}
``python
from collections import deque

q = deque() # пустой
q = deque([1, 2, 3]) # со значениями

q.append(4) # добавление в правую часть
q.appendleft(0) # добавление в левую часть
print(q) # => deque([0, 1, 2, 3, 4])

x = q.pop() # удаление и возврат из правой части
y = q.popleft() # удаление и возврат из левой части
print(x) # => 4
print(y) # => 0
print(q) # => deque([1, 2, 3])

q.rotate(1) # поворот на 1 шаг вправо
print(q) # => deque([3, 1, 2])
```
Deque - это двусторонняя очередь с временем O(1) для операций добавления/открытия с обеих сторон. Используется как стеки и очереди. См: [Deque](https://docs.python.org/3/library/collections.html#collections.deque)



Строки Python
------------

### Массивоподобные

``python
>>> hello = "Hello, World"
>>> print(hello[1])
e
>>> print(hello[-1])
d
```
Получение символа, находящегося в позиции 1 или последней

### Петля

``python
>>> for char in "foo":
... print(char)
f
o
o
```
Перебор букв в слове "foo"



### Нарезка строки {.row-span-4}
``java
 ┌───┬───┬───┬───┬───┬───┬───┐
 | m | y | b | a | c | o | n |
 └───┴───┴───┴───┴───┴───┴───┘
 0 1 2 3 4 5 6 7
-7 -6 -5 -4 -3 -2 -1
```

---

``python
>>> s = 'mybacon'
>>> s[2:5]
'bac'
>>> s[0:2]
'my'
```


``python
>>> s = 'mybacon'
>>> s[:2]
'my'
>>> s[2:]
'bacon'
>>> s[:2] + s[2:]
'mybacon'
>>> s[:]
'mybacon'
```


``python
>>> s = 'mybacon'
>>> s[-5:-1]
'baco'
>>> s[2:6]
'baco'
```


#### С помощью страйда
``python
>>> s = '12345' * 5
>>> s
'1234512345123451234512345'
>>> s[::5]
'11111'
>>> s[4::5]
'55555'
>>> s[::-5]
'55555'
>>> s[::-1]
'5432154321543215432154321'
```





### Длина строки


``python
>>> hello = "Hello, World!"
>>> print(len(hello))
13
```
Функция len() возвращает длину строки


### Множественные копии
``python
>>> s = '===+'
>>> n = 8
>>> s * n
'===+===+===+===+===+===+===+===+'
```

### Проверка строки

``python
>>> s = 'spam'
>>> s in 'Я видел спамалот!'
True
>>> s not in 'I saw The Holy Grail!'
True

```

### Конкатенаты
``python
>>> s = 'spam'
>>> t = 'egg'
>>> s + t
'spamegg'
>>> 'spam' 'egg'
'spamegg'
```


### Форматирование {.col-span-2}
``python
name = "John"
print("Hello, %s!" % name)
```

``python
имя = "Джон"
возраст = 23
print("%s is %d years old." % (имя, возраст))
```

Метод #### format()
``python
txt1 = "Меня зовут {fname}, мне {age}".format(fname="John", age=36)
txt2 = "Меня зовут {0}, мне {1}".format("Джон", 36)
txt3 = "Меня зовут {}, я {}".format("John", 36)
```

### Ввод
```python
>>> name = input("Введите ваше имя: ")
Введите ваше имя: Том
>>> имя
'Tom'
```
Получение входных данных из консоли


### Присоединяйтесь
``python
>>> "#".join(["John", "Peter", "Vicky"])
'John#Peter#Vicky'
```

### Endswith
``python
>>> "Hello, world!".endswith("!")
True
```

F-строки Python (начиная с Python 3.6+)
----------------


### Использование f-строк
``python
>>> website = 'Quickref.ME'
>>> f "Hello, {website}"
"Hello, Quickref.ME"

>>> num = 10
>>> f'{num} + 10 = {num + 10}'
'10 + 10 = 20'

>>> f"""Он сказал {"Я Джон"}""""
"Он сказал, что я Джон"

>>> f'5 {"{звезд}"}'
'5 {звезд}'
>>> f'{{5}} {"stars"}'
'{5} звезд'

>>> имя = 'Eric'
>>> возраст = 27
>>> f"""Hello!
...     Я - {имя}.
...     Мне {возраст}."""
"Здравствуйте!\n Я Эрик.\n Мне 27 лет."
```
доступна начиная с Python 3.6, также см: [Форматированные строковые литералы](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)



### f-Strings Fill Align
``python
>>> f'{"text":10}' # [width]
'text '
>>> f'{"test":*>10}' # заполнение слева
'******test'
>>> f'{"test":*<10}' # заполнение справа
'test******'
>>> f'{"test":*^10}' # fill center
'***test***'
>>> f'{12345:0>10}' # заполнение цифрами
'0000012345'
```


### f-Strings Type
``python
>>> f'{10:b}' # двоичный тип
'1010'
>>> f'{10:o}' # восьмеричный тип
'12'
>>> f'{200:x}' # шестнадцатеричный тип
'c8'
>>> f'{200:X}'
'C8'
>>> f'{345600000000:e}' # научная нотация
'3.456000e+11'
>>> f'{65:c}' # тип символа
'A'
>>> f'{10:#b}' # [тип] с обозначением (основание)
'0b1010'
>>> f'{10:#o}'
'0o12'
>>> f'{10:#x}'
'0xa'
```


### F-строки Другие
``python
>>> f'{-12345:0=10}' # отрицательные числа
'-000012345'
>>> f'{12345:010}' # [0] сокращение (без выравнивания)
'0000012345'
>>> f'{-12345:010}'
'-000012345'
>>> import math # [.precision]
>>> math.pi
3.141592653589793
>>> f'{math.pi:.2f}'
'3.14'
>>> f'{1000000:,.2f}' # [grouping_option]
'1,000,000.00'
>>> f'{1000000:_.2f}'
'1_000_000.00'
>>> f'{0.25:0%}' # процент
'25.000000%'
>>> f'{0.25:.0%}'
'25%'
```


### F-Strings Sign
``python
>>> f'{12345:+}' # [знак] (+/-)
'+12345'
>>> f'{-12345:+}'
'-12345'
>>> f'{-12345:+10}'
' -12345'
>>> f'{-12345:+010}'
'-000012345'
```

Списки Python
------------



### Определение
``python
>>> li1 = []
>>> li1
[]
>>> li2 = [4, 5, 6]
>>> li2
[4, 5, 6]
>>> li3 = list((1, 2, 3))
>>> li3
[1, 2, 3]
>>> li4 = list(range(1, 11))
>>> li4
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```



### Генерируем {.col-span-2}
``python
>>> list(filter(lambda x : x % 2 == 1, range(1, 20)))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

>>> [x ** 2 for x in range (1, 11) if x % 2 == 1]
[1, 9, 25, 49, 81]

>>> [x for x in [3, 4, 5, 6, 7] if x > 5]
[6, 7]

>>> list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))
[6, 7]
```


### Append
``python
>>> li = []
>>> li.append(1)
>>> li
[1]
>>> li.append(2)
>>> li
[1, 2]
>>> li.append(4)
>>> li
[1, 2, 4]
>>> li.append(3)
>>> li
[1, 2, 4, 3]
```


### Нарезка списка {.col-span-2 .row-span-3}
Синтаксис нарезки списка:
``python
a_list[start:end]
a_list[start:end:step]
```
#### Slicing
``python
>>> a = ['спам', 'яйцо', 'бекон', 'помидор', 'ветчина', 'лобстер']
>>> a[2:5]
['бекон', 'помидор', 'ветчина']
>>> a[-5:-2]
['яйцо', 'бекон', 'помидор']
>>> a[1:4]
['яйцо', 'бекон', 'помидор']
```
#### Опускание индекса
``python
>>> a[:4]
['спам', 'яйцо', 'бекон', 'помидор']
>>> a[0:4]
['spam', 'egg', 'bacon', 'tomato']
>>> a[2:]
['бекон', 'помидор', 'ветчина', 'лобстер']
>>> a[2:len(a)]
['бекон', 'помидор', 'ветчина', 'лобстер']
>>> a
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a[:]
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
```
#### С помощью страйда
``python
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a[0:6:2]
['спам', 'бекон', 'ветчина']
>>> a[1:6:2]
['яйцо', 'помидор', 'лобстер']
>>> a[6:0:-2]
['лобстер', 'помидор', 'яйцо']
>>> a
['спам', 'яйцо', 'бекон', 'помидор', 'ветчина', 'лобстер']
>>> a[::-1]
['лобстер', 'ветчина', 'помидор', 'бекон', 'яйцо', 'спам']
```




### Удалить
``python
>>> li = ['хлеб', 'масло', 'молоко']
>>> li.pop()
'milk'
>>> li
['хлеб', 'масло']
>>> del li[0]
>>> li
['масло']
```





### Доступ
``python
>>> li = ['a', 'b', 'c', 'd']
>>> li[0]
'a'
>>> li[-1]
'd'
>>> li[4]
Traceback (последний последний вызов):
  Файл "<stdin>", строка 1, в <module>.
IndexError: индекс списка выходит за пределы диапазона
```


### Конкатенация {.row-span-2}
``python
>>> odd = [1, 3, 5]
>>> odd.extend([9, 11, 13])
>>> odd
[1, 3, 5, 9, 11, 13]
>>> odd = [1, 3, 5]
>>> odd + [9, 11, 13]
[1, 3, 5, 9, 11, 13]
```


### Сортировка и реверс {.row-span-2}
``python
>>> li = [3, 1, 3, 2, 5]
>>> li.sort()
>>> li
[1, 2, 3, 3, 5]
>>> li.reverse()
>>> li
[5, 3, 3, 2, 1]
```


### Счет
``python
>>> li = [3, 1, 3, 2, 5]
>>> li.count(3)
2
```


### Повторение
``python
>>> li = ["re"] * 3
>>> li
['re', 're', 're']
```

Управление потоком в Python
------------

### Базовый
``python
num = 5
if num > 10:
    print("num полностью больше 10.")
elif num < 10:
    print("num меньше 10.")
else:
    print("num действительно равно 10.")
```

### Одна строка
```python
>>> a = 330
>>> b = 200
>>> r = "a" if a > b else "b"
>>> print(r)
a
```

### else if

``python
value = True
if not value:
    print("Value is False")
elif value is None:
    print("Value is None")
else:
    print("Значение равно True")
```

### match case

``python
x = 1
совпадение x:
  case 0:
    print("zero")
  case 1:
    print("один")
  case _:
    print("несколько")
```




Циклы Python
--------

### Basic

``python
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
```
Печатает: 2 3 5 7




### С индексом

``python
animals = ["dog", "cat", "mouse"]
# enumerate() добавляет счетчик в итерабельную таблицу
for i, value in enumerate(animals):
    print(i, value)
```
Печатает: 0 собака 1 кошка 2 мышь



### While
``python
x = 0
while x < 4:
    print(x)
    x += 1 # Сокращение для x = x + 1
```
Печатает: 0 1 2 3




### Break
``python
x = 0
for index in range(10):
    x = index * 10
    if index == 5:
    	break
    print(x)
```
Печатает: 0 10 20 30 40



### Продолжить

``python
for index in range(3, 8):
    x = index * 10
    if index == 5:
    	продолжить
    print(x)
```
Печатает: 30 40 60 70



### Диапазон
``python
for i in range(4):
    print(i) # Печатает: 0 1 2 3

for i in range(4, 8):
    print(i) # Prints: 4 5 6 7

for i in range(4, 10, 2):
    print(i) # Печатает: 4 6 8
```



### С zip()
``python
words = ['Mon', 'Tue', 'Wed']
nums = [1, 2, 3]
# Используем zip для упаковки в кортежный список
for w, n in zip(words, nums):
    print('%d:%s, ' %(n, w))
```
Печатает: 1:Mon, 2:Tue, 3:Wed,



### for/else
``python
nums = [60, 70, 30, 110, 90]
for n in nums:
    if n > 100:
        print("%d больше 100" %n)
        break
else:
    print("Не найдено!")
```
Также см: [Советы по Python](https://book.pythontips.com/en/latest/for_-_else.html)




Функции Python
--------

### Basic

``python
def hello_world():  
    print('Hello, World!')
```



### Возврат

``python
def add(x, y):
    print("x - %s, y - %s" %(x, y))
    return x + y

add(5, 6) # => 11
```

### Позиционные аргументы
``python
def varargs(*args):
    return args

varargs(1, 2, 3) # => (1, 2, 3)
```

Тип "args" - кортеж.


### Аргументы ключевых слов
``python
def keyword_args(**kwargs):
    return kwargs

# => { "big": "foot", "loch": "ness"}
keyword_args(big="foot", loch="ness")
```

Тип "kwargs" - dict.


### Возвращение множества
``python
def swap(x, y):
    return y, x

x = 1
y = 2
x, y = swap(x, y) # => x = 2, y = 1
```


### Значение по умолчанию
``python
def add(x, y=10):
    return x + y

add(5) # => 15
add(5, 20) # => 25
```

### Анонимные функции
``python
# => True
(lambda x: x > 2)(3)

# => 5
(lambda x, y: x ** 2 + y ** 2)(2, 1)
```



Модули Python
--------


### Импорт модулей
``python
импорт математики
print(math.sqrt(16))  # => 4.0
```


### Из модуля

``python
from math import ceil, floor
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0
```


### Импорт всех

``python
from math import *
```


### Сокращение модуля

``python
import math as m

# => True
math.sqrt(16) == m.sqrt(16)
```


### Функции и атрибуты

``python
импорт математики
dir(math)
```



Обработка файлов в Python
----------


### Чтение файла
#### Построчно
``python
with open("myfile.txt") as file:
    for line in file:
        print(line)
```
#### С номером строки
``python
file = open('myfile.txt', 'r')
for i, line in enumerate(file, start=1):
    print("Number %s: %s" % (i, line))
```


### String

#### Запись строки
``python
contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w+") as file:
    file.write(str(contents))
```

#### Чтение строки
``python
with open('myfile1.txt', "r+") as file:
    contents = file.read()
print(contents)
```

### Объект

#### Запись объекта
``python
contents = {"aa": 12, "bb": 21}
with open("myfile2.txt", "w+") as file:
    file.write(json.dumps(contents))
```

#### Чтение объекта
``python
with open('myfile2.txt', "r+") as file:
    contents = json.load(file)
print(contents)
```


### Удаление файла

``python
импорт os
os.remove("myfile.txt")
```



### Проверка и удаление

``python
импорт os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("Файл не существует")
```


### Удаление папки

``python
импорт os
os.rmdir("myfolder")
```





Классы и наследование в Python
--------


### Определение

``python
класс MyNewClass:
    pass

# Инстанцирование класса
my = MyNewClass()
```



### Конструкторы

``python
класс Animal:
    def __init__(self, voice):
        self.voice = voice
 
cat = Animal('Meow')
print(cat.voice) # => Мяу
 
собака = Animal('Woof')
print(dog.voice) # => Гав
```



### Метод
``python
class Dog:

    # Метод класса
    def bark(self):
        print("Ham-Ham")
 
charlie = Dog()
charlie.bark() # => "Ham-Ham"
```



### Переменные класса {.row-span-2}

``python
class MyClass:
    class_variable = "Переменная класса!"

# => Переменная класса!
print(MyClass.class_variable)

x = MyClass()
 
# => Переменная класса!
print(x.class_variable)
```



### Super() Функция {.row-span-2}

``python
class ParentClass:
    def print_test(self):
        print("Метод родителя")
 
class ChildClass(ParentClass):
    def print_test(self):
        print("Метод дочернего класса")
        # Вызывает родительский метод print_test()
        super().print_test()
```
---

``python
>>> child_instance = ChildClass()
>>> child_instance.print_test()
Метод дочернего класса
Родительский метод
```




### метод repr()

``python
class Employee:
    def __init__(self, name):
        self.name = name
 
    def __repr__(self):
        return self.name
 
john = Employee('John')
print(john) # => Джон
```


### Определяемые пользователем исключения
``python
class CustomError(Exception):
    pass
```



### Полиморфизм

``python
class ParentClass:
    def print_self(self):
        print('A')
 
class ChildClass(ParentClass):
    def print_self(self):
        print('B')
 
obj_A = ParentClass()
obj_B = ChildClass()
 
obj_A.print_self() # => A
obj_B.print_self() # => B
```

### Переопределение
``python
class ParentClass:
    def print_self(self):
        print("Parent")
 
class ChildClass(ParentClass):
    def print_self(self):
        print("Child")
 
child_instance = ChildClass()
child_instance.print_self() # => Child
```

### Наследование
``python
class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
        
class Dog(Animal):
    def sound(self):
        print("Woof!")
 
Yoki = Dog("Yoki", 4)
print(Yoki.name) # => YOKI
print(Yoki.legs) # => 4
Yoki.sound() # => Гав!
```




Подсказки типов в Python (начиная с Python 3.5)
--------


### Переменная и параметр
``python
string: str = "ha"
times: int = 3


# неправильное попадание, но выполняется корректно
результат: str = 1 + 2
print(result) # => 3


def say(name: str, start: str = "Привет"):
    return start + ", " + name

print(say("Python"))  # => Привет, Python
```


### Встроенный тип даты
``python
from typing import Dict, Tuple, List

bill: Dict[str, float] = {
    "apple": 3.14,
    "арбуз": 15.92,
    "ананас": 6.53,
}
completed: Кортеж[str] = ("DONE",)
succeeded: Tuple[int, str] = (1, "SUCCESS")
статусы: Кортеж[str, ...] = (
    "DONE", "SUCCESS", "FAILED", "ERROR",
)
коды: List[int] = (0, 1, -1, -2)
```


### Встроенный тип даты (3.10+)
``python
bill: dict[str, float] = {
    "apple": 3.14,
    "арбуз": 15.92,
    "ананас": 6.53,
}
завершено: tuple[str] = ("DONE",)
удалось: tuple[int, str] = (1, "SUCCESS")
статусы: tuple[str, ...] = (
    "DONE", "SUCCESS", "FAILED", "ERROR",
)
коды: list[int] = (0, 1, -1, -2)
```


### Позиционный аргумент
``python
def calc_summary(*args: int):
    return sum(args)

print(calc_summary(3, 1, 4))  # => 8
```

Укажите, что тип всех аргументов - int.


### Возвращается
``python
def say_hello(name) -> str:
    return "Hello, " + name

var = "Python"
print(say_hello(var))  # => Hello, Python
```


### Возвращенный союз
``python
from typing import Union

def resp200(meaningful) -> Union[int, str]:
    return "OK" if meaningful else 200
```

Означает, что тип возвращаемого значения может быть int или str.


### Аргумент ключевого слова
``python
def calc_summary(**kwargs: int):
    return sum(kwargs.values())

print(calc_summary(a=1, b=2))  # => 3
```

Укажите, что тип значения всех параметров - int.


### Множественные возвраты
``python
def resp200() -> (int, str):
    return 200, "OK"

returns = resp200()
print(returns) # => (200, 'OK')
print(type(returns))  # кортеж
```


### Возвращаемый союз (3.10+)
``python
def resp200(meaningful) -> int | str:
    return "OK" if meaningful else 200
```

Начиная с версии Python 3.10


### Свойства
``python
class Employee:
    name: str
    возраст: int

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.graduated: bool = False
```


### Экземпляр Self
``python
class Employee:
    name: str

    def set_name(self, name) -> "Сотрудник":
        self.name = name
        return self

    def copy(self) -> 'Сотрудник':
        return type(self)(self.name)
```


### Экземпляр Self (3.11+)
``python
from typing import Self

class Employee:
    name: str
    возраст: int

    def set_name(self: Self, name) -> Self:
        self.name = name
        return self
```


### Type & Generic {.col-span-2}
``python
from typing import TypeVar, Type

T = TypeVar("T")

# "mapper" - это тип, например, int, str, MyClass и т.д.
# "default" - экземпляр типа T, например, 314, "string", MyClass() и т.д.
# возвращаемый экземпляр также является экземпляром типа T.
def converter(raw, mapper: Type[T], default: T) -> T:
    try:
        return mapper(raw)
    except:
        return default

raw: str = input("Введите целое число: ")
result: int = converter(raw, mapper=int, default=0)
```


### Функция {.col-span-2}
``python
from typing import TypeVar, Callable, Any

T = TypeVar("T")

def converter(raw, mapper: Callable[[Any], T], default: T) -> T:
    try:
        return mapper(raw)
    except:
        return default

# Callable[[Any], ReturnType] означает объявление функции как:
# def func(arg: Any) -> ReturnType:
# pass

# Callable[[str, int], ReturnType] означает объявление функции следующим образом:
# def func(string: str, times: int) -> ReturnType:
# pass

# Callable[..., ReturnType] означает объявление функции, как:
# def func(*args, **kwargs) -> ReturnType:
# pass

def is_success(value) -> bool:
    return value in (0, "OK", True, "success")

resp = dict(code=0, message="OK", data=[])
successed: bool = converter(resp.message, mapper=is_success, default=False)
```




Разное
----------

### Комментарии

``python
# Это однострочный комментарий.
```

``python
""" Многострочные строки могут быть записаны
    используя три "s", и часто используются
    в качестве документации.
"""
```
``python
''' Многострочные строки могут быть записаны
    используя три 's, и часто используются
    в качестве документации.
'''
```


### Генераторы
``python
def double_numbers(iterable):
    for i in iterable:
        yield i + i
```

Генераторы помогают создавать "ленивый" код.


### Генератор для списка
``python
values = (-x for x in [1,2,3,4,5])
gen_to_list = list(values)

# => [-1, -2, -3, -4, -5]
print(gen_to_list)
```


### Обработка исключений {.col-span-3}
``python
try:
    # Используйте команду "raise", чтобы выдать ошибку
    raise IndexError("Это ошибка индекса")
except IndexError as e:
    pass # Pass - это просто отказ. Обычно здесь выполняется восстановление.
except (TypeError, NameError):
    pass # При необходимости можно обрабатывать несколько исключений вместе.
else:                    # Необязательный пункт в блоке try/except. Должен следовать за всеми блоками except
    print("Все хорошо!") # Выполняется только в том случае, если код в try не вызывает исключений
finally:                 # Выполняется при любых обстоятельствах
    print("Здесь мы можем очистить ресурсы")
```
