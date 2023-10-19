---
title: "шпаргалка по javascript"
date: 2023-10-12T08:39:58+08:00
tag: ["javascript", "шпаргалка"]
---
# Шпаргалка по Javascript

## If - Else

```
If - Else⇵
if ((age >= 14) && (age < 19)) { // логическое условие
status = "Допустимо."; // выполняется, если условие истинно
} else { // блок else является необязательным
status = "Not eligible."; // выполняется, если условие ложно
}
```

## Заявление о переключении

```
switch (new Date().getDay()) { // на входе текущий день
case 6:                         // if (day == 6)
	text = "Суббота";
	break;
case 0: // if (day == 0)
	text = "Воскресенье";
	break;
default:                        // else...
	text = "Без разницы";
}
```

## Основы ➤

#### Скрипт на странице

```
<script type="text/javascript"> ...
</script>
```

#### Включение внешнего JS-файла

```
<script src="filename.js"></script>
```

#### Задержка - тайм-аут 1 секунда

```
setTimeout(function () {

}, 1000);
```

#### Функции

```
функция addNumbers(a, b) {
return a + b; ;
}
x = addNumbers(1, 2);
```

#### Редактирование элемента DOM

```
document.getElementById("elementID").innerHTML = "Hello World!";
```

#### Вывод

```
console.log(a); // запись в консоль браузера
document.write(a); // запись в HTML
alert(a); // вывод в окно оповещения
confirm("Really?"); // диалог "да/нет", возвращает true/false в зависимости от щелчка пользователя
prompt("Ваш возраст?", "0"); // диалог ввода. Второй аргумент - начальное значение
```

#### Комментарии

```
/* Многострочный
комментарий */
// Одна строка
```

## **Типы данных**

```
var возраст = 18; // число
var name = "Jane"; // строка
var name = {first: "Jane", last: "Doe"}; // объект
var truth = false; // булево
var sheets = ["HTML", "CSS", "JS"]; // массив
var a; typeof a; // undefined
var a = null; // значение null
```

#### Объекты

```
var student = { // имя объекта
firstName: "Jane", // список свойств и значений
lastName: "Doe",
возраст:18,
рост:170,
fullName : function() { // функция объекта
   return this.firstName + " " + this.lastName;
}
};
student.age = 19; // установка значения
student[age]++; // увеличение
name = student.fullName(); // вызов функции объекта
```

## Loops↶

#### Цикл For

```
for (var i = 0; i < 10; i++) {
document.write(i + ": " + i*3 + "<br />");
}
var sum = 0;
for (var i = 0; i < a.length; i++) {
sum + = a[i];
}               // разбор массива
html = "";
for (var i of custOrder) {
html += "<li>" + i + "</li>";
}
```

#### Цикл While

```
var i = 1; // инициализация
while (i < 100) { // входит в цикл, если утверждение истинно
i *= 2; // увеличивается, чтобы избежать бесконечного цикла
document.write(i + ", "); // вывод
}
```

#### Цикл Do While

```
var i = 1; // инициализация
do { // входит в цикл хотя бы один раз
i *= 2; // увеличивается, чтобы избежать бесконечного цикла
document.write(i + ", "); // вывод
} while (i < 100) // повторяет цикл, если в конце утверждение истинно
```

#### Break

```
for (var i = 0; i < 10; i++) {
if (i == 5) { break; }          // остановка и выход из цикла
document.write(i + ", "); // последнее выведенное число равно 4
}
```

#### Продолжить

```
for (var i = 0; i < 10; i++) {
if (i == 5) { continue; }       // пропускает оставшуюся часть цикла
document.write(i + ", "); // пропускает 5
}
```

## **Строки**⊗

```
var abc = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST";
var esc = 'Я не знаю'; // \n новая строка
var len = abc.length; // длина строки
abc.indexOf("lmno"); // находим подстроку, -1, если не содержит
abc.lastIndexOf("lmno"); // последнее вхождение
abc.slice(3, 6); // вырезает "def", отрицательные значения считаются сзади
abc.replace("abc", "123"); // поиск и замена, использует регулярные выражения
abc.toUpperCase(); // преобразование в верхний регистр
abc.toLowerCase(); // преобразование в нижний регистр
abc.concat(" ", str2); // abc + " " + str2
abc.charAt(2); // символ по индексу: "c"
abc[2]; // небезопасно, abc[2] = "C" не работает
abc.charCodeAt(2); // код символа по индексу: "c" -> 99
abc.split(","); // разделение строки на запятые дает массив
abc.split(""); // разделение по символам
128.toString(16); // перевод числа в шестнадцатеричную (16), восьмеричную (8) или двоичную (2) системы счисления
```

## **События**🕖



```
<button onclick="myFunction();">
Нажмите здесь
</button>
```

#### Мышь

