---
Название: XPath
дата: 2020-12-19 22:15:43
фон: bg-[#77aeeb]
tags:
    - документ
    - выражение
    - выбор
категории:
    - Инструментарий
введение: |
    Это шпаргалка по селекторам [XPath](https://en.wikipedia.org/wiki/XPath), в которой перечислены часто используемые методы позиционирования XPath и селекторы CSS
плагины:
    - copyCode
---

XPath Selectors {.cols-6}
--------

### Начало работы {.col-span-2}

- [Xpath test bed](http://www.whitebeam.org/library/guide/TechNotes/xpathtestbed.rhtm) _(whitebeam.org)_

Протестируйте в консоли Firefox или Chrome:
``console
$x('/html/body')
$x('//h1')
$x('//h1')[0].innerText
$x('//a[text()="XPath"]')[0].click()
```



### Селекторы-потомки {.col-span-2}

| Xpath | CSS |
|--------------|--------------|
| `//h1` | h1 |
| | `//div//p` | div p |
| `//ul/li` | ul > li |
| `//ul/li/a` | ul > li > a |
| | `//div/*` | div > * |
| `/` | :root |
| `/html/body` | :root > body |
{.show-header}


### Заказать селекторы {.col-span-2}

| Xpath | CSS |
|---------------------|----------------------|
| `//ul/li[1]` | ul > li:first-child |
| `//ul/li[2]` | ul > li:nth-child(2) |
| `//ul/li[last()]` | ul > li:last-child |
| `//li[@id="id"][1]` | li#id:first-child |
| | `//a[1]` | a:first-child |
| `//a[last()]` | a:last-child |
{.show-header}


### Селекторы атрибутов {.col-span-3 .row-span-2}

| Xpath | CSS |
|---------------------------------|----------------------|
| `//*[@id="id"]` | #id |
| `//*[@class="class"]` | .class |
| `//input[@type="submit"]` | input[type="submit"]|
| | `//a[@id="abc"][@for="xyz"]` | a#abc[for="xyz"] |
| | `//a[@rel]` | a[rel] |
| `//a[starts-with(@href, '/')]` | | a[href^='/'] |
| `//a[ends-with(@href, '.pdf')]` | a[href$='pdf'] |
| `//a[contains(@href, '://')]` | | a[href*='`:`//'] |
| `//a[contains(@rel, 'help')]` | | a[rel~='help'] |
{.show-header}


### Родные братья и сестры {.col-span-3}
| Xpath | CSS |
|--------------------------------------|----------|
| `//h1/following-sibling::ul` | h1 ~ ul |
| | `//h1/following-sibling::ul[1]` | h1 + ul |
| | `//h1/following-sibling::[@id="id"]` | h1 ~ #id |
{.show-header}


### jQuery {.col-span-3}
| Xpath | CSS |
|----------------------------------|----------------------------|
| | `//ul/li/...` | $('ul > li').parent() |
| `//li/ancestor-or-self::section` | $('li').closest('section') |
| `//a/@href` | $('a').attr('href') |
| | `//span/text()` | $('span').text() |
{.show-header}


### Misc селекторы {.col-span-3}
| Xpath | CSS |
|-----------------------------------|---------------------------|
| `//h1[not(@id)]` | h1:not([id])|
| `//button[text()="Submit"]` | | Text match |
| `//button[contains(text(), "Go")]` | Текст содержит (подстроку) |
| `//product[@price > 2.50]` | Арифметика |
| `//ul[*]` | Имеет дочерние элементы |
| `//ul[li]` | Имеет дочерние элементы (конкретные) |
| `//a[@name или @href]` | Или логика |
| | `//a | //div` | Объединение (объединяет результаты) |
{.show-header}



Выражения XPath
-----------

### Шаги и оси {.secondary}
<br/>

| - | - | - | - |
|------|------|------|-----------------|
| `//` | `ul` | `/` | `a[@id='link']` |
| Axis | Step | Axis | Step |
{.left-text}


### Префиксы

| Префикс | Пример | Средства |
|--------|-----------------------|----------|
| `//` | `//hr[@class='edge']` | Anywhere |
| `/` | `/html/body/div` | Корень |
| `./` | `./div/p` | Относительный |
{.show-header}


### Оси

| Ось | Пример | Средства |
|------|---------------------|------------|
| `/` | `//ul/li/a` | Child |
| `//` | `//[@id="list"]//a` | Descendant |
{.show-header}



Предикаты XPath
----------

### Предикаты

``bash
//div[true()]
//div[@class="head"]
//div[@class="head"][@id="top"]
```

Ограничивает набор узлов только в том случае, если некоторое условие истинно. Они могут быть соединены в цепочку.

### Операторы

``bash
# Сравнение
//a[@id = "xyz"]
//a[@id != "xyz"]
//a[@price > 25]
```

``bash
# Логика (и/или)
//div[@id="head" and position()=2]
//div[(x и y) или not(z)]
```


### Использование узлов

``bash
# Использование узлов внутри функций
//ul[count(li) > 2]
//ul[count(li[@class='hide']) > 0]
```

``bash
# Возвращает `<ul>`, у которого есть дочерний `<li>`.
//ul[li]
```

Вы можете использовать узлы внутри предикатов.

### Индексирование

``bash
//a[1] # первый <a>
//a[last()] # last <a>
//ol/li[2] # второй <li>
//ol/li[position()=2] # то же, что и выше
//ol/li[position()>1] #:not(:first-child)
```

Используйте `[]` с числом, или `last()`, или `position()`.

### Порядок цепочки

``bash
a[1][@href='/']
a[@href='/'][1]
```

Порядок имеет значение, эти два варианта отличаются.

### Вложенные предикаты

```
//section[.//h1[@id='hi']]
```

Возвращается `<section>`, если у него есть потомок `<h1>` с `id='hi'`.

Функции XPath {.cols-2}
---------

### Функции узлов

``bash
name() # //[starts-with(name(), 'h')]
text() # //button[text()="Submit"]
                  # //button/text()
lang(str)
namespace-uri()
```

``bash
count() # //table[count(tr)=1]
position() # //ol/li[position()=2]
```


### Строковые функции

``bash
contains() # font[contains(@class, "head")]
starts-with() # font[starts-with(@class, "head")]
ends-with() # font[ends-with(@class, "head")]
```

``bash
concat(x,y)
substring(str, start, len)
substring-before("01/02", "/") #=> 01
substring-after("01/02", "/") #=> 02
translate()
normalize-space()
string-length()
```


### Булевы функции

``bash
not(expr) # button[not(starts-with(text(), "Submit"))]
```

### Преобразование типов

```bash
строка()
число()
boolean()
```

Оси XPath {.cols-2}
----

### Использование осей

``bash
//ul/li # ul > li
//ul/child::li # ul > li (то же самое)
//ul/following-sibling::li # ul ~ li
//ul/descendant-or-self::li # ul li
//ul/ancestor-or-self::li # $('ul').closest('li')
```
----
| | | | |
|------|------|------------|------|
| `//` | `ul` | `/child::` | `li` |
| Axis | Step | Axis | Step |
{.left-text}

Шаги выражения разделяются символом `/`, который обычно используется для выбора дочерних узлов. Это не всегда верно: с помощью `::` можно указать другую "ось".

### Дочерняя ось

``bash
# обе одинаковые
//ul/li/a
//child::ul/child::li/child::a
```

`child::` - это ось по умолчанию. Это обеспечивает работу `//a/b/c`.

``bash
# оба одинаковые
# это работает, потому что `child::li` является истиной.
//ul[li]
//ul[child::li]
```

``bash
# оба одинаковые
//ul[count(li) > 2]
//ul[count(child::li) > 2]
```

### Ось "спуск-или-самостоятельность

```bash
# оба одинаковы
//div//h4
//div/descendant-or-self::h4
```

`//` - это сокращение для оси `descendant-or-self::`.

``bash
# оба одинаковые
//ul//[last()]
//ul/descendant-or-self::[last()]
```

### Другие оси {.row-span-2}

| Axis | Abbrev | Notes |
|--------------------|--------|-------|
| `ancestor` | | | |
| `ancestor-or-self` | | | |

| | `attribute` | `@` | `@href` - сокращение от `attribute::href` |
| `child` | | `div` - сокращение от `child::div` |
| | `descendant` | | | |
| | `descendant-or-self` | `//` | `//` - это сокращение от `/descendant-or-self::node()/` |
| `namespace` | | | |

| `self` | `.` | `.` - это сокращение от `self::node()` |
| | `parent` | `..` | `..` - это сокращение от `parent::node()` |

| `following` | | | |
| | `следующий-сестринский` | | | | |
| `preceding` | | | |
| | `предшествующий-брат` | | | |
{.headers}

Существуют и другие оси, которые можно использовать.

### Союзы

``bash
//a | //span
```

Используйте `|` для соединения двух выражений.

XPath Дополнительные примеры {.cols-2}
-------------

### Примеры

``bash
//* # все элементы
count(//*) # подсчет всех элементов
(//h1)[1]/text() # текст первого заголовка h1
//li[span] # найти <li> с <span> внутри
                    # ...расширяется до //li[child::span]
//ul/li/...          # используйте ... для выбора родителя
```

### Найти родителя

``bash
//section[h1[@id='section-name']]
```
Находит `<секцию>`, которая непосредственно содержит `h1#section-name`.

``bash
//section[//h1[@id='section-name']]
```

Находит `<секцию>`, содержащую `h1#section-name`.
(То же самое, что и выше, но вместо child используется descendant-or-self)

### Ближайший

``bash
./ancestor-or-self::[@class="box"]
```

Работает аналогично jQuery'овскому `$().closest('.box')`.

### Атрибуты

``bash
//item[@price > 2*@discount]
```

Находит `<item>` и проверяет его атрибуты

Также см.
--------
* [Devhints](https://devhints.io/xpath) _(devhints.io)_
* [Xpath test bed](http://www.whitebeam.org/library/guide/TechNotes/xpathtestbed.rhtm) _(whitebeam.org)_




