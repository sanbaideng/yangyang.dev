---
название: HTML
дата: 2021-07-20 19:16:42
фон: bg-[#cc5534]
теги:
    - веб
категории:
    - Программирование
intro: |
    В этой шпаргалке по HTML в удобной для чтения форме перечислены общие теги HTML и HTML5.
плагины:
    - copyCode
---


Начало работы
------------

### hello.html {.col-span-2 .row-span-2}

``html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML5 Boilerplate</title>
</head>
<body>
    <h1>Здравствуй мир, здравствуй CheatSheets.zip!</h1>
</body>
</html>
```

Или попробуйте это сделать в [jsfiddle](https://jsfiddle.net/Fechin/1e4wz20b/)

### Комментарий

``html
<!-- это комментарий -->

<!--
    Или вы можете закомментировать
    большое количество строк.
-->
```


### Параграф

``html
<p>Я из CheatSheets.zip</p>
<p>Обмен быстрыми справочными шпаргалками.</p>
```
См: [Элемент Paragraph](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p)




### HTML-ссылка

``html
<a href="https://cheatsheets.zip">Чит-листы</a>
<a href="mailto:jack@abc.com">Email</a>
<a href="tel:+12345678">Call</a>
<a href="sms:+12345678&body=ha%20ha">Msg</a>
```
---

| | | |
|---|----------|-----------------------------------------------------------------|
| | | `href` | URL, на который указывает гиперссылка |
| | | `rel` | Отношение к URL, на который указывает гиперссылка |
| | | `target` | Целевое местоположение ссылки: <br/> `_self`, `_blank`, `_top`, `_parent` |
{.left-text}

См: [Атрибуты \<a>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#attributes)



### Тег изображения

``html {.wrap}
<img loading="lazy" src="https://xxx.png" alt="Опишите изображение здесь" width="400" height="400">
```
---

| | | |
|---|-----------|------------------------------------------|
| | | `src` | Обязательно, расположение изображения _(URL \| Path)_ |
| | | `alt` | Описание изображения |
| | | `width` | Ширина изображения |
| | | `height` | Высота изображения |
| | | `loading` | Как должен загружаться браузер |
{.left-text}

См: [Элемент Image Embed](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)



### Теги форматирования текста

``html
<b>Жирный текст</b>
<strong>Этот текст важен</strong>
<i>Италический текст</i>
<em>Этот текст подчеркнут</em>
<u>Подчеркнутый текст</u>
<pre>Преформатированный текст</pre>
<code>Исходный код</code>
<del>Удаленный текст</del>
<mark>Выделенный текст (HTML5)</mark>
<ins>Вставленный текст</ins>
<sup>Сделать текст надстрочным</sup>
<sub>Сделать текст подстрочным</sub>
<small>Сделать текст меньше</small>
<kbd>Ctrl</kbd>
<blockquote>Цитата текстового блока</blockquote>
```


### Заголовки
``html
<h1> Это заголовок 1 </h1>
<h2> Это заголовок 2 </h2>
<h3> Это заголовок 3 </h3>
<h4> Это заголовок 4 </h4>
<h5> Это заголовок 5 </h5>
<h6> Это заголовок 6 </h6>
```
На странице должен быть только один заголовок h1


### Разделы раздела

| | |
|-----------------|--------------------------------------|
| `<div></div>` | Раздел или секция содержимого страницы |
| `<span></span>` | Раздел текста внутри другого содержания |
| `<p></p>` | Абзац текста |
| `<br>` | Разрыв строки |
| | `<hr>` | Основная горизонтальная линия |

Эти теги используются для разделения страницы на разделы



### Inline Frame {.row-span-2}
``html {.wrap}
<iframe title="Нью-Йорк"
    width="342"
    height="306"
    id="gmap_canvas"
    src="https://maps.google.com/maps?q=2880%20Broadway,%20New%20York&t=&z=13&ie=UTF8&iwloc=&output=embed"
    scrolling="no">
</iframe>
```
#### ↓ Предварительный просмотр
<iframe title="Нью-Йорк"
    width="342"
    height="306"
    id="gmap_canvas"
    src="https://maps.google.com/maps?q=2880%20Broadway,%20New%20York&t=&z=13&ie=UTF8&iwloc=&output=embed"
    scrolling="no">
</iframe>


См: [Элемент Inline Frame](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)


### JavaScript в HTML

``html
<script type="text/javascript">
    let text = "Hello CheatSheets.zip";
    alert(text);
</script>
```


#### Внешний JavaScript

``html
<body>
    ...
    
    <script src="app.js"></script>.
</body>
```


### CSS в HTML

``html
<style type="text/css">
    h1 {
        цвет: фиолетовый;
    }
</style>
```

#### Внешняя таблица стилей

``html
<head>
...
<link rel="stylesheet" href="style.css"/>.
</head>
```



Теги HTML5
-------------

### Документ
``html
<body>
  <заголовок>
    <nav>...</nav>
  </header>
  <main>
    <h1>CheatSheets.zip</h1>
  </main>
  <footer>
    <p>©2023 CheatSheets.zip</p>
  </footer>
</body>
```


### Навигация по заголовку
``html
<header>
  <nav>
    <ul>
      <li><a href="#">Редактировать страницу</a></li>
      <li><a href="#">Twitter</a></li>
      <li><a href="#">Facebook</a></li>
    </ul>
  </nav>
</header>
```


### Теги HTML5 {.row-span-4}

| | |
|------------------------------------------------------------------------------------|----------------------------------------|
| [article](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article) | Самостоятельный контент |
| [aside](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside) | Второстепенный контент |
| [audio](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio) | Вставка звука или аудиопотока |
| [bdi](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi) | Двунаправленный элемент изоляции |
| [canvas](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas) | Рисование графики с помощью JavaScript |
| [data](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data) | Машиночитаемое содержимое |
| [datalist](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) | Набор предопределенных опций |
| [details](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) | Дополнительная информация |
| [dialog](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog) | Диалоговое окно или подокно |
| [embed](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed) | Встраивание внешнего приложения |
| [figcaption](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption) | Надпись или легенда для рисунка |
| [figure](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure) | Рисунок с иллюстрацией |
| [footer](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer) | Нижний или наименее важный колонтитул |
| [header](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header) | Верхний колонтитул или важная информация |
| [main](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main) | Основное содержание документа |
| [mark](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark) | Текст, выделенный цветом |
| [метр](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter) | Скалярное значение в известном диапазоне |
| [nav](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav) | Раздел навигационных ссылок |
| [output](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output) | Результат вычисления |
| [picture](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture) | Контейнер для нескольких источников изображений |
| [progress](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress) | Ход выполнения задачи |
| [rp](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rp) | Предоставляет обратную скобку |
| [rt](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt) | Определяет произношение символов |
| [ruby](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) | Представляет собой рубиновую аннотацию |
| [section](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section) | Группа в серии связанных материалов |
| [source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) | Ресурсы для медиа-элементов |
| | [summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary) | Резюме для элемента \<details> |
| | [template](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template) | Определяет фрагменты HTML |
| | [time](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time) | Время или дата |
| [track](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track) | Текстовые дорожки для медиа-элементов |
| [video](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video) | Встраивает видео |
| [wbr](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr) | Возможность переноса строки |


### HTML5 Video
``html {.wrap}
<video controls="" width="100%">
    <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4" type="video/mp4">.
    Извините, ваш браузер не поддерживает встроенное видео.
</video>
```
#### ↓ Предварительный просмотр
<video controls="" width="100%">
    <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4" type="video/mp4">.
    Извините, ваш браузер не поддерживает встроенное видео.
</video>


### HTML5 Audio
``html {.wrap}
<aуправление аудио
    src="https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3">
    Ваш браузер не поддерживает элемент audio.
</audio>
```
#### ↓ Предварительный просмотр
<audio controls class="w-full"
    src="https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3">
    Ваш браузер не поддерживает аудиоэлемент.
</audio>




### HTML5 Ruby
``html {.wrap}
<ruby>
  汉 <rp>(</rp><rt>hàn</rt><rp>)</rp>
  字 <rp>(</rp><rt>zì</rt><rp>)</rp>
</ruby>
```
#### ↓ Предварительный просмотр
<ruby class="mt-4 text-center text-5xl">
  汉 <rp>(</rp><rt>hàn</rt><rp>)</rp>
  字 <rp>(</rp><rt>zì</rt><rp>)</rp>
</ruby>


### HTML5 kdi
``html
<ul>
 <li>Пользователь <bdi>hrefs</bdi>: 60 баллов</li>.
 <li>Пользователь <bdi>jdoe</bdi>: 80 баллов</li>
 <li>Пользователь <bdi>إيان</bdi>: 90 баллов</li>.
</ul>
```
#### ↓ Предварительный просмотр
<ul>
 <li>Пользователь <bdi>hrefs</bdi>: 60 баллов</li>
 <li>Пользователь <bdi>jdoe</bdi>: 80 баллов</li>
 <li>Пользователь <bdi>إيان</bdi>: 90 баллов</li>.
</ul>


### Прогресс HTML5
``html
<progress value="50" max="100"></progress>
```
<progress value="50" max="100" class="w-full"></progress>


### Знак HTML5
``html
<p>Я люблю <mark>CheatSheets.zip</mark></p>
```
<p>Я люблю <mark>CheatSheets.zip</mark></p>


Таблицы HTML
--------------

### Пример таблицы {.row-span-2}
``html
<table>
    <thead>
        <tr>
            <td> имя</td>
            <td> возраст</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Роберта</td>
            <td>39</td>
        </tr>
        <tr>
            <td>Оливер</td>
            <td>25</td>
        </tr>
    </tbody>
</table>
```



### Теги HTML-таблицы {.row-span-2}

| Tag | Description |
|-----------------------------------------------------------------------------------|----------------------------------|
| [\<table>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table) | Определяет таблицу |
| [\<th>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) | Определяет ячейку заголовка в таблице |
| [\<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) | Определяет строку в таблице |
| [\<td>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td) | Определяет ячейку в таблице |
| [\<caption>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption) | Определяет надпись в таблице |
| [\<colgroup>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup) | Определяет группу столбцов |
| [\<col>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col) | Определяет столбец в таблице |
| [\<thead>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead) | Группирует содержимое заголовка |
| [\<tbody>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody) | Группирует содержимое заголовка |
| [\<tfoot>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot) | Группирует содержимое нижнего колонтитула |

### \<td> Атрибуты

| Атрибут | Описание |
|-----------|-----------------------------------------------|
| `colspan` | Количество столбцов, которые должна охватывать ячейка |
| `headers` | Одна или несколько ячеек заголовка, с которыми связана ячейка |
| `rowspan` | Количество строк, которые должна охватывать ячейка |

См: [td\#Атрибуты](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td#attributes)



### \<th>Атрибуты

| Атрибут | Описание |
|----------------------------------------------------------------------------------|-----------------------------------------------|
| `colspan` | Количество столбцов, которые должна охватывать ячейка |
| `headers` | Одна или несколько ячеек заголовка, с которыми связана ячейка |
| `rowspan` | Количество строк, которые должна охватывать ячейка |
| `abbr` | Описание содержимого ячейки |
| [scope](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th#attr-scope) | Элемент заголовка, к которому относится ячейка |

См: [th\#Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th#attributes)



Списки HTML
--------------


### Неупорядоченный список
``html
<ul>
    <li>Я - элемент</li>
    <li>Я другой элемент</li>
    <li>Я другой элемент</li>
</ul>
```
См: [Элемент неупорядоченного списка](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)


### Упорядоченный список

``html
<ol>
    <li>Я - первый элемент</li>
    <li>Я второй элемент</li>
    <li>Я третий элемент</li>
</ol>
```
См: [Элемент "Упорядоченный список"](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)


### Список определений

``html
<dl>
    <dt>Термин</dt>
    <dd>Определение термина</dd>
    <dt>Другой термин</dt>
    <dd>Определение другого термина</dd>
</dl>
```
См: [Элемент "Список описаний"](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)




HTML-формы
-----------


### Теги формы {.row-span-2}
``html
<form method="POST" action="api/login">
  <label for="mail">Электронная почта: </label>
  <input type="email" id="mail" name="mail">
  <br/>
  <label for="pw">Пароль: </label>
  <input type="password" id="pw" name="pw">
  <br/>
  <input type="submit" value="Login">
  <br/>
  <input type="checkbox" id="ck" name="ck">
  <label for="ck">Запомнить меня</label>.
</form>
```

#### ↓ Предварительный просмотр
<form method="POST" action="api/login" style="padding: 20px;">
    <label for="email">Электронная почта: </label>
    <input type="email" id="email" name="email" class="border border-slate-400 mt-2">
    <br/>
    <label for="pwd">Пароль: </label>
    <input type="password" id="pwd" name="pwd" class="border border-slate-400 mt-2">
    <br/>
    <input type="submit" value="Login" class="mt-2">
    <br/>
    <input type="checkbox" id="ck" name="ck" class="mt-2">
    <label for="ck">Запомнить меня</label>.
</form>


Элемент HTML `<form>` используется для сбора и отправки информации во внешний источник.


### Атрибут формы
| Атрибут | Описание |
|------------|-----------------------------------------------------------------------------------------------------|
| `name` | Имя формы для скриптинга |
| `action` | URL скрипта формы |
| | `method` | Метод HTTP, `POST` / `GET` _(по умолчанию)_ |
| `enctype` | Тип носителя, см. [enctype](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/enctype)|
| | `onsubmit` | Выполняется, когда форма была отправлена |
| | `onreset` | Выполняется, когда форма была сброшена |





### Теги ярлыков
``html
<!-- Вложенная этикетка -->
<label>Нажмите на меня
<input type="text" id="user" name="name"/>
</label>
```
---
``html
<!-- Атрибут 'for' -->
<label for="user">Нажмите на меня</label>
<input id="user" type="text" name="name"/>
```
``for`` в метке ссылается на атрибут ``id`` входа





### Входные теги
``html
<label for="Name">Имя:</label>
<input type="text" name="Имя" id="">
```
#### ↓ Предварительный просмотр
<form style="padding: 20px;">
    <label for="username">Имя пользователя:</label>
    <input type="text" name="username" id="username" class="border border-slate-400">
</form>

См: [HTML-теги ввода](/html#html-input-tags)


### Теги текстовой области
``html {.wrap}
<textarea rows="2" cols="30" name="адрес" id="адрес"></textarea>
```
#### ↓ Предварительный просмотр
<form style="padding: 20px;">
    <textarea rows="2" cols="30" name="адрес" id="адрес" class="border border-slate-400 "style="width: 100%"></textarea>.
</form>

Textarea - это элемент управления многострочным вводом текста



### Радиокнопки
``html
<input type="radio" name="gender" id="m">
<label for="m">Мужчина</label>
<input type="radio" name="gender" id="f">
<label for="f">женщина</label>
```
#### ↓ Предварительный просмотр
<form style="padding: 20px;">
    <input type="radio" name="gender" id="m">
    <label for="m">Мужчина</label>
    <input type="radio" name="gender" id="f">
    <label for="f">женщина</label>.
</form>

Радиокнопки используются для того, чтобы пользователь мог выбрать только один вариант



### Чекбоксы
``html
<input type="checkbox" name="s" id="soc">
<label for="soc">Футбол</label>
<input type="checkbox" name="s" id="bas">
<label for="bas">Бейсбол</label>
```
#### ↓ Предварительный просмотр
<form style="padding: 20px;">
    <input type="checkbox" name="sports" id="soccer">
    <label for="soccer">Футбол</label>
    <input type="checkbox" name="sports" id="baseball">
    <label for="baseball">Бейсбол</label>.
</form>

Флажки позволяют пользователю выбрать один или несколько вариантов



### Выберите теги
``html
<label for="city">Город:</label>
<select name="city" id="city">
    <option value="1">Сидней</option>
    <option value="2">Мельбурн</option>
    <option value="3">Кромвель</option>.
</select>
```

#### ↓ Предварительный просмотр
<form style="padding: 20px">
    <label for="city">Город:</label>
    <select name="city" id="city" class="border border-slate-400">
        <option value="1">Сидней</option>
        <option value="2">Мельбурн</option>
        <option value="3">Кромвель</option>.
    </select>
</form>

Поле выбора представляет собой выпадающий список вариантов



### Теги полей
``html
<fieldset>
    <legend>Ваш любимый монстр</legend>
    <input type="radio" id="kra" name="m">
    <label for="kraken">Кракен</label><br/>
    <input type="radio" id="sas" name="m">
    <label for="sas">Сасквотч</label>.
</fieldset>
```
#### ↓ Предварительный просмотр
<form style="padding: 20px">
    <fieldset class="border border-slate-400" style="padding: 20px">
        <legend>Ваш любимый монстр</legend>
        <input type="radio" id="kra" name="monster">
        <label for="kra">Кракен</label><br/>
        <input type="radio" id="sas" name="monster">
        <label for="sas">Сасквотч</label>.
    </fieldset>
</form>




### Теги Datalist(HTML5)
``html
<label for="b">Выберите браузер: </label>
<input list="list" id="b" name="browser"/>
<datalist id="list">
  <option value="Chrome">
  <option value="Firefox">
  <option value="Internet Explorer">
  <option value="Opera">
  <option value="Safari">
  <option value="Microsoft Edge">
</datalist>
```

#### ↓ Предварительный просмотр
<form style="padding: 20px">
    <label for="myBrowser">Выберите браузер:</label>
    <input list="browsers" id="myBrowser" name="myBrowser" class="border border-slate-400"/>
    <datalist id="browsers">
      <option value="Chrome">
      <option value="Firefox">
      <option value="Internet Explorer">
      <option value="Opera">
      <option value="Safari">
      <option value="Microsoft Edge">
    </datalist>
</form>




### Кнопки отправки и сброса
``html
<form action="register.php" method="post">
  <label for="foo">Имя:</label>
  <input type="text" name="name" id="foo">
  <input type="submit" value="Отправить">
  <input type="reset" value="Reset">
</form>
```
#### ↓ Предварительный просмотр
<form action="register.php" method="post" style="padding: 20px">
    <label for="name">Имя:</label>
    <input type="text" name="name" id="name" class="border border-slate-400">
    <input type="submit" value="Отправить">
    <input type="reset" value="Reset">
</form>

`Отправить` данные на сервер; `Сбросить` значения по умолчанию





Теги ввода HTML {.cols-2}
-----------


### Атрибуты ввода {.row-span-2}
Тег input представляет собой пустой элемент, определяющий конкретный тип информации о поле, которую необходимо получить от пользователя.
``html {.wrap}
<input type="text" name="?" value="?" minlength="6" required />
```

----

| - | | |
|---|-------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| | | `type="..."` | Тип вводимых данных |
| | | `value="..."` | Значение по умолчанию |
| | | `name="..."` | Используется для описания этих данных в HTTP-запросе |
| | | `id="..."` | Уникальный идентификатор, который используется другими элементами HTML |
| | | `readonly` | Запрещает пользователю изменять данные |
| | | `disabled` | Прекращает любое взаимодействие |
| | | `checked` | Радио- или чекбокс выбирается или нет |
| | | `required` | Быть обязательным, См. [required](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/required#example)|
| | | `placeholder="..."` | Добавляет временный, См. [::placeholder](https://developer.mozilla.org/en-US/docs/Web/CSS/::placeholder#examples)|
| | | `autocomplete="off"` | Отключить автозавершение |
| | | `autocapitalize="none"` | Отключить автоматическую капитализацию |
| | | `inputmode="..."` | Отображение определенной клавиатуры, см. [inputmode](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode) |
| | | `list="..."` | Идентификатор связанного [datalist](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) |
| | | `maxlength="..."` | Максимальное количество символов |
| | | `minlength="..."` | Минимальное количество символов |
| | | `min="..."` | Минимальное числовое значение диапазона и числа |
| | | `max="..."` | Максимальное числовое значение диапазона и числа |
| | | `step="..."` | Как будет увеличиваться число в диапазоне & number |
| | | `pattern="..."` | Задает [регулярное выражение](/regex), см. [pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/pattern) |
| | | `автофокус` | Быть сфокусированным |
| | | `spellcheck` | Выполнить проверку правописания |
| | | `multiple` | Разрешать ли значения [multiple](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/multiple) |
| | | `accept=""` | Ожидаемый тип файла в элементах управления загрузкой [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file) |
{.left-text}

Также см: [Атрибуты для элемента \<input>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#attributes)


### Типы ввода

| | |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `type="checkbox"` | <input type="checkbox" class="border border-slate-400"> | `type="checkbox"` | <input type="checkbox" class="border border-slate-400">.
| `type="radio"` | <input type="radio" class="border border-slate-400"> |
| `type="file"` | <input type="file" class="border border-slate-400"> |
| `type="hidden"` | <input type="hidden" class="border border-slate-400"> |
| `type="text"` | <input type="text" class="border border-slate-400"> |
| `type="password"` | <input type="password" class="border border-slate-400"> |
| `type="image"` | <input type="image" src="https://raw.githubusercontent.com/mdn/learning-area/master/html/forms/image-type-example/login.png" width="70"> |
| `type="reset"` | <input type="reset" class="border border-slate-400"> |
| `type="button"` | <input type="button" class="border border-slate-400">Кнопка</input> |
| `type="submit"` | <input type="submit" class="border border-slate-400"> |

#### Новые типы ввода в HTML5
| | |
|-------------------------|---------------------------------------------------------------------|
| `type="color"` | <input type="color" value="#0FB881" class="border border-slate-400"> | | `type="color"` | <input type="color" value="#0FB881" class="border border-slate-400">.
| `type="date"` | <input type="date" class="border border-slate-400"> |
| `type="time"` | <input type="time" class="border border-slate-400"> |
| `type="month"` | <input type="month" class="border border-slate-400"> | |
| `type="datetime-local"` | <input type="datetime-local" class="border border-slate-400"> |
| `type="week"` | <input type="week" class="border border-slate-400"> |
| `type="email"` | <input type="email" class="border border-slate-400"> |
| `type="tel"` | <input type="tel" class="border border-slate-400"> |
| `type="url"` | <input type="url" class="border border-slate-400"> |
| `type="number"` | <input type="number" class="border border-slate-400"> |
| `type="search"` | <input type="search" class="border border-slate-400"> |
| `type="range"` | <input type="range" class="border border-slate-400"> |


### Входные CSS-селекторы

| | |
|---------------|---------------------------|
| `input:focus` | Когда клавиатура сфокусирована |
См: [Псевдоклассы ввода](/css#input-pseudo-classes)


Мета-теги HTML {.cols-2}
-----------

### Мета-теги {.row-span-3}

Мета-тег описывает метаданные в HTML-документе. Он поясняет дополнительные сведения о HTML.


``html
<meta charset="utf-8">
```

``html
<!-- Заголовок -->
<title>---</title>
<meta property="og:title" content="---">
<meta name="twitter:title" content="---">
```
---

``html
<!-- url -->
<link rel="canonical" href="https://---">
<meta property="og:url" content="https://---">
<meta name="twitter:url" content="https://---">
```
---

``html
<!-- описание -->
<meta name="description" content="---">
<meta property="og:description" content="---">
<meta name="twitter:description" content="---">
```
---

``html
<!-- изображение -->
<meta property="og:image" content="https://---">
<meta name="twitter:image" content="https://---">
```
---

``html
<!-- ua -->
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
```
---

``html
<!-- viewport -->
<meta name="viewport" content="width=device-width">
<meta name="viewport" content="width=1024">
```




### Open Graph
``html
<meta property="og:type" content="website">
<meta property="og:locale" content="en_CA">
<meta property="og:title" content="HTML cheatsheet">
<meta property="og:url" content="https://cheatsheets.zip/html">
<meta property="og:image" content="https://xxx.com/image.jpg">
<meta property="og:site_name" content="Название вашего сайта">
<meta property="og:description" content="Описание этой страницы">
```
Используется Facebook, Instagram, Pinterest, LinkedIn и др.


### Twitter Cards
``html
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@FechinLi">
<meta name="twitter:title" content="HTML шпаргалка">
<meta name="twitter:url" content="https://cheatsheets.zip/html">
<meta name="twitter:description" content="Описание этой страницы"> <meta name="twitter:description" content="Описание этой страницы">
<meta name="twitter:image" content="https://xxx.com/image.jpg">
```
См: [Документация по картам Twitter](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/summary)



### Геотаггинг
``html
<meta name="МБР" content="45.416667,-75.7">
<meta name="geo.position" content="45.416667;-75.7">
<meta name="geo.region" content="ca-on">
<meta name="geo.placename" content="Ottawa">
```
См: [Geotagging](https://en.wikipedia.org/wiki/Geotagging#HTML_pages)



Также см.
--------

- [Спецификация HTML 4.01](https://www.w3.org/TR/REC-html40/cover.html#minitoc) _(w3.org)_
