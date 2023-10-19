---
название: JavaScript
дата: 2020-12-24 17:12:25
фон: bg-[#ebd94e]
теги:
    - js
    - веб
категории:
  - Программирование
intro: |
    Шпаргалка по JavaScript, содержащая наиболее важные понятия, функции, методы и многое другое. Полный краткий справочник для начинающих.
плагины:
    - copyCode
---




Начало работы
------------

### Введение
JavaScript - это легкий интерпретируемый язык программирования.

- [JSON cheatsheet](/json) _(cheatsheets.zip)_
- [Regex в JavaScript](/regex#regex-in-javascript) _(cheatsheets.zip)_


### Консоль

``javascript
// => Hello world!
console.log('Hello world!');

// => Hello CheatSheets.zip
console.warn('hello %s', 'CheatSheets.zip');

// Вывод сообщения об ошибке в stderr
console.error(new Error('Oops!'));
```


### Числа

```javascript
let amount = 6;
let price = 4.99;
```



### Переменные

``javascript
let x = null;
let name = "Тэмми";
const found = false;

// => Tammy, false, null
console.log(name, found, x);

var a;
console.log(a); // => undefined
```


### Строки

``javascript
let single = "Где моя разбойничья шапка?";
let double = "Где моя разбойничья шапка?";

// => 21
console.log(single.length);

```



### Арифметические операторы

``javascript
5 + 5 = 10 // Сложение
10 - 5 = 5 // Вычитание
5 * 10 = 50 // Умножение
10 / 5 = 2 // Деление
10 % 5 = 0 // Модуло
```


### Комментарии

```javascript
// Эта строка будет обозначать комментарий

/*
Приведенная ниже конфигурация должна быть
перед развертыванием.
*/

```


### Операторы присваивания

```javascript
let number = 100;

// Оба оператора прибавят 10
number = number + 10;
number += 10;

console.log(number);
// => 120
```


### Интерполяция строк

```javascript
let age = 7;

// Конкатенация строк
'Tommy is ' + age + ' years old.';

// Интерполяция строк
``Томми сейчас ${age} лет``;
```




### let Keyword

``javascript
let count;
console.log(count); // => неопределено
count = 10;
console.log(count); // => 10
```


### const Ключевое слово

``javascript
const NumberOfColumns = 4;

// TypeError: Присвоение константе...
numberOfColumns = 8;
```



JavaScript Conditionals
------------


Утверждение ### if

``javascript
const isMailSent = true;

if (isMailSent) {
  console.log('Почта отправлена получателю');
}
```



### Тернарный оператор

``javascript
var x=1;

// => true
result = (x == 1) ? true : false;
```


### Операторы {.row-span-2}

``javascript
true || false; // true
10 > 5 || 10 > 20; // true
false || false; // false
10 > 100 || 10 > 20; // false
```
#### Логический оператор &&
``javascript
true && true; // true
1 > 2 && 2 > 1; // false
true && false; // false
4 === 4 && 3 > 1; // true
```
#### Операторы сравнения
``javascript
1 > 3 // false
3 > 1 // true
250 >= 250 // true
1 === 1 // true
1 === 2 // false
1 === '1' // false
```
#### Логический оператор !
``javascript
let lateToWork = true;
let oppositeValue = !lateToWork;

// => false
console.log(oppositeValue);
```
#### Оператор коалесценции Nullish ?
``javascript
null ?? 'I win'; // 'I win'
undefined ?? 'Я тоже'; // 'Я тоже'

false ?? 'Я проиграл' // false
0 ?? 'Я снова проиграл' // 0
'' ?? 'Черт возьми' // ''
```



### else if

``javascript
const size = 10;

if (size > 100) {
  console.log('Big');
} else if (size > 20) {
  console.log('Medium');
} else if (size > 4) {
  console.log('Small');
} else {
  console.log('Tiny');
}
// Печать: Маленький
```




### switch Statement

``javascript
const food = 'salad';

switch (food) {
  case 'oyster':
    console.log('Вкус моря');
    break;
  case 'pizza':
    console.log('Вкусный пирог');
    break;
  default:
    console.log('Приятного аппетита');
}
```

### == vs ===
```javascript
0 == false // true
0 === false // false, другой тип
1 == "1" // true, автоматическое преобразование типа
1 === "1" // false, другой тип
null == undefined // true
null === undefined // false
'0' == false // true
'0' === false // false
```
`==` проверяет только значение, `===` проверяет и значение, и тип.


Функции JavaScript
------------


### Функции

``javascript
// Определение функции:
function sum(num1, num2) {
  return num1 + num2;
}

// Вызов функции:
sum(3, 6); // 9
```


### Анонимные функции

```javascript
// Именованная функция
function rocketToMars() {
  return 'BOOM!';
}

// Анонимная функция
const rocketToMars = function() {
  return 'BOOM!';
}
```



### Функции стрелок (ES6) {.row-span-2}
#### С двумя аргументами
``javascript
const sum = (param1, param2) => {
  return param1 + param2;
};
console.log(sum(2,5)); // => 7
```
#### Без аргументов
```javascript
const printHello = () => {
  console.log('hello');
};
printHello(); // => hello
```
#### С одним аргументом
```javascript
const checkWeight = weight => {
  console.log(`Weight : ${weight}`);
};
checkWeight(25); // => Вес : 25
```
#### Краткие стрелочные функции
``javascript
const multiply = (a, b) => a * b;
// => 60
console.log(multiply(2, 30));
```
[Функция стрелки](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) доступна начиная с ES2015



### return Keyword

``javascript''
// С возвратом
function sum(num1, num2) {
  return num1 + num2;
}

// Функция не выводит сумму
function sum(num1, num2) {
  num1 + num2;
}
```


### Вызов функций

```javascript
// Определение функции
function sum(num1, num2) {
  return num1 + num2;
}

// Вызов функции
sum(2, 4); // 6
```



### Функциональные выражения

``javascript
const dog = function() {
  return 'Woof!';
}
```


### Параметры функции

``javascript
// Параметром является имя
function sayHello(name) {
  return ``Привет, ${name}!``;
}
```


### Декларация функции

```javascript
function add(num1, num2) {
  return num1 + num2;
}
```




Область применения JavaScript
------------


### Область применения

``javascript
function myFunction() {
  
  var pizzaName = "Маргарита";
  // Код здесь может использовать pizzaName
  
}

// Код здесь не может использовать pizzaName
```


### Переменные, привязанные к блоку

```javascript
const isLoggedIn = true;

if (isLoggedIn == true) {
  const statusMessage = 'Вошел в систему.'
}

// Uncaught ReferenceError...
console.log(statusMessage);

```


### Глобальные переменные

```javascript
// Переменная, объявленная глобально
const color = 'blue';

function printColor() {
  console.log(color);
}

printColor(); // => синий
```


### let vs var
```javascript
for (let i = 0; i < 3; i++) {
  // Это максимальная область применения функции 'let'
  // i accessible ✔️
}
// i недоступно ❌

```
---
```javascript
for (var i = 0; i < 3; i++) {
  // i доступно ✔️
}
// i accessible ✔️
```
`var` скопирован на ближайший блок функций, а `let` - на ближайший объемлющий блок.

### Циклы с замыканиями
``javascript{.wrap}
// Печатает 3 трижды, а не то, что мы имели в виду.
for (var i = 0; i < 3; i++) {
  setTimeout(_ => console.log(i), 10);
}
```
---
```javascript{.wrap}
// Печатает 0, 1 и 2, как и ожидалось.
for (let j = 0; j < 3; j++) {
  setTimeout(_ => console.log(j), 10);
}
```
Переменная имеет собственную копию с помощью `let`, а переменная имеет общую копию с помощью `var`.





Массивы JavaScript
------------


### Массивы

``javascript
const fruits = ["яблоко", "апельсин", "банан"];

// Различные типы данных
const data = [1, 'chicken', false];
```

### Свойство .length

``javascript
const numbers = [1, 2, 3, 4];

numbers.length // 4
```


### Индекс

```javascript
// Доступ к элементу массива
const myArray = [100, 200, 300];

console.log(myArray[0]); // 100
console.log(myArray[1]); // 200
```


### Взаимозаменяемая диаграмма
| | add | remove | start | end |
|:----------|:---:|:------:|:-----:|:---:|
| `push` | ✔ | | | | ✔ | ✔ |
| `pop` | | ✔ | | ✔ | ✔ |
| `unshift` | ✔ | | ✔ | | ✔ |
| `shift` | | ✔ | ✔ | ✔ | |
{.show-header}


### Метод .push()

``javascript
// Добавление одного элемента:
const cart = ['apple', 'orange'];
cart.push('pear');

// Добавление нескольких элементов:
const numbers = [1, 2];
numbers.push(3, 4, 5);
```
Добавляет элементы в конец и возвращает новую длину массива.


### Метод .pop()

``javascript
const fruits = ["яблоко", "апельсин", "банан"];

const fruit = fruits.pop(); // 'банан'
console.log(fruits); // ["яблоко", "апельсин"]
```
Удаляет элемент из конца и возвращает удаленный элемент.


### Метод .shift()

``javascript
let cats = ['Bob', 'Willy', 'Mini'];

cats.shift(); // ['Willy', 'Mini']
```
Удаляет элемент из начала и возвращает удаленный элемент.


### Метод .unshift()

``javascript
let cats = ['Bob'];

// => ['Willy', 'Bob'].
cats.unshift('Willy');

// => ['Puff', 'George', 'Willy', 'Bob']
cats.unshift('Puff', 'George');
```
Добавляет элементы в начало и возвращает новую длину массива.




### Метод .concat()
``javascript
const numbers = [3, 2, 1]
const newFirstNumber = 4
    
// => [ 4, 3, 2, 1 ]
[newFirstNumber].concat(numbers)
    
// => [ 3, 2, 1, 4 ]
numbers.concat(newFirstNumber)
```
Если вы хотите избежать мутации исходного массива, можно использовать concat.


JavaScipt Set
------------

### Создать набор

``javascript
// Пустой объект Set
const emptySet = new Set()

// Объект Set со значениями
const setObj = new Set([1, true, "hi"])
```


### Add

```javascript
const emptySet = new Set()

// добавляем значения
emptySet.add('a') // 'a'
emptySet.add(1) // 'a', 1
emptySet.add(true) // 'a', 1, true
emptySet.add('a') // 'a', 1, true
```


### Delete

``javascript
const emptySet = new Set([1, true, 'a'])

// удаляем значения
emptySet.delete('a') // 1, true
emptySet.delete(true) // 1
emptySet.delete(1) //
```


### Has

```javascript
const setObj = new Set([1, true, 'a'])

// возвращает true или false
setObj.has('a') // true
setObj.has(1) // true
setObj.has(false) // false
```


### Очистить

```javascript
const setObj = new Set([1, true, 'a'])

// очищает набор
console.log(setObj) // 1, true, 'a'
setObj.clear() //
```


### Размер

```javascript
const setObj = new Set([1, true, 'a'])

consoloe.log(setObj.size) // 3
```


### ForEach

``javascript
const setObj = new Set([1, true, 'a'])

setObj.forEach(function(value){
  console.log(value)
})

// 1
// true
// 'a'
```


Циклы JavaScript
------------


### Цикл While

``javascript
while (condition) {
  // блок кода, который будет выполнен
}

let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}
```


### Обратный цикл

``javascript
const fruits = ["яблоко", "апельсин", "банан"];

for (let i = fruits.length - 1; i >= 0; i--) {
  console.log(`${i}. ${fruits[i]}`);
}

// => 2. банан
// => 1. апельсин
// => 0. яблоко
```


### Do...While Statement

```javascript
x = 0
i = 0

do {
  x = x + i;
  console.log(x)
  i++;
} while (i < 5);
// => 0 1 3 6 10
```


### For Loop

```javascript
for (let i = 0; i < 4; i += 1) {
  console.log(i);
};

// => 0, 1, 2, 3
```


### Перебор массивов

```javascript
for (let i = 0; i < array.length; i++){
  console.log(array[i]);
}

// => Каждый элемент массива
```


### Break

```javascript
for (let i = 0; i < 99; i += 1) {
  if (i > 5) {
     break;
  }
  console.log(i)
}
// => 0 1 2 3 4 5
```

### Продолжение
```javascript
for (i = 0; i < 10; i++) {
  if (i === 3) { continue; }
  text += "Число равно " + i + "<br>";
}
```


### Вложенные

```javascript
for (let i = 0; i < 2; i += 1) {
  for (let j = 0; j < 3; j += 1) {
    console.log(`${i}-${j}`);
  }
}
```



### for...in loop

``javascript
const fruits = ["яблоко", "апельсин", "банан"];

for (let index in fruits) {
  console.log(index);
}
// => 0
// => 1
// => 2
```

### для... цикла

``javascript
const fruits = ["яблоко", "апельсин", "банан"];

for (let fruit of fruits) {
  console.log(fruit);
}
// => яблоко
// => апельсин
// => банан
```


Итераторы JavaScript {.cols-2}
------------


### Функции, присваиваемые переменным

``javascript
let plusFive = (number) => {
  return number + 5;
};
// f присваивается значение plusFive
let f = plusFive;

plusFive(3); // 8
// Поскольку f имеет значение функции, ее можно вызывать.
f(9); // 14

```


### Функции обратного вызова

```javascript
const isEven = (n) => {
  return n % 2 == 0;
}

let printMsg = (evenFunc, num) => {
  const isNumEven = evenFunc(num);
  console.log(`${num} - четное число: ${isNumEven}.`)
}

// Передаем isEven в качестве функции обратного вызова
printMsg(isEven, 4);
// => Число 4 является четным числом: True.
```

### Метод массива .reduce()

```javascript
const numbers = [1, 2, 3, 4];

const sum = numbers.reduce((accumulator, curVal) => {
  return accumulator + curVal;
});

console.log(sum); // 10
```


### Метод массива .map()

``javascript
const members = ["Тейлор", "Дональд", "Дон", "Наташа", "Бобби"];

const announcements = members.map((member) => {
  return member + " присоединился к конкурсу."
});

console.log(announcements);
```


### Метод массива .forEach()

```javascript
const numbers = [28, 77, 45, 99, 27];

numbers.forEach(number => {
  console.log(number);
});
```


### Метод массива .filter()

``javascript
const randomNumbers = [4, 11, 42, 14, 39];
const filteredArray = randomNumbers.filter(n => {
  return n > 5;
});
```



Объекты JavaScript {.cols-2}
------------


### Доступ к свойствам

``javascript
const apple = {
  цвет: 'Green',
  цена: { bulk: '$3/kg', smallQty: '$4/кг' }
};
console.log(apple.color); // => зеленый
console.log(apple.price.bulk); // => $3/кг
```


### Свойства именования

```javascript
// Пример недопустимых имен ключей
const trainSchedule = {
  // Недопустимо из-за пробела между словами.
  platform num: 10,
  // Выражения не могут быть ключами.
  40 - 10 + 2: 30,
  // Знак + недопустим, если он не заключен в кавычки.
  +compartment: 'C'
}
```



### Несуществующие свойства

``javascript
const classElection = {
  дата: '12 января'
};

console.log(classElection.place); // undefined
```


### Mutable {.row-span-2}

``javascript
const student = {
  имя: 'Sheldon',
  оценка: 100,
  оценка: 'A',
}

console.log(student)
// { { name: 'Sheldon', score: 100, grade: 'A' }

delete student.score
student.grade = 'F'
console.log(student)
// { { имя: 'Sheldon', оценка: 'F' }

student = {}
// TypeError: Присвоение константной переменной.
```



### Синтаксис сокращения присваивания

``javascript
const person = {
  имя: 'Tom',
  возраст: '22',
};
const {name, age} = person;
console.log(name); // 'Tom'
console.log(age); // '22'
```




### Оператор удаления

``javascript
const person = {
  firstName: "Матильда",
  возраст: 27,
  хобби: "вязание",
  цель: "изучение JavaScript"
};

delete person.hobby; // или delete person[hobby];

console.log(person);
/*
{
  firstName: "Матильда"
  возраст: 27
  цель: "изучение JavaScript"
}
*/
	
```


### Объекты в качестве аргументов

```javascript
const origNum = 8;
const origObj = {color: 'blue'};

const changeItUp = (num, obj) => {
  num = 7;
  obj.color = 'red';
};

changeItUp(origNum, origObj);

// Будет выведено 8, так как целые числа передаются по значению.
console.log(origNum);

// Будет выведено 'red', так как объекты передаются
// по ссылке и поэтому могут быть изменены.
console.log(origObj.color);
```


### Создание коротких объектов

``javascript
const activity = 'Серфинг';
const beach = { activity };
console.log(beach); // { { activity: 'Surfing' }
```


### это ключевое слово

``javascript
const cat = {
  имя: 'Pipey',
  возраст: 8,
  whatName() {
    return this.name
  }
};
console.log(cat.whatName()); // => Pipey
```



### Фабричные функции

``javascript''
// Фабричная функция, принимающая параметры 'name',
// 'age', and 'breed' parameters to return
// настраиваемый объект собаки.
const dogFactory = (name, age, breed) => {
  return {
    имя: имя,
    age: age,
    порода: порода,
    bark() {
      console.log('Гав!');
    }
  };
};

```


### Методы

``javascript
const engine = {
  // сокращение метода, с одним аргументом
  start(adverb) {
    console.log(``Двигатель запускает ${adverb}...``);
  },
  // анонимное выражение стрелочной функции без аргументов
  sputter: () => {
    console.log('Двигатель глохнет...');
  },
};

engine.start('noisily');
engine.sputter();
```


### Геттеры и сеттеры

``javascript
const myCat = {
  _name: 'Dottie',
  get name() {
    return this._name;
  },
  set name(newName) {
    this._name = newName;
  }
};

// Ссылка вызывает геттер
console.log(myCat.name);

// Назначение вызывает сеттер
myCat.name = 'Yankee';
```



Классы JavaScript
------------


### Статические методы

``javascript
class Dog {
  constructor(name) {
    this._name = name;
  }
  
  introduce() {
    console.log('Это ' + this._name + ' !');
  }
  
  // Статический метод
  static bark() {
    console.log('Гав!');
  }
}

const myDog = new Dog('Buster');
myDog.introduce();

// Вызов статического метода
Dog.bark();
```


### Класс

``javascript
класс Song {
  constructor() {
    this.title;
    this.author;
  }
  
  play() {
    console.log('Песня играет!');
  }
}

const mySong = new Song();
mySong.play();
```


### Конструктор класса

``javascript
класс Song {
  constructor(title, artist) {
    this.title = title;
    this.artist = artist;
  }
}

const mySong = new Song('Bohemian Rhapsody', 'Queen');
console.log(mySong.title);
```


### Методы класса

``javascript
класс Song {
  play() {
    console.log('Playing!');
  }
  
  stop() {
    console.log('Stopping!');
  }
}
```


### extends

``javascript
// Родительский класс
class Media {
  constructor(info) {
    this.publishDate = info.publishDate;
    this.name = info.name;
  }
}

// Дочерний класс
class Song extends Media {
  constructor(songData) {
    super(songData);
    this.artist = songData.artist;
  }
}

const mySong = new Song({
  artist: 'Queen',
  name: 'Bohemian Rhapsody',
  publishDate: 1975
});
```




Модули JavaScript {.cols-2}
------------


### Экспорт

``javascript
// myMath.js

// Экспорт по умолчанию
export default function add(x,y){
    return x + y
}

// Обычный экспорт
export function subtract(x,y){
    return x - y
}

// Множественный экспорт
function multiply(x,y){
    return x * y
}
function duplicate(x){
    return x * 2
}
export {
    multiply,
    duplicate
}
```


### Импорт

```javascript
// main.js
import add, { subtract, multiply, duplicate } из './myMath.js';

console.log(add(6, 2)); // 8
console.log(subtract(6, 2)) // 4
console.log(multiply(6, 2)); // 12
console.log(duplicate(5)) // 10

// index.html
<script type="module" src="main.js"></script>
```


### Модуль экспорта

```javascript
// myMath.js

function add(x,y){
    return x + y
}
function subtract(x,y){
    return x - y
}
function multiply(x,y){
    return x * y
}
function duplicate(x){
    return x * 2
}

// Множественный экспорт в node.js
module.exports = {
    add,
    вычитать,
    умножать,
    дублировать
}
```


### Требуемый модуль

```javascript
// main.js
const myMath = require('./myMath.js')

console.log(myMath.add(6, 2)); // 8
console.log(myMath.subtract(6, 2)) // 4
console.log(myMath.multiply(6, 2)); // 12
console.log(myMath.duplicate(5)) // 10
```


JavaScript Promises {.cols-2}
------------


### Promise states {.row-span-2}

``javascript
const promise = new Promise((resolve, reject) => {
  const res = true;
  // Асинхронная операция.
  if (res) {
    resolve('Resolved!');
  }
  else {
    reject(Error('Ошибка'));
  }
});

promise.then((res) => console.log(res), (err) => console.error(err));
```


### Функция-исполнитель

```javascript
const executorFn = (resolve, reject) => {
  resolve('Решено!');
};

const promise = new Promise(executorFn);
```


### setTimeout()

```javascript
const loginAlert = () =>{
  console.log('Login');
};

setTimeout(loginAlert, 6000);
```



### Метод .then()

``javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Result')
  }, 200);
});

promise.then((res) => {
  console.log(res);
}, (err) => {
  console.error(err);
});
```


### .catch() метод

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject(Error('Promise Rejected Unconditionally.'))
  }, 1000);
});

