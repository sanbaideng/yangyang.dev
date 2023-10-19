---
Название: Kotlin
дата: 2023-02-26 16:24:31
фон: bg-[#7954f6]
тэги:
  - Кроссплатформенность
  - Android
категории:
  - Программирование
intro: |
  Краткая справочная шпаргалка по Kotlin, включающая использование, примеры и многое другое.
плагины:
    - copyCode
---


Введение в Kotlin
----



### main()

``котлин
fun main() {
  println("Приветствую тебя, CheatSheets.zip!")
  // Код находится здесь
}
```

Функция main() является начальной точкой каждой Kotlin-программы и должна быть включена в код перед выполнением



### Оператор печати

``котлин
println("Приветствую тебя, землянин!")
print("Отведите меня к ")
print("К своему лидеру").

/*
Печать:
Приветствую тебя, землянин!
Отведи меня к своему лидеру.
*/
```



### Примечания

``котлин''
// это однострочный комментарий

/*
это
примечание
для
многих
*/
```



### Порядок выполнения

``котлин
fun main() {
  println("Я буду напечатан первым.")
  println("Я буду напечатан вторым.")
  println("Я буду напечатан третьим.")
}
```

Типы данных и переменные
---



### Переменные с возможностью изменения

``котлин
var age = 25
возраст = 26
```



### Неизменяемые переменные

``котлин
val goldenRatio = 1.618
```



### Вывод типа

``котлин''
// Следующим переменным присваивается буквальное значение внутри двойных кавычек
// поэтому выводимый тип - String

var color = "Purple"
```



### Конкатенация строк

``kotlin
var streetAddress = "123 Main St."
var cityState = "Brooklyn, NY"

println(streetAddress + " " + cityState)
// Печать: 123 Main St. Brooklyn, NY
```



### Шаблоны строк

``kotlin
var address = "123 Main St."
println("The address is $address")
// prints: Адрес - 123 Main St.
```



### Встроенные свойства и функции
``котлин
var monument = "Статуя Свободы"

println(monument. capitalize())
// print: Статуя Свободы
println(monument. length)
// print: 21
```



### Вывод символов {.row-span-2}

``kotlin {.wrap}
print("\"Превосходно!\" я заплакал.\"Элементарно,\" сказал он.")

// Печать: "Превосходно!" Я заплакал. "Элементарно", - сказал он.
```

- `\n` вставить новую строку
- `\t` вставляет табуляцию
- `\r` вставляет возврат каретки
- `\'`вставляет одинарную кавычку
- `\``вставляет двойную кавычку
- `\\\\` вставляет обратную косую черту
- `\$` вставляет знак доллара



### Арифметические операторы

``котлин
5 + 7 // 12
9 -2 // 7
8 *4 // 32
25 /5 // 5
31 % 2 // 1
```

`+` сложение, `-` вычитание, `*` умножение, `/` деление и `%` модуль



### Порядок выполнения операций

``котлин
5 + 8 *2 /4 -3 // 6
3 + (4 + 4) /2 // 7
4 *2 + 1 *7 // 15
3 + 18 /2 *1 // 12
6 -3 % 2 + 2 // 7
```



### Улучшенный оператор присваивания

``kotlin
var BatteryPercentage = 80

// длинный синтаксис
batteryPercentage = batteryPercantage + 10

// короткий синтаксис с дополненным оператором присваивания
batteryPercentage += 10
```



### Операторы инкремента и декремента

``котлин
var year = 2019
год++ // 2020
год-- // 2019
```



### Математическая библиотека

``kotlin
Math.pow(2.0, 3.0) // 8.0
Math.min(6, 9) // 6
Math.max(10, 12) // 12
Math. round(13.7) // 14
```





Условное выражение
----


### Выражение If

``котлин
var утро = true

if (morning) {
  println("Проснись и пой!")
}
// Печать: Проснись и пой!
```



### Else-expression

``котлин
var rained = false

if (rained) {
  println("Сегодня не нужно поливать растения.")
} else {
  println("Растение нужно полить!")
}
// print: Растение нужно полить!
```



### Выражения Else-If

``котлин
var возраст = 65

if (age < 18 ) {
  println("Вы считаетесь несовершеннолетним")
} else if (age < 60) {
  println("Вы считаетесь совершеннолетним")
} else {
  println("Вы считаетесь пенсионером")
}

// print: you are considered senior
```



### Операторы сравнения

``котлин
var myAge = 19
var sisterAge = 11
var cousinAge = 11

myAge > sisterAge // true
myAge < cousinAge // false
myAge >= cousinAge // true
myAge <= sisterAge // false
```



### Логические операторы

``котлин
var влажно = true
var дождь = true
var куртка = false

println(!humid)
// print: false
println(jacket && raining)
// print: true
println(humid || raining)
// print: true
```



### Оператор AND: &&

``kotlin
var влажно = true
var дождь = true
var шорты = false
var sunny = false

// true И true
println(humid && raining) // true
// true AND false
println(humid && shorts) // false
// false AND true
println(sunny && raining) // false
// false И false
println(shorts && sunny) // false
```



### Оператор Or:||

``kotlin
var late = true
var skipBreakfast = true
var underslept = false
var checkEmails = false

// true ИЛИ true
println(skipBreakfast || late) // true
// true ИЛИ false
println(late || checkEmails) // true
// ложно ИЛИ истинно
println(underslept || late) // true
// false ИЛИ false
println(checkEmails || underslept) // false
```



### оператор NOT

``котлин
var hungry = true
var сытый = false

println(!hungry) // false
println(!full) // true
```



### Порядок оценки

``kotlin
!true && (false || true) // false
/*
(false || true) сначала оценивается, чтобы вернуть true.
Затем выполняется оценка !true && true и возвращается конечный результат false
*/

!false && true || false // true
/*
Сначала выполняется оценка !false, которая возвращает true.
Затем выполняется оценка true && true, возвращающая true.
затем true || оценивается до false и в итоге возвращает true
*/
```



### Вложенные условия

``котлин
var изучено = true
var well Rested = true

if (wellRested) {
  println("Удачи сегодня!")
  if (studied) {
    println("Вам следует подготовиться к экзамену!")
  } else {
    println("Потратьте несколько часов на подготовку перед экзаменом!")
  }
}

// Печать: Удачи сегодня!
// print: Вы должны быть готовы к экзамену!
```



### Когда выражение

``котлин
var Оценка = "A"

when (grade) {
  "A" -> println("Отличная работа!")
  "B" -> println("Отличная работа!")
  "C" -> println("Вы сдали!")
  else -> println("Закрыто! В следующий раз готовьтесь лучше!")
}
// print: Отличная работа!
```



### Оператор диапазона

``kotlin {.wrap}
var height = 46 // дюймы

if (height in 1..53) {
  println("Извините, для катания на горке ваш рост должен быть не менее 54 дюймов")
}
// Печать: Sorry, you must be at least 54 inches to ride the roller coaster
```



### Операторы равенства

``котлин
var myAge = 22
var sisterAge = 21

myAge == sisterAge // false
myAge !== sisterAge // true
```




Коллекции
---



### Неизменяемый список

``kotlin {.wrap}
var programmingLanguages = listOf("C#", "Java", "Kotlin", "Ruby")
```



### Mutable List

``kotlin {.wrap}
var fruits = mutableListOf("Апельсин", "Яблоко", "Банан", "Манго")
```



### Список доступа

``kotlin {.wrap}
var cars = listOf("BMW", "Ferrari", "Volvo", "Tesla")

println(cars[2]) // Печатает: Volvo
```



### Атрибут размера

``kotlin {.wrap}
var worldContinents = listOf("Азия", "Африка", "Северная Америка", "Южная Америка", "Антарктида", "Европа", "Австралия")

println(worldContinents.size) // Печатает: 7
```



### Манипуляции со списком {.row-span-2}

``kotlin {.wrap}
var seas = listOf("Черное море", "Карибское море", "Северное море")
println(seas. contains("Северное море")) // Выводит: true

// Функция contains() выполняет операцию чтения любого списка и определяет, существует ли элемент
seas.add("Балтийское море") // Ошибка: невозможно записать в неизменяемый список
// Функция add() может быть вызвана только для мутабельных списков, поэтому приведенный выше код выдает ошибку
```



### Неизменяемые множества

``kotlin {.wrap}
var primaryColors = setOf("Red", "Blue", "Yellow")
```



### Взаимозаменяемые множества

``kotlin {.wrap}
var womenInTech = mutableSetOf("Ада Лавлейс", "Грейс Хоппер", "Радия Перлман", "Сестра Мэри Кеннет Келлер")
```



### Доступ к элементам коллекции {.row-span-2}

``kotlin {.wrap}
var companies = setOf("Facebook", "Apple", "Netflix", "Google")

println(companies.elementAt(3))
// Выводит: Google
println(companies.elementAt(4))
// Возврат и ошибка
println(companies.elementAtOrNull(4))
// Выводит: null
```



### Неизменяемая карта

``kotlin {.wrap}
var averageTemp = mapOf("зима" - 35, "весна" - 60, "лето" - 85, "осень" - 55)
```



### Mutable Mapping

``kotlin {.wrap}
var europeanDomains = mutableMapOf("Германия" - "de", "Словакия" - "sk", "Венгрия" - "hu", "Норвегия" - "no")
```



### Получение ключей и значений карты

``kotlin {.wrap}
var oscarWinners = mutableMapOf("Паразит" - "Бонг Джун-хо", "Зеленая книга" - "Джим Берк", "Форма воды" - "Гильермо дель Торо")

println(oscarWinners.keys)
// Выводит: [Parasite, Green Book, The Shape Of Water].

println(oscarWinners.values)
// Печатается: [Бонг Джун-хо, Джим Берк, Гильермо дель Торо]
println(oscarWinners["Parasite"])
// Prints: Бонг Джун-хо
```



### Добавление и удаление записей на карте

``kotlin {.wrap}
var worldCapitals = mutableMapOf("Соединенные Штаты" - "Вашингтон", "Германия" - "Берлин", "Мексика" - "Мехико", "Франция" - "Париж")

worldCapitals.put("Бразилия", "Бразилиа")
println(worldCapitals)
// Prints: {Соединенные Штаты=Вашингтон, Германия=Берлин, Мексика=Мехико, Франция=Париж, Бразилия=Бразилия}

worldCapitals.remove("Германия")
println(worldCapitals)
// Выводит: {United States=Washington D.C., Mexico=Mexico City, France=Paris, Brazil=Brasilia}
```




Функция
---



### Функция

``котлин
fun greet() {
  println("Привет!")
}

fun main() {
  //Вызов функции
  greet() //Приветствует: Привет!
}
```



### Параметры функции

``kotlin {.wrap}
fun birthday(name: String, age: Int) {
   println("С днем рождения $name! Сегодня тебе исполнилось $age!")
}

fun main() {
  birthday("Oscar", 26)
  //Prints: С днем рождения Оскар! Сегодня тебе исполняется 25 лет!
  birthday("Amarah", 30)
  //Prints: С днем рождения Амара! Сегодня тебе исполняется 30 лет!
}
```



### Параметры по умолчанию

``kotlin {.wrap}
fun favoriteLanguage(name, language = "Kotlin") {
  println("Здравствуйте, $name. Ваш любимый язык программирования - $language")
}

fun main() {
  favoriteLanguage("Manon")
  //Prints: Здравствуйте, Манон. Ваш любимый язык программирования - Kotlin
  
  favoriteLanguage("Lee", "Java")
  //Prints: Здравствуйте, Ли. Ваш любимый язык программирования - Java
}
```



### Именованные параметры

``kotlin {.wrap}
fun findMyAge(currentYear: Int, birthYear: Int) {
   var myAge = currentYear -birthYear
println("Мне $myAge лет.")
}

fun main() {
  findMyAge(currentYear = 2020, birthYear = 1995)
  //Принтлн: Мне 25 лет.
  findMyAge(birthYear = 1920, currentYear = 2020)
  //Prints: Мне 100 лет.
}
```



### Заявление о возврате

``kotlin {.wrap}
// Тип возврата объявляется вне круглых скобок
fun getArea(length: Int, width: Int): Int {
  var area = length *width

  //Оператор возврата
  return area
}

fun main() {
  var myArea = getArea(10, 8)
println("Площадь равна $myArea.")
//Принт: Площадь равна 80.
}
```



### Функция одиночного выражения

``kotlin{.wrap}
fun fullName(firstName: String, lastName: String) = "$firstName $lastName"

fun main() {
  println(fullName("Ariana", "Ortega"))
  //Prints: Ариана Ортега
  println(fullName("Kai", "Gittens"))
  //Prints: Кай Гиттенс
}
```



### Литералы функций

``kotlin{.wrap}
fun main() {
  //Анонимная функция:
  var getProduct = fun(num1: Int, num2: Int): Int {
return num1 * num2
  }
  println(getProduct(8, 3))
  //Принт: 24
// Лямбда-выражение
  var getDifference = { num1: Int, num2: Int -> num1 -num2 }
  println(getDifference(10, 3))
  //Prints: 7
}
```




Класс
---


### Пример класса

``kotlin''
//класс со свойствами, содержащими значения по умолчанию
class Student {
  var name = "Lucia"
  var семестр = "Осень"
  var gpa = 3.95
}

// синтаксис сокращений без тела класса
класс Студент
```


### Экземпляр класса

``котлин''
// Класс
класс Студент {
  var name = "Lucia"
  var семестр = "Осень"
var gpa = 3.95
}

fun main() {
  var student = Student()
  // Экземпляр
  println(student.name)
  // Печатает: Lucia
  println(student.semester)
  // Печатает: Осень
  println(student.gpa)
  // Печатает: 3.95
}
```

### Первичный конструктор

``kotlin {.wrap}
class Student(val name: String, val gpa: Double, val semester: String, val estimatedGraduationYear: Int)

fun main() {
  var student = Student("Lucia", 3.95, "Fall", 2022)
  println(student.name)
  //Prints: Lucia
  println(student.gpa)
  //Принты: 3.95
  println(student.semester)
  //Prints: Осень
  println(student.estimatedGraduationYear)
  //Принц: 2022
}
```



### Блок инициализации

``kotlin {.wrap}
class Student(val name: String, val gpa: Double, val semester: String, val estimatedGraduationYear: Int) {
  init {
    println("У $name осталось ${estimatedGraduationYear -2020} лет в колледже.")
  }
}

fun main() {
  var student = Student("Lucia", 3.95, "Fall", 2022)
//Примечания: Люсии осталось учиться в колледже 2 года.
}
```



### Функция-член {.col-span-2}

``kotlin {.wrap}
class Student(val name: String, val gpa: Double, val semester: String, val estimatedGraduationYear: Int) {

  init {
println("У $name осталось ${estimatedGraduationYear -2020} лет в колледже.")
  }

  // функция-член
  fun calculateLetterGrade(): String {
    return when {
      gpa >= 3.0 -> "A"
      gpa >= 2.7 -> "B"
      gpa >= 1.7 -> "C"
gpa >= 1.0 -> "D"
      else -> "E"
    }
  }
}

//При создании экземпляра и вызове функции будет выполнено выражение when, которое вернет буквенную оценку
fun main() {
  var student = Student("Lucia", 3.95, "Fall", 2022)
//Примечания: Люсии осталось учиться в колледже 2 года.
  println("Буквенная оценка ${student.name} равна ${student.calculateLetterGrade()}.")
  //Печатается: Буквенная оценка Люсии - A.
}
```

См. также
---

- [Kotlin Language Official Documentation](https://kotlinlang.org/) _(kotlinlang.org)_