onclick, oncontextmenu, ondblclick, onmousedown, onmouseenter, onmouseleave, onmousemove, onmouseover, onmouseout, onmouseup

#### Клавиатура

onkeydown, onkeypress, onkeyup

#### Рамка

onabort, onbeforeunload, onerror, onhashchange, onload, onpageshow, onpagehide, onresize, onscroll, onunload

#### Форма

onblur, onchange, onfocus, onfocusin, onfocusout, oninput, oninvalid, onreset, onsearch, onselect, onsubmit

#### Перетаскивание

ondrag, ondragend, ondragenter, ondragleave, ondragover, ondragstart, ondrop

#### Буфер обмена

oncopy, oncut, onpaste

#### Медиа

onabort, oncanplay, oncanplaythrough, ondurationchange, onended, onerror, onloadeddata, onloadedmetadata, onloadstart, onpause, onplay, onplaying, onprogress, onratechange, onseeked, onseeking, onstalled, onsuspend, ontimeupdate, onvolumechange, onwaiting

#### Анимация

конец анимации, итерация анимации, начало анимации

#### Разное

transition end, onmessage, onmousewheel, ononline, onoffline, onpopstate, onshow, onstorage, ontoggle, onwheel, ontouchcancel, ontouchend, ontouchmove, ontouchstart

## **Регулярные выражения**

```
var a = str.search(/CheatSheet/i);
```

#### Модификаторы

| **i** | выполняют поиск без учета регистра |
| :---- | --------------------------------- |
| **g** | выполнить глобальное совпадение |
| **m** | выполнить многострочное соответствие |



#### Шаблоны

Шаблоны | | |
| ------------- | ---------------------------------------- |
| **\\\** | Escape символ |
| **\d** | *найти цифру* |
| **\s** | найти символ пробела |
| **\b** | найти совпадение в начале или конце слова |
| **n+** | содержит хотя бы одно n | |
| **n\*** | содержит ноль или более вхождений n |
| **n?** | содержит ноль или одно вхождение n |
| **^** | Начало строки |
| **$** | Конец строки |
| **\uxxxx** | найти символ Юникода |
| **.** | Любой одиночный символ |
| **(a\|b)** | a или b |
| **(...)** | Групповая секция |
| **[abc]** | В диапазоне (a, b или c)|
| **[0-9]** | Любая из цифр между скобками |
| **[^abc]** | Не в диапазоне |
| **\s** | Белое пространство |
| **a?** | Ноль или один из a |
| **a\*** | Ноль или больше из a |
| **a*?** | Ноль или больше, без согласования |
| **a+** | Одно или более из a |
| **a+?** | Один или более, несогласованный |
| **a{2}** | Ровно 2 из a |
| **a{2,}** | 2 или более из a |
| **a{,5}** | До 5 из a |
| **a{2,5}** | От 2 до 5 из a |
| **a{2,5}** | От 2 до 5 от a, без согласования |
| **[:punct:]** | Любой знак препинания |
| **[:пробел:]** | Любой символ пробела |
| **[:blank:]** | Пробел или табуляция |

## **Победы** Þ

```
function sum (a, b) {
return Promise(function (resolve, reject) {
 setTimeout(function () { // отправляем ответ через 1 секунду
   if (typeof a !== "число" || typeof b !== "число") { // проверка типов входных данных
	 return reject(new TypeError("Inputs must be numbers"));
   }
   resolve(a + b);
 }, 1000);
});
}
var myPromise = sum(10, 5);
myPromsise.then(function (result) {
document.write(" 10 + 5: ", result);
return sum(null, "foo"); // Неверные данные и возврат другого обещания
}).then(function () { // Не будет вызвана из-за ошибки
}).catch(function (err) { // Вместо этого вызывается обработчик catch, спустя еще секунду
console.error(err); // => Укажите два числа для суммирования.
});
```

#### Состояния

```
ожидание, выполнение, отказ
```



#### Свойства

```
Promise.length, Promise.prototype
```



#### Методы

```
Promise.all(iterable), Promise.race(iterable), Promise.reject(reason), Promise.resolve(value)
```

## **Переменные**

```
var a; // переменная
var b = "init"; // строка
var c = "Hi" + " " + "Joe"; // = "Hi Joe"
var d = 1 + 2 + "3"; // = "33"
var e = [2,3,5,8]; // массив
var f = false; // булево
var g = /()/; // RegEx
var h = function(){}; // объект функции
const PI = 3,14; // константа
var a = 1, b = 2, c = a + b; // одна строка
let z = 'zzz'; // локальная переменная в области видимости блока
```

#### Строгий режим

```
"use strict"; // Используйте строгий режим для написания безопасного кода
x = 1; // Выбрасывается ошибка, так как переменная не объявлена
```

#### Значения

