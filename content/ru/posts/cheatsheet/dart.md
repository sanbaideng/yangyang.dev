---
название: Dart
дата: 2021-11-04 10:12:25
фон: bg-[#58aee9]
теги:
    - дротик
    - флаттер
категории:
  - Программирование
intro: |
    Шпаргалка по Dart, содержащая наиболее важные понятия, функции, методы и многое другое. Полный краткий справочник для начинающих.
плагины:
    - copyCode
---




Начало работы {.cols-2}
------------

### hello.dart
``dart
// функция верхнего уровня, с которой начинается выполнение приложения
void main(){
    print("Hello World!"); // Печать в консоль
}
```
Каждое приложение имеет функцию main()


### Переменные

``dart
int x = 2; // явно типизированная переменная
var p = 5; // type inferred - Generic var with type inference

dynamic z = 8; // переменная может принимать любой тип
z = "cool"; // cool

// если вы никогда не собираетесь изменять переменную, используйте final или const. Примерно так:

final email = "temid@gmail.com"; // то же, что и var, но не может быть переназначен
final String email = "temid@gmail.com"; // Вы не можете изменить значение

const qty = 5; // Константа времени компиляции
```


### Дататипы

``dart

int age = 20; // целые числа, диапазон от -2^63 до 2^63 - 1
double height = 1.85; // числа с плавающей точкой

// Можно также объявить переменную как num
num x = 1; // x может иметь значения как int, так и double
num += 2.5;
print(num); //Печать: 3.5

String name = "Nicola";

bool isFavourite = true;
bool isLoaded = false;
```


### Интерполяция строк

``dart''
// можно использовать одинарные или двойные qoutes для типа String
var FirstName = 'Nicola';
var LastName = "Tesla";

//можно встраивать переменные в строку с помощью $
String fullName = "$firstName $lastName";

// конкатенировать с +
var name = "Albert " + "Einstein";

String upperCase = '${firstName.toUpperCase()}';
print(upperCase); //Печать: НИКОЛА
```

### Комментарии
``dart
// Это обычный однострочный комментарий.

/// Это комментарий документации, используемый для документирования библиотек,
/// классов и их членов. Такие инструменты, как IDE и dartdoc, специально обрабатывают /// doc-комментарии.
/// doc-комментариям особым образом.

/* Также поддерживаются такие комментарии, как. */
```

### Импорт
``dart
// Импорт основных библиотек
import 'dart:math';

// Импорт библиотек из внешних пакетов
import 'package:test/test.dart';

// Импорт файлов
import 'path/to/my_other_file.dart';
```


Операторы {.cols-2}
------------

### Арифметические операторы
``dart
print(2 + 3); //Печать: 5
print(2 - 3); //Печать: -1
print(2 * 3); //Print: 6
print(5 / 2); //Печать: 2,5 - Результат равен двойке
print(5 ~/ 2); //Печать: 2 - Результат равен int
print(5 % 2); //Печать: 1 - Остаток

int a = 1, b;
// Инкремент
b = ++a; // preIncrement - увеличение a до того, как b получит свое значение.
b = a++; // postIncrement - увеличение a ПОСЛЕ того, как b получит свое значение.

//Decrement
b = --a; // predecrement - Уменьшение a до того, как b получит свое значение.
b = a--; // postdecrement - Уменьшение a ПОСЛЕ того, как b получит свое значение.
```


### Операторы равенства и реляционные операторы
``dart
print(2 == 2); //Печать: true - Равно
print(2 != 3); //Print: true - Не равно
print(3 > 2); //Print: true - Больше, чем
print(2 < 3); //Print: true - Меньше, чем
print(3 >= 3); //Print: true - Больше или равно
print(2 <= 3); //Print: true - Меньше или равно
```


### Логические операторы
``dart''
// !expr инвертирует выражение (меняет false на true, и наоборот)
// || логическое ИЛИ
// && логическое И
bool isOutOfStock = false;
int quantity = 3;
if (!isOutOfStock && (quantity == 2 || quantity == 3)) {
  // ...Заказать товар...
}
```




Потоки управления : Условные знаки {.cols-2}
------------


### if и else if
``дарт
if(age < 18){
    print("Подросток");
} else if( age > 18 && age <60){
    print("Взрослый");
} else {
    print("Старый");
}
```


### switch case
``dart
enum Pet {dog, cat}
Pet myPet = Pet.dog;
switch(myPet){
    case Pet.dog:
        print('Мой питомец - собака');
        break;
    case Pet.cat:
        print('Мой питомец - кошка');
        break;
    default:
        print('У меня нет домашнего животного');
}
// Prints: Мое домашнее животное - собака.
```




Потоки управления : Циклы
------------


### цикл while
``дарт
while (!dreamsAchieved) {
  workHard();
}
```
цикл while проверяет условие перед итерацией цикла

### цикл do-while
``dart
do {
  workHard();
} while (!dreamsAchieved);
```
цикл do-while проверяет условие после выполнения операторов внутри цикла

### цикл for
``dart
for(int i=0; i< 10; i++){
    print(i);
}

var numbers = [1,2,3];
// цикл for-in для списков
for(var number in numbers){
    print(number);
}
```



Коллекции {.cols-2}
------------

### Списки

``dart''
// упорядоченная группа объектов
var list = [1, 2, 3];

print(list.length); //Печать: 3
print(list[1]); //Печать: 2

// другие способы объявления и инициализации списка

List<String> cities = <String>["New York", "Mumbai", "Tokyo"];

// Для создания списка, являющегося константой времени компиляции
const constantCities = const ["New York", "Mumbai", "Tokyo"];
```


### Наборы

``dart
// Набор в Dart - это неупорядоченная коллекция уникальных элементов.
var halogens = {'fluorine', 'chlorine', 'bromine', 'iodine', 'astatine'};

// для создания пустого множества
var names = <String>{};
Set<String> names = {}; // Это тоже работает.
//var names = {}; // Создается карта, а не набор.
```


### Карты

``Дарт.
// карта - это объект, связывающий ключи и значения
var person = Map<String, String>();
// Чтобы инициализировать карту, сделайте следующее:
person['firstName'] = 'Nicola';
person['lastName'] = 'Tesla';

print(person); //Печать: {firstName: Nicola, LastName: Tesla}
print(person['lastName']); //Print: Tesla


var nobleGases = {
  // Ключ: Значение
  2: 'гелий',
  10: 'неон',
  18: 'аргон',
};
```



Функции {.cols-2}
------------

### Функции
``dart
// функции в dart являются объектами и имеют тип
int add(int a, int b){
    return a+b;
}

// функции можно присваивать переменным
int sum = add(2,3); // возвращается: 5

// могут передаваться в качестве аргументов другим функциям
int totalSum = add(2, add(2,3)); // возвращается : 7
```


### Синтаксис стрелки (=>)
``dart
// Функции, содержащие только одно выражение, можно использовать сокращенный синтаксис
bool isFav(Product product) => favProductsList.contains(product);
```

### Анонимные (лямбда) функции
``dart
// маленькие однострочные функции, не имеющие имени
int add(a,b) => a+b;

// лямбда-функции в основном передаются в качестве параметра другим функциям
const list = ['яблоки', 'бананы', 'апельсины'];
list.forEach(
(item) => print('${list.indexOf(item)}: $item'));
//Печати: 0: яблоки 1: бананы 2: апельсины
```

Классы и объекты
----------

### Класс
``dart
class Cat {
    Строковое имя;

    // метод
    void voice(){
        print("Meow");
    }
}
```


### Объект
``dart
// экземпляр класса
// ниже myCat является объектом класса Cat

void main(){
    Cat myCat = Cat();
    myCat.name = "Kitty";
    myCat.voice(); // Печатает: Meow
}
```


### Конструкторы
``dart
class Cat {
    String name;
    Cat(this.name);
}
void main(){
    Cat myCat = Cat("Kitty");
    print(myCat.name); // Печатает: Kitty
}
```


### Абстрактные классы
``dart
// Абстрактный класс - класс, который не может быть инстанцирован
// Этот класс объявлен абстрактным и поэтому не может быть инстанцирован.
abstract class AbstractContainer {
  // Определяем конструкторы, поля, методы...

  void updateChildren(); // Абстрактный метод.
}
```


### Getters Setters
``dart
// предоставляем доступ к свойствам объекта на чтение и запись
class Cat {
    String name;
    
    // геттер
    String get catName {
        return name;
    }

    // setter
    void set catName(String name){
        this.name = name;
    }
}
```


Неявные интерфейсы {.cols-2}
------------

### Базовый интерфейс
``dart''
// Человек. Неявный интерфейс содержит greet().
class Person {
  // Находится в интерфейсе, но виден только в этой библиотеке.
  final String _name;

  // Не в интерфейсе, так как это конструктор.
  Person(this._name);

  // В интерфейсе.
  String greet(String who) => 'Привет, $who. Я - $_name.';
}

// Реализация интерфейса Person.
class Impostor implements Person {
  String get _name => '';

  String greet(String who) => 'Привет $who. Ты знаешь, кто я?';
}

String greetBob(Person person) => person.greet('Bob');

void main() {
  print(greetBob(Person('Kathy'))); // Здравствуйте, Боб. Я Кэти.
  print(greetBob(Impostor())); // Привет, Боб. Знаешь ли ты, кто я?
}
```

### Расширение класса
``dart
класс Phone {

    void use(){
        _call();
        _sendMessage();
    }
}
// Использование extends для создания подкласса
class SmartPhone extends Phone {
    void use(){
        // Используйте super для обращения к суперклассу
        super.use();
        _takePhotos();
        _playGames();
    }
}
```

Исключения
------------

### Бросок
``dart''
// бросает или поднимает исключение
throw IntegerDivisionByZeroException();

// Вы также можете бросать произвольные объекты
throw "Товара нет в наличии!";
```

### Catch
``dart

try {
    int c = 3/0;
    print(c);
} on IntegerDivisionByZeroException {
    // Конкретное исключение
    print('Невозможно разделить целое число на 0.')
} on Exception catch (e) {
    // Любое другое исключение
    print('Неизвестное исключение: $e')
} catch (e) {
    // Тип не указан, обрабатывает все
    print('Что-то действительно неизвестное: $e');
}

```
### Наконец-то
``Дарт
// Чтобы обеспечить выполнение некоторого кода независимо от того, будет ли выброшено исключение или нет
try {
  cookFood();
} catch (e) {
  print('Error: $e'); // Сначала обрабатываем исключение.
} finally {
  cleanKitchen(); // Затем выполнить уборку.
}
```


Фьючерсы
------------
### Async Await
``дарт''
// функции, которые являются асинхронными: они возвращаются после выполнения возможно длительной операции
// Ключевые слова async и await поддерживают асинхронное программирование

Future<String> login() {
 String userName="Temidjoy";
 return
  Future.delayed(
    Duration(seconds: 4), () => userName);
}

// Асинхронный
main() async {
 print('Authenticating please wait...');
 print(await userName());
}
```



Разное {.cols-2}
------------

### Нуль и нулевое знание

``dart
int x; // Начальное значение любого объекта равно null

// Оператор null aware

x ??=6; // Оператор присваивания ??=, который присваивает значение переменной только в том случае, если эта переменная в данный момент равна null
print(x); //Печать: 6

x ??=3;
print(x); //Печать: 6 - результат по-прежнему равен 6

print(null ?? 10); // Печать: 10. Выведите значение слева, если оно не равно null, иначе верните значение справа
```



### Тернарный оператор
``dart
// condition ? exprIfTrue : exprIfFalse
bool isAvailable;

isAvailable ? orderproduct() : addToFavourite();
```


### Оператор спреда (...)

```dart
// для вставки нескольких значений в коллекцию.
var list = [1, 2, 3];
var list2 = [0, ...list];

print(list2.length); //Печать: 4
```

### Каскадная нотация (...)

``dart''
// позволяет выполнять последовательность операций над одним и тем же объектом

// вместо того, чтобы делать следующее
var user = User();
user.name = "Nicola";
user.email = "nicola@g.c";
user.age = 24;

// можно сделать так
var user = User()
  ..name = "Nicola"
  ..email = "nicola@g.c"
  ..age = 24;
```

### Условный доступ к свойствам
``dart
userObject?.userName

//Приведенный фрагмент кода эквивалентен следующему:
(userObject != null) ? userObject.userName : null

//Вы можете объединить несколько вариантов использования ?. в одно выражение
userObject?.userName?.toString()

// Предшествующий код возвращает null и никогда не вызывает toString(), если userObject или userObject.userName равны null
```
