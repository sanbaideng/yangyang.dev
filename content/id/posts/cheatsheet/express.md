---
title: Express
date: 2023-02-26 15:23:31
tag: ["Express"] 
---

# express



### Hello World {.row-span-2}

- "Buat proyek, tambahkan konfigurasi `package.json`
  ```bash
  $ mkdir myapp # membuat direktori
  $ cd myapp # masuk ke direktori
  $ npm init -y # Inisialisasi konfigurasi
  ```

- Menginstal dependensi
  ``` bash
  $ npm install express
  ```

- Masukkan berkas `index.js` dan tambahkan kode:
  ```js
  const express = require('express')
  const app = express()
  const port = 3000
  app.get('/', (req, res) => {
    res. send('Hello World!')
  })
  app. listen(port, () => {
    console.log(`Mendengarkan port pada ${port}`)
  })
  ```

- Jalankan aplikasi menggunakan perintah berikut
  ``` bash
  $ node index.js
  ```
{.marker-timeline}



### express -h {.row-span-2}

```bash
Penggunaan: express [opsi] [dir]
Pilihan:
  -h, --help informasi penggunaan keluaran
      --version nomor versi keluaran
  -e, --ejs menambahkan dukungan mesin ejs
      --hbs menambahkan dukungan mesin hbs
      --pug tambahkan dukungan mesin pug
  -h, --hogan tambahkan dukungan mesin hogan.js
      --no-view Tidak ada tampilan mesin yang dihasilkan
  -v, --view <engine> tambahkan dukungan view <engine> (ejs|hbs|hjs|jade|pug|twig|vash) (default jade)
  -c, --css <engine> tambahkan dukungan stylesheet <engine> (less|stylus|compass|sass) (css default)
      --git tambahkan .gitignore
  -f, --force paksa direktori yang tidak kosong
```
{.wrap-text}

Membuat proyek `myapp`

``` bash
$ express --view = pug myapp
# jalankan aplikasi
$ DEBUG = myapp:*npm start
```



### express()