promise.then((res) => {
  console.log(value);
});

promise.catch((err) => {
  console.error(err);
});
```


### Promise.all()

```javascript
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve(3);
  }, 300);
});
const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve(2);
  }, 200);
});

Promise.all([promise1, promise2]).then((res) => {
  console.log(res[0]);
  console.log(res[1]);
});
```


### Избегая вложенных Promise и .then()

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('*');
  }, 1000);
});

const twoStars = (star) => {
  return (star + star);
};

const oneDot = (star) => {
  { return (star + '.')
};

const print = (val) => {
  console.log(val);
};

// Соединяем их вместе
promise.then(twoStars).then(oneDot).then(print);
```



### Создание

``javascript
const executorFn = (resolve, reject) => {
  console.log('Функция-исполнитель обещания!');
};

const promise = new Promise(executorFn);
```

### Цепочка из нескольких .then()

```javascript
const promise = new Promise(resolve => setTimeout(() => resolve('dAlan'), 100));

promise.then(res => {
  return res === 'Alan' ? Promise.resolve('Привет, Алан!') : Promise.reject('Кто ты?')
}).then((res) => {
  console.log(res)
}, (err) => {
  console.error(err)
});
```

### Имитация http-запроса с помощью Promise

```javascript
const mock = (success, timeout = 1000) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if(success) {
        resolve({status: 200, data:{}});
      } else {
        reject({message: 'Error'});
      }
    }, timeout);
  });
}
const someEvent = async () => {
  try {
    await mock(true, 1000);
  } catch (e) {
    console.log(e.message);
  }
}
```



JavaScript Async-Await {.cols-2}
------------


### Асинхронный

``javascript
function helloWorld() {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve('Hello World!');
    }, 2000);
  });
}

const msg = async function() { //Async Function Expression
  const msg = await helloWorld();
  console.log('Message:', msg);
}

const msg1 = async () => { //Async Стрелочная функция
  const msg = await helloWorld();
  console.log('Message:', msg);
}

msg(); // Сообщение: Hello World! <-- через 2 секунды
msg1(); // Сообщение: Hello World! <-- через 2 секунды
```


