---
Judul: ES6
tanggal: 2023-01-08 18:26:55
latar belakang: bg-[#edc545]
tags:
   - config
   - format
kategori:
   - Pemrograman
intro: |
    Lembar contekan referensi singkat tentang apa yang baru dalam JavaScript untuk ES2015, ES2016, ES2017, ES2018, dan seterusnya
pengaya:
    - copyCode
---


Memulai
--------



### Block-scoped {.row-span-2}



#### Biarkan

```js{2,4}
fungsi fn () {
  let x = 0
  if (true) {
    let x = 1 // hanya di dalam `if` ini
  }
}
```



#### Const

```js
const a = 1
```

`let` adalah `var` yang baru. Konstanta (`const`) bekerja seperti `let`, tetapi tidak dapat dipindahkan.
Lihat: [Let dan const](https://babeljs.io/learn-es2015/#let--const)



### Template String {.row-span-2}



#### Interpolasi

```js
const message = `Halo ${nama}`
```



#### String multi-baris

```js
const str = `
halo
dunia
`
```

Templat dan string multiline.
Lihat: [string templat](https://babeljs.io/learn-es2015/#template-strings)



### Literal biner dan oktal

```js
let bin = 0b1010010
let oct = 0o755
```

Lihat: [Biner dan Oktal Literal](https://babeljs.io/learn-es2015/#binary-and-octal-literals)



### Operator Eksponensial

```js {1}
const byte = 2 **8
```

Sama seperti: Math.pow(2, 8)



### Penambahan pustaka baru



#### Metode string baru

```js
"halo".repeat(3)
"halo". includes("akan")
"halo". startsWith("he")
"halo".padStart(8) // "halo"
"halo".padEnd(8) // "halo"
"halo".padEnd(8, '!') // halo!!!
"\u1E9B\u0323".normalize("NFC")
```



#### Metode Nomor Baru

```js
Number.EPSILON
Number.isInteger(Infinity) // false
Number.isNaN("NaN") // false
```



#### Metode Matematika Baru

```js
Math.acosh(3) // 1.762747174039086
Math.hypot(3, 4) // 5
Math.imul(Math.pow(2, 32) -1, Math.pow(2, 32) -2) // 2
```



#### Metode-metode Larik Baru

```js
//mengembalikan larik nyata
Array.from(document.querySelectorAll("*"))
//mirip dengan new Array(...), tetapi tanpa perilaku argumen tunggal khusus
Array.of(1, 2, 3)
```
Lihat: [Penambahan pustaka baru] (https://babeljs.io/learn-es2015/#math--number--string--object-apis)



### jenis

```js
class Lingkaran extends Bentuk {
```



#### Konstruktor

```js {1}
konstruktor (radius) {
  this.radius = radius
}
```



#### metode

```js {1}
getArea () {
  return Math.PI * 2 * this.radius
}
```



#### Panggil metode superclass

```js {2}
expand(n) {
  return super.expand(n) *Math.PI
}
```



#### Metode statis

```js {1}
static createFromDiameter(diameter) {
  return new Circle(diameter /2)
}
```

Gula sintaksis untuk prototipe.
Lihat: [classes](https://babeljs.io/learn-es2015/#classes)



### Kelas pribadi

Kolom default javascript adalah publik (`public`), jika Anda perlu menunjukkan privat, Anda dapat menggunakan (`#`)

```js
class Anjing {
  #nama
  konstruktor (nama) {
    this.#nama = nama;
  }
  printNama() {
    // Hanya field pribadi yang bisa dipanggil di dalam kelas
    console.log(`Nama Anda adalah ${this.#nama}`)
  }
}

const dog = new Dog("dempul")
//console.log(this.#nama)
//Pengenal pribadi tidak diperbolehkan di luar badan kelas.
dog.printName()
```



#### Kelas privat statis

```js
class ClassWithPrivate {
  static #privateStaticField;
static #privateStaticFieldWithInitializer = 42;

  static #privateStaticMethod() {
    // ...
  }
}
```

Janji
--------



### membuat komitmen

```js {1}
new Promise((resolve, reject) => {
  if (ok) { resolve(hasil) }
  else { tolak (error) }
})
```

untuk pemrograman asinkron.
Lihat: [Janji-janji](https://babeljs.io/learn-es2015/#promises)



### Menggunakan Janji

```js{2,3}
promise
  .then((hasil) => { --- })
  .catch((error) => { --- })
```



### Menggunakan Janji dalam akhirnya

```js {4}
promise
  .then((hasil) => { --- })
  .catch((error) => { --- })
  .finally(() => {
    /*logika tidak bergantung pada keberhasilan/kesalahan */
  })
```

Handler dipanggil ketika janji dipenuhi atau ditolak



### Fungsi janji

```js
Promise.all(---)
Promise.race(---)
Promise.reject(---)
Promise.resolve(---)
```



### Async-tunggu

```js{2,3}
fungsi asinkronisasi run () {
  const user = await getUser()
  const tweets = await getTweets(user)
  return [user, tweets]
}
```

Fungsi `async` adalah cara lain untuk menggunakan fungsi.
Lihat: [Fungsi Asinkronisasi](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)



Penghancuran
-------------



### Penugasan destrukturisasi



#### Array

```js {1}
const [first, last] = ['Nikola', 'Tesla']
```



#### Objek

```js {1}
let {judul, penulis} = {
  judul: 'Ulat Sutra',
  penulis: 'R. Galbraith'
}
```

Mendukung pencocokan larik dan objek.
Lihat: [Destructuring](https://babeljs.io/learn-es2015/#destructuring)



### Default

```js
const nilai = [22, 33]
const [math = 50, sci = 50, arts = 50] = nilai
```

----

```js
//Result:
//math === 22, sci === 33, arts === 50
```

Nilai default dapat ditetapkan saat mendestrukturisasi larik atau objek



### Parameter fungsi

```js {1}
function menyapa({ nama, salam }) {
  console.log(`${salam}, ${nama}!`)
}
```

----

```js
menyapa ({ nama: 'Larry', sapaan: 'Ahoy' })
```

Destrukturisasi objek dan larik juga dapat dilakukan dalam parameter fungsi



### Default

```js {1}
function menyapa({ nama = 'Rauno' } = {}) {
  console.log(`Hai ${nama}!`);
}
```

----

```js
greet() // Hai Rauno!
greet({ name: 'Larry' }) // Hai Larry!
```



### Menetapkan ulang kunci

```js {1}
function printCoordinates({ left: x, top: y }) {
  console.log(`x: ${x}, y: ${y}`)
}
```

----

```js
printCoordinates({ left: 25, top: 90 })
```

Contoh ini menetapkan `x` ke nilai kunci `kiri`



### Perulangan

```js {1}
for (let {judul, artis} dari lagu) {
  ---
}
```

Ekspresi penugasan juga berfungsi dalam perulangan



### Dekonstruksi Objek

```js {1}
const { id, ... detail } = lagu;
```

Gunakan operator `rest(...)` untuk mengekstrak beberapa kunci satu per satu dan kunci lainnya di dalam objek

Operator Penyebaran Penyebaran
------



### Ekstensi Objek



#### dengan ekstensi objek

```js {2}
const options = {
  ... default,
  visible: true
}
```



#### Tidak ada ekstensi objek

```js
const options = Object.assign(
  {}, defaults,
  { visible: true })
```

Operator penyebaran objek memungkinkan Anda membuat objek baru dari objek lain.
Lihat: [Penyebaran Objek](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator)



### Perluasan Larik



#### dengan ekstensi larik

```js{2,3}
const users = [
  ... admin,
  ... editor,
  'rstacruz'
]
```



#### Tidak ada ekspansi larik

```js
const users = admins
  .concat(editor)
  .concat([ 'rstacruz' ])
```

Operator spread memungkinkan Anda untuk membuat larik baru dengan cara yang sama.
Lihat: [Operator penyebaran](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator)

Fungsi
---------



### Parameter fungsi {.row-span-3}



#### Parameter default

```js {1}
function menyapa (nama = 'Jerry') {
  return `Halo ${nama}`
}
```



#### Parameter istirahat

```js {1}
function fn(x, ... y) {
  // y adalah sebuah array
  return x * y.length
}
```



#### Ekstensi

```js {1}
fn(...[1, 2, 3])
//sama seperti fn(1, 2, 3)
```

Default (bawaan), istirahat, penyebaran (ekstensi).
Lihat: [parameter fungsi](https://babeljs.io/learn-es2015/#default--rest--spread)



### Fungsi panah {.row-span-3}



#### Fungsi panah

```js {1}
setTimeout(() => {
  ---
})
```



#### dengan parameter

```js {1}
readFile('text.txt', (err, data) => {
  ...
})
```



#### pengembalian implisit
```js{1,4,5,6}
arr.map(n => n*2)
//tidak ada kurung kurawal = pengembalian implisit
//Sama seperti: arr.map(function (n) { return n*2 })
arr.map(n => ({
  hasil: n*2
}))
//Pengembalian objek secara implisit membutuhkan tanda kurung di sekitar objek
```

Seperti sebuah fungsi, tetapi mempertahankan `ini`.
Lihat: [Fungsi Panah](https://babeljs.io/learn-es2015/#arrows-and-lexical-this)



### Nilai default pengaturan parameter

```js
function log(x, y = 'World') {
  console.log(x, y);
}

log('Halo') // Halo Dunia
log('Halo', 'China') // Halo China
log('Halo', '') // Halo
```



### Digunakan bersama dengan destrukturisasi penugasan default

```js
function foo({x, y = 5} = {}) {
  console.log(x, y);
}

foo() // tidak terdefinisi 5
```



### atribut nama

```js
function foo() {}
foo.name // "foo"
```



Properti panjang ### panjang

```js
fungsi foo(a, b){}
foo.length // 2
```

Objek
-------



### Sintaksis Singkatan

```js
module.exports = { halo, selamat tinggal }
```

sama di bawah ini:

``` js
module.exports = {
  halo: halo, selamat tinggal: selamat tinggal
}
```

Lihat: [Objek Literal yang Disempurnakan](https://babeljs.io/learn-es2015/#enhanced-object-literals)



Metode ###

```js {2}
const App = {
  start () {
    console.log('running')
  }
}
//Sama seperti: App = { start: function () {---} }
```

Lihat: [Literal Objek yang Disempurnakan](https://babeljs.io/learn-es2015/#enhanced-object-literals)



### Pengambil dan pengatur

```js{2,5}
const App = {
  get closed () {
    return this.status === 'closed'
  },
  set closed (nilai) {
    this.status = nilai ? 'tertutup' : 'terbuka'
  }
}
```

Lihat: [Objek Literal yang Disempurnakan](https://babeljs.io/learn-es2015/#enhanced-object-literals)



### Nama properti yang dihitung

```js {3}
let event = 'klik'
let handlers = {
  [`on${event}`]: true
}
//Sama seperti: handlers = { 'onclick': true }
```

Lihat: [Object Literals yang Disempurnakan](https://babeljs.io/learn-es2015/#enhanced-object-literals)



### Ekstrak nilai

```js{3,5}
const fatherJS = { umur: 57, nama: "Zhang San" }
Object.values(fatherJS)
//[57, "Zhang San"]
Object.entries(fatherJS)
//[["umur", 57], ["nama", "Zhang San"]]
```

Modul modul
-------



### Impor impor

```js
import 'helpers'
//aka: require('---')
```

----

``` js
import Express dari 'express'
//aka: const Express = require('---').default || require('---')
```

----

``` js
import { indent } from 'helpers'
//aka: const indent = require('---').indent
```

----

```js
import * as Helpers from 'helpers'
//aka: const Helpers = require('---')
```

----

```js
import { indentSpaces as indent } from 'helpers'
//aka: const indent = require('---').indentSpaces
```

`import` adalah `require()` yang baru.
Lihat: [Impor modul] (https://babeljs.io/learn-es2015/#modules)



### Ekspor ekspor

```js
ekspor fungsi default () { --- }
//aka: module.exports.default = ---
```

----

```js
fungsi ekspor mymethod () { --- }
//aka: module.exports.mymethod = ---
```

----

```js
export const pi = 3.14159
//aka: module.exports.pi = ---
```

----

```js
const firstName = 'Michael';
const lastName = 'Jackson';
const year = 1958;
export { nama depan, nama belakang, tahun };
```

----

``` js
ekspor * dari "lib/math";
```

`export` adalah `module.exports` yang baru.
Lihat: [Module exports](https://babeljs.io/learn-es2015/#modules)



### Penggantian nama kata kunci `as`

```js{2,8,12-14}
import {
  nama_akhir sebagai nama keluarga // import ganti nama
} from './profile.js';

function v1() { ... }
function v2() { ... }

mengekspor { v1 sebagai default };
//Setara dengan mengekspor default v1;

ekspor {
  v1 sebagai streamV1, // ekspor ganti nama
  v2 sebagai streamV2, // ekspor ganti nama
  v2 as streamLatestVersion // ekspor ganti nama
};
```



### Memuat modul secara dinamis

```js
button.addEventListener('click', event => {
  import('./dialogBox.js')
    .then(dialogBox => {
      dialogBox. open();
    })
    .catch(error => {
      /*Penanganan kesalahan */
    })
});
```
[Proposal ES2020] (https://github.com/tc39/proposal-dynamic-import) memperkenalkan fungsi `import()`



### import() memungkinkan jalur modul dibuat secara dinamis

```js
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

[ES2020](https://github.com/tc39/proposal-import-meta) Menambahkan properti meta `import.meta` ke perintah `import`, yang mengembalikan informasi meta dari modul saat ini

```js
URL baru ('data.txt', import.meta.url)
```
Di lingkungan Node.js, `import.meta.url` selalu mengembalikan jalur lokal, yaitu string protokol `file:URL`, seperti `file:/// home/user/foo.js`



### Mengimpor Pernyataan {.col-span-2}



#### impor statis

```js
import json from "./package.json" assert {type: "json"}
//Impor semua objek dalam berkas json
```



#### Impor Dinamis

```js
const json =
     menunggu impor ("./package.json", { assert: { type: "json" } })
```

Generator
----------

### Fungsi generator

```js
function * idMaker () {
  let id = 0
  while (true) { hasilkan id++ }
}
```

----

```js
let gen = idMaker()
gen.next().value // → 0
gen.next().value // → 1
gen.next().value // → 2
```

itu rumit.
Lihat: [Generator](https://babeljs.io/learn-es2015/#generators)



### For..of + iterator {.row-span-2}

```js
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
  // memotong urutan pada 1000
  if (n > 1000) break;
  console.log(n);
}
```

Untuk mengulang generator dan larik.
Lihat: [Untuk..iterasi](https://babeljs.io/learn-es2015/#iterators--forof)



### Hubungan dengan antarmuka Iterator

```js
var gen = {};
gen [Symbol.iterator] = function*() {
  menghasilkan 1
  hasil 2
  hasil 3
};

[... gen] // => [1, 2, 3]
```

Fungsi `Generator` ditetapkan ke properti `Symbol.iterator`, sehingga objek `gen` memiliki antarmuka `Iterator`, yang dapat dilalui oleh operator `...`
### Properti Symbol.iterator

```js
function*gen() { /*beberapa kode */}
var g = gen();

g[Symbol.iterator]() === g // true
```

`gen` adalah fungsi `Generator`, memanggilnya akan menghasilkan objek penjelajah `g`. Properti `Symbol.iterator`, yang juga merupakan fungsi penghasil objek iterator, akan dikembalikan setelah eksekusi

lihat juga
---

- [Belajar ES2015] (https://babeljs.io/docs/en/learn/) _(babeljs.io)
- [Ikhtisar Fitur ECMAScript 6](https://github.com/lukehoban/es6features#readme) _(github.com)_