:-| :-
:-| :-
`express.json()` | [#](http://expressjs.com/en/4x/api.html#express.json)
`express.raw()` | [#](http://expressjs.com/en/4x/api.html#express.raw)
`express.Router()` | [#](http://expressjs.com/en/4x/api.html#express.router)
`express.static()` | [#](http://expressjs.com/en/4x/api.html#express.static)
`express.text()` | [#](http://expressjs.com/en/4x/api.html#express.text)
`express.urlencoded()` | [#](http://expressjs.com/en/4x/api.html#express.urlencoded)



### Router

:-| :-
:-| :-
`router.all()` | [#](http://expressjs.com/en/4x/api.html#router.all)
`router.METHOD()` | [#](http://expressjs.com/en/4x/api.html#router.METHOD)
`router.param()` | [#](http://expressjs.com/en/4x/api.html#router.param)
`router.route()` | [#](http://expressjs.com/en/4x/api.html#router.route)
`router.use()` | [#](http://expressjs.com/en/4x/api.html#router.use)



### Aplikasi

```js
var express = require('express')
var app = express()

console.dir(app.locals.title)
//=> 'Aplikasi Saya'
console.dir(app.locals.email)
//=> 'me@myapp.com'
```



#### Atribut

:-| :-
:-| :-
`app.locals` | Variabel lokal dalam aplikasi [#](http://expressjs.com/en/4x/api.html#app.locals)
`app.mountpath` | Pola jalur untuk pemasangan sub-aplikasi [#](http://expressjs.com/en/4x/api.html#app.mountpath)



#### Peristiwa

:-| :-
:-| :-
`mount` | Aplikasi anak dipasang pada aplikasi induk, dan peristiwa dipicu pada aplikasi anak [#](http://expressjs.com/en/4x/api.html#app.onmount)



#### Metode

:-| :-
:-| :-
`app.all()` | [#](http://expressjs.com/en/4x/api.html#app.all)
`app.delete()` | [#](http://expressjs.com/en/4x/api.html#app.delete.method)
`app.disable()` | [#](http://expressjs.com/en/4x/api.html#app.disable)
`app.disabled()` | [#](http://expressjs.com/en/4x/api.html#app.disabled)
`app.enable()` | [#](http://expressjs.com/en/4x/api.html#app.enable)
`app.enabled()` | [#](http://expressjs.com/en/4x/api.html#app.enabled)
`app.engine()` | [#](http://expressjs.com/en/4x/api.html#app.engine)
`app.get(name)` | [#](http://expressjs.com/en/4x/api.html#app.get)
`app.get(path, callback)` | [#](http://expressjs.com/en/4x/api.html#app.get.method)
`app.listen()` | [#](http://expressjs.com/en/4x/api.html#app.listen)
`app.METHOD()` | [#](http://expressjs.com/en/4x/api.html#app.METHOD)
`app.param()` | [#](http://expressjs.com/en/4x/api.html#app.param)
`app.path()` | [#](http://expressjs.com/en/4x/api.html#app.path)
`app.post()` | [#](http://expressjs.com/en/4x/api.html#app.post.method)
`app.put()` | [#](http://expressjs.com/en/4x/api.html#app.put.method)
`app.render()` | [#](http://expressjs.com/en/4x/api.html#app.render)
`app.route()` | [#](http://expressjs.com/en/4x/api.html#app.route)
`app.set()` | [#](http://expressjs.com/en/4x/api.html#app.set)
`app.use()` | [#](http://expressjs.com/en/4x/api.html#app.use)



### Permintaan



#### Atribut

:-| :-
:-| :-
`req.app` | [#](http://expressjs.com/en/4x/api.html#req.app)
`req.baseUrl` | [#](http://expressjs.com/en/4x/api.html#req.baseUrl)
`req.body` | [#](http://expressjs.com/en/4x/api.html#req.body)
`req.cookies` | [#](http://expressjs.com/en/4x/api.html#req.cookies)
`req.fresh` | [#](http://expressjs.com/en/4x/api.html#req.fresh)
`req.hostname` | [#](http://expressjs.com/en/4x/api.html#req.hostname)
`req.ip` | [#](http://expressjs.com/en/4x/api.html#req.ip)
`req.ips` | [#](http://expressjs.com/en/4x/api.html#req.ips)
`req.method` | [#](http://expressjs.com/en/4x/api.html#req.method)
`req.originalUrl` | [#](http://expressjs.com/en/4x/api.html#req.originalUrl)
`req.params` | [#](http://expressjs.com/en/4x/api.html#req.params)
`req.path` | [#](http://expressjs.com/en/4x/api.html#req.path)
`req.protocol` | [#](http://expressjs.com/en/4x/api.html#req.protocol)
`req.query` | [#](http://expressjs.com/en/4x/api.html#req.query)
`req.route` | [#](http://expressjs.com/en/4x/api.html#req.route)
`req.secure` | [#](http://expressjs.com/en/4x/api.html#req.secure)
`req.signedCookies` | [#](http://expressjs.com/en/4x/api.html#req.signedCookies)
`req.stale` | [#](http://expressjs.com/en/4x/api.html#req.stale)
`req.subdomain` | [#](http://expressjs.com/en/4x/api.html#req.subdomains)
`req.xhr` | [#](http://expressjs.com/en/4x/api.html#req.xhr)



#### Metode

:-| :-
:-| :-
`req.accepts()` | [#](http://expressjs.com/en/4x/api.html#req.accepts)
`req.acceptsCharsets()` | [#](http://expressjs.com/en/4x/api.html#req.acceptsCharsets)
`req.acceptsEncodings()` | [#](http://expressjs.com/en/4x/api.html#req.acceptsEncodings)
`req.acceptsLanguages()` | [#](http://expressjs.com/en/4x/api.html#req.acceptsLanguages)
`req.get()` | Dapatkan bidang header permintaan HTTP [#](http://expressjs.com/en/4x/api.html#req.get)
`req.is()` | [#](http://expressjs.com/en/4x/api.html#req.is)
`req.param()` | [#](http://expressjs.com/en/4x/api.html#req.param)
`req.range()` | [#](http://expressjs.com/en/4x/api.html#req.range)



### Tanggapan

```js
app.get('/', function (req, res) {
  console.dir(res.headersSent) //false
  res.send('OK')
console.dir(res.headersSent) //true
})
```



#### Atribut

:-| :-
:-| :-
`res.app` | [#](http://expressjs.com/en/4x/api.html#res.app)
`res.headersSent` | [#](http://expressjs.com/en/4x/api.html#res.headersSent)
`res.locals` | [#](http://expressjs.com/en/4x/api.html#res.locals)



#### Metode

:-| :-
:-| :-
`res.append()` | [#](http://expressjs.com/en/4x/api.html#res.append)
`res.attachment()` | [#](http://expressjs.com/en/4x/api.html#res.attachment)
`res.cookie()` | [#](http://expressjs.com/en/4x/api.html#res.cookie)
`res.clearCookie()` | [#](http://expressjs.com/en/4x/api.html#res.clearCookie)
`res.download()` | Meminta file untuk diunduh [#](http://expressjs.com/en/4x/api.html#res.download)
`res.end()` | mengakhiri proses respons [#](http://expressjs.com/en/4x/api.html#res.end)
`res.format()` | [#](http://expressjs.com/en/4x/api.html#res.format)
`res.get()` | [#](http://expressjs.com/en/4x/api.html#res.get)
`res.json()` | Kirim respons JSON [#](http://expressjs.com/en/4x/api.html#res.json)
`res.jsonp()` | Kirim respons dengan dukungan JSONP [#](http://expressjs.com/en/4x/api.html#res.jsonp)
`res.links()` | [#](http://expressjs.com/en/4x/api.html#res.links)
`res.location()` | [#](http://expressjs.com/en/4x/api.html#res.location)
`res.redirect()` | Permintaan pengalihan [#](http://expressjs.com/en/4x/api.html#res.redirect)
`res.render()` | merender templat tampilan [#](http://expressjs.com/en/4x/api.html#res.render)
`res.send()` | Mengirim berbagai jenis tanggapan [#](http://expressjs.com/en/4x/api.html#res.send)
`res.sendFile()` ` Mengirim berkas sebagai aliran oktet [#](http://expressjs.com/en/4x/api.html#res.sendFile)
`res.sendStatus()` | [#](http://expressjs.com/en/4x/api.html#res.sendStatus)
`res.set()` | [#](http://expressjs.com/en/4x/api.html#res.set)
`res.status()` | [#](http://expressjs.com/en/4x/api.html#res.status)
`res.type()` | [#](http://expressjs.com/en/4x/api.html#res.type)
`res.vary()` | [#](http://expressjs.com/en/4x/api.html#res.vary)







Contoh
----


### Router {. row-span-2}

Dipanggil untuk setiap permintaan yang diteruskan ke router ini

```js
router. use (function (req, res, next) {
  //.. beberapa logika di sini.. seperti middleware lainnya
  next()
})
```

akan menangani setiap permintaan yang diakhiri dengan `/events`

```js
// Tergantung di mana router "use()"
router. get('/events', (req, res, next) => {
  //..
})
```



### Tanggapan

Objek `res` mewakili respons HTTP yang dikirim oleh aplikasi `Express` ketika menerima permintaan HTTP

```js
app.get('/user/:id', (req, res) => {
  res.send('user' + req.params.id)
})
```



### Permintaan

Objek `req` merepresentasikan permintaan `HTTP` dan memiliki properti untuk string kueri permintaan, parameter, badan, header HTTP, dll.

```js
app.get('/user/:id', (req, res) => {
  res.send('user' + req.params.id)
})
```



### res. end()

```js
res. end()
res.status(404).end()
```

Mengakhiri proses respons. Metode ini sebenarnya berasal dari inti Node, khususnya metode `response.end()` dari `http.ServerResponse`


### res.json([body])

```js
res.json(null)
res.json({ user: 'tobi' })
res.status(500).json({ error: 'message' })
```



### app.all

```js
app.all('/secret', function (req, res, next) {
  console.log('mengakses bagian rahasia...')
  next() // Limpahkan kontrol ke penangan berikutnya
})
```



### app.delete

```js
app.delete('/', function (req, res) {
  res.send('HAPUS permintaan ke beranda')
})
```



### app.disable(nama)

```js
app.disable('trust proxy')
app.get('trust proxy')
// => false
```



### app.disabled(nama)

```js
app.disabled('trust proxy')
// => true

app.enable('trust proxy')
app.disabled('trust proxy')
// => false
```



### app.engine(ext, callback)

```js
var engines = require('consolidate')

app.engine('haml', engines.haml)
app.engine('html', engines.hogan)
```



### app.listen([port[, host[, backlog]]][, callback])

```js
var express = require('express')

var app = express()
app.listen(3000)
```


### Perutean
``` js
const express = require('express')
const app = express()

//Merespons "halo dunia" saat membuat permintaan GET ke beranda
app.get('/', (req, res) => {
  res.send('halo dunia')
})
```

```js
// Perutean metode GET
app.get('/', (req, res) => {
  res.send('GET permintaan ke beranda')
})

// Perutean metode POST
app.post('/', (req, res) => {
  res.send('POST permintaan ke beranda')
})
```


### Middleware

```js
function logOriginalUrl (req, res, next) {
  console.log('ReqURL:', req.originalUrl)
  next()
}

function logMethod (req, res, next) {
  console.log('Tipe Permintaan:', req.method)
  next()
}

const log = [logOriginalUrl, logMethod]

app.get('/user/:id', log,
  (req, res, next)=>{
    res.send('Info Pengguna')
  }
)
```



### Menggunakan templat

```js
app.set('view engine', 'pug')
```

Buat berkas templat `Pug` bernama `index.pug` di direktori `views` dengan konten berikut

``` pug
html
  kepala
    title = judul
  tubuh
    h1 = pesan
```

Buat rute untuk merender berkas `index.pug`. Jika properti mesin penampil tidak diatur, ekstensi berkas penampil harus ditentukan

```js
app.get('/', (req, res) => {
  res. render('index', {
    title: 'Hai', pesan: 'Halo!'
  })
})
```