### Разрешение обещаний

```javascript
let pro1 = Promise.resolve(5);
let pro2 = 44;
let pro3 = new Promise(function(resolve, reject) {
  setTimeout(resolve, 100, 'foo');
});

Promise.all([pro1, pro2, pro3]).then(function(values) {
  console.log(values);
});
// expected => Array [5, 44, "foo"]
```


### Async Await Promises

```javascript
function helloWorld() {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve('Hello World!');
    }, 2000);
  });
}

async function msg() {
  const msg = await helloWorld();
  console.log('Message:', msg);
}

msg(); // Сообщение: Hello World! <-- через 2 секунды
```


### Обработка ошибок

```javascript
let json = '{ "возраст": 30 }'; // неполные данные

try {
  let user = JSON.parse(json); // <-- ошибок нет
  console.log( user.name ); // нет имени!
} catch (e) {
  console.error( "Неверные JSON-данные!" );
}
```


### Aysnc await operator

```javascript
function helloWorld() {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve('Hello World!');
    }, 2000);
  });
}

async function msg() {
  const msg = await helloWorld();
  console.log('Message:', msg);
}

msg(); // Сообщение: Hello World! <-- через 2 секунды
```



Запросы JavaScript
------------

### JSON

``json
const jsonObj = {
  "name": "Rick",
  "id": "11A",
  "level": 4
};
```
Также см: [JSON cheatsheet](/json)



### XMLHttpRequest

``javascript
const xhr = new XMLHttpRequest();
xhr.open('GET', 'mysite.com/getjson');
```
`XMLHttpRequest` - это API на уровне браузера, позволяющий клиенту писать сценарии передачи данных с помощью JavaScript, НЕ являющегося частью языка JavaScript.



