---
название: Swift
дата: 2023-02-28 14:50:01
фон: bg-[#eb4e38]
теги:
    - Apple
    - iOS
    - iPadOS
категории:
    - Программирование
intro: |
    Эта шпаргалка содержит примеры использования Swift, которые охватывают базовые знания Swift, поток управления и т.д.
плагины:
    - copyCode
---




Начало работы
---



### Переменная {.row-span-2}

``swift
var score = 0 // Переменная
let pi = 3.14 // Постоянная

var greeting = "Hello"
var numberOfToys = 8
var isMorning = true

var numberOfToys: Int = 8
numberOfToys += 1

print(numberOfToys)
// печатает "9"
```



### Аннотации типов

``swift
var greeting: String = "Hello"
var NumberOfToys: Int = 8
var isMorning: Bool = true
var price: Double = 8.99
```



### Арифметические операторы {.row-span-3}

- `+` Сложение
- `-` Вычитание
- `*` Умножение
- `/` Деление
- `%` Остаток
{.cols-2 .marker-none}

----

``сдвиг
var x = 0
x = 4 + 2 // x теперь равно 6
x = 4 - 2 // x теперь равно 2
x = 4 * 2 // x теперь равно 8
x = 4 / 2 // x теперь 2
x = 4 % 2 // x теперь 0
```

----

- `+=` Складывает и присваивает суммы
- `-=` Вычитание и присваивание разности
- `*=` Умножение и присваивание
- `/=` Деление и присваивание делителя
- `%=` Деление и присваивание остатка
{.marker-none}



#### Составные операторы присваивания

``swift
var numberOfDogs = 100
numberOfDogs += 1
print("Есть \(numberOfDogs) далматинцев!")

// print: 101 далматинец!
```


### Интерполяция строк

``сдвиг
var apples = 6
print("У меня \(яблок) яблок!")

// print: У меня 6 яблок!
```



### Многострочная строка

``swift
let myLongString = """
Swift?
Это мой любимый язык!
Да!
"""
```



### Комментарии к коду

``swift
// Эта строка представляет собой комментарий в Swift.

/*
Здесь все закомментировано.
Ни один не будет запущен!
*/
```



### Формируем кортеж {.col-span-2}

``swift
let player = ("Maya", 5, 150)

print(player) // ("Maya", 5, 150)
print("\(player.0): уровень \(player.1), \(player.2) pts") // Майя: уровень 5, 150 pts
```



### Разложить кортеж

``swift
let player = (name: "Maya", level: 5)
let (currentName, curLevel) = player
print("\(currentName): level \(curLevel)")
// print: Майя: уровень 5
```



### Специальный синтаксис комментария (MARK)

``swift''
// MARK: - настройки вида
```
`MARK` может быть использован для отображения комментариев в колонке



### Специальный синтаксис комментариев (TODO)

``swift''
// TODO: обновить логику для учета изменений данных
```

`TODO` используется для отображения напоминаний о том, что необходимо сделать



### Синтаксис специальных комментариев (FIXME)

``swift''
// FIXME: Исправление ошибок при внесении изменений в существующие записи
```

`FIXME` используется для отображения напоминаний о том, что необходимо исправить




Переменная
----



### Объявление переменной

Переменные объявляются с помощью `var`:

``swift
var greeting = "Hello"
var numberOfToys = 8
var isMorning = true
```

Для наглядности объявления переменных могут содержать аннотации типов:

``swift
var greeting: String = "Hello"
var NumberOfToys: Int = 8
var isMorning: Bool = true
```

Переменные являются мутабельными. Их значения могут быть изменены:

``swift
var NumberOfToys: Int = 8
numberOfToys += 1

print(numberOfToys)
// print "9"
```



### Константы

Константы объявляются с помощью `let`:

``swift
let greeting = "Hello"
let numberOfToys = 8
let isMorning = true
```

Для наглядности объявления констант могут содержать аннотации типов:

``swift
let greeting: String = "Hello"
let NumberOfToys: Int = 8
let isMorning: Bool = true
```

Константы являются неизменяемыми. Их значения не могут быть изменены:

``swift
let NumberOfToys: Int = 8
numberOfToys += 1
// Ошибка: numberOfToys является неизменяемым
```



### Вычисляемые переменные (get и set) {.row-span-3}

``swift
импорт Foundation

let df = DateFormatter()
df.dateFormat = "d MMMM yyyy"

guard var birth = df.date(from: "5 June 1999") else {
    print("Дата не действительна")
    return
}

var age: Int {
    Calendar.current
        .dateComponents([.year],
                        from: birth,
                        to: Date()).year!
}

print(age) // 23
guard let birth2 = df.date(from: "5 июня 2002 года") else {
    print("Дата не действительна")
    return
}
birth = birth2
print(age) // 20
```

В приведенном ниже примере у distanceInFeet есть `getter` и `setter`. Из-за наличия `setter`, для `getter` требуется ключевое слово `get`:

``swift
var distanceInMeters: Float = 100

var distanceInFeet: Float {
  get {
    distanceInMeters *3.28
  }
  set(newDistance) {
    distanceInMeters = newDistance /3.28
  }
}

print(distanceInMeters) // 100.0
print(distanceInFeet) // 328.0

distanceInFeet = 250
print(distanceInMeters) // 76.21951
print(distanceInFeet) // 250.0

distanceInMeters = 800
print(distanceInMeters) // 800.0
print(distanceInFeet) // 2624.0
```



### willSet {.row-span-2}

``swift
var distance = 5 {
  willSet {
    print("Расстояние будет установлено")
  }
}

distance = 10 // print: distance will be set
```

Доступ к новому значению можно получить в `willSet`:

``swift
var distance = 5 {
  willSet(newDistance) {
    print("Расстояние будет установлено \(newDistance)")
  }
}

distance = 10 // print: расстояние будет установлено равным 10
```

`willSet` можно использовать для выполнения некоторого кода перед установкой значения переменной



### didSet

``сдвиг
var distance = 5 {
  didSet {
    print("Расстояние установлено в \(distance)")
    print("Его старое значение равно: \(oldValue)")
  }
}
distance = 10 // print: distance будет установлено в 10
              // print: его старое значение равно: 5
```



### willSet и didSet

``сдвиг
var distance = 5 {
  willSet(newDistance) {
    print("Расстояние будет установлено в \(newDistance)")
  }
  didSet {
    print("Расстояние установлено в \(расстояние)")
    print("Его старое значение равно: \(oldValue)")
  }
}
distance = 10
```

Условия
---



### оператор if

``swift
var halloween = true
if halloween {
  print("Кошелек или жизнь!")
}
// print: Кошелек или жизнь!
if 5 > 3 {
  print("5 больше 3")
} else {
  print("5 не больше 3")
}
// вывод: "5 больше 3"
```



### else statement

``swift
var turbulence = false

if turbulence {
  print("Пожалуйста, сядьте.")
} else {
  print("Вы можете свободно передвигаться.")
}
// print: Вы можете свободно передвигаться.
```



### else if statement

``swift
var погода = "дождливая"
if weather == "sunny" {
  print("Нанесите солнцезащитный крем")
} else if weather == "rainy" {
  print("Возьми зонтик")
} else if weather == "snowing" {
  print("Наденьте сапоги")
} else {
  print("Неверная погода")
}
// print: take a umbrella
```



### Операторы сравнения

``swift
5 > 1 // true
6 < 10 // true
2 >= 3 // false
3 <= 5 // true
"A" == "a" // false
"B" != "b" // true
```

-`<` меньше чем
-`>` больше
-`<=` меньше или равно
-`>=` больше или равно
-`==` равно
-`!=` не равно {.style-round cols-2}



### Тернарный условный оператор

``swift
var driverLicense = true

driverLicense
    ? print("место водителя") : print("место пассажира")
// print: водительское место
```



### оператор switch

``swift
var secondaryColor = "зеленый"

switch secondaryColor {
  case "orange":
    print("Смесь красного и желтого")
  case "purple":
    print("Смесь красного и синего")
  default:
    print("Это не может быть вторичным цветом")
}
// print: смесь синего и желтого
```



### оператор switch: согласование интервалов

``swift
пусть год = 1905
var artPeriod: String

switch year {
  case 1860...1885:
    artPeriod = "Импрессионизм"
  case 1886...1910:
    artPeriod = "Постимпрессионизм"
  default:
    artPeriod = "Unknown"
}
// print: post-impressionism
```



### оператор switch: составной случай

``swift
let service = "Seamless"

switch service {
case "Uber", "Lyft":
    print("travel")
  case "DoorDash", "Seamless", "GrubHub":
    print("Доставка ресторанов")
  case "Instacart", "FreshDirect":
    print("Доставка продуктов")
  default:
    print("Неизвестный сервис")
}
// print: ресторан на вынос
```



### оператор switch: условие where

``swift
пусть num = 7

switch num {
  case let x where x % 2 == 0:
    print("\(num) - четное")
  case let x where x % 2 == 1:
    print("\(num) нечетное число")
  по умолчанию:
    print("\(num) недействительно")
}

// print: 7 odd
```



### Логические операторы

``сдвиг
!true // false
!false //true
```
### Логические операторы &&

``сдвиг
true && true // true
true && false // false
false && true // false
false && false // false
```



### Логические операторы ||

``сдвиг
true || true // true
true || false // true
false || true // true
false || false // false
```



### Комбинированные логические операторы

``сдвиг
!false && true || false // true
```

Сначала `!false && true` оценивает и возвращает `true` Затем выражение `true` || `false` оценивает и возвращает конечный результат `true`.

``сдвиг
false || true && false // false
```
Сначала выражение `true && false` возвращает значение `false`, затем выражение `false` || `false` оценивается и возвращает конечный результат `false`.



### Управление порядком выполнения

``swift

// без круглых скобок:
true || true && false || false
//----> true

// со скобками:
(true || true) && (false || false)
//----> false

```



### Простые охранники

``swift
func greet(name: String?) {
  guard let unwrapped = name else {
    print("Hello guest!")
    return
  }
  print("Привет \(unwrapped)!")
}
greet(name: "Asma") // output: Hello Asma!
greet(name: nil) // output: Hello guest!
```

цикл
----



### scope

``сдвиг
let zeroToThree = 0...3
//zeroToThree: 0, 1, 2, 3
```



### функция stride()

``swift
for oddNum in stride(from: 1, to: 5, by: 2) {
  print(oddNum)
}
// print: 1
// print: 3
```



### цикл for-in

``swift
for char in "hehe" {
  print(char)
}
// print: h
// print: e
// print: h
// print: e
```



### продолжить ключевое слово

``swift
for num in 0...5 {
  if num % 2 == 0 {
    продолжить
  }
  print(num)
}
// print: 1
// print: 3
// print: 5
```

Ключевое слово `continue` заставит цикл продолжить работу на следующей итерации



### ключевое слово break

``swift
for char in "supercalifragilistic" {
if char == "c" {
    break
  }
  print(char)
}
// print: s
// print: u
// print: p
// print: e
// print: r
```



### Используйте символы подчеркивания

``swift
for _ in 1...3 {
  print("Ole")
}
// print: Ole
// print: Ole
// print: Ole
```



### цикл while

``сдвиг
var counter = 1
var stopNum = Int. random(in: 1...10)

while counter < stopNum {
  print(counter)
  counter += 1
}
// цикл для печати до тех пор, пока не будет выполнено условие остановки
```

Цикл `while` принимает условие и продолжает выполнять свой основной код до тех пор, пока заданное условие является `истинным`. Если условие никогда не будет ложным, то цикл продолжит выполняться, и программа застрянет в `бесконечном цикле`.

Массивы и коллекции
----



### Массив

``swift
var scores = [Int]()
// массив пуст: []
```



### Свойство .count

``swift
var grocery = ["🥓", "🥞", "🍪", "🥛", "🍊"]
print(grocery.count)
// print: 5
```



### индекс {.row-span-2}

Индекс обозначает позицию элемента в упорядоченном списке, а одиночный элемент извлекается из массива с помощью подстрочного синтаксиса `array[index]`.

``swift
var vowels = ["a", "e", "i", "o", "u"]

print(vowels[0]) // печатает: a
print(vowels[1]) // печатает: e
print(vowels[2]) // print: i
print(vowels[3]) // prints: o
print(vowels[4]) // prints: u
```

Примечание: массивы Swift имеют нулевую индексацию, то есть первый элемент имеет индекс 0.



### Инициализация с помощью литерала массива

``swift''
// используем вывод типов:
var snowfall = [2.4, 3.6, 3.4, 1.8, 0.0]
// явный тип:
var temp: [Int] = [33, 31, 30, 38, 44]
```



### Метод .append() и оператор +=

``swift
var gymBadges = ["Boulder", "Cascade"]
gymBadges.append("Thunder")
gymBadges += ["Радуга", "Душа"]
// ["Валун", "Каскад", "Гром",
// "Rainbow", "Soul"]
```



### Методы .insert() и .remove()

``swift
var moon = ["🌖", "🌗", "🌘", "🌑"]
moon.insert("🌕", at: 0)
// ["🌕", "🌖", "🌗", "🌘", "🌑"]

moon. remove(at: 4)
// ["🌕", "🌖", "🌗", "🌘"]
```



### Обход массива

``swift
var employees = ["Peter", "Denial", "Jame"]
for person in employees {
  print(person)
}
// print: Питер
// print: Отказ
// print: Jam
```



### Коллекция (набор)

``swift
var paintingsInMOMA: Set = [
  "Сон",
  "Звездная ночь",
  "Ложное зеркало"
]
```

Мы можем использовать коллекцию (`Set`) для хранения `уникальных` элементов одного и того же типа данных



### Пустая коллекция (Set)

``swift
var team = Set<String>()

print(team)
// print: []
```



### Пополнение коллекции

``swift
var vowels: Set = ["a", "e", "i", "o", "u"]
```

Чтобы создать набор, заполненный значениями, используйте ключевое слово `Set` перед оператором присваивания.



### .insert()

``swift
var cookieJar: Набор = [
  "Шоколадная крошка",
  "Овсяный изюм"
]
// добавляем новый элемент
cookieJar.insert("Peanut Butter Chip")
```



### Методы .remove() и .removeAll()

``swift
var oddNumbers: Set = [1, 2, 3, 5]

// удалить существующий элемент
oddNumbers.remove(2)
// удалить все элементы
oddNumbers.removeAll()
```

### .contains()

```swift
var names: Set = ["Rosa", "Doug", "Waldo"].
print(names.contains("Lola")) // print: false

if names.contains("Waldo"){
  print("Вот и Уолдо!")
} else {
  print("Где Уолдо?")
}
// print: There's Waldo!
```

### Итерация над коллекцией

``swift
var recipe: Набор = ["Яйцо", "Мука", "Сахар"]

for ingredient in recipe {
  print ("Включить \(ингредиент) в рецепт")
}
```



### Свойство .isEmpty

``swift
var emptySet = Set<String>()
print(emptySet.isEmpty) // print: true

var populatedSet: Set = [1, 2, 3]
print(populatedSet.isEmpty) // print: false
```

### Свойство .count

```swift
var band: Set = ["Peter", "Denial", "Jame"].

print("В группе \(band.count) игроков.")
// print: В группе 4 игрока.
```



### .intersection() Пересечение

``пересечение
var setA: Set = ["A", "B", "C", "D"]
var setB: Set = ["C", "D", "E", "F"]

var setC = setA.intersection(setB)
print(setC) // print: ["D", "C"]
```


### .union()

```swift
var setA: Set = ["A", "B", "C", "D"]
var setB: Set = ["C", "D", "E", "F"]

var setC = setA.union(setB)
print(setC)
// print: ["B", "A", "D", "F", "C", "E"]
```
### .symmetricDifference() Симметричная разность

```swift
var setA: Set = ["A", "B", "C", "D"]
var setB: Set = ["C", "D", "E", "F"]

var setC = setA.symmetricDifference(setB)
print(setC)
// print: ["B", "E", "F", "A"]
```



### .subtracting() Вычитание
```swift
var setA: Set = ["A", "B", "C", "D"]
var setB: Set = ["C", "D"]

var setC = setA.subtracting(setB)
print(setC)
// print: ["B", "A"]
```
словарь
---



### Базовый словарь

``swift
var dictionaryName = [
  "Key1": "Value1",
  "Key2": "Value2",
  "Key3": "Value3"
]
```

Неупорядоченная коллекция пар данных или пар ключ-значение



### Ключи

``swift
var fruitStand = [
  "Кокосы": 12,
  "Ананасы": 12,
  "Папайя": 12
]
```

Каждый `ключ` является `уникальным`, даже если все они содержат одно и то же `значение`.



### Согласованность типов

``swift
var NumberOfSides = [
  "triangle": 3,
  "квадрат": 4,
  "прямоугольник": 4
]
```

Содержит только ключи `String` и значения `Int`.



### Инициализация и заполнение словаря

``swift
var employeeID = [
  "Гамлет": 1367,
  "Горацио": 8261,
  "Офелия": 9318
]
```
### Инициализация пустого словаря

```swift
// Синтаксис инициализатора:
var yearlyFishPopulation = [Int: Int]()

// Синтаксис литерала пустого словаря:
var yearlyBirdPopulation: [Int: Int] = [:]
```



### добавить в словарь

``свифт
var pronunciation = [
  "library": "lai-breh-ree",
  "apple": "a-pl"
]
// новый ключ: "programming", новое значение: "prow gra"
pronunciation["programming"] = "prow-gra"
```



### Удалить пару ключ-значение {.row-span-2}

``swift
var bookShelf = [
  "Спокойной ночи": "Маргарет Уайз Браун",
  "The BFG": "Roald Dahl",
  "Falling Up": "Шел Сильверстайн",
  "Нет, Дэвид!": "David Shannon"
]
// удалить значение, установив ключ в nil
bookShelf["The BFG"] = nil

// удаляем значение с помощью функции .removeValue()
bookShelf. removeValue(forKey: "Goodnight")

// удалить все значения
bookShelf. removeAll()
```

### Модифицируем пару ключ-значение {.row-span-2}

``swift
var change = [
  "Квартал": 0.29,
  "Дайм": 0.15,
  "Никель": 0.05
]

// Изменение значения с использованием синтаксиса субскриптов
change["Quarter"] = .25

// Изменение значения с помощью функции .updateValue()
change.updateValue(.10, forKey: "Dime")
```

Для изменения значения пары ключ-значение можно воспользоваться методом `.updateValue()` или синтаксисом subscript, добавив к имени словаря скобки `[ ]` с существующими внутри ключами, затем оператор присваивания _(`= `)_, за которым следует измененное значение



### Свойство .isEmpty

``swift
var bakery = [String:Int]()

// проверяем, пуст ли словарь
print(bakery.isEmpty) // печатает true
bakery["Cupcakes"] = 12
// проверяем, пуст ли словарь
print(bakery.isEmpty) // выводит false
```
### Свойство .count

```swift
var fruitStand = [
  "Яблоки": 12,
  "Апельсины": 17
]
print(fruitStand.count) // print: 2
```



### Присвоение значений переменным

``swift
var hex = [
  "red": "#ff0000",
  "желтый": "#ffff00",
  "blue": "#0000ff",
]

print("Шестнадцатеричный код синего цвета \(hex["blue"])")
// печать: синий шестнадцатеричный код Optional("#0000ff")

if let redHex = hex["red"] {
  print("красный шестнадцатеричный код \(redHex)")
}
// print: красный шестнадцатеричный код #ff0000
```

Присвоение переменной значения пары ключ-значение возвращает опциональное значение. Для извлечения значений используйте расширение optional



### Обход словаря

``swift
var emojiMeaning = [
  "🤔": "Задумчивое лицо",
  "😪": "Сонное лицо",
  "😵": "Головокружение"
]
// перебор ключей и значений
for (emoji, meaning) in emojiMeaning {
  print("\(emoji) называется '\(meaning)Emoji'")
}
// итерация только по ключам
for emoji in emojiMeaning. keys {
  print(emoji)
}
// итерация только по значениям
for meaning in emojiMeaning. values {
  print(meaning)
}
```



функция
---



### Основные функции

``swift
func washCar() -> Void {
  print("Мыло")
  print("Скраб")
  print("Ополаскиватель")
  print("Dry")
}
```



### Вызов функций

``swift
func greetLearner() {
 print("Добро пожаловать на CheatSheets.zip!")
}
// вызов функции:
greetLearner()
// print: Welcome to CheatSheets.zip!
```



### возвращаемое значение

``swift
var birthYear = 1994
var CurrentYear = 2020

func findAge() -> Int {
  return currentYear-birthYear
}

print(findAge()) // prints: 26
```



### Множественные параметры {.col-span-2}

``swift
func convertFracToDec(numerator: Double, denominator: Double) -> Double {
  return numerator / denominator
}

let decimal = convertFracToDec(numerator: 1.0, denominator: 2.0)
print(decimal) // prints: 0.5
```



### Опустить метки параметров

``swift
func findDiff(_ a: Int, b: Int) -> Int {
  return a -b
}

print(findDiff(6, b: 4)) // prints: 2
```



### возвращает несколько значений {.col-span-2}

``swift
func smartphoneModel() -> (name: String, version: String, yearReleased: Int) {
  return ("iPhone", "8 Plus", 2017)
}
let phone = smartphoneModel()

print(phone.name) // print: iPhone
print(phone.version) // print: 8 Plus
print(phone.yearReleased) // print: 2017
```



### Параметры и аргументы

``swift
func findSquarePerimet(side: Int) -> Int {
  return side *4
}

let perimeter = findSquarePerimet(side: 5)
print(perimeter) // print: 20

// Параметр: side
// Аргумент: 5
```



### Неявный возврат
``swift
func nextTotalSolarEclipse() -> String {
  "8 апреля 2024 🌎"
}

print(nextTotalSolarEclipse())
// print: 8 апреля 2024 года 🌎
```


### Параметры по умолчанию

```swift
func greet(person: String = "guest") {
  print("Привет \(person)")
}
greet() // Здравствуй гость
greet(person: "Aliya") // Hello Aliya
```



### Входные и выходные параметры {.row-span-2}

``swift
var CurrentSeason = "Зима"

func season(month: Int, name: inout String) {
  switch month {
    case 1...2:
      name = "Winter ⛄️"
    case 3...6:
      name = "Весна 🌱"
    case 7...9:
      name = "Лето ⛱"
    case 10...11:
      name = "Осень 🍂"
    default:
      name = "Unknown"
  }
}
season(month: 4, name: &currentSeason)

print(currentSeason) // Весна 🌱
```



### переменная параметр

``swift
func totalStudent(data: String...) -> Int {
  let numStudents = data.count
  return numStudents
}

print(totalStudent(data: "Отказ", "Петр"))
// print: 2
```



### Необязательные параметры

``swift
func getFirstInitial(from name: String?) -> String? {
  return name?.first
}
```

Функции могут принимать необязательные типы и возвращать необязательные типы. Если функция не может вернуть разумный экземпляр запрашиваемого типа, она должна возвращать `nil`.

структура
----



### Создание структуры

``swift
struct Building {
  var адрес: String
  var этажи: Int
  init(address: String, floors: Int) {
    self.address = address
    self.floors = floors
  }
}
```

Структуры или structs используются для программного представления реальных объектов в коде. Структура создается с помощью ключевого слова `struct`, за которым следует ее имя, а затем тело, содержащее ее свойства и методы



### Значения свойств по умолчанию

``swift
struct Car {
  var numOfWheels = 4
  var topSpeed = 80
}

var reliantRobin = Car(numOfWheels: 3)

print(reliantRobin.numOfWheels) // prints: 3
print(reliantRobin.topSpeed) // print: 80
```



### Создание структурного экземпляра

``swift
struct Person {
  var name: String
  var возраст: Int

  init(name: String, age: Int) {
    self.name = name
    self.age = age
  }
}

// Экземпляр Person:
var morty = Person(name: "Peter", age: 14)
```

### init() метод {.row-span-2}

``swift
struct TV {
  var size: Int
  var type: String
  
  init(size: Int, type: String) {
    self.size = size
    self.type = type
  }
}
```

Использование класса `TV`

``swift
var newTV = TV(size: 65, type: "LED")
```



### Проверка типа

``swift
print(type(of: "abc")) // print: Строка
print(type(of: 123)) // print: 123
```



### Метод мутации (mutating) {.row-span-2}

``сдвиг
struct Menu {
  var menuItems = ["Картофель фри", "Бургеры"]
  mutating func addToMenu(dish: String) {
    self.menuItems.append(dish)
  }
}
```

Использование класса `Menu`

``swift
var dinerMenu = Menu()
dinerMenu.addToMenu(dish: "Toast")
print(dinerMenu.menuItems)
// prints: ["Картофель фри", "Бургеры", "Тост"]
```



### Структурные методы

``свифт
struct Dog {
  func bark() {
    print("Гав")
  }
}
let fido = Dog()
fido.bark() // prints: Гав
```

класс
----



### ссылочный тип (класс) {.row-span-2}

``swift
class Player {
  var name: String

  init(name: String) {
    self.name = name
  }
}

var player1 = Player(name: "Tomoko")
var player2 = player1
player2.name = "Isabella"

print(player1.name) // Изабелла
print(player2.name) // Isabella
```



### экземпляр класса

``swift
class Person {
  var name = ""
  var age = 0
}

var sonny = Person()
// sonny теперь является экземпляром Person
```



### init() метод {.row-span-2}

``swift
класс Fruit {
  var hasSeeds = true
  var color: String

  init(color: String) {
    self.color = color
  }
}
```

Использование класса Fruit

``swift
let apple = Fruit(color: "red")
```
Инициализация класса может быть выполнена с помощью метода `init()` и соответствующих свойств инициализации. В методе `init()` ключевое слово `self` используется для ссылки на реальный экземпляр класса, присваивающий значения свойствам



### Атрибуты класса

``swift
var ferris = Student()

ferris.name = "Феррис Бюллер"
ferris.year = 12
ferris.gpa = 3.81
ferris.honors = false
```



### Наследуем {.row-span-2}

Предположим, что у нас есть класс BankAccount:

``swift
class BankAccount {
  var balance = 0.0
  func deposit(amount: Double) {
    balance += amount
  }
  func withdraw(amount: Double) {
    баланс -= сумма
  }
}
```

Класс `SavingsAccount` расширяет класс `BankAccount`.

``swift
класс SavingsAccount: BankAccount {
  varinterest = 0.0

  func addInterest() {
    let interest = balance *0.005
    self. deposit(amount: interest)
  }
}
```

Новый класс `SavingsAccount` (подкласс) автоматически получает все характеристики класса `BankAccount` (суперкласс). Кроме того, класс `SavingsAccount` определяет свойство `.interest` и метод `.addInterest()`.



### Пример

использовать тип данных

``swift
класс Студент {
  var name: String
  var year: Int
  var gpa: Double
  var honors: Bool
}
```

Использование значений свойств по умолчанию

``swift
class Student {
  var name = ""
  var gpa = 0.0
  var honors = false
}
```
### Это пример определения структуры и класса

``swift
struct Resolution {
  var width = 0
  var height = 0
}
class VideoMode {
  var resolution = Resolution()
  var interlaced = false
  var frameRate = 0.0
  var name: String?
}
```

Определение структуры `Resolution` и определение класса `VideoMode` описывают только внешний вид `Resolution` или `VideoMode`, создать экземпляр структуры или класса невозможно:

``swift
let resolution = Resolution(width: 1920)
let someVideoMode = VideoMode()
```


Перечислить
----



### Определите перечисление

``swift
enum Day {
  случай понедельник
  случай вторник
  случай среда
  четверг
  случай пятница
  суббота
  случай воскресенья
}

let casualWorkday: Day = .friday
```



### Оператор переключения

``swift
enum Dessert {
  case cake(flavor: String)
  case vanillaIceCream(scoops: Int)
  case brownie
}

let customerOrder: Dessert = .cake(flavor: "Red Velvet")
switch customerOrder {
  case let .cake(flavor):
    print("Вы заказали торт \(вкус)")
  case .brownie:
    print("Вы заказали шоколадный торт")
}
// prints: "Вы заказали торт "Красный бархат""
```



### CaseIterable

``swift
enum Season: CaseIterable {
  случай зима
  случай весна
  лето
  случай осень
}

for season in Season.allCases {
  print(season)
}
```

Добавляем соответствие протоколу `CaseIterable` для доступа к свойству `allCases`, которое возвращает массив всех случаев перечисления



### Оригинальное значение

``swift
enum Beatle: String {
  case john paul george ringo
}

print("The Beatles - это \(Beatle.john.rawValue).")
// print: The Beatles is john.
```



### Связанные значения

``swift
enum Dessert {
  case cake(flavor: String)
  case vanillaIceCream(scoops: Int)
  case brownie
}

let order: Dessert = .cake(flavor: "Red Velvet")
```



### метод экземпляра {.row-span-2}

``swift
enum Traffic {
  лёгкий
  тяжёлый

  mutating func reportAccident() {
    self = .heavy
  }
}

var currentTraffic: Traffic = .light

currentTraffic. reportAccident()
// currentTraffic теперь .heavy
```

Как и классы и структуры, перечисления могут иметь методы экземпляра. Если метод экземпляра изменяет значение перечисления, то он должен быть помечен как `mutating`.



### Инициализация из примитивного значения

``swift
enum Hello: String {
  case english = "Hello"
  case japanese = "Hello!"
  case emoji = "👋"
}
let hello1 = Hello(rawValue: "Привет!")
let hello2 = Hello(rawValue: "Привет")
print(hello1) // Optional(Hello.japanese)
print(hello2) // nil
```



### Вычисленные свойства

``swift
enum ShirtSize: String {
  case small = "S"
  case medium = "M"
  case large = "L"
  case extraLarge = "XL"
  var description: String {
    return "Размер этой рубашки \(self.rawValue)"
  }
}
```

Также см.
----

- [Swift Documentation (Official)](https://www.swift.org/documentation/) _(swift.or)_
- [Язык программирования Swift (официальный)](https://docs.swift.org/swift-book/) _(swift.or)_
- [One-Stop Quick Reference for Swift Developers](https://swiftly.dev/) _(swiftly.dev)_
