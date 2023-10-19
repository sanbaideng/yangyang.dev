---
название: Экспресс
дата: 2023-02-26 15:23:31
фон: bg-[#edc545]
теги:
  - config
  - формат
категории:
  - Программирование
intro: |
  Краткая справочная шпаргалка по Express, гибкому и оптимизированному веб-фреймворку для Node.js
плагины:
    - copyCode
---

Начало работы
---



### Hello World {.row-span-2}

- "Создать проект, добавить конфигурацию `package.json`
  ``bash
  $ mkdir myapp # создать каталог
  $ cd myapp # войти в каталог
  $ npm init -y # Инициализация конфигурации
  ```

- Установка зависимостей
  ``bash
  $ npm install express
  ```

- Добавляем код в файл `index.js`:
  ``js
  const express = require('express')
  const app = express()
  const port = 3000
  app.get('/', (req, res) => {
    res. send('Hello World!')
  })
  app.listen(port, () => {
    console.log(`Прослушивание порта на ${порт}`)
  })
  ```

- Запустите приложение с помощью следующей команды
  ``bash
  $ node index.js
  ```
{.marker-timeline}



### express -h {.row-span-2}

``bash
Использование: express [options] [dir]
Опции:
  -h, --help вывод информации об использовании
      --version вывод номера версии
  -e, --ejs добавить поддержку движка ejs
      --hbs добавить поддержку движка hbs
      --pug добавить поддержку движка pug
  -H, --hogan Добавить поддержку движка hogan.js
      --no-view Не генерируется движок представления
  -v, --view <engine> добавить поддержку <движка> представления (ejs|hbs|hjs|jade|pug|twig|vash) (по умолчанию jade)
  -c, --css <engine> добавить поддержку таблицы стилей <engine> (less|stylus|compass|sass) (по умолчанию css)
      --git добавить .gitignore
  -f, --force принудительное использование непустых каталогов
```
{.wrap-text}

Создание проекта `myapp`

``bash
$ express --view=pug myapp
# запустить приложение
$ DEBUG=myapp:*npm start
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



### Приложение

``js
var express = require('express')
var app = express()

console.dir(app.locals.title)
//=> 'My App'
console.dir(app.locals.email)
//=> 'me@myapp.com'
```



#### Атрибут

:-| :-
:-| :-
`app.locals` | Локальные переменные в приложении [#](http://expressjs.com/en/4x/api.html#app.locals)
`app.mountpath` | Шаблон пути для монтирования субприложений [#](http://expressjs.com/en/4x/api.html#app.mountpath)



#### События

:-| :-
:-| :-
`mount` | Дочернее приложение монтируется на родительское приложение, и событие срабатывает на дочернем приложении [#](http://expressjs.com/en/4x/api.html#app.onmount)



#### Метод

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



### Запрос



#### Атрибут

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
`req.subdomains` | [#](http://expressjs.com/en/4x/api.html#req.subdomains)
`req.xhr` | [#](http://expressjs.com/en/4x/api.html#req.xhr)



#### Метод

:-| :-
:-| :-
`req.accepts()` | [#](http://expressjs.com/en/4x/api.html#req.accepts)
`req.acceptsCharsets()` | [#](http://expressjs.com/en/4x/api.html#req.acceptsCharsets)
`req.acceptsEncodings()` | [#](http://expressjs.com/en/4x/api.html#req.acceptsEncodings)
`req.acceptsLanguages()` | [#](http://expressjs.com/en/4x/api.html#req.acceptsLanguages)
`req.get()` | Получение полей заголовка HTTP-запроса [#](http://expressjs.com/en/4x/api.html#req.get)
`req.is()` | [#](http://expressjs.com/en/4x/api.html#req.is)
`req.param()` | [#](http://expressjs.com/en/4x/api.html#req.param)
`req.range()` | [#](http://expressjs.com/en/4x/api.html#req.range)



### Response

``js
app.get('/', function (req, res) {
  console.dir(res.headersSent) //false
  res.send('OK')
console.dir(res.headersSent) //true
})
```



#### Атрибут

:-| :-
:-| :-
`res.app` | [#](http://expressjs.com/en/4x/api.html#res.app)
`res.headersSent` | [#](http://expressjs.com/en/4x/api.html#res.headersSent)
`res.locals` | [#](http://expressjs.com/en/4x/api.html#res.locals)



#### Метод

:-| :-
:-| :-
`res.append()` | [#](http://expressjs.com/en/4x/api.html#res.append)
`res.attachment()` | [#](http://expressjs.com/en/4x/api.html#res.attachment)
`res.cookie()` | [#](http://expressjs.com/en/4x/api.html#res.cookie)
`res.clearCookie()` | [#](http://expressjs.com/en/4x/api.html#res.clearCookie)
`res.download()` | Запрос на скачивание файлов [#](http://expressjs.com/en/4x/api.html#res.download)
`res.end()` | Завершение процесса ответа [#](http://expressjs.com/en/4x/api.html#res.end)
`res.format()` | [#](http://expressjs.com/en/4x/api.html#res.format)
`res.get()` | [#](http://expressjs.com/en/4x/api.html#res.get)
`res.json()` | Отправить JSON-ответ [#](http://expressjs.com/en/4x/api.html#res.json)
`res.jsonp()` | Отправить ответ с поддержкой JSONP [#](http://expressjs.com/en/4x/api.html#res.jsonp)
`res.links()` | [#](http://expressjs.com/en/4x/api.html#res.links)
`res.location()` | [#](http://expressjs.com/en/4x/api.html#res.location)
`res.redirect()` | Перенаправление запроса [#](http://expressjs.com/en/4x/api.html#res.redirect)
`res.render()` | Рендеринг шаблона представления [#](http://expressjs.com/en/4x/api.html#res.render)
`res.send()` | Отправка различных типов ответов [#](http://expressjs.com/en/4x/api.html#res.send)
`res.sendFile()` | Отправка файла в виде октетного потока [#](http://expressjs.com/en/4x/api.html#res.sendFile)
`res.sendStatus()` | [#](http://expressjs.com/en/4x/api.html#res.sendStatus)
`res.set()` | [#](http://expressjs.com/en/4x/api.html#res.set)
`res.status()` | [#](http://expressjs.com/en/4x/api.html#res.status)
`res.type()` | [#](http://expressjs.com/en/4x/api.html#res.type)
`res.vary()` | [#](http://expressjs.com/en/4x/api.html#res.vary)







Пример
----


### Маршрутизатор {. row-span-2}

Вызывается для любого запроса, переданного этому маршрутизатору

``js
router. use(function (req, res, next) {
  //... здесь есть некоторая логика... как и в любом другом промежуточном ПО
  next()
})
```

будет обрабатывать любой запрос, заканчивающийся на `/events`.

``js
//зависит от того, где маршрутизатор "использует()"
router. get('/events', (req, res, next) => {
  //..
})
```



### Ответ

Объект `res` представляет собой HTTP-ответ, отправляемый приложением `Express` при получении HTTP-запроса

``js
app.get('/user/:id', (req, res) => {
  res.send('user' + req.params.id)
})
```



### Запрос

Объект `req` представляет собой `HTTP` запрос и имеет свойства для строки запроса, параметров, тела запроса, HTTP-заголовков и т.д.

``js
app.get('/user/:id', (req, res) => {
  res.send('user' + req.params.id)
})
```



### res. end()

``js
res. end()
res.status(404).end()
```

Завершение процесса получения ответа. Этот метод фактически пришел из ядра Node, а именно из метода `response.end()` функции `http.ServerResponse`.


### res.json([body])

``js
res.json(null)
res.json({ user: 'tobi' })
res.status(500).json({ error: 'message' })
```



### app.all

``js
app.all('/secret', function (req, res, next) {
  console.log('доступ к секретному разделу...')
  next() // Передаем управление следующему обработчику
})
```



### app.delete

``js
app.delete('/', function (req, res) {
  res.send('DELETE запрос на главную страницу')
})
```



### app.disable(name)

``js
app.disable('trust proxy')
app.get('trust proxy')
// => false
```



### app.disabled(name)

``js
app.disabled('trust proxy')
// => true

app.enable('trust proxy')
app.disabled('trust proxy')
// => false
```



### app.engine(ext, callback)

``js
var engines = require('consolidate')

app.engine('haml', engines.haml)
app.engine('html', engines.hogan)
```



### app.listen([port[, host[, backlog]]][, callback])

``js
var express = require('express')

var app = express()
app.listen(3000)
```


### Маршрутизация
``js
const express = require('express')
const app = express()

//Ответ на запрос "hello world" при выполнении GET-запроса к домашней странице
app.get('/', (req, res) => {
  res.send('hello world')
})
```

``js
// Маршрутизация метода GET
app.get('/', (req, res) => {
  res.send('GET-запрос на главную страницу')
})

// Маршрутизация методом POST
app.post('/', (req, res) => {
  res.send('POST-запрос на главную страницу')
})
```


### Middleware

``js
function logOriginalUrl (req, res, next) {
  console.log('ReqURL:', req.originalUrl)
  next()
}

function logMethod (req, res, next) {
  console.log('Тип запроса:', req.method)
  next()
}

const log = [logOriginalUrl, logMethod]

app.get('/user/:id', log,
  (req, res, next)=>{
    res.send('Информация о пользователе')
  }
)
```



### Использование шаблонов

``js
app.set('view engine', 'pug')
```

Создайте файл шаблона `Pug` с именем `index.pug` в каталоге `views` со следующим содержимым

``` pug
html
  заголовок
    заголовок= title
  тело
    h1=сообщение
```

Создайте маршрут для рендеринга файла `index.pug`. Если свойство view engine не задано, то необходимо указать расширение файла представления

``js
app.get('/', (req, res) => {
  res. render('index', {
    title: 'Привет', message: 'Hello there!'
  })
})
```
