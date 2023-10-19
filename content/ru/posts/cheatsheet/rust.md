---
title: Rust
date: 2022-01-01 11:51:44
фон: bg-black
tags:
категории:
    - Программирование
intro: |
    Краткая справочная шпаргалка по Rust, цель которой - помочь в написании базового синтаксиса и методов.
плагины:
    - copyCode
---


Начало работы
---------------

### Hello_World.rs

``rust
fn main() {
  println!("Hello, World!");
}
```
#### Компиляция и запуск
``Оболочка
$ rustc Hello_World.rs
$ ./Hello_World
Привет, мир!
```

### Примитивные типы

| | |
|---------------------------|----------------------------------|
| `bool` | Boolean (`true` _/_ `false`)|
| `char` | символ |
| | `f32`, `f64` | 32-битные, 64-битные плавающие числа |
| `i64`, `i32`, `i16`, `i8` | подписанные 16- ... целые числа |
| | `u64`, `u32`, `u16`, `u8` | беззнаковые 16-, ... целые числа |
| | `isize` | целые числа со знаком указателя |
| `usize` | целые беззнаковые числа с размером указателя |

См: [Rust Types](#rust-types)


### Форматирование {.row-span-2}

``rust {.wrap}
// Одиночный заполнитель
println!("{}", 1);

// Множественный плейсхолдер
println!("{} {}", 1, 3);

// Позиционные аргументы
println!("{0} - это {1} {2}, также {0} является {3} языком программирования", "Rust", "cool", "language", "safe");

// Именованные аргументы
println!("{страна} - это многообразная нация, обладающая единством.", страна = "Индия");

// Черты-заместители :b - двоичная система счисления, :0x - шестнадцатеричная система счисления, :o - восьмеричная система счисления
println!("Выведем 76 - двоичное число, которое равно {:b} , шестнадцатеричный эквивалент - {:0x} и восьмеричный эквивалент - {:o}", 76, 76, 76);

// Отладочный тракт
println!("Выведем сюда все, что хотим, используя отладочный признак {:?}", (76, 'A', 90));

// Новые строки формата в 1.58
let x = "world";
println!("Hello {x}!");
```


### Стили печати

```rust
// Печать вывода
print!("Hello World\n");

// Добавляет новую строку после печати
println!("Добавление новой строки");

// Печатается как ошибка
eprint!("Это ошибка\n");

// Печатается как ошибка с новой строкой
eprintln!("Это ошибка с новой строкой");
```


### Переменные

```rust
// Инициализация и объявление переменной
let some_variable = "This_is_a_variable";

// Делаем переменную мутабельной
let mut mutable_variable = "Mutable";

// Присвоение нескольких переменных
let (name, age) = ("ElementalX", 20);

// (Глобальная) константа
const SCREAMING_SNAKE_CASE:i64 = 9;
```



### Комментарии

``rust
// Комментарии к строкам
/*.............Block Comments */
/// Внешние комментарии к документу
//! Внутренние комментарии к документам
```
См: [Comment](https://doc.rust-lang.org/reference/comments.html)



### Функции

``rust
fn test(){
  println!("Это функция!");
}

fn main(){
  test();
}
```
См: [Функции](#rust-functions)




Типы Rust
--------------


### Integer

``rust
let mut a: u32 = 8;
let b: u64 = 877;
let c: i64 = 8999;
пусть d = -90;
```


### Плавающая точка

``rust
let mut sixty_bit_float: f64 = 89.90;
let thirty_two_bit_float: f32 = 7.90;
let just_a_float = 69.69;
```


### Boolean

```rust {.wrap}
let true_val: bool = true;
let false_val: bool = false;
let just_a_bool = true;
let is_true = 8 < 5; // => false
```


### Character

```rust
let first_letter_of_alphabet = 'a';
let explicit_char: char = 'F';
let implicit_char = '8';
let emoji = "\u{1f600}"; // => 😀
```


### Строковый литерал

```rust {.wrap}
let community_name = "AXIAL";
let no_of_members: &str = "10";

println!("Название сообщества - {имя_сообщества} и в нем {no_of_members} членов");
```
См: [Строки](#rust-strings)


### Массивы

``rust
┌─────┬─────┬─────┬─────┬─────┬─────┐
| 92 | 97 | 98 | 99 | 98 | 94 |
└─────┴─────┴─────┴─────┴─────┴─────┘
   0 1 2 3 4 5
```
----

``rust
пусть массив: [i64; 6] = [92,97,98,99,98,94];
```



### Многомерный массив {.row-span-2}

``Руст
     j0 j1 j2 j3 j4 j5
   ┌────┬────┬────┬────┬────┬────┐
i0 | 1 | 2 | 3 | 4 | 5 | 6 |
   ├────┼────┼────┼────┼────┼────┤
i1 | 6 | 5 | 4 | 3 | 2 | 1 |
   └────┴────┴────┴────┴────┴────┘
```
----

``rust
пусть массив: [[i64; 6] ;2] = [
            [1,2,3,4,5,6],
            [6,5,4,3,2,1]];
```

### Mutable Array

``rust
let mut array: [i32 ; 3] = [2,6,10];

array[1] = 4;
array[2] = 6;
```
Для того чтобы сделать его мутабельным, используйте ключевое слово `mut`.



### Slices

``rust
пусть mut array: [ i64; 4] = [1,2,3,4];
let mut slices: &[i64] = &array[0..3] // Нижний диапазон - включительно, верхний - исключительно

println!("The elements of the slices are : {slices:?}");
```


### Векторы

``Руст
пусть some_vector = vec![1,2,3,4,5];
```
Вектор объявляется с помощью макроса `vec!`.


### Кортежи

``rust
let tuple = (1, 'A' , "Cool", 78, true);
```



Строки Rust
--------------

### Строковый литерал

``rust
let cs:&str = "шпаргалка";

// => Поделиться шпаргалкой для разработчиков
println!("Поделиться {cs} для разработчиков");
```


### Строковый объект

```rust
// Создание пустого строкового объекта
let my_string = String::new;

// Преобразование в строковый объект
let S_string = a_string.to_string()

// Создание инициализированного строкового объекта
let lang = String::from("Rust");
println!("Первый язык - {lang}");
 ```

### .capacity()

 ``rust
let rand = String::from("Случайная строка");
rand.capacity() // => 13
```
Вычисляет емкость строки в байтах.


### .contains()

``rust
let name = String::from("ElementalX");
name.contains("Element") // => true
```
Проверяет, содержится ли подстрока внутри исходной строки или нет.


### Вставка одного символа

``rust
let mut half_text = String::from("Hal");
half_text.push('f'); // => Half
```


### Толкание целой строки

``rust
let mut hi = String::from("Привет...");
hi.push_str("Как дела??");

// => Привет... Как дела?
println!("{hi}");
```



Операторы Rust
-----------


### Операторы сравнения

| | |
|----------|----------------------------------|
| `e == f` | `e` равно `f` |
| `e != f` | `e` НЕ равно `f` |
| `e < f` | `e` меньше, чем `f` |
| `e > f` | `e` больше `f` |
| `e <= f` | `e` меньше или равно `f` |
| `e >= f` | `e` больше или равно `f` |

---------

``rust
пусть (e, f) = (1, 100);

let greater = f > e; // => true
let less = f < e; // => false
let greater_equal = f >= e; // => true
let less_equal = e <= f; // => true
let equal_to = e == f; // => false
let not not_equal_to = e != f; // => true
```


### Арифметические операторы

| | |
|----------|--------------------------------------------|
| `a + b` | `a` прибавляется к `b` |
| | `a - b` | `b` вычитается из `a` |
| | `a / b` | `a` делится на `b` |
| | `a % b` | Получение остатка от `a` путем деления на `b` |
| `a * b` | `a` умножается на `b` |

------

``rust {.wrap}
пусть (a, b) = (4, 5);

let sum: i32 = a + b; // => 9
let вычитание: i32 = a - b; // => -1
let умножение: i32 = a * b; // => 20
let деление: i32 = a / b; // => 0
let modulus: i32 = a % b; // => 4
```




### Побитовые операторы

| Оператор | Описание |
|----------|-------------------------|
| `g & h` | Двоичное И |
| `g | h` | Двоичное ИЛИ |
| `g ^ h` | Двоичное XOR |
| | `g ~ h` | Двоичное дополнение |
| `g << h` | Двоичный сдвиг влево |
| `g >> h` | Двоичный сдвиг вправо |

-----

``rust {.wrap}
пусть (g, h) = (0x1, 0x2);

let bitwise_and = g & h; // => 0
let bitwise_or = g | h; // => 3
let bitwise_xor = g ^ h; // => 3
let right_shift = g >> 2; // => 0
let left_shift = h << 4; // => 32
```



### Логические операторы

| Пример | Значение |
|----------------|------------------------|
| `c && d` | Оба истинны _(AND)_ |
| `c || d` | Любое из них истинно _(OR)_ |
| `!c` | `c` ложно _(NOT)_ |

------

``rust
пусть (c, d) = (true, false);

let and = c && d; // => false
let or = c || d; // => true
let not = !c; // => false
```


### Составной оператор присваивания

``Руст
let mut k = 9;
let mut l = k;
```

----

| Оператор | Описание |
|-----------|-----------------------------------------|
| `k += l` | Добавить значение и присвоить, тогда k=9 |
| `k -= l` | Вычесть значение и присвоить, тогда k=18 |
| `k /= l` | Разделить значение и присвоить, тогда k=9 |
| `k *= l` | Умножить значение и присвоить, тогда k=81 |
| `k |= l` | Побитовое ИЛИ и присвоение, тогда k=89 |





Регулятор расхода ржавчины
--------------

### Выражение If

``rust
let case1: i32 = 81;
let case2: i32 = 82;

if case1 < case2 {
  println!("case1 больше case2");
}
```

### Выражение If...Else

``Руст
let case3 = 8;
пусть case4 = 9;

if case3 >= case4 {
  println!("case3 лучше, чем case4");
} else {
  println!("case4 больше, чем case3");
}
```



### If...Else...if...Else Expression

``Руст
let foo = 12;
let bar = 13;

if foo == bar {
  println!("foo равно bar");
} else if foo < bar {
  println!("foo меньше bar");
} else if foo != bar {
  println!("foo не равно bar");
} else {
  println!("Ничего");
}
```


### Если... Пусть выражение {.row-span-3}

``rust
let mut arr1:[i64 ; 3] = [1,2,3];
if let[1,2,_] = arr1{
    println!("Работает с массивом");
}

let mut arr2:[&str; 2] = ["один", "два"];
if let["Apple", _] = arr2{
    println!("Работает и с массивом str");
}
```
----
``rust
let tuple_1 = ("Индия", 7, 90, 90.432);
if let(_, 7, 9, 78.99) = tuple_1{
    println!("Работает и с кортежами");
}

let tuple_2 = ( 9, 7, 89, 12, "Хорошо");
if let(9, 7,89, 12, blank) = tuple_2 {
    println!("Все {blank} совпало?");
}

let tuple_3 = (89, 90, "Да");
if let(9, 89, "Да") = tuple_3{
    println!("Шаблон совпал");
}
else {
    println!("Шаблон не совпал");
}
```

### Выражение соответствия {.row-span-3}

``rust
let day_of_week = 2;
match day_of_week {
  1 => {
    println!("Это понедельник, чуваки");
  },
  2 => {
    println!("Сегодня вторник, мои чуваки");
  },
  3 => {
    println!("Сегодня среда, мои чуваки");
  },
  4 => {
    println!("Сегодня четверг, мои чуваки");
  },
  5 => {
    println!("Сегодня пятница, мои чуваки");
  },
  6 => {
    println!("Сегодня суббота, мои чуваки");
  },
  7 => {
    println!("Сегодня воскресенье, мои чуваки");
  },
  _ => {
    println!("По умолчанию!")
  }
};
```


### Вложенное... выражение If

``rust
пусть nested_conditions = 89;
if nested_conditions == 89 {
    let just_a_value = 98;
    if just_a_value >= 97 {
        println!("Больше 97");
    }
}
```


### For Loop

```rust
for mut i in 0..15 {
  i-=1;
  println!("Значение i равно : {i}");
}
```



### Цикл While

``rust
let mut check = 0;
while check < 11{
  println!("Check is : {check}");
  check+=1;
  println!("После инкрементирования: {check}");

  if check == 10{
    break; // stop while
  }
}
```


### Ключевое слово Loop

``Руст
цикл {
  println!("hello world forever!");
}
```
Указанный бесконечный цикл.

### Заявление Break

``Раст
let mut i = 1;
цикл {
  println!("i равно {i}");
  if i > 100 {
    break;
  }
  i *= 2;
}
```


### Continue Statement

```rust
for (v, c) in (0..10+1).enumerate(){
  println!("Цикл перебора чисел {c}");
  if v == 9{
    println!("Продолжаем?");
    continue;
  }
  println!{"Значение v равно : {v}"}
}
```



Функции Rust
--------------


### Базовая функция

``Руст

fn print_message(){
  println!("Привет, CheatSheets.zip!");
}

fn main(){
  //Вызов функции в Rust.
  print_message();
}
```

### Передача по значению

``rust
fn main()
{
  let x:u32 = 10;
  let y:u32 = 20;
  
  // => 200
  println!("Calc: {}", cal_rect(x, y));
}
fn cal_rect(x:u32, y:u32) -> u32
{
  x * y
}
```

### Передача по ссылке

``rust
fn main(){
  let mut by_ref = 3; // => 3
  power_of_three(&mut by_ref);
  println!("{by_ref}"); // => 9
}

fn power_of_three(by_ref: &mut i32){
  // отмена ссылок важна
  *by_ref = *by_ref * *by_ref;
  println!("{by_ref}"); // => 9
}
```



### Возвраты

``rust {.wrap}
fn main(){
  let(mut radius, mut pi) = (3.0, 3.14);
  let(area, _perimeter) = calculate (
      &mut radius,
      &mut pi
  );
  println!("Площадь и периметр круга равны: {area} & {_периметр}");
}

fn calculate(radius : &mut f64, pi: &mut f64) -> (f64, f64){
  let perimeter = 2.0 * *pi * *radius;
  let area = *pi * *radius * *radius;
  return (area, perimeter);
}
```

### Массивы в качестве аргументов

``rust
fn main(){
  let mut array: [i32 ; 5] = [1,2,3,4,6];
  print_arrays(array);
  println!("Элементы: {array:?}");
}

fn print_arrays(mut array:[i32; 5]) {
  array[0] = 89;
  array[1] = 90;
  array[2] = 91;
  array[3] = 92;
  array[4] = 93;
  println!("Элементы: {array:?}");
}
```

### Возврат массивов

``rust

fn main(){
  let mut arr:[i32; 5] = [2,4,6,8,10];
  multiply(arr);
  println!("Массив равен : {:?}", multiply(arr));
}

fn multiply (mut arr: [i32 ; 5]) -> [i32 ; 5]{
  arr[2] = 90;
  for mut i in 0..5 {
      arr[i] = arr[i] * arr[2];
  }
  return arr;
}
```




Разное
--------------


### Type Casting

``Руст
let a_int = 90; // int
// int to float
let mut type_cast = (a_int as f64);
```
------
``rust
let orginal: char = 'I';
// char to int => 73
let type_casted: i64 = orginal as i64;
```

Для выполнения приведения типов в Rust необходимо использовать ключевое слово `as`.




### Заимствование

``Рост
let mut foo = 4;
let mut borrowed_foo = &foo;
println!("{borrowed_foo}");
```
------
``rust
let mut bar = 3;
let mut mutable_borrowed_bar = &mut bar;
println!("{mutable_borrowed_bar}");
```

Здесь заимствованное значение заимствует значение из значения один с помощью оператора `&`.



### Отмена ссылки

``rust
let mut borrow = 10;
let deref = &mut borrow;

println!("{}", *deref);
```

Отмена ссылок в rust может быть выполнена с помощью оператора `*`


### Область видимости переменных
``rust
{
  // Область видимости, ограниченная этой скобкой
  let a_number = 1;
}
println!("{a_number}");
```
Это приведет к ошибке, так как область видимости переменной `a_number` заканчивается на скобках


Также см.
--------

- [The Rust Document](https://doc.rust-lang.org/book/ch00-00-introduction.html) _(doc.rust-lang.org)_
- [The Rust Reference](https://doc.rust-lang.org/reference/introduction.html) _(doc.rust-lang.org)_
- [Rust Cheatsheet](https://phaiax.github.io/rust-cheatsheet/) _(phaiax.github.io)_
