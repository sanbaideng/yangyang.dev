---
Название: ES6
дата: 2023-01-08 18:26:55
фон: bg-[#edc545]
теги:
   - config
   - формат
категории:
   - Программирование
intro: |
    Краткая справочная шпаргалка о том, что нового появилось в JavaScript для ES2015, ES2016, ES2017, ES2018 и последующих версий
плагины:
    - copyCode
---


Начало работы
--------



### Block-scoped {.row-span-2}



#### Пусть

``js{2,4}
function fn () {
  пусть x = 0
  if (true) {
    let x = 1 // только внутри этого `if`
  }
}
```



#### Const

``js
const a = 1
```

`let` - это новый `var`. Константы (`const`) работают так же, как `let`, но не могут быть переназначены.
См: [Let и const](https://babeljs.io/learn-es2015/#let--const)



### Строки шаблонов {.row-span-2}



#### Интерполяция

``js
const message = ``Здравствуйте ${name}``
```



#### Многострочная строка

``js
const str = `
привет
мир
`
```

Шаблоны и многострочные строки.
См: [шаблонные строки](https://babeljs.io/learn-es2015/#template-strings)



### Двоичные и восьмеричные литералы

``js
let bin = 0b1010010
let oct = 0o755
```

См: [Двоичные и восьмеричные литералы](https://babeljs.io/learn-es2015/#binary-and-octal-literals)



### Экспоненциальный оператор

``js {1}
const byte = 2 **8
```

Аналогично: Math.pow(2, 8)



### Новые дополнения к библиотеке



#### Новые строковые методы

``js
"hello".repeat(3)
"hello".includes("ll")
"hello".startsWith("he")
"hello".padStart(8) // "hello"
"hello".padEnd(8) // "hello"
"hello".padEnd(8, '!') // hello!!!
"\u1E9B\u0323".normalize("NFC")
```



#### Методы новых чисел

``js
Number.EPSILON
Number.isInteger(Infinity) // false
Number.isNaN("NaN") // false
```



#### Новые методы математики

``js
Math.acosh(3) // 1.762747174039086
Math.hypot(3, 4) // 5
Math.imul(Math.pow(2, 32) -1, Math.pow(2, 32) -2) // 2
```



#### Новые методы массивов

``js
// возвращает реальный массив
Array.from(document.querySelectorAll("*"))
//похож на new Array(...), но без специального одноаргументного поведения
Array.of(1, 2, 3)
```
См: [Новые дополнения к библиотеке](https://babeljs.io/learn-es2015/#math--number--string--object-apis)



### kind

``js
class Circle extends Shape {
```



#### Конструктор

``js {1}
constructor (radius) {
  this.radius = radius
}
```



метод ####

``js {1}
getArea () {
  return Math.PI *2 *this.radius
}
```



#### Вызов метода суперкласса

``js {2}
expand(n) {
  return super.expand(n)*Math.PI
}
```



#### Статические методы

``js {1}
static createFromDiameter(diameter) {
  return new Circle(diameter /2)
}
```

Синтаксический сахар для прототипов.
См: [classes](https://babeljs.io/learn-es2015/#classes)



### Частный класс

В javascript по умолчанию используется поле public (`public`), если необходимо указать private, то можно использовать (`#`)

``js
class Dog {
  #name;
  constructor(name) {
    this.#name = name;
  }
  printName() {
    // Внутри класса можно вызывать только приватные поля
    console.log(`Ваше имя ${this.#name}`)
  }
}

const dog = new Dog("putty")
//console.log(this.#name)
//Приватные идентификаторы не допускаются вне тела класса.
dog.printName()
```



#### Статический частный класс

``js
class ClassWithPrivate {
  static #privateStaticField;
static #privateStaticFieldWithInitializer = 42;

  static #privateStaticMethod() {
    // ...
  }
}
```

Обещания
--------



### взять на себя обязательство

``js {1}
new Promise((resolve, reject) => {
  if (ok) { resolve(result) }
  else { reject(error) }
})
```

для асинхронного программирования.
См: [Promises](https://babeljs.io/learn-es2015/#promises)



### Использование обещаний

``js{2,3}
promise
  .then((result) => { --- })
  .catch((error) => { --- })
```



### Использование Promises в finally

``js {4}
обещание
  .then((result) => { --- })
  .catch((error) => { --- })
  .finally(() => {
    /* логика не зависит от успеха/ошибки */
  })
```

Обработчик вызывается, когда обещание выполнено или отклонено



### Функция обещания

``js
Promise.all(---)
Promise.race(---)
Promise.reject(---)
Promise.resolve(---)
```



### Async-await

``js{2,3}
async function run () {
  const user = await getUser()
  const tweets = await getTweets(user)
  return [user, tweets]
}
```

Функции `async` - это еще один способ использования функций.
См: [Async Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)



Деструктуризация
-------------



### Назначение деструктуризации



#### Массивы

``js {1}
const [first, last] = ['Nikola', 'Tesla']
```



#### Объекты

``js {1}
let {title, author} = {
  title: 'Шелкопряд',
  author: 'R. Galbraith'
}
```

Поддерживает сопоставление массивов и объектов.
См: [Деструктуризация](https://babeljs.io/learn-es2015/#destructuring)



### По умолчанию

``js
const scores = [22, 33]
const [math = 50, sci = 50, arts = 50] = scores
```

----

``js
//Result:
//math === 22, sci === 33, arts === 50
```

Значение по умолчанию может быть присвоено при деструктуризации массива или объекта



### Параметры функции

``js {1}
function greet({ name, greeting }) {
  console.log(`${greeting}, ${name}!`)
}
```

----

``js
greet({ name: 'Larry', greeting: 'Ahoy' })
```

Деструктуризация объектов и массивов также может быть выполнена в параметрах функции



### Defaults

``js {1}
function greet({ name = 'Rauno' } = {}) {
  console.log(`Привет ${имя}!`);
}
```

----

``js
greet() // Привет Рауно!
greet({ name: 'Larry' }) // Привет Ларри!
```



### Переназначение ключей

``js {1}
function printCoordinates({ left: x, top: y }) {
  console.log(`x: ${x}, y: ${y}`)
}
```

----

``js
printCoordinates({ left: 25, top: 90 })
```

В этом примере значению ключа `left` присваивается значение `x`.



### Loop

``js {1}
for (let {title, artist} of songs) {
  ---
}
```

Выражения присваивания также работают в циклах



### Деконструкция объектов

``js {1}
const { id, ...detail } = song;
```

Используйте оператор `rest(...)` для извлечения некоторых ключей по отдельности и остальных ключей в объекте

Оператор Spread Оператор Spread
------



### Расширения объектов



#### с расширениями объектов

``js {2}
const options = {
  ... по умолчанию,
  visible: true
}
```



#### Нет расширения объекта

``js
const options = Object.assign(
  {}, defaults,
  { visible: true })
```

Оператор разнесения объектов позволяет создавать новые объекты из других объектов.
См: [Object Spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator)



### Расширение массива



#### с расширением массива

``js{2,3}
const users = [
  ...администраторы,
  ...редакторы,
  'rstacruz'
]
```



#### Нет расширения массива

``js
const users = admins
  .concat(editors)
  .concat([ 'rstacruz' ])
```

Оператор spread позволяет аналогичным образом строить новые массивы.
См: [Spread operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator)

Функции
---------



### Параметры функции {.row-span-3}



#### Параметры по умолчанию

``js {1}
function greet (name = 'Jerry') {
  return `Hello ${name}`
}
```



#### Параметры отдыха

``js {1}
function fn(x, ...y) {
  // y - массив
  return x * y.length
}
```



#### Расширения

``js {1}
fn(...[1, 2, 3])
// то же, что и fn(1, 2, 3)
```

Default (по умолчанию), rest (остаток), spread (расширение).
См: [параметры функции](https://babeljs.io/learn-es2015/#default--rest--spread)



### Функция стрелки {.row-span-3}



#### Стрелочные функции

``js {1}
setTimeout(() => {
  ---
})
```



#### с параметрами

``js {1}
readFile('text.txt', (err, data) => {
  ...
})
```



#### implicit return
```js{1,4,5,6}
arr.map(n => n*2)
//без фигурных скобок = неявный return
//Так же как: arr.map(function (n) { return n*2 })
arr.map(n => ({
  result: n*2
}))
//Для неявного возврата объекта требуются круглые скобки вокруг объекта
```

Как функция, но сохраняет `this`.
См: [Стрелочные функции](https://babeljs.io/learn-es2015/#arrows-and-lexical-this)



### Значение параметра по умолчанию

``js
function log(x, y = 'World') {
  console.log(x, y);
}

log('Hello') // Hello World
log('Hello', 'China') // Hello China
log('Hello', '') // Hello
```



### Используется в сочетании с деструктуризацией присваивания по умолчанию

``js
function foo({x, y = 5} = {}) {
  console.log(x, y);
}

foo() // undefined 5
```



### атрибут name

``js
function foo() {}
foo.name // "foo"
```



### свойство длины

``js
function foo(a, b){}
foo.length // 2
```

Объекты
-------



### Краткий синтаксис

``js
module.exports = { hello, bye }
```

то же самое ниже:

``js
module.exports = {
  hello: hello, bye: bye
}
```

См: [Object Literals Enhanced](https://babeljs.io/learn-es2015/#enhanced-object-literals)



### метод

``js {2}
const App = {
  start () {
    console.log('running')
  }
}
//Так же: App = { start: function () {---} }
```

См: [Object Literals Enhanced](https://babeljs.io/learn-es2015/#enhanced-object-literals)



### Геттеры и сеттеры

``js{2,5}
const App = {
  get closed () {
    return this.status === 'closed'
  },
  set closed (value) {
    this.status = value ? 'closed' : 'open'
  }
}
```

См: [Object Literals Enhanced](https://babeljs.io/learn-es2015/#enhanced-object-literals)



### Вычисляемое имя свойства

``js {3}
let event = 'click'
let handlers = {
  [`on${event}`]: true
}
//Так же как: handlers = { 'onclick': true }
```

См: [Object Literals Enhanced](https://babeljs.io/learn-es2015/#enhanced-object-literals)



### Извлечение значения

``js{3,5}
const fatherJS = { возраст: 57, имя: "Чжан Сань" }
Object.values(fatherJS)
//[57, "Zhang San"]
Object.entries(fatherJS)
//[["возраст", 57], ["имя", "Чжан Сань"]]
```

Модуль Модули
-------



### Импорт импорт

``js
import 'helpers'
//aka: require('---')
```

----

``js
import Express from 'express'
//aka: const Express = require('---').default || require('---')
```

----

``js
import { indent } from 'helpers'
//aka: const indent = require('---').indent
```

----

``js
import *as Helpers from 'helpers'
//aka: const Helpers = require('---')
```

----

``js
import { indentSpaces as indent } from 'helpers'
//aka: const indent = require('---').indentSpaces
```

`импорт` - это новый `require()`.
См: [Импорт модулей](https://babeljs.io/learn-es2015/#modules)



### Экспорт экспорт

``js
export default function () { --- }
//aka: module.exports.default = ---
```

----

``js
export function mymethod () { --- }
//aka: module.exports.mymethod = ---
```

----

``js
export const pi = 3.14159
//aka: module.exports.pi = ---
```

----

``js
const FirstName = 'Michael';
const LastName = 'Jackson';
const year = 1958;
export { firstName, lastName, year };
```

----

``js
export *from "lib/math";
```

``export`` - это новый ``module.exports``.
См: [Module exports](https://babeljs.io/learn-es2015/#modules)



### Переименование ключевого слова `as`

``js{2,8,12-14}
импорт {
  lastName as surname // переименование импорта
} из './profile.js';

function v1() { ... }
function v2() { ... }

export { v1 as default }
//Эквивалентно export default v1;

export {
  v1 как streamV1, // экспортное переименование
  v2 as streamV2, // export rename
  v2 as streamLatestVersion // export rename
};
```



### Динамическая загрузка модулей

``js
button.addEventListener('click', event => {
  import('./dialogBox.js')
    .then(dialogBox => {
      dialogBox. open();
    })
    .catch(error => {
      /*Обработка ошибок */
    })
});
```
[Предложение ES2020](https://github.com/tc39/proposal-dynamic-import) ввести функцию `import()`.



### import() позволяет динамически генерировать пути к модулям

``js
const main = document.querySelector('main')

import(`./modules/${someVariable}.js`)
  .then(module => {
    module.loadPageInto(main);
  })
  .catch(err => {
    main.textContent = err.message;
  });
```



### import.meta

[ES2020](https://github.com/tc39/proposal-import-meta) В команду `import` добавлено мета-свойство `import.meta`, которое возвращает мета-информацию текущего модуля

``js
new URL('data.txt', import.meta.url)
```
В среде Node.js `import.meta.url` всегда возвращает локальный путь, то есть строку протокола `file:URL`, например `file:/// home/user/foo.js`.



### Утверждения импорта {.col-span-2}



#### статический импорт

``js
import json from "./package.json" assert {type: "json"}
//Импортируем все объекты в json-файле
```



#### Динамический импорт

``js
const json =
     await import("./package.json", { assert: { type: "json" } })
```

Генераторы
----------

### Функция генератора

``js
function*idMaker () {
  let id = 0
  while (true) { yield id++ }
}
```

----

``js
let gen = idMaker()
gen.next().value // → 0
gen.next().value // → 1
gen.next().value // → 2
```

это сложно.
См: [Генераторы](https://babeljs.io/learn-es2015/#generators)



### Для... из + итератора {.row-span-2}

``js
let fibonacci = {
  [Symbol.iterator]() {
    let pre = 0, cur = 1;
    return {
      next() {
        [pre, cur] = [cur, pre + cur];
return { done: false, value: cur }
      }
    }
  }
}

for (var n of fibonacci) {
  // усечение последовательности на 1000
  if (n > 1000) break;
  console.log(n);
}
```

Для итерации по генераторам и массивам.
См: [Для... итерации](https://babeljs.io/learn-es2015/#iterators--forof)



### Взаимосвязь с интерфейсом Iterator

``js
var gen = {};
gen[Symbol.iterator] = function*() {
  yield 1;
  yield 2;
  yield 3;
};

[...gen] // => [1, 2, 3]
```

Функция `Generator` присваивается свойству `Symbol.iterator`, так что объект `gen` обладает интерфейсом `Iterator`, который может быть обойден оператором `...`.
### Свойство Symbol.iterator

``js
function*gen() { /*некоторый код */}
var g = gen();

g[Symbol.iterator]() === g // true
```

`gen` - это функция `генератор`, вызов которой приводит к генерации объекта обходчика `g`. Ее свойство `Symbol.iterator`, которое также является функцией генерации объекта итератора, возвращает себя после выполнения

см. также
---

- [Learn ES2015](https://babeljs.io/docs/en/learn/)_(babeljs.io)_
- [Обзор возможностей ECMAScript 6](https://github.com/lukehoban/es6features#readme)_(github.com)_