### GET

``javascript
const req = new XMLHttpRequest();
req.responseType = 'json';
req.open('GET', '/getdata?id=65');
req.onload = () => {
  console.log(xhr.response);
};

req.send();
```


### POST {.row-span-2}

``javascript
const data = {
  рыба: 'Лосось',
  вес: '1.5 кг',
  единицы: 5
};
const xhr = new XMLHttpRequest();
xhr.open('POST', '/inventory/add');
xhr.responseType = 'json';
xhr.send(JSON.stringify(data));

xhr.onload = () => {
  console.log(xhr.response);
};
```


### fetch api {.row-span-2}

``javascript
fetch(url, {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
      'apikey': apiKey
    },
    body: data
  }).then(response => {
    if (response.ok) {
      return response.json();
    }
    throw new Error('Request failed!');
  }, networkError => {
    console.log(networkError.message)
  })
}
```


### JSON Formatted

```javascript
fetch('url-that-returns-JSON')
.then(response => response.json())
.then(jsonResponse => {
  console.log(jsonResponse);
});
```


### promise url parameter fetch api

``javascript
fetch('url')
.then(
  response => {
    console.log(response);
  },
 rejection => {
    console.error(rejection.message);
);
```


### Функция API Fetch

``javascript
fetch('https://api-xxx.com/endpoint', {
  method: 'POST',
 body: JSON.stringify({id: "200"})
}).then(response => {
  if(response.ok){
	  return response.json();
  }
	throw new Error('Запрос не прошел!');
}, networkError => {
  console.log(networkError.message);
}).then(jsonResponse => {
  console.log(jsonResponse);
})
```


### async await syntax {.col-span-2}

``javascript
const getSuggestions = async () => {
  const wordQuery = inputField.value;
  const endpoint = `${url}${queryParams}${wordQuery}`;
  try{
const response = await fetch(endpoint, {cache: 'no-cache'});
    if(response.ok){
      const jsonResponse = await response.json()
    }
  }
  catch(error){
    console.log(error)
  }
}
```
