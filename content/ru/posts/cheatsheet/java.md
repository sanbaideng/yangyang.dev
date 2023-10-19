---
название: Java
дата: 2021-03-10 19:50:01
фон: bg-[#d33731]
тэги:
    - объектно-ориентированный
    - класс
категории:
    - Программирование
введение
    Эта шпаргалка представляет собой краш-курс для начинающих программистов на Java и помогает рассмотреть основной синтаксис языка Java.
плагины:
    - tooltip
    - copyCode
---


Начало работы
--------

### Hello.java {.row-span-2}
``java
public class Hello {
  // метод main
  public static void main(String[] args)
  {
    // Выходные данные: Hello, world!
    System.out.println("Hello, world!");
  }
}
```
Компиляция и запуск
````shell скрипт
$ javac Hello.java
$ java Hello
Привет, мир!
```



### Переменные
``java
int num = 5;
float floatNum = 5.99f;
char letter = 'D';
boolean bool = true;
String site = "cheatsheets.zip";
```

### Примитивные типы данных {.row-span-2}
| Тип данных | Размер | По умолчанию | Диапазон |.
|-----------|--------|---------|---------------------|
| `byte` | 1 байт | 0 | -128 ^to^ 127 |
| `short` | 2 байта | 0 | -2^15^to^ 2^15^-1 |
| `int` | 4 байта | 0 | -2^31^to^ 2^31^-1 |
| `long` | 8 байт | 0 | -2^63^^to^ 2^63^-1 |
| `float` | 4 байта | 0.0f | _N/A_ |
| `double` | 8 байт | 0.0d | _N/A_ |
| `char` | 2 байта | 0 ^to^ 65535 |
| `boolean` | _N/A_ | false | true / false |
{.show-header}




### Строки
``java
String first = "John"
String last = "Doe";
String name = first + " " + last;
System.out.println(name);
```
Смотрите: [Strings](#java strings)




### Циклы
````java
String word = "Шпаргалки";
for (char c: word.toCharArray()) {
  System.out.print(c + "-");
}
// Выходные данные: c-h-e-a-t-S-h-e-t-s-.
```
Смотрите: [Loops](#java-loops)


### Массивы
````java
char[] chars = new char[10];
chars[0] = 'a'
chars[1] = 'b'

String[] letters = {'A', 'B', 'C'};
int[] mylist = {100, 200};
boolean[] answers = {true, false};
```
Смотрите: [Массивы](#java массивы)


### Swap
````java
int a = 1;
int b = 2;
System.out.println(a + " " + b); // 1 2

int temp = a;
a = b;
b = temp;
System.out.println(a + " " + b); // 2 1
```

### Кастинг типов
``java
// Расширение
// byte<short<int<long<float<double
int i = 10;
long l = i; // 10

// Сужение
double d = 10.02;
long l = (long)d; // 10

String.valueOf(10); // "10"
Integer.parseInt("10"); // 10
Double.parseDouble("10"); // 10.0
```

### Conditionals
````java
int j = 10;

if (j == 10) {
  System.out.println("Меня печатают");
} else if (j > 10) {
  System.out.println("Меня не печатают");
} else {
  System.out.println("Я тоже не печатаюсь");
}
```
Смотрите: [Conditionals](#java-conditionals)



### Пользовательский ввод
``java
Scanner in = new Scanner(System.in);
String str = in.nextLine();
System.out.println(str);

int num = in.nextInt();
System.out.println(num);
```

Строки Java
-------

### Базовый

````java
String str1 = "value";
String str2 = new String("value");
String str3 = String.valueOf(123);
```


### Конкатенация
````java
String s = 3 + "str" + 3; // 3str3
String s = 3 + 3 + "str"; // 6str
String s = "3" + 3 + "str"; // 33str
String s = "3" + "3" + "23"; // 3323
String s = "" + 3 + 3 + "23"; // 3323
String s = 3 + 3 + 23; // 29
```


### StringBuilder {.row-span-3}
StringBuilder sb = new StringBuilder(10);
``java
┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
| | | | | | | | | |
└───┴───┴───┴───┴───┴───┴───┴───┴───┘
0 1 2 3 4 5 6 7 8 9
```
sb.append("QuickRef");
```java
┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
| Q | u | i | c | k | R | e | f | f
└───┴───┴───┴───┴───┴───┴───┴───┴───┘
0 1 2 3 4 5 6 7 8 9
```
sb.delete(5, 9);
``java
┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
| Q | u | i | c | k | | | | |
└───┴───┴───┴───┴───┴───┴───┴───┴───┘
0 1 2 3 4 5 6 7 8 9
```
sb.insert(0, "My ");
``java
┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
| M | y | Q | u | i | c | k |
└───┴───┴───┴───┴───┴───┴───┴───┴───┘
0 1 2 3 4 5 6 7 8 9
```
sb.append("!");
``java
┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
| M | y | Q | u | i | c | k | ! |
└───┴───┴───┴───┴───┴───┴───┴───┴───┘
0 1 2 3 4 5 6 7 8 9
```


### Сравнение
````java
String s1 = new String("QuickRef");
String s2 = new String("QuickRef");

s1 == s2 // false
s1.equals(s2) // true

"AB".equalsIgnoreCase("ab") // true
```


### Манипуляция
````java
String str = "Abcd";

str.toUpperCase(); // ABCD
str.toLowerCase(); // abcd
str.concat("#"); // Abcd#
str.replace("b", "-"); // A-cd

" abc ".trim(); // abc
"ab".toCharArray(); // {'a', 'b'}
```


### Информация
```java
String str = "abcd";

str.charAt(2); // c
str.indexOf("a") // 0
str.indexOf("z") // -1
str.length(); // 4
str.toString(); // abcd
str.substring(2); // cd
str.substring(2,3); // c
str.contains("c"); // true
str.endsWith("d"); // true
str.startsWith("a"); // true
str.isEmpty(); // false
```



### Неизменяемый
````java
String str = "hello";
str.concat("world");

// Выходные данные: hello
System.out.println(str);
```

---

````java
String str = "hello";
String concat = str.concat("world");

// Выходные данные: helloworld
System.out.println(concat);
```

Созданный однажды String не может быть изменен, любая модификация создает новый String




Массивы Java
-------


### Объявление
``java
int[] a1;
int[] a2 = {1, 2, 3};
int[] a3 = new int[]{1, 2, 3};

int[] a4 = new int[3];
a4[0] = 1;
a4[2] = 2;
a4[3] = 3;
```


### Модификация
``java
int[] a = {1, 2, 3};
System.out.println(a[0]); // 1

a[0] = 9;
System.out.println(a[0]); // 9

System.out.println(a.length); // 3
```


### Цикл (чтение и изменение)
``java
int[] arr = {1, 2, 3};
for (int i=0; i < arr.length; i++) {
    arr[i] = arr[i] * 2;
    System.out.print(arr[i] + " ");
}
// Выходные данные: 2 4 6
```


### Цикл (чтение)
``java
String[] arr = {"a", "b", "c"};
for (int a: arr) {
    System.out.print(a + " ");
}
// Выходные данные: a b c
```


### Многомерные массивы
``java
int[][] matrix = { {1, 2, 3}, {4, 5} };

int x = matrix[1][0]; // 4
// [[1, 2, 3], [4, 5]]
Arrays.deepToString(matrix)

for (int i = 0; i < a.length; ++i) {
  for (int j = 0; j < a[i].length; ++j) {
    System.out.println(a[i][j]);
  }
}
// Выходные данные: 1 2 3 4 5 6 7
```


### Сортировка
``java
char[] chars = {'b', 'a', 'c'};
Arrays.sort(chars);

// [a, b, c]
Arrays.toString(chars);
```




Java Conditionals
-----------


### Операторы {.row-span-2}
- <a href="javascript:void(0);" data-tooltip="Оператор сложения (также используется для конкатенации строк)">+</a>
- <a href="javascript:void(0);" data-tooltip="Оператор вычитания">-</a>
- <a href="javascript:void(0);" data-tooltip="Оператор умножения">*</a>
- <a href="javascript:void(0);" data-tooltip="Оператор деления">/</a>
- <a href="javascript:void(0);" data-tooltip="Оператор остатка">%</a>
- <a href="javascript:void(0);" data-tooltip="Простой оператор присваивания">=</a>
- <a href="javascript:void(0);" data-tooltip="Оператор инкремента; увеличивает значение на 1">++</a>
- <a href="javascript:void(0);" data-tooltip="Оператор Decrement; уменьшает значение на 1">--</a>
- <a href="javascript:void(0);" data-tooltip="Оператор логического дополнения; инвертирует значение булевой величины">!</a>
{.marker-none .cols-4}

----

- <a href="javascript:void(0);" data-tooltip="Равносильно">==</a>
- <a href="javascript:void(0);" data-tooltip="Не равно">!=</a>
- <a href="javascript:void(0);" data-tooltip="Больше, чем">></a>
- <a href="javascript:void(0);" data-tooltip="Больше или равно">>=</a>
- <a href="javascript:void(0);" data-tooltip="Меньше, чем"><</a>
- <a href="javascript:void(0);" data-tooltip="Меньше или равно"><=</a>
{.marker-none .cols-4}

----

- <a href="javascript:void(0);" data-tooltip="Conditional-AND">&&</a>
- <a href="javascript:void(0);" data-tooltip="Conditional-OR">||</a>
- [?:](#ternary-operator){data-tooltip="Тернарный (сокращение для оператора if-then-else)"}
{.marker-none .cols-4}

----

- <a href="javascript:void(0);" data-tooltip="Сравнивает объект с заданным типом">instanceof</a>
{.marker-none}

----

- <a href="javascript:void(0);" data-tooltip="Унарное побитовое дополнение">~</a>
- <a href="javascript:void(0);" data-tooltip="Подписанный сдвиг влево"><<</a>
- <a href="javascript:void(0);" data-tooltip="Знаковый сдвиг вправо">>></a>
- <a href="javascript:void(0);" data-tooltip="Беззнаковый сдвиг вправо">>>></a>
- <a href="javascript:void(0);" data-tooltip="Побитовое И">&</a>
- <a href="javascript:void(0);" data-tooltip="Побитовое исключающее ИЛИ">^</a>
- <a href="javascript:void(0);" data-tooltip="Побитовое исключающее ИЛИ">|</a>
{.marker-none .cols-4}


### If else
``java
int k = 15;
if (k > 20) {
  System.out.println(1);
} else if (k > 10) {
  System.out.println(2);
} else {
  System.out.println(3);
}
```

### Переключатель {.row-span-2}
``java
int month = 3;
String str;
switch (month) {
  case 1:
    str = "Январь";
    break;
  case 2:
    str = "февраль";
    break;
  case 3:
    str = "Март";
    break;
  default:
    str = "Какой-то другой месяц";
    break;
}

// Выходные данные: Результат Март
System.out.println("Результат " + str);
```


### Тернарный оператор
```java
int a = 10;
int b = 20;
int max = (a > b) ? a : b;

// Выходные данные: 20
System.out.println(max);
```


Циклы Java
----

##### Цикл For Loop
``java
for (int i = 0; i < 10; i++) {
  System.out.print(i);
}
// Выходные данные: 0123456789
```

------

``java
for (int i = 0,j = 0; i < 3; i++,j--) {
  System.out.print(j + "|" + i + " ");
}
// Выходные данные: 0|0 -1|1 -2|2
```

### Усовершенствованный цикл For Loop
``java
int[] numbers = {1,2,3,4,5};

for (int number: numbers) {
  System.out.print(number);
}
// Выходные данные: 12345
```
Используется для обхода массивов или списков


##### Цикл While
``java
int count = 0;

while (count < 5) {
  System.out.print(count);
  count++;
}
// Выходные данные: 01234
```

##### Цикл Do While
````java
int count = 0;

do {
  System.out.print(count);
  count++;
} while (count < 5);
// Выходные данные: 01234
```

### Continue Statement
```java
for (int i = 0; i < 5; i++) {
  if (i == 3) {
    continue;
  }
  System.out.print(i);
}
// Выходные данные: 01245
```

### Break Statement
````java
for (int i = 0; i < 5; i++) {
  System.out.print(i);
  if (i == 3) {
    break;
  }
}
// Выходные данные: 0123
```

Java Collections Framework
--------------------

### Java Collections {.col-span-2}

| Коллекция | Интерфейс | Упорядоченный | Сортированный | Потокобезопасный | Дублирующий | Нулевой
|--------------------------------------------------------------------------------------------------------------------|-------------|---------|--------|-------------|-----------|--------------------|
| [ArrayList](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html) | List | Y | _N_ | Y | | Y
| [Vector](https://docs.oracle.com/javase/8/docs/api/java/util/Vector.html) | List | Y | _N_ | Y | Y
| [LinkedList](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html) | List, Deque | Y | _N_ | Y | Y
| [CopyOnWriteArrayList](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CopyOnWriteArrayList.html) | Список | Y | _N_ | Y | Y | Y
| [HashSet](https://docs.oracle.com/javase/8/docs/api/java/util/HashSet.html) | Набор | _N_ | _N_ | _N_ | Один `null` |
| [LinkedHashSet](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedHashSet.html) | Set | Y | _N_ | _N_ | _N_ | One `null` |
| [TreeSet](https://docs.oracle.com/javase/8/docs/api/java/util/TreeSet.html) | Set | Y | _N_ | _N_ | _N_ | _N_.
| [CopyOnWriteArraySet](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CopyOnWriteArraySet.html) | Set | Y | _N_ | _N_ | Один `null` |
| [ConcurrentSkipListSet](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentSkipListSet.html) | Set | Y | Y | _N_ | _N_ | _N_ | _N_
| [HashMap](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html) | Map | _N_ | _N_ | _N (key)_ | One `null` _(key)_ |
| [HashTable](https://docs.oracle.com/javase/8/docs/api/java/util/Hashtable.html) | Map | _N_ | _N_ | _N (key)_ | _N (key)_
| [LinkedHashMap](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedHashMap.html) | Map | Y | _N_ | _N (key)_ | One `null` _(key)_ |
| [TreeMap](https://docs.oracle.com/javase/8/docs/api/java/util/TreeMap.html) | Map | Y | _N_ | _N (ключ)_ | _N (ключ)_ |
| [ConcurrentHashMap](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html) | Map | _N_ | Y | _N (key)_ | _N_ |
| [ConcurrentSkipListMap](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentSkipListMap.html) | Map | Y | Y | _N (key)_ | _N_ |
| [ArrayDeque](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayDeque.html) | Deque | Y | _N_ | Y | _N_ | _N_.
| [PriorityQueue](https://docs.oracle.com/javase/8/docs/api/java/util/PriorityQueue.html) | Очередь | Y | _N_ | _N_ | Y | _N_ | _N_.
| [ConcurrentLinkedQueue](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentLinkedQueue.html) | Очередь | Y | _N_ | Y | _N_ | _N_.
| [ConcurrentLinkedDeque](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentLinkedDeque.html) | Deque | Y | _N_ | Y | _N_ | Y.
| [ArrayBlockingQueue](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ArrayBlockingQueue.html) | Queue | Y | _N_ | Y | _N_ | _N_.
| [LinkedBlockingDeque](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/LinkedBlockingDeque.html) | Deque | Y | _N_ | Y | _N_ | Y
| [PriorityBlockingQueue](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/PriorityBlockingQueue.html) | Queue | Y | _N_ | Y | Y | _N_ | Y | _N_ |
{.show-header .left-text}


### ArrayList
``java
List<Integer> nums = new ArrayList<>();

// Добавление
nums.add(2);
nums.add(5);
nums.add(8);

// Извлечение
System.out.println(nums.get(0));

// Индексирование для итерации цикла
for (int i = 0; i < nums.size(); i++) {
    System.out.println(nums.get(i));
}

nums.remove(nums.size() - 1);
nums.remove(0); // ОЧЕНЬ медленно

for (Integer value : nums) {
    System.out.println(value);
}
```

### HashMap
``java
Map<Integer, String> m = new HashMap<>();
m.put(5, "Пять");
m.put(8, "Восемь");
m.put(6, "Шесть");
m.put(4, "Четыре");
m.put(2, "Два");

// Получение
System.out.println(m.get(6));

// Лямбда forEach
m.forEach((key, value) -> {
    String msg = key + ": " + value;
    System.out.println(msg);
});
```

### HashSet
```java
Set<String> set = new HashSet<>();
if (set.isEmpty()) {
    System.out.println("Пусто!");
}

set.add("собака");
set.add("кошка");
set.add("мышь");
set.add("змея");
set.add("медведь");

if (set.contains("cat")) {
    System.out.println("Содержит кошку");
}

set.remove("cat");
for (String element : set) {
    System.out.println(element);
}
```

### ArrayDeque
``java
Deque<String> a = new ArrayDeque<>();

// Использование функции add()
a.add("Dog");

// Использование addFirst()
a.addFirst("Cat");

// Использование addLast()
a.addLast("Лошадь");

// [Cat, Dog, Horse].
System.out.println(a);

// Элемент доступа
System.out.println(a.peek());

// Удалить элемент
System.out.println(a.pop());
```

Misc
----


### Модификаторы доступа {.col-span-2}
| Модификатор | Класс | Пакет | Подкласс | Мир |
|-------------|-------|---------|----------|-------|
| public | Y | Y
protected | protected | Y | Y | _N_ | Y
| без модификатора | Y | _N_ | _N_
| private | Y | _N_ | _N_
{.show-header .left-text}


### Регулярные выражения
``java
String text = "Я изучаю Java";
// Удаление всех пробелов
text.replaceAll("Я изучаю Java+", "");

// Разделение строки
text.split("|");
text.split(Pattern.quote("|"));
```
Смотрите: [Regex в java](/regex#regex-in-java)



### Комментарий
``java
// Я - однострочный комментарий!
 
/*
А я
многострочный комментарий!
*/

/**
 * Это
 * это
 * документация
 * комментарий
 */
```

### Ключевые слова {.col-span-2}
- абстрактный
- продолжать
- для
- новый
- переключатель
- утверждать
- по умолчанию
- переходить
- пакет
- синхронизированный
- логический
- делать
- if
- частный
- this
- break
- двойной
- реализация
- защищённый
- бросок
- байт
- else
- импорт
- public
- броски
- case
- перечисление
- instanceof
- возврат
- переходный
- catch
- extends
- int
- короткий
- try
- char
- final
- интерфейс
- статический
- пустота
- класс
- наконец
- long
- strictfp
- летучий
- const
- float
- родной
- супер
- while
{.marker-none .cols-6}

### Математические методы

| Метод | Описание
|-----------------------|------------------------|
| `Math.max(a,b)` |Максимум из a и b |Максимум из a и b |Max.min(a,b)|Макс.
| | `Math.min(a,b)` |Минимум из a и b | | |Math.abs(a,b)|| из a и b
| | `Math.abs(a)` | Абсолютное значение a
| | `Math.sqrt(a)` | Квадратный корень из a
| | `Math.pow(a,b)` | Мощность b | Мощность b
| | `Math.round(a)` | Ближайшее целое число |
| `Math.sin(ang)` | Синус угла
| | `Math.cos(ang)` | Косинус угла
| | `Math.tan(ang)` | Тангенс угла
| | `Math.asin(ang)` | Обратный синус угла
| `Math.log(a)` | Натуральный логарифм от a
| | `Math.toDegrees(rad)` | Угол rad в градусах
| `Math.toRadians(deg)` | Угол deg в радианах |

### Try/Catch/Finally
``java
try {
  // что-то
} catch (Exception e) {
  e.printStackTrace();
} finally {
  System.out.println("всегда печатается");
}
```