```
false, true // булево
18, 3.14, 0b10011, 0xF6, NaN // число
"цветок", 'Джон' // строка
undefined, null , Infinity // специальное значение
```

#### Операторы

```
a = b + c - d; // сложение, вычитание
a = b * (c / d); // умножение, деление
x = 100 % 48; // модулор. 100 / 48 остаток = 4
a++; b--; // постфиксный инкремент и декремент
```

#### Побитовые операторы

| & | И | 5 & 1 (0101 & 0001) | 1 (1) |
| ---- | --------------------- | --------------------- | --------- |
| \| | OR | 5 \| 1 (0101 \| 0001) | 5 (101) |
| ~ | НЕ | ~ 5 (~0101) | 10 (1010) |
| ^ | XOR | 5 ^ 1 (0101 ^ 0001) | 4 (100) |
<< | | сдвиг влево | 5 << 1 (0101 << 1) | 10 (1010) |
| >> | правый сдвиг | 5 >> 1 (0101 >> 1) | 2 (10) |
| >>> | нулевая заливка правый сдвиг | 5 >>> 1 (0101 >>> 1) | 2 (10) |

#### Арифметика

```
a * (b + c) // группировка
person.age // член
person[age] // член
!(a == b) // логическое не
a != b // не равно
typeof a // тип (число, объект, функция...)
x << 2 x >> 3 // минимальный сдвиг
a = b // присваивание
a == b // равно
a != b // неравенство
a === b // строгое равенство
a !== b // строгое неравенство
a < b a > b // меньше и больше, чем
a <= b a >= b // меньше или равно, больше или равно
a += b // a = a + b (работает с - * %...)
a && b // логическое и
a || b // логическое или
```

## Массивы

```
var dogs = ["бульдог", "бигль", "лабрадор"];
var dogs = new Array("Bulldog", "Beagle", "Labrador"); // декларация

alert(dogs[1]); // доступ к значению по индексу, первый элемент - [0]
dogs[0] = "Bull Terier"; // изменение первого элемента

for (var i = 0; i < dogs.length; i++) { // разбор с использованием array.length
console.log(dogs[i]);
}
```

#### Методы

```
dogs.toString(); // преобразование в строку: результаты "Bulldog,Beagle,Labrador"
dogs.join(" * "); // объединить: "Bulldog * Beagle * Labrador"
dogs.pop(); // удалить последний элемент
dogs.push("Chihuahua"); // добавление нового элемента в конец
dogs[dogs.length] = "Chihuahua"; // то же, что и push
dogs.shift(); // удаление первого элемента
dogs.unshift("Chihuahua"); // добавление нового элемента в начало
delete dogs[0]; // изменить элемент на неопределенный (не рекомендуется)
dogs.splice(2, 0, "Мопс", "Боксер"); // добавляем элементы (куда, сколько удалять, список элементов)
var animals = dogs.concat(cats,birds); // объединить два массива (собаки, затем кошки и птицы)
dogs.slice(1,4); // элементы от [1] до [4-1]
dogs.sort(); // сортировка строки в алфавитном порядке
dogs.reverse(); // сортировка строки в порядке убывания
x.sort(function(a, b){return a - b}); // числовая сортировка
x.sort(function(a, b){return b - a}); // числовая сортировка по убыванию
highest = x[0]; // первый элемент отсортированного массива является наименьшим (или наибольшим) значением
x.sort(function(a, b){return 0.5 - Math.random()}); // сортировка в случайном порядке
```

------

concat, copyWithin, every, fill, filter, find, findIndex, forEach, indexOf, isArray, join, lastIndexOf, map, pop, push, reduce, reduceRight, reverse, shift, slice, some, sort, splice, toString, unshift, valueOf



## Ошибки

```
try { // блок кода для попытки
undefinedFunction();
}
catch(err) { // блок обработки ошибок
console.log(err.message);
}
```

#### Выброс ошибки

```
throw "My error message"; // throw a text
```

#### Валидация ввода

```
var x = document.getElementById("mynum").value; // получение входного значения
try {
if(x == "") throw "пусто"; // ошибки
if(isNaN(x)) throw "не число";
x = Number(x);
if(x > 10) throw "слишком много";
}
catch(err) { // если есть ошибка
document.write("Input is " + err); // ошибка вывода
console.error(err); // запись ошибки в консоль
}
finally {
document.write("</br />Done"); // выполняется независимо от результата try / catch
}
```

#### Значения имен ошибок

| RangeError | **Число находится "вне диапазона** |
| ------------------ | ------------------------------------- |
| **Ошибка ссылки** | **Неправильная ссылка** |
| **SyntaxError** | **Возникла ошибка encodeURI()** |
| **TypeError** | **Произошла ошибка типа** |
| **URIError** | **Возникла ошибка encodeURI()** |

