---
название: PHP
дата: 2021-01-04 15:23:28
фон: bg-[#7477a9]
теги:
    - веб
категории:
    - Программирование
intro: |
    Эта шпаргалка [PHP](https://www.php.net/manual/en/) позволяет быстро найти правильный синтаксис для наиболее часто используемого кода.
плагины:
    - copyCode
---


Начало работы
---------------


### hello.php
``php
<?php // начинается с тега PHP open.

echo "Hello World\n";
print("Hello cheatsheets.zip");

?>
```
Команда запуска PHP
``Основной сценарий
$ php hello.php
```



### Переменные
``php
$boolean1 = true;
$boolean2 = True;

$int = 12;
$float = 3.1415926;
unset($float); // Удаление переменной

$str1 = "Как дела?";
$str2 = "Отлично, спасибо";
```
См: [Types](#php-types)




### Строки
``php
$url = "cheatsheets.zip";
echo "Я изучаю PHP по адресу $url";

// Конкатенация строк
echo "Я изучаю PHP по адресу " . $url;

$hello = "Hello, ";
$hello .= "World!";
echo $hello; # => Hello, World!
```
См: [Строки](#php-strings)




### Массивы
``php
$num = [1, 3, 5, 7, 9];
$num[5] = 11;
unset($num[2]); // Удаление переменной
print_r($num); # => 1 3 7 9 11
echo count($num); # => 5
```
См: [Массивы](#php-arrays)



### Операторы
``php
$x = 1;
$y = 2;

$sum = $x + $y;
echo $sum; # => 3
```
См: [Операторы](#php-operators)


### Включить {.row-span-3}
#### vars.php
``php
<?php // начинаем с тега PHP open.
$fruit = 'apple';
echo "Яблоко было импортировано";
return 'Все, что угодно';
?>
```
#### test.php
``php
<?php
включить 'vars.php';
echo $fruit . "\n"; # => яблоко

/* То же, что и include,
вызывать ошибку, если не может быть включена*/
require 'vars.php';

// Также работает
include('vars.php');
require('vars.php');

// Включение через HTTP
include 'http://x.com/file.php';

// Включение и оператор возврата
$result = include 'vars.php';
echo $result; # => Все, что угодно.
?>
```



### Функции
``php
function add($num1, $num2 = 1) {
    return $num1 + $num2;
}
echo add(10); # => 11
echo add(10, 5); # => 15
```
См: [Функции](#php-functions)




### Комментарии
``php
# Это однострочный комментарий в стиле shell

// Это однострочный комментарий в стиле c++

/* Это многострочный комментарий
   еще одна строка комментария */
```



### Константы
``php
const MY_CONST = "hello";

echo MY_CONST; # => hello

# => MY_CONST is: hello
echo 'MY_CONST is: ' . MY_CONST;
```





### Классы
``php
класс Студент {
    public function __construct($name) {
        $this->name = $name;
    }
}
$alex = new Student("Alex");
```
См: [Классы](#php-classes)





Типы PHP
---------------


### Boolean {.row-span-2}
``php
$boolean1 = true;
$boolean2 = TRUE;
$boolean3 = false;
$boolean4 = FALSE;

$boolean5 = (boolean) 1; # => true
$boolean6 = (boolean) 0; # => false
```
Булевы выражения не чувствительны к регистру




### Integer {.row-span-2}
``php
$int1 = 28; # => 28
$int2 = -32; # => -32
$int3 = 012; # => 10 (восьмеричное)
$int4 = 0x0F; # => 15 (шестнадцатеричное)
$int5 = 0b101; # => 5 (двоичное)

# => 2000100000 (десятичная, PHP 7.4.0)
$int6 = 2_000_100_000;
```
См. также: [Integers](https://www.php.net/manual/en/language.types.integer.php)


### Строки
``php
echo 'это простая строка';
```
См: [Strings](#php-strings)

### Массивы
``php
$arr = array("hello", "world", "!");
```
См: [Массивы](#php-arrays)


### Float (Double)
``php
$float1 = 1.234;
$float2 = 1.2e7;
$float3 = 7E-10;

$float4 = 1_234.567; // по состоянию на PHP 7.4.0
var_dump($float4); // float(1234.567)

$float5 = 1 + "10.5"; # => 11.5
$float6 = 1 + "-1.3e3"; # => -1299
```



### Null
```php
$a = null;
$b = 'Hello php!';
echo $a ?? 'a is unset'; # => a is unset
echo $b ?? 'b is unset'; # => Hello php

$a = array();
$a == null # => true
$a === null # => false
is_null($a) # => false
```


### Iterables
``php
function bar(): iterable {
    return [1, 2, 3];
}
function gen(): iterable {
    yield 1;
    yield 2;
    yield 3;
}
foreach (bar() as $value) {
    echo $value; # => 123
}
```


Строки PHP
---------------



### Строка
``php
# => '$String'
$sgl_quotes = '$String';

# => 'Это $String'.
$dbl_quotes = "Это $sgl_quotes.";

# => символ табуляции.
$escaped = "\t символ табуляции.";

# => косая черта и буква "t": \t
$unescaped = 'косая черта и t: \t';
```




### Многострочный
``php
$str = "foo";

// Неинтерполированные многострочники
$nowdoc = <<'END'
Многострочная строка
$str
END;

// Выполнит интерполяцию строк
$heredoc = <<END
Многострочный
$str
END;
```



### Манипуляции
``php
$s = "Hello Phper";
echo strlen($s); # => 11

echo substr($s, 0, 3); # => Hel
echo substr($s, 1); # => ello Phper
echo substr($s, -4, 3);# => hpe

echo strtoupper($s); # => HELLO PHPER
echo strtolower($s); # => hello phper

echo strpos($s, "l"); # => 2
var_dump(strpos($s, "L")); # => false
```
См: [Строковые функции](https://www.php.net/manual/en/ref.strings.php)



Массивы PHP
---------------

### Определение {.row-span-2}
``php
$a1 = ["hello", "world", "!"].
$a2 = array("hello", "world", "!");
$a3 = explode(",", "apple,pear,peach");
```
#### Смешанные ключи int и string
``php
$array = array(
    "foo" => "bar",
    "bar" => "foo",
    100 => -100,
    -100 => 100,
);
var_dump($array);
```
#### Краткий синтаксис массива
``php
$array = [
    "foo" => "bar",
    "bar" => "foo",
];
```



### Мультимассив
```php
$multiArray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
];

print_r($multiArray[0][0]) # => 1
print_r($multiArray[0][1]) # => 2
print_r($multiArray[0][2]) # => 3
```


### Мультитип {.row-span-2}
```php
$array = array(
    "foo" => "bar",
    42 => 24,
    "multi" => array(
         "dim" => array(
             "a" => "foo"
         )
    )
);

# => string(3) "bar"
var_dump($array["foo"]);

# => int(24)
var_dump($array[42]);

# => string(3) "foo"
var_dump($array["multi"]["dim"]["a"]);
```



### манипуляция
```php
$arr = array(5 => 1, 12 => 2);
$arr[] = 56; // Добавление
$arr["x"] = 42; // Добавление с ключом
sort($arr); // Сортировка
unset($arr[5]); // Удалить
unset($arr); // Удалить все
```
См: [Функции работы с массивами](https://www.php.net/manual/en/ref.array.php)

### Индексирование итерации
``php
$array = array('a', 'b', 'c');
$count = count($array);

for ($i = 0; $i < $count; $i++) {
    echo "i:{$i}, v:{$array[$i]}\n";
}
```

### Итерация значений
``php
$colors = array('red', 'blue', 'green');

foreach ($colors as $color) {
    echo "Вам нравится $color?\n";
}
```
### Ключевая итерация
```php
$arr = ["foo" => "bar", "bar" => "foo"];

foreach ( $arr as $key => $value )
{
  	echo "key: " . $key . "\n";
    echo "val: {$arr[$key]}\n";
}
```

### Конкатенация массивов
```php
$a = [1, 2];
$b = [3, 4];

// PHP 7.4 later
# => [1, 2, 3, 4]
$result = [...$a, ...$b];
```

### В функции
```php
$array = [1, 2];

function foo(int $a, int $b) {
	echo $a; # => 1
  	echo $b; # => 2
}
foo(...$array);
```


### Оператор Splat
``php
function foo($first, ...$other) {
	var_dump($first); # => a
  	var_dump($other); # => ['b', 'c']
}
foo('a', 'b', 'c' /*, ...*/ );
// или
function foo($first, string ...$other){}
```



Операторы PHP {.cols-4}
---------------



### Арифметика
| - | - |
|------|----------------|
| `+` | Сложение |
| `-` | Вычитание |
| `*` | Умножение |
| `/` | Деление |
| `%` | Модуль |
| `**` | Экспонирование |

### Задание
| - | - |
|----------|---------------------|
| `a += b` | То же, что `a = a + b` |
| `a -= b` | То же, что `a = a - b` |
| `a *= b` | То же, что `a = a * b` |
| `a /= b` | То же, что `a = a / b` |
| `a %= b` | То же, что `a = a % b` |


### Сравнение {.row-span-2}
| - | - |
|-------|------------------------------|
| `==` | Equal |
| `===` | Одинаковые |
| `!=` | Не равно |
| `<>` | Не равны |
| `!==` | Не идентичны |
| `<` | Меньше |
| `>` | Больше |
| `<=` | Меньше или равно |
| `>=` | Больше или равно |
| `<=>` | Меньше/равнее/больше |

### Логические
| - | - |
|-------|--------------|
| `and` | And |
| `or` | Or |
| `xor` | Исключительное или |
| `!` | Не |
| `&&` | And |
| `||` | Or |




### Арифметика {.col-span-2}
``php
// Арифметика
$sum = 1 + 1; // 2
$difference = 2 - 1; // 1
$product = 2 * 2; // 4
$quotient = 2 / 1; // 2

// Сокращенная арифметика
$num = 0;
$num += 1; // Увеличение $num на 1
echo $num++; // Выводит 1 (увеличивается после оценки)
echo ++$num; // Выводит 3 (увеличивает до оценки)
$num /= $float; // Разделить и присвоить цитату $num
```



### Побитовый
| - | - |
|------|--------------------|
| `&` | And |
| `|` | Or (инклюзивное или) |
| `^` | Xor (исключающее или) |
| `~` | Не |
| `<<` | Сдвиг влево |
| `>>` | Сдвиг вправо |




Условия PHP
---------------

### If elseif else
``php
$a = 10;
$b = 20;

if ($a > $b) {
    echo "a больше, чем b";
} elseif ($a == $b) {
    echo "a равно b";
} else {
    echo "a меньше b";
}
```


### Переключатель
```php
$x = 0;
switch ($x) {
    case '0':
        print "it's zero";
        break;
    case '2':
    case '3':
        // сделайте что-нибудь
        break;
    default:
        // do something
}
```

### Тернарный оператор
``php
# => Does
print (false ? 'Not' : 'Does');

$x = false;
# => Does
print($x ?: 'Does');

$a = null;
$b = 'Does print';
# => a не задано
echo $a ?? 'a is unset';
# => печать
echo $b ?? 'b is unset';
```

### Match
```php
$statusCode = 500;
$message = match($statusCode) {
  200, 300 => null,
  400 => 'не найдено',
  500 => 'ошибка сервера',
  default => 'известный код состояния',
};
echo $message; # => ошибка сервера
```
См: [Match](https://www.php.net/manual/en/control-structures.match.php)


### Соответствие выражений
``php
$age = 23;

$result = match (true) {
    $age >= 65 => 'senior',
    $age >= 25 => "взрослый",
    $age >= 18 => 'young adult',
    default => 'kid',
};

echo $result; # => young adult
```


Циклы PHP
---------------


### while
``php
$i = 1;
# => 12345
while ($i <= 5) {
    echo $i++;
}
```

### do while
```php
$i = 1;
# => 12345
do {
    echo $i++;
} while ($i <= 5);
```


### for i
```php
# => 12345
for ($i = 1; $i <= 5; $i++) {
    echo $i;
}
```

### break
``php
# => 123
for ($i = 1; $i <= 5; $i++) {
    if ($i === 4) {
        break;
    }
    echo $i;
}
```

### continue
``php
# => 1235
for ($i = 1; $i <= 5; $i++) {
    if ($i === 4) {
        продолжить;
    }
    echo $i;
}
```

### foreach
```php
$a = ['foo' => 1, 'bar' => 2];
# => 12
foreach ($a as $k) {
    echo $k;
}
```
См: [Итерация массива](#php-value-iteration)



Функции PHP
---------------


### Возврат значений
``php
function square($x)
{
    return $x * $x;
}

echo square(4); # => 16
```

### Возвращаемые типы
```php
// Базовое объявление возвращаемого типа
function sum($a, $b): float {/*...*/}
function get_item(): string {/*...*/}

class C {}
// Возвращение объекта
function getC(): C { return new C; }
```

### Нулевые возвращаемые типы
``php
// Доступно в PHP 7.1
function nullOrString(int $v) : ?string
{
    return $v % 2 ? "odd" : null;
}
echo nullOrString(3); # => odd
var_dump(nullOrString(4)); # => NULL
```
См: [Nullable types](https://www.php.net/manual/en/migration71.new-features.php)

### Функции Void
``php
// Доступно в PHP 7.1
функция voidFunction(): void
{
	echo 'Hello';
	return;
}

voidFunction(); # => Hello
```

### Функции переменных
``php
function bar($arg = '')
{
    echo "В bar(); arg: '$arg'.\n';
}

$func = 'bar';
$func('test'); # => In bar(); arg: test
```





### Анонимные функции
``php
$greet = function($name)
{
    printf("Hello %s\r\n", $name);
};

$greet('World'); # => Hello World
$greet('PHP'); # => Hello PHP
```




### Рекурсивные функции
``php
function recursion($x)
{
    if ($x < 5) {
        echo "$x";
        recursion($x + 1);
    }
}
recursion(1); # => 1234
```



### Параметры по умолчанию
``php
function coffee($type = "cappuccino")
{
    return "Делаем чашку кофе $type.\n";
}
# => Делаем чашку капучино.
echo coffee();
# => Делаем чашку .
echo coffee(null);
# => Приготовление чашки эспрессо.
echo coffee("espresso");
```



### Функции стрелок
``php
$y = 1;
 
$fn1 = fn($x) => $x + $y;

// эквивалентно использованию $y по значению:
$fn2 = function ($x) use ($y) {
    return $x + $y;
};
echo $fn1(5); # => 6
echo $fn2(5); # => 6
```




Классы PHP
---------------


### Конструктор
``php
class Student {
    public function __construct($name) {
        $this->name = $name;
    }
  	public function print() {
        echo "Имя: " . $this->name;
    }
}
$alex = new Student("Alex");
$alex->print(); # => Имя: Алекс
```

### Наследование
``php
class ExtendClass extends SimpleClass
{
    // Переопределяем родительский метод
    function displayVar()
    {
        echo "Расширение класса\n";
        parent::displayVar();
    }
}

$extended = new ExtendClass();
$extended->displayVar();
```

### Переменные класса {.row-span-2}
``php
class MyClass
{
    const MY_CONST = 'value';
    static $staticVar = 'static';

    // Видимость
    public static $var1 = 'pubs';

    // Только класс
    private static $var2 = 'pris';

    // Класс и подклассы
    protected static $var3 = 'pros';

    // Класс и подклассы
    protected $var6 = 'pro';

    // Только класс
    private $var7 = 'pri';
}
```
Доступ статически
``php
echo MyClass::MY_CONST; # => значение
echo MyClass::$staticVar; # => static
```



### Магические методы
``php
класс MyClass
{
    // Объект рассматривается как строка
    public function __toString()
    {
        return $property;
    }
    // противоположность функции __construct()
    public function __destruct()
    {
        print "Destroying";
    }
}
```


### Интерфейс
``php
интерфейс Foo
{
    public function doSomething();
}
интерфейс Bar
{
    public function doSomethingElse();
}
class Cls implements Foo, Bar
{
    public function doSomething() {}
    public function doSomethingElse() {}
}
```

Разное
-------------

### Базовая обработка ошибок
``php
try {
    // Делаем что-нибудь
} catch (Exception $e) {
    // Обработка исключения
} finally {
    echo "Всегда печатайте!";
}
```

### Исключение в PHP 8.0 {.col-span-2}
``php {.wrap}
$nullableValue = null;

try {
	$value = $nullableValue ?? throw new InvalidArgumentException();
} catch (InvalidArgumentException) { // Переменная необязательна
    // Обработка моего исключения
    echo "print me!";
}
```

### Пользовательское исключение {.row-span-2}
``php
class MyException extends Exception {
    // сделать что-нибудь
}
```
Использование
``php
try {
    $condition = true;
    if ($condition) {
        throw new MyException('bala');
    }
} catch (MyException $e) {
    // Обработка моего исключения
}
```

### Nullsafe Operator {.row-span-2}
``php
// Начиная с версии PHP 8.0.0, эта строка:
$result = $repo?->getUser(5)?->name;

// Эквивалентно следующему коду:
if (is_null($repo)) {
    $result = null;
} else {
    $user = $repository->getUser(5);
    if (is_null($user)) {
        $result = null;
    } else {
        $result = $user->name;
    }
}
```
См. также: [Nullsafe Operator](https://wiki.php.net/rfc/nullsafe_operator)

### Регулярные выражения
``php
$str = "Посетите сайт Quickref.me";
echo preg_match("/qu/i", $str); # => 1
```
См: [Regex в PHP](/regex#regex-in-php)

### режим fopen()

| - | - |
|------|--------------------------|
| `r` | Чтение |
| `r+` | Чтение и запись, добавление |
| `w` | Запись, усечение |
| `w+` | Чтение и запись, усечение |
| `a` | Запись, добавление |
| `a+` | Чтение и запись, добавление |



### Константы, определяемые временем выполнения
``php
define("CURRENT_DATE", date('Y-m-d'));

// Одно из возможных представлений
echo CURRENT_DATE; # => 2021-01-05

# => CURRENT_DATE is: 2021-01-05
echo 'CURRENT_DATE is: ' . CURRENT_DATE;
```


Также см.
-------

- [PHP Docs](https://www.php.net/manual/en/index.php)
- [Выучить X за Y минут](https://learnxinyminutes.com/docs/php/)




