---
title: EJS
date: 2023-04-07
latar belakang: bg-[#b4ca65]
tag:
  - EJS
  - Frontend
  - Kerangka kerja
kategori:
  - Pemrograman
intro: EJS (Embedded JavaScript) adalah bahasa templat sederhana yang memungkinkan Anda menghasilkan markah HTML dengan JavaScript biasa.
pengaya:
  - copyCode
---

Memulai { .cols-3 }
-----------

### Halo dunia

#### install
```
npm install ejs
```

#### hello.ejs
``` html
<% if (user.email) { %>
  <h1><%= user.email %></h1>
<% } %>
```

#### CLI
``` shell
$ ejs hello.ejs -o hello.html
```



### Merender dengan Data

```
let ejs = require('ejs');

let people = ['geddy', 'neil', 'alex'];
let tpl = '<%= people.join(", "); %>';

let html = ejs.render(tpl, {people: people});
console.log(html);
```
Berikan EJS sebuah string templat dan beberapa data.



### Dukungan Peramban

```
<script src="ejs.js"></script>
<script>
  let people = ['geddy', 'neil', 'alex'];
  let html = ejs.render('<%= people.join(", "); %>', {people: people});
</script>
```
Gunakan ejs dalam tag skrip.



### Variabel
| | |
|--------------|----------------------------------|

| `<%- var %>` | Mencetak tanpa melarikan diri dari HTML


### CLI

Merender dan menentukan berkas keluaran.
```shell
$ ejs hello.ejs -o hello.html
```

Memberinya berkas templat dan berkas data
```shell
$ ejs hello.ejs -f data.json -o hello.html
```



### Komentar
```html
<%# Baris ini akan menunjukkan sebuah komentar %>
```
---------
```html
<%# Ini adalah komentar EJS multi-baris.
    Komentar ini dapat terdiri dari beberapa baris,
    tetapi tidak akan ditampilkan
    dalam keluaran HTML akhir.
%>
```




### Metode

```
let ejs = require('ejs');
let template = ejs.compile(str, options);

template(data);
// => String HTML yang dirender

ejs.render(str, data, options);
// => String HTML yang dirender

ejs.renderFile(namafile, data, options, function(err, str){
    // str => String HTML yang dirender
});
```



### Menyertakan File

```html
<%- include('partials/navbar.ejs') %>
```

Menyertakan templat dengan data:

```html
<% include('header', { title: 'Halaman Saya' }) %>
```
------------

```html
<ul>
  <% users.forEach(function(user){ %>
    <%- include('item', {user: user}); %>
  <% }); %>
</ul>
```

Untuk menyertakan templat, membutuhkan opsi nama file, jalur bersifat relatif



Dokumen {.cols-3}
--------


### Kondisional
```html
<% if (userLoggedIn) { %>
  <p>Selamat datang, <%= nama pengguna %>!</p>
<% } else { %>
  <p>Silakan masuk.</p>
<% } %>
```


### Menggunakan perulangan
```html
<% if (userLoggedIn) { %>
  <p>Selamat datang, <%= nama pengguna %>!</p>
<% } else { %>
  <p>Silakan masuk.</p>
<% } %>
```



### Pembatas khusus

```
let ejs = require('ejs'),
    users = ['geddy', 'neil', 'alex'];

// Hanya satu template
ejs.render('<?= users.join(" | "); ?>',
    {pengguna: pengguna},
    {pembatas: '?'});
// => 'geddy | neil | alex'

// Atau secara global
ejs.delimiter = '$';
ejs.render('<$= users.join(" | "); $>',
    {pengguna: pengguna});
// => 'geddy | neil | alex'
```




### Caching

```
let ejs = require('ejs'),
LRU = require('lru-cache');

// Cache LRU dengan batas 100 item
ejs.cache = LRU(100);
```

### Pemuat berkas khusus

```
let ejs = require('ejs');
let myFileLoader = function (filePath) {
  return 'myFileLoader: '+ fs.readFileSync(filePath);
};

ejs.fileLoader = myFileLoader;
```

### Tata Letak

```
<%- include('header'); -%>
<h1>
  Judul
</h1>
<p>
  Halaman saya
</p>
<%- include('footer'); -%>
```

## Dukungan sisi klien { .cols-2 }

### Contoh

```
<div id="output"></div>
<script src="ejs.min.js"></script>
<script>
  let people = ['geddy', 'neil', 'alex'],
      html = ejs.render('<%= people.join(", "); %>', {people: people});
  // Dengan jQuery:
  $('#output').html(html);
  // Vanilla JS:
  document.getElementById('output').innerHTML = html;
</script>
```

### Peringatan

```
let str = "Halo <%= include('file', {person: 'John'}); %>",
      fn = ejs.compile(str, {klien: true});

fn(data, null, function(path, d){ // menyertakan callback
  // path -> 'file'
  // d -> {person: 'John'}
  // Letakkan kode Anda di sini
  // Kembalikan isi file sebagai string
}); // mengembalikan string yang dirender
```


## Pilihan { .cols-1 }

### Daftar opsi
| Opsi | Deskripsi | Keterangan
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cache | Fungsi yang dikompilasi ditembolok, membutuhkan nama file |
| nama file | Digunakan oleh cache untuk cache kunci, dan untuk menyertakan |
| root | Mengatur root proyek untuk menyertakan dengan jalur absolut (misal, /file.ejs). Dapat berupa larik untuk mencoba menyelesaikan include dari beberapa direktori.                                                                                  |
| views | Larik jalur untuk digunakan saat menyelesaikan include dengan jalur relatif.                                                                                                                                                        |
| context | Konteks eksekusi fungsi
| compileDebug | Bila salah, tidak ada instrumentasi debug yang dikompilasi
| client | Mengembalikan fungsi yang dikompilasi secara mandiri
| delimiter | Karakter yang digunakan untuk pembatas bagian dalam, secara default '%' |
| openDelimiter | Karakter yang digunakan untuk pembatas pembuka, secara default '<'                                                                                                                                                                       |
| closeDelimiter | Karakter yang digunakan untuk pembatas penutup, secara default '>'                                                                                                                                                                       |
| debug | Keluaran yang dihasilkan badan fungsi | | debug
| strict | Ketika diset ke `true`, fungsi yang dihasilkan dalam mode ketat
| _with | Apakah akan menggunakan konstruksi with() {} atau tidak. Jika salah, maka lokal akan disimpan dalam objek lokal. (Mengimplikasikan `--strict`) | | _with
| localsName | Nama yang akan digunakan untuk objek yang menyimpan variabel lokal ketika tidak menggunakan Default untuk locals |
| rmWhitespace | Menghapus semua spasi yang aman untuk dihilangkan, termasuk spasi di depan dan di belakang. Ini juga memungkinkan versi yang lebih aman dari -%> pemenggalan baris untuk semua tag skriplet (tidak menghilangkan baris baru dari tag di tengah-tengah baris).  |
| escape | Fungsi pelarian yang digunakan dengan <%= construct. Fungsi ini digunakan dalam rendering dan di-.toString() dalam pembuatan fungsi klien. (Secara default meloloskan XML).                                                                 |
| outputFunctionName | Ditetapkan ke sebuah string (misalnya, 'echo' atau 'print') untuk sebuah fungsi yang akan mencetak output di dalam tag scriptlet.                                                                                                                              |
| async | Jika benar, EJS akan menggunakan fungsi asinkronisasi untuk merender. (Tergantung pada dukungan asinkronisasi/tunggu dalam runtime JS.                                                                                                                  |

## Tag { .cols-1 }

### Daftar tag
| Tag | Deskripsi |
|------|----------------------------------------------------------------------|
| <% | Tag 'Scriptlet', untuk aliran kontrol, tanpa keluaran | | <%_ | Tag Scriptlet 'Scriptlet', untuk aliran kontrol, tanpa keluaran
| <%_ | Tag Scriptlet 'Penghilangan Spasi', menghilangkan semua spasi di depannya
| <%= | Mengeluarkan nilai ke dalam templat (HTML dilewatkan) | | <%= | Mengeluarkan nilai ke dalam templat
| <%- | Mengeluarkan nilai yang tidak di-escape ke dalam templat
| <%# | Tag komentar, tidak ada eksekusi, tidak ada keluaran |
| <%% | Mengeluarkan '<%' secara harfiah
| %> | Tag akhiran biasa
| -%> | Tag trim-mode ('newline slurp'), memangkas setelah baris baru |
| _%> | Tag akhiran 'Spasi Seruput', menghapus semua spasi setelahnya | | _%> | Tag akhiran 'Spasi Seruput', menghapus semua spasi setelahnya

## Cli { .cols-1 }

### Daftar Cli
| Pilihan | Deskripsi | Keterangan
|----------------|-------------------------------------------------------------------------------------------------------------------------|
| cache | Fungsi yang dikompilasi di-cache, membutuhkan nama berkas |
| -o / --output-file FILE | Menuliskan output yang dirender ke FILE, bukan ke stdout.                                                  |
| -f / --data-file FILE | Harus berformat JSON. Gunakan masukan yang diuraikan dari FILE sebagai data untuk dirender.                              |
| -i / --data-input STRING | Harus berformat JSON dan dikodekan dengan URI. Gunakan masukan yang diuraikan dari STRING sebagai data untuk dirender.            |
| -m / --pembatas CHARACTER | Gunakan CHARACTER dengan tanda kurung siku untuk buka/tutup (standarnya adalah %).                                      |
| -p / --pembatas buka-tutup CHARACTER | Gunakan CHARACTER sebagai pengganti kurung sudut kiri untuk membuka.                                                   |
| -c / --tutup-pembatas CHARACTER | Gunakan CHARACTER sebagai pengganti tanda kurung siku kanan untuk menutup.                                                 |
| -s / --ketat | Ketika diatur ke `true`, fungsi yang dihasilkan dalam mode ketat | | -s / --ketat | Ketika diatur ke `true`, fungsi yang dihasilkan dalam mode ketat
| -n / --no-with | Gunakan objek 'locals' untuk variabel daripada menggunakan `with` (mengimplikasikan --strict).                              |
| -l / --locals-name | Nama yang digunakan untuk objek yang menyimpan variabel lokal ketika tidak menggunakan `with`.                              |
| -w / --rm-whitespace | Menghapus semua spasi yang aman untuk dihilangkan, termasuk spasi di depan dan di belakang.                       |
| -d / --debug | Keluaran yang dihasilkan badan fungsi |
| -h / --help | Menampilkan pesan bantuan.                                                                             |
| -V/v / --version | Menampilkan versi EJS.                                                                               |


Contoh penggunaan :
```
$ ejs -p [ -c ] ./template_file.ejs -o ./output.html
$ ejs ./test/fixtures/user.ejs name=Lerxst
$ ejs -n -l _ ./some_template.ejs -f ./data_file.json
```
