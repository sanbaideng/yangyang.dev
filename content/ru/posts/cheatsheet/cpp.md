---
title: C++
date: 2021-06-01 11:51:44
фон: bg-[#6d94c7]
tags:
категории:
  - Программирование
intro: |
    Краткая справочная шпаргалка по C++, содержащая основные сведения о синтаксисе и методах.
плагины:
    - copyCode
---


Начало работы
--------

### hello.cpp

``cpp
#include <iostream

int main() {
    std::cout << "Привет, читы\n";
    return 0;
}
```

Компиляция и запуск

``Основной сценарий
$ g++ hello.cpp -o hello
$ ./hello
Шпаргалки по Hello
```

### Переменные

``cpp
int number = 5; // Целое число
float f = 0.95; // Плавающее число
double PI = 3.14159; // Плавающее число
char yes = 'Y'; // Символ
std::string s = "ME"; // Строка (текст)
bool isRight = true; // Булево

// Константы
const float RATE = 0.8;
```

----

``cpp
int age {25}; // С C++11
std::cout << age; // Вывести 25
```

### Примитивные типы данных

| Тип данных | Размер | Диапазон |
|-----------|----------------|---------------------|
| `int` | 4 байта | -2^31^ ^to^ 2^31^-1 |
| `float` | 4 байта | _N/A_ |
| `double` | 8 байт | _N/A_ |
| `char` | 1 байт | -128 ^to^ 127 |
| `bool` | 1 байт | true / false |
| `void` | _N/A_ | _N/A_ |
| `wchar_t` | 2 ^или^ 4 байта | 1 широкий символ |
{.show-header}

### Пользовательский ввод

``cpp
int num;

std::cout << "Введите число: ";
std::cin >> num;

std::cout << "Вы ввели " << num;
```

### Swap

``cpp
int a = 5, b = 10;
std::swap(a, b);

// Выходные данные: a=10, b=5
std::cout << "a=" << a << ", b=" << b;
```

### Комментарии

``cpp
// Одиночный однострочный комментарий на языке C++

/* Многострочный комментарий
   в C++ */
```

### Оператор If

``cpp
if (a == 10) {
    // сделайте что-нибудь
}
```

См: [Conditionals](#c-conditionals)

### Циклы

``cpp
for (int i = 0; i < 10; i++) {
    std::cout << i << "\n";
}
```

См: [Loops](#c-loops)

### Функции

``cpp
#include <iostream
 
void hello(); // Объявление
 
int main() { // главная функция
    hello(); // Вызов
}
 
void hello() { // Определение
    std::cout << "Hello CheatSheets!\n";
}
```

См: [Функции](#c-functions)

### Ссылки

``cpp
int i = 1;
int& ri = i; // ri - это ссылка на i

ri = 2; // i теперь меняется на 2
std::cout << "i=" << i;

i = 3; // i теперь изменяется на 3
std::cout << "ri=" << ri;
```

`ri` и `i` ссылаются на одну и ту же ячейку памяти.

### Пространства имен

``cpp
#include <iostream
namespace ns1 {int val(){return 5;}}
int main()
{
    std::cout << ns1::val();
}
```

---

``cpp
#include <iostream
namespace ns1 {int val(){return 5;}}
using namespace ns1;
using namespace std;
int main()
{
    cout << val();
}
```

Пространства имен позволяют использовать глобальные идентификаторы под одним именем

Массивы в C++
------

### Декларация

``cpp
std::array<int, 3> marks; // Определение
marks[0] = 92;
marks[1] = 97;
marks[2] = 98;

// Определение и инициализация
std::array<int, 3> = {92, 97, 98};

// С пустыми членами
std::array<int, 3> marks = {92, 97};
std::cout << marks[2]; // Выходные данные: 0
```

### Манипуляция

``cpp
┌─────┬─────┬─────┬─────┬─────┬─────┐
| 92 | 97 | 98 | 99 | 98 | 94 |
└─────┴─────┴─────┴─────┴─────┴─────┘
   0 1 2 3 4 5
```

---

``cpp
std::array<int, 6> marks = {92, 97, 98, 99, 98, 94};

// Печать первого элемента
std::cout << marks[0];

// Изменим второй элемент на 99
marks[1] = 99;

// Принимаем ввод от пользователя
std::cin >> marks[2];
```

### Отображение

``cpp
char ref[5] = {'R', 'e', 'f'};

// Цикл для работы с диапазонами
for (const int &n : ref) {
    std::cout << std::string(1, n);
}

// Традиционный цикл for
for (int i = 0; i < sizeof(ref); ++i) {
    std::cout << ref[i];
}
```

### Многомерность

``cpp
     j0 j1 j2 j3 j4 j5
   ┌────┬────┬────┬────┬────┬────┐
i0 | 1 | 2 | 3 | 4 | 5 | 6 |
   ├────┼────┼────┼────┼────┼────┤
i1 | 6 | 5 | 4 | 3 | 2 | 1 |
   └────┴────┴────┴────┴────┴────┘
```

---

``cpp
int x[2][6] = {
    {1,2,3,4,5,6}, {6,5,4,3,2,1}
};
for (int i = 0; i < 2; ++i) {
    for (int j = 0; j < 6; ++j) {
        std::cout << x[i][j] << " ";
    }
}
// Выходные данные: 1 2 3 4 5 6 6 5 4 3 2 1
```

Условия в C++
------------

### Клаузула If

``cpp
if (a == 10) {
    // сделайте что-нибудь
}
```

---

``cpp
int number = 16;

if (number % 2 == 0)
{
    std::cout << "чет";
}
else
{
    std::cout << "odd";
}

// Выходные данные: четные
```

### Else if Statement

``cpp
int score = 99;
if (score == 100) {
    std::cout << "Superb";
}
else if (score >= 90) {
    std::cout << "Отлично";
}
else if (score >= 80) {
    std::cout << "Очень хорошо";
}
else if (score >= 70) {
    std::cout << "Хорошо";
}
else if (score >= 60)
    { std::cout << "OK";
else
    std::cout << "Что?";
```

### Операторы {.row-span-2}

#### Реляционные операторы

| | |
|----------|------------------------------|
| `a == b` | a равно b |
| `a != b` | a НЕ равно b |
| `a < b` | a меньше b |
| `a > b` | a больше b |
| `a <= b` | a меньше или равно b |
| `a >= b` | a больше или равно b |

#### Операторы присваивания

| Пример | Эквивалентно |
|----------|-----------------|
| `a += b` | _Aka_ a = a + b |
| `a -= b` | _Aka_ a = a - b |
| `a *= b` | _Aka_ a = a * b |
| `a /= b` | _Aka_ a = a / b |
| `a %= b` | _Aka_ a = a % b |

#### Логические операторы

| Пример | Значение |
|----------------|------------------------|
| `exp1 && exp2` | Оба истинны _(AND)_ |
| `exp1 || exp2` | Любое из них истинно _(OR)_ |
| `!exp` | `exp` является ложным _(NOT)_ |

#### Побитовые операторы

| Оператор | Описание |
|----------|-------------------------|
| `a & b` | Двоичное И |
| `a | b` | Двоичное ИЛИ |
| `a ^ b` | Двоичное XOR |
| | `~ a` | Двоичное дополнение единицы |
| | `a << b` | Двоичный сдвиг влево |
| `a >> b` | Двоичный сдвиг вправо |

### Тернарный оператор

```
           ┌──── True ──┐
Результат = Условие ? Exp1 : Exp2;
           └───── False ─────┘
```

---

``cpp
int x = 3, y = 5, max;
max = (x > y) ? x : y;

// Выходные данные: 5
std::cout << max << std::endl;
```

---

``cpp
int x = 3, y = 5, max;
if (x > y) {
    max = x;
} else {
    max = y;
}
// Выходные данные: 5
std::cout << max << std::endl;
```

### Переключающее утверждение

``cpp
int num = 2;
switch (num) {
    case 0:
        std::cout << "Ноль";
        break;
    case 1:
        std::cout << "Один";
        break;
    case 2:
        std::cout << "Два";
        break;
    case 3:
        std::cout << "Три";
        break;
    default:
        std::cout << "Что?";
        break;
}
```

Циклы C++
------------

### While

``cpp
int i = 0;
while (i < 6) {
    std::cout << i++;
}

// Выходные данные: 012345
```

### Do-while

``cpp
int i = 1;
do {
    std::cout << i++;
} while (i <= 5);

// Выходные данные: 12345
```

### Продолжение утверждений

``cpp
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) {
        continue;
    }
    std::cout << i;
} // Выходные данные: 13579
```

### Бесконечный цикл

``cpp
while (true) { // true или 1
    std::cout << "бесконечный цикл";
}
```

---

``cpp
for (;;) {
    std::cout << "бесконечный цикл";
}
```

---

``cpp
for(int i = 1; i > 0; i++) {
    std::cout << "бесконечный цикл";
}
```

### for_each (с C++11)

```cpp
#include <iostream

int main()
{
    auto print = [](int num) { std::cout << num << std::endl; }

    std::array<int, 4> arr = {1, 2, 3, 4};
    std::for_each(arr.begin(), arr.end(), print);
    return 0;
}
```

### Range-based (Since C++11)

``cpp
for (int n : {1, 2, 3, 4, 5}) {
    std::cout << n << " ";
}
// Выходные данные: 1 2 3 4 5
```

---

``cpp
std::string hello = "CheatSheets.zip";
for (char c: hello)
{
    std::cout << c << " ";
}
// Выходные данные: Q u i c k R e f . M E
```

### Прерывание утверждений

``cpp
int password, times = 0;
while (password != 1234) {
    if (times++ >= 3) {
        std::cout << "Заблокировано!\n";
        break;
    }
    std::cout << "Пароль: ";
    std::cin >> password; // input
}
```

### Несколько вариантов

``cpp
for (int i = 0, j = 2; i < 3; i++, j--){
    std::cout << "i=" << i << ",";
    std::cout << "j=" << j << ";";
}
// Выходные данные: i=0,j=2;i=1,j=1;i=2,j=0;
```

Функции C++
------------

### Аргументы и возвраты

``cpp
#include <iostream

int add(int a, int b) {
    return a + b;
}

int main() {
    std::cout << add(10, 20);
}
```

``add`` - это функция, принимающая 2 инта и возвращающая int

### Перегрузка

``cpp
void fun(string a, string b) {
    std::cout << a + " " + b;
}
void fun(string a) {
    std::cout << a;
}
void fun(int a) {
    std::cout << a;
}
```

### Встроенные функции

``cpp
#include <iostream>
#include <cmath> // импорт библиотеки
 
int main() {
    // sqrt() из cmath
    std::cout << sqrt(9);
}
```

Классы и объекты C++ {.cols-2}
-----------------

### Определение класса

``cpp
класс MyClass {
  public:             // Спецификатор доступа
    int myNum; // Атрибут (переменная int)
    string myString; // Атрибут (строковая переменная)
};

```

### Создание объекта

``cpp
MyClass myObj; // Создание объекта MyClass

myObj.myNum = 15; // Устанавливаем значение myNum равным 15
myObj.myString = "Hello"; // Установить значение myString равным "Hello"

cout << myObj.myNum << endl; // Вывести значение 15
cout << myObj.myString << endl; // Выводим "Hello"

```

### Конструкторы

``cpp
класс MyClass {
  public:
    int myNum;
    string myString;
    MyClass() { // Конструктор
      myNum = 0;
      myString = "";
    }
};

MyClass myObj; // Создание объекта MyClass

cout << myObj.myNum << endl; // Выводим 0
cout << myObj.myString << endl; // Вывод ""

```

### Деструкторы

``cpp
класс MyClass {
  public:
    int myNum;
    string myString;
    MyClass() { // Конструктор
      myNum = 0;
      myString = "";
    }
    ~MyClass() { // Деструктор
      cout << "Объект уничтожен". << endl;
    }
};

MyClass myObj; // Создание объекта MyClass

// Код здесь...

// Объект уничтожается автоматически при выходе программы из области видимости


```


### Методы класса

``cpp
класс MyClass {
  public:
    int myNum;
    string myString;
    void myMethod() { // Метод/функция, определенная внутри класса
      cout << "Hello World!" << endl;
    }
};

MyClass myObj; // Создаем объект MyClass
myObj.myMethod(); // Вызов метода
```


### Модификаторы доступа

``cpp
класс MyClass {
  public:     // Спецификатор доступа public
    int x; // Публичный атрибут
  private:    // Спецификатор частного доступа
    int y; // Частный атрибут
  protected:  // Спецификатор защищенного доступа
    int z; // Защищенный атрибут
};

MyClass myObj;
myObj.x = 25; // Разрешено (public)
myObj.y = 50; // Не разрешено (private)
myObj.z = 75; // Не разрешено (protected)

```


### Геттеры и сеттеры

``cpp
класс MyClass {
  private:
    int myNum;
  public:
    void setMyNum(int num) { // Setter
      myNum = num;
    }
    int getMyNum() { // Getter
      return myNum;
    }
};

MyClass myObj;
myObj.setMyNum(15); // Устанавливаем значение myNum равным 15
cout << myObj.getMyNum() << endl; // Выводим значение 15

```


### Наследование

``cpp
класс Vehicle {
  public:
    string brand = "Ford";
    void honk() {
      cout << "Туут, туут!" << endl;
    }
};

class Car : public Vehicle {
  public:
    string model = "Mustang";
};

Car myCar;
myCar.honk(); // Вывод "Туут, туут!".
cout << myCar.brand + " " + myCar.model << endl; // Вывод "Ford Mustang"
```



Препроцессор C++
------------

### Препроцессор {.row-span-3}

- [if](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [elif](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [else](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [endif](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [ifdef](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [ifndef](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [define](https://en.cppreference.com/w/cpp/preprocessor/replace)
- [undef](https://en.cppreference.com/w/cpp/preprocessor/replace)
- [include](https://en.cppreference.com/w/cpp/preprocessor/include)
- [line](https://en.cppreference.com/w/cpp/preprocessor/line)
- [error](https://en.cppreference.com/w/cpp/preprocessor/error)
- [pragma](https://en.cppreference.com/w/cpp/preprocessor/impl)
- [defined](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [__has_include](https://en.cppreference.com/w/cpp/feature_test)
- [__has_cpp_attribute](https://en.cppreference.com/w/cpp/feature_test)
- [export](https://en.cppreference.com/w/cpp/keyword/export)
- [import](https://en.cppreference.com/mwiki/index.php?title=cpp/keyword/import&amp;action=edit&amp;redlink=1)
- [module](https://en.cppreference.com/mwiki/index.php?title=cpp/keyword/module&amp;action=edit&amp;redlink=1)
{.marker-none .cols-2}

### Включает

``cpp
#include "iostream"
#include <iostream>
```

### Определяет

``cpp
#define FOO
#define FOO "hello"

#undef FOO
```

### Если {.row-span-2}

``cpp
#ifdef DEBUG
  console.log('hi');
#elif defined VERBOSE
  ...
#else
  ...
#endif
```

### Ошибка

``cpp
#if VERSION == 2.0
  #error Не поддерживается
  #warning Не поддерживается
#endif
```

### Макрос

``cpp
#define DEG(x) ((x) * 57.29)
```

### Конкатенация токенов

``cpp
#define DST(name) name##_s name##_t
DST(object); #=> object_s object_t;
```

### Стрингизация

``cpp
#define STR(name) #name
char * a = STR(object); #=> char * a = "object";
```

### файл и строка

``cpp
#define LOG(msg) console.log(__FILE__, __LINE__, msg)
#=> console.log("file.txt", 3, "hey")
```

Разное
-------------

### Escape Sequences

| Последовательности экранирования | Символы |
|------------------|-----------------------|
| `\b` | Backspace |
| `\f` | Форма подачи |
| `\n` | Новая строка |
| `\r` | Возврат |
| `\t` | Горизонтальная вкладка |
| `\v` | Вертикальная табуляция |
| `\\\` | Обратная косая черта |
| | `\'` | Одинарная кавычка |
| | `\"` | Двойная кавычка |
| `\?` | Вопросительный знак |
| `\0` | Нулевой символ |

### Ключевые слова {.col-span-2 .row-span-2}

- [alignas](https://en.cppreference.com/w/cpp/keyword/alignas)
- [alignof](https://en.cppreference.com/w/cpp/keyword/alignof)
- [and](https://en.cppreference.com/w/cpp/keyword/and)
- [and_eq](https://en.cppreference.com/w/cpp/keyword/and_eq)
- [asm](https://en.cppreference.com/w/cpp/keyword/asm)
- [atomic_cancel](https://en.cppreference.com/w/cpp/keyword/atomic_cancel)
- [atomic_commit](https://en.cppreference.com/w/cpp/keyword/atomic_commit)
- [atomic_noexcept](https://en.cppreference.com/w/cpp/keyword/atomic_noexcept)
- [auto](https://en.cppreference.com/w/cpp/keyword/auto)
- [bitand](https://en.cppreference.com/w/cpp/keyword/bitand)
- [bitor](https://en.cppreference.com/w/cpp/keyword/bitor)
- [bool](https://en.cppreference.com/w/cpp/keyword/bool)
- [break](https://en.cppreference.com/w/cpp/keyword/break)
- [case](https://en.cppreference.com/w/cpp/keyword/case)
- [catch](https://en.cppreference.com/w/cpp/keyword/catch)
- [char](https://en.cppreference.com/w/cpp/keyword/char)
- [char8_t](https://en.cppreference.com/w/cpp/keyword/char8_t)
- [char16_t](https://en.cppreference.com/w/cpp/keyword/char16_t)
- [char32_t](https://en.cppreference.com/w/cpp/keyword/char32_t)
- [class](https://en.cppreference.com/w/cpp/keyword/class)
- [compl](https://en.cppreference.com/w/cpp/keyword/compl)
- [concept](https://en.cppreference.com/w/cpp/keyword/concept)
- [const](https://en.cppreference.com/w/cpp/keyword/const)
- [consteval](https://en.cppreference.com/w/cpp/keyword/consteval)
- [constexpr](https://en.cppreference.com/w/cpp/keyword/constexpr)
- [constinit](https://en.cppreference.com/w/cpp/keyword/constinit)
- [const_cast](https://en.cppreference.com/w/cpp/keyword/const_cast)
- [continue](https://en.cppreference.com/w/cpp/keyword/continue)
- [co_await](https://en.cppreference.com/w/cpp/keyword/co_await)
- [co_return](https://en.cppreference.com/w/cpp/keyword/co_return)
- [co_yield](https://en.cppreference.com/w/cpp/keyword/co_yield)
- [decltype](https://en.cppreference.com/w/cpp/keyword/decltype)
- [default](https://en.cppreference.com/w/cpp/keyword/default)
- [delete](https://en.cppreference.com/w/cpp/keyword/delete)
- [do](https://en.cppreference.com/w/cpp/keyword/do)
- [double](https://en.cppreference.com/w/cpp/keyword/double)
- [dynamic_cast](https://en.cppreference.com/w/cpp/keyword/dynamic_cast)
- [else](https://en.cppreference.com/w/cpp/keyword/else)
- [enum](https://en.cppreference.com/w/cpp/keyword/enum)
- [explicit](https://en.cppreference.com/w/cpp/keyword/explicit)
- [export](https://en.cppreference.com/w/cpp/keyword/export)
- [extern](https://en.cppreference.com/w/cpp/keyword/extern)
- [false](https://en.cppreference.com/w/cpp/keyword/false)
- [float](https://en.cppreference.com/w/cpp/keyword/float)
- [for](https://en.cppreference.com/w/cpp/keyword/for)
- [friend](https://en.cppreference.com/w/cpp/keyword/friend)
- [goto](https://en.cppreference.com/w/cpp/keyword/goto)
- [if](https://en.cppreference.com/w/cpp/keyword/if)
- [inline](https://en.cppreference.com/w/cpp/keyword/inline)
- [int](https://en.cppreference.com/w/cpp/keyword/int)
- [long](https://en.cppreference.com/w/cpp/keyword/long)
- [mutable](https://en.cppreference.com/w/cpp/keyword/mutable)
- [namespace](https://en.cppreference.com/w/cpp/keyword/namespace)
- [new](https://en.cppreference.com/w/cpp/keyword/new)
- [noexcept](https://en.cppreference.com/w/cpp/keyword/noexcept)
- [not](https://en.cppreference.com/w/cpp/keyword/not)
- [not_eq](https://en.cppreference.com/w/cpp/keyword/not_eq)
- [nullptr](https://en.cppreference.com/w/cpp/keyword/nullptr)
- [operator](https://en.cppreference.com/w/cpp/keyword/operator)
- [or](https://en.cppreference.com/w/cpp/keyword/or)
- [or_eq](https://en.cppreference.com/w/cpp/keyword/or_eq)
- [private](https://en.cppreference.com/w/cpp/keyword/private)
- [protected](https://en.cppreference.com/w/cpp/keyword/protected)
- [public](https://en.cppreference.com/w/cpp/keyword/public)
- [reflexpr](https://en.cppreference.com/w/cpp/keyword/reflexpr)
- [register](https://en.cppreference.com/w/cpp/keyword/register)
- [reinterpret_cast](https://en.cppreference.com/w/cpp/keyword/reinterpret_cast)
- [requires](https://en.cppreference.com/w/cpp/keyword/requires)
- [return](https://en.cppreference.com/w/cpp/language/return)
- [short](https://en.cppreference.com/w/cpp/keyword/short)
- [signed](https://en.cppreference.com/w/cpp/keyword/signed)
- [sizeof](https://en.cppreference.com/w/cpp/keyword/sizeof)
- [static](https://en.cppreference.com/w/cpp/keyword/static)
- [static_assert](https://en.cppreference.com/w/cpp/keyword/static_assert)
- [static_cast](https://en.cppreference.com/w/cpp/keyword/static_cast)
- [struct](https://en.cppreference.com/w/cpp/keyword/struct)
- [switch](https://en.cppreference.com/w/cpp/keyword/switch)
- [synchronized](https://en.cppreference.com/w/cpp/keyword/synchronized)
- [template](https://en.cppreference.com/w/cpp/keyword/template)
- [this](https://en.cppreference.com/w/cpp/keyword/this)
- [thread_local](https://en.cppreference.com/w/cpp/keyword/thread_local)
- [throw](https://en.cppreference.com/w/cpp/keyword/throw)
- [true](https://en.cppreference.com/w/cpp/keyword/true)
- [try](https://en.cppreference.com/w/cpp/keyword/try)
- [typedef](https://en.cppreference.com/w/cpp/keyword/typedef)
- [typeid](https://en.cppreference.com/w/cpp/keyword/typeid)
- [typename](https://en.cppreference.com/w/cpp/keyword/typename)
- [union](https://en.cppreference.com/w/cpp/keyword/union)
- [unsigned](https://en.cppreference.com/w/cpp/keyword/unsigned)
- [using](https://en.cppreference.com/w/cpp/keyword/using)
- [virtual](https://en.cppreference.com/w/cpp/keyword/virtual)
- [void](https://en.cppreference.com/w/cpp/keyword/void)
- [volatile](https://en.cppreference.com/w/cpp/keyword/volatile)
- [wchar_t](https://en.cppreference.com/w/cpp/keyword/wchar_t)
- [while](https://en.cppreference.com/w/cpp/keyword/while)
- [xor](https://en.cppreference.com/w/cpp/keyword/xor)
- [xor_eq](https://en.cppreference.com/w/cpp/keyword/xor_eq)
- [final](https://en.cppreference.com/w/cpp/language/final)
- [override](https://en.cppreference.com/w/cpp/language/override)
- [transaction_safe](https://en.cppreference.com/w/cpp/language/transactional_memory)
- [transaction_safe_dynamic](https://en.cppreference.com/w/cpp/language/transactional_memory)
{.marker-none .cols-5}

### Препроцессор

- [if](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [elif](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [else](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [endif](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [ifdef](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [ifndef](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [define](https://en.cppreference.com/w/cpp/preprocessor/replace)
- [undef](https://en.cppreference.com/w/cpp/preprocessor/replace)
- [include](https://en.cppreference.com/w/cpp/preprocessor/include)
- [line](https://en.cppreference.com/w/cpp/preprocessor/line)
- [error](https://en.cppreference.com/w/cpp/preprocessor/error)
- [pragma](https://en.cppreference.com/w/cpp/preprocessor/impl)
- [defined](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [__has_include](https://en.cppreference.com/w/cpp/feature_test)
- [__has_cpp_attribute](https://en.cppreference.com/w/cpp/feature_test)
- [export](https://en.cppreference.com/w/cpp/keyword/export)
- [import](https://en.cppreference.com/mwiki/index.php?title=cpp/keyword/import&amp;action=edit&amp;redlink=1)
- [module](https://en.cppreference.com/mwiki/index.php?title=cpp/keyword/module&amp;action=edit&amp;redlink=1)
{.marker-none .cols-2}

## Также см.

- [C++ Infographics & Cheat Sheets](https://hackingcpp.com/cpp/cheat_sheets.html) _(hackingcpp.com)_

- [C++ reference](https://en.cppreference.com/w/) _(cppreference.com)_
- [C++ Language Tutorials](http://www.cplusplus.com/doc/tutorial/) _(cplusplus.com)_
