---
Название: CSS 3
дата: 2020-12-25 20:22:47
фон: bg-[#3473b5]
теги:
    - веб
    - css
    - стиль
категории:
    - Программирование
intro: |
    Это краткая шпаргалка по CSS, в которой перечислены синтаксис селекторов, свойства, единицы измерения и другие полезные сведения.
плагины:
    - copyCode
---



Начало работы
------------

### Введение {.row-span-3}
CSS обладает богатыми возможностями и представляет собой нечто большее, чем просто компоновка страниц.

#### Внешняя таблица стилей
``html {.wrap}
<link href="./path/to/stylesheet/style.css" rel="stylesheet" type="text/css">
```

#### Внутренняя таблица стилей
``html
<style>
тело {
    background-color: linen;
}
</style>
```

#### Инлайн-стили
``html {.wrap}
<h2 style="text-align: center;">Выравнивание текста по центру</h2>

<p style="color: blue; font-size: 18px;">Синий, 18-пунктовый текст</p>
```


### Добавить класс

``html
<div class="classname"></div>
<div class="class1 ... classn"></div>
```
Поддержка нескольких классов в одном элементе.



### !important

``css
.post-title {
    color: blue !important;
}
```

Отменяет все предыдущие правила стилизации.


### Селектор

``css
h1 { }
#job-title { }
div.hero { }
div > p { }
```

См: [Selectors](#css-selectors)



### Цвет текста

``css
color: #2a2aff;
цвет: зеленый;
color: rgb(34, 12, 64, 0.6);
color: hsla(30 100% 50% / 0.6);
```

См: [Цвета](#css-colors)




### Фон

``css
background-color: blue;
background-image: url("nyan-cat.gif");
background-image: url("../image.png");
```

См: [Фоны](#css-backgrounds)



### Шрифт

``css
.page-title {
    font-weight: bold;
    font-size: 30px;
    font-family: "Courier New";
}
```
См: [Шрифты](#css-fonts)




### Положение

``css
.box {
    position: relative;
    top: 20px;
    left: 20px;
}
```

См. также: [Position](https://learn-the-web.algonquindesign.ca/topics/css-layout-cheat-sheet/)



### Анимация
``css

анимация: 300 мс линейная 0 с бесконечная;

анимация: bounce 300ms linear infinite;

```
См: [Анимация](#css-animation)


### Комментарий
``css

/* Это однострочный комментарий */

/* Это
   многострочный комментарий */
```


### Flex-макет

``css
div {
    display: flex;
    justify-content: center;
}
div {
    display: flex;
    justify-content: flex-start;
}
```

См: [Flexbox](#css-flexbox) | [Flex Tricks](#css-flexbox-tricks)




### Разметка сетки

``css
#container {
  display: grid;
  grid: repeat(2, 60px) / auto-flow 80px;
}

#container > div {
  background-color: #8ca0ff;
  ширина: 50px;
  height: 50px;
}
```

См: [Grid Layout](#css-grid-layout)



### Переменные и счетчики
``css
счетчик-установка: подраздел;
счетчик-инкремент: подраздел;
счетчик-сброс: подраздел 0;

:root {
  --bg-color: brown;
}
element {
  background-color: var(--bg-color);
}
```

См: [Динамический контент](#css-dynamic-content)


Селекторы CSS
-----------


### Примеры {.row-span-2}

#### Селектор групп
``css
h1, h2 {
    цвет: красный;
}
```
#### Селектор цепочки
``css
h3.section-heading {
    цвет: синий;
}
```
#### Селектор атрибутов
``css
div[attribute="SomeValue"] {
    background-color: red;
}
```
#### Селектор первого ребенка
``css
p:first-child {
    font-weight: bold;
}
```
#### Селектор отсутствия детей
``css
.box:empty {
  фон: lime;
  высота: 80px;
  width: 80px;
}
```


### Основной

| | |
|--------------|-----------------------------|
| `*` | Все элементы |
| `div` | Все теги div |
| | `.classname` | Все элементы с классом |
| `#idname` | Элемент с идентификатором |
| `div,p` | Все div и параграфы |
| `#idname *` | Все элементы внутри #idname |
См. также: [Тип](https://developer.mozilla.org/en-US/docs/Web/CSS/Type_selectors) / [Класс](https://developer.mozilla.org/en-US/docs/Web/CSS/Class_selectors) / [ID](https://developer.mozilla.org/en-US/docs/Web/CSS/ID_selectors) / [Универсальный](https://developer.mozilla.org/en-US/docs/Web/CSS/Universal_selectors) селекторы


### Комбинаторы

| Селектор | Описание |
|-----------------|---------------------------------------|
| `div.classname` | Div с определенным именем класса |
| `div#idname` | Div с определенным ID |
| `div p` | Абзацы внутри div'ов |
| `div > p` | Все теги p<br>_на один уровень в глубину div_ |
| `div + p` | P-теги сразу после div |
| `div ~ p` | P-теги, которым предшествует div |
См. также: [Смежные](https://developer.mozilla.org/en-US/docs/Web/CSS/Adjacent_sibling_combinator) / [Родные](https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_combinator) / [Детские](https://developer.mozilla.org/en-US/docs/Web/CSS/Child_combinator) селекторы



### Селекторы атрибутов

| | |
|----------------------|------------------------------------|
| | `a[target]` | С атрибутом <yel>target</yel> |
| | `a[target="_blank"]` | Открыть в новой вкладке |
| | `a[href^="/index"]` | Начинается с <yel>/index</yel> |
| `[class|="chair"]` | Начинается с <yel>chair</yel> |
| | `[class*="chair"]` | Содержит <yel>chair</yel> |
| | `[title~="chair"]` | Содержит слово <yel>chair</yel> |
| `a[href$=".doc"]` | Заканчивается на <yel>.doc</yel> |
| `[type="button"]` | Указанный тип |

См. также: [Селекторы атрибутов](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors)




### Псевдоклассы действий пользователя
| | |
|--------------|-------------------------|
| `a:link` | Ссылка в нормальном состоянии |
| | `a:active ` | Ссылка в состоянии нажатия |
| | `a:hover ` | Ссылка при наведении на нее мыши |
| | `a:visited ` | Посещенная ссылка |



### Псевдоклассы
| | |
|-------------------|-----------------------------------------------------------------------------------------|
| `p::after` | Добавить содержимое после p |
| `p::before` | Добавить содержимое перед p |
| `p::first-letter` | Первая буква в p |
| `p::first-line` | Первая строка в p |
| `::selection` | Выбранная пользователем |
| `::placeholder` | Атрибут [Placeholder](https://developer.mozilla.org/en-US/docs/Web/CSS/::placeholder) |
| `:root` | Корневой элемент документа |
| | `:target` | Выделить активный якорь |
| | `div:empty` | Элемент без дочерних элементов |
| | `p:lang(en)` | P с атрибутом языка en |
| `:not(span)` | Элемент, не являющийся span |



### Входные псевдоклассы
| | |
|-----------------------|---------------------------------------------------------------------------------------------|
| `input:checked` | Проверенные входы |
| `input:disabled` | Отключенные входы |
| `input:enabled` | Включенные входы |
| `input:focus` | Вход имеет фокус |
| `input:in-range` | Значение в диапазоне |
| `input:out-of-range` | Значение входа вне диапазона |
| `input:valid` | Ввод с действительным значением |
| `input:invalid` | Ввод с недопустимым значением |
| `input:optional` | Нет обязательного атрибута |
| `input:required` | Ввод с обязательным атрибутом |
| `input:read-only` | С атрибутом readonly |
| `input:read-write` | Без атрибута readonly |
| `input:indeterminate` | С состоянием [indeterminate](https://developer.mozilla.org/en-US/docs/Web/CSS/:indeterminate)|



### Структурные псевдоклассы
| | |
|-------------------------|----------------------------|
| `p:first-child` | Первый ребенок |
| `p:last-child` | Последний ребенок |
| `p:first-of-type` | Первый из некоторого типа |
| | `p:last-of-type` | Last of some type |
| | `p:nth-child(2)` | Второй ребенок своего родителя |
| | `p:nth-child(3n42)` | Формула Nth-child (an + b)|
| `p:nth-last-child(2)` | Второй ребенок сзади |
| `p:nth-of-type(2)` | Второй p своего родителя |
| `p:nth-last-of-type(2)` | ...сзади |
| | `p:only-of-type` | Уникальность своего родителя |
| `p:only-child` | Единственный ребенок своего родителя |



Шрифты CSS
------


### Свойства {.row-span-3}

| Свойство | Описание |
|-------------------|-----------------|
| `font-family:` | \<font> <fontN> |
| `font-size:` | \<size> |
| `letter-spacing:` | \<size> |
| `line-height:` | \<number> |

| `font-weight:` | \<number> / bold / normal |
| `font-style:` | \<номер> / курсив / нормальный |
| `text-decoration:` | underline / none |

| ``text-align:`` | left / right<br>center / justify |
| ``text-transform:`` | capitalize / uppercase / lowercase |
{.left-text}

См. также: [Font](https://developer.mozilla.org/en-US/docs/Web/CSS/font)

### Сокращение {.secondary .col-span-2}

| style | weight | size (required) | | | line-height | family |
|---------|----------|--------|-----------------|-----|-------------|-------------------|
| `font:` | `italic` | `400` | `14px` | `/` | `1.5` | `sans-serif` |
| | style | weight | size (required) | | | line-height | family (required) |

### Пример

``css
font-family: Arial, sans-serif;
font-size: 12pt;
letter-spacing: 0.02em;
```


### Case {.row-span-2}

``css

/* Hello */
text-transform: capitalize;

/* HELLO */
text-transform: uppercase;

/* привет */
text-transform: lowercase;
```


### @font-face

``css
@font-face {
    font-family: 'Glegoo';
    src: url('../Glegoo.woff');
}
```




Цвета CSS
------------


### Именованный цвет

``css
цвет: красный;
цвет: оранжевый;
цвет: tan;
цвет: rebeccapurple;
```


### Шестнадцатеричный цвет

``css
color: #090;
цвет: #009900;
color: #090a;
цвет: #009900aa;
```



### rgb() Цвета

``css
color: rgb(34, 12, 64, 0.6);
color: rgba(34, 12, 64, 0.6);
color: rgb(34 12 64 / 0.6);
color: rgba(34 12 64 / 0.3);
color: rgb(34.0 12 64 / 60%);
color: rgba(34.6 12 64 / 30%);
```


### Цвета HSL

```css
color: hsl(30, 100%, 50%, 0.6);
color: hsla(30, 100%, 50%, 0.6);
color: hsl(30 100% 50% / 0.6);
color: hsla(30 100% 50% / 0.6);
color: hsl(30.0 100% 50% / 60%);
color: hsla(30.2 100% 50% / 60%);
```

### Другое
```css
цвет: наследуется;
цвет: начальный;
color: unset;
цвет: прозрачный;

color: currentcolor; /* ключевое слово */
```







Фоны CSS
----------

### Свойства {.row-span-2}

| Свойство | Описание |
|---------------|---------------|
| `background:` | _(Shorthand)_ |

| `background-color:` | См: [Цвета](#css-colors)|
| `background-image:` | url(...) |
| `background-position:` | left/center/right<br/>top/center/bottom |
| `background-size:` | cover X Y |
| `background-clip:` | border-box<br/>padding-box<br/>content-box |
| `background-repeat:` | no-repeat<br/>repeat-x<br/>repeat-y |
| | `background-attachment:` | scroll/fixed/local |
{.left-text}

### Сокращение {.secondary .col-span-2}

| color | image | positionX | positionY | | size | repeat | attachment |
|---------------|--------|--------------|-----------|-----------|-----|----------------|-------------|------------|
| `background:` | `#ff0` | `url(a.jpg)` | `left` | `top` | `/` | `100px` `auto` | `no-repeat` | `fixed;` | |
| `background:` | `#abc` | `url(b.png)` | `center` | `center` | `/` | `cover` | `repeat-x` | `local;` |
| | color | image | posX | posY | | size | repeat | attach...   |

### Примеры {.col-span-2}

``css {.wrap}
background: url(img_man.jpg) no-repeat center;

background: url(img_flwr.gif) right bottom no-repeat, url(paper.gif) left top repeat;

background: rgb(2,0,36);
background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(13,232,230,1) 35%, rgba(0,212,255,1) 100%);
```




CSS Модель коробки
------------


### Максимумы/минимумы

``css
.column {
    max-width: 200px;
    ширина: 500px;
}
```
См. также: [max-width](https://developer.mozilla.org/en-US/docs/Web/CSS/max-width) / [min-width](https://developer.mozilla.org/en-US/docs/Web/CSS/min-width) / [max-height](https://developer.mozilla.org/en-US/docs/Web/CSS/max-height) / [min-height](https://developer.mozilla.org/en-US/docs/Web/CSS/min-height)



### Margin / Padding

``css
.block-one {
    margin: 20px;
    padding: 10px;
}
```
См. также: [Margin](https://developer.mozilla.org/en-US/docs/Web/CSS/margin) / [Padding](https://developer.mozilla.org/en-US/docs/Web/CSS/padding)


### Размер ящика

``css
.container {
    box-sizing: border-box;
}
```
См. также: [Box-sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Box-sizing)



### Видимость

``css
.invisible-elements {
    видимость: скрытый;
}
```
См. также: [Видимость](https://developer.mozilla.org/en-US/docs/Web/CSS/visibility)


### Ключевое слово Auto

``css
div {
    margin: auto;
}
```
См. также: [Margin](https://developer.mozilla.org/en-US/docs/Web/CSS/margin)


### Переполнение

``css
.small-block {
    overflow: scroll;
}
```
См. также: [Переполнение](https://developer.mozilla.org/en-US/docs/Web/CSS/overflow)




CSS-анимация {.cols-5}
---------


### Короткое обозначение {.col-span-5 .secondary}

| | name | duration | timing-function | delay | count | direction | fill-mode | play-state |
|--------------|----------|----------|-----------------|---------|------------|---------------------|-----------|------------|
| `анимация:` | `bounce` | `300ms` | `linear` | `100ms` | `infinite` | `alternate-reverse` | `both` | `reverse` |
| | name | duration | timing-function | delay | count | direction | fill-mode | play-state |

### Свойства {.row-span-2 .col-span-2}

| Свойство | Значение |
|------------------------------|--------------------------------------------------------|
| `анимация:` | _(сокращение)_ |
| `animation-name:` | \<name> |
| `animation-duration:` | \<time>ms |
| `animation-timing-function:` | ease / linear / ease-in / ease-out / ease-in-out |
| ``animation-delay:`` | \<time>ms |
| ``animation-iteration-count:`` | infinite / \<number> |
| ``направление анимации`` | нормальное / обратное / альтернативное / альтернативно-обратное |
| ``animation-fill-mode:`` | none / forward / backwards / both / initial / inherit |
| ``animation-play-state:`` | normal / reverse / alternate / alternate-reverse |
{.left-text}

См. также: [Анимация](https://developer.mozilla.org/en-US/docs/Web/CSS/animation)


### Пример {.col-span-3}

``css
/* @keyframes duration | timing-function | delay |
   iteration-count | direction | fill-mode | play-state | name */
анимация: 3s ease-in 1s 2 reverse both paused slidein;

/* @keyframes duration | timing-function | delay | name */
анимация: 3s linear 1s slidein;

/* @keyframes duration | name */
анимация: 3s slidein;

анимация: 4s linear 0s infinite alternate move_eye;
анимация: bounce 300ms linear 0s infinite normal;
анимация: bounce 300ms linear infinite;
анимация: bounce 300ms linear infinite alternate-reverse;
анимация: bounce 300ms linear 2s infinite alternate-reverse forwards normal;
```

### Javascript Event {.col-span-3}

``js
.one('webkitAnimationEnd oanimationend msAnimationEnd animationend')
```



CSS Flexbox {.cols-2}
-------


### Простой пример

``css
.container {
  display: flex;
}
```

``css
.container > div {
  flex: 1 1 auto;
}
```

### Контейнер {.row-span-2}

.container {

``css
  display: flex;
  display: inline-flex;
```

```css
  flex-direction: row; /* ltr - по умолчанию */
  flex-direction: row-reverse; /* rtl */
  flex-direction: column; /* top-bottom */
  flex-direction: column-reverse; /* bottom-top */
```

``css
  flex-wrap: nowrap; /* однострочный */
  flex-wrap: wrap; /* многострочный */
```

```css
  align-items: flex-start; /* вертикальный выравнивание по верху */
  align-items: flex-end; /* вертикальный выравнивание по низу */
  align-items: center; /* вертикальный выравнивание по центру */
  align-items: stretch; /* одинаковая высота для всех (по умолчанию) */
```

```css
  justify-content: flex-start; /* [xxx ] */
  justify-content: center; /* [ xxx ] */
  justify-content: flex-end; /* [ xxx] */
  justify-content: space-between; /* [x x x] */
  justify-content: space-around; /* [ x x x ] */
  justify-content: space-evenly; /* [ x x x ] */
```

}

### Child

.container > div {

``css
  /* Это: */
  flex: 1 0 auto;

  /* Эквивалентно этому: */
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: auto;
```

``css
  order: 1;
```

``css
  align-self: flex-start; /* left */
  margin-left: auto; /* right */
```

}


Приемы CSS Flexbox
--------------

### Вертикальный центр

``css
.container {
  display: flex;
}

.container > div {
  width: 100px;
  высота: 100px;
  margin: auto;
}
```

### Вертикальный центр (2)

``css
.container {
  display: flex;

  /* вертикальный */
  align-items: center;

  /* горизонтальный */
  justify-content: center;
}
```

### Переупорядочивание

``css
.container > .top {
 порядок: 1;
}

.container > .bottom {
 порядок: 2;
}
```

### Мобильная верстка


```css
.container {
  display: flex;
  flex-direction: column;
}

.container > .top {
  flex: 0 0 100px;
}

.container > .content {
  flex: 1 0 auto;
}
```

Верхний бар фиксированной высоты и область содержимого динамической высоты.

### Таблицеподобный {.col-span-2}

``css

.container {
  display: flex;
}


/* значения 'px' здесь - это просто предлагаемые проценты */
.container > .checkbox { flex: 1 0 20px; }
.container > .subject { flex: 1 0 400px; }
.container > .date { flex: 1 0 120px; }
```

Таким образом, создаются колонки, имеющие разную ширину, но размеры которых зависят от обстоятельств.
в зависимости от обстоятельств.

### Вертикальный


``css
.container {
  align-items: center;
}
```

Вертикально центрирует все элементы.

### Левый и правый {.col-span-2}

``css
.menu > .left { align-self: flex-start; }
.menu > .right { align-self: flex-end; }
```




CSS Grid Layout
------------


### Колонки шаблона сетки

``css
#grid-container {
    display: grid;
    ширина: 100px;
    grid-template-columns: 20px 20% 60%;
}
```


### fr Относительная единица измерения

``css
.grid {
    display: grid;
    width: 100px;
    grid-template-columns: 1fr 60px 1fr;
}

```


### Зазор между сетками

```css
/* Расстояние между строками составляет 20px*/
/*Расстояние между столбцами 10px*/
#grid-container {
    display: grid;
    grid-gap: 20px 10px;
}
```


### CSS Сетка уровней блоков

``css
#grid-container {
    display: block;
}
```


### CSS grid-row

Синтаксис CSS:
- grid-row: grid-row-start / grid-row-end;
#### Пример
``css
.item {
    grid-row: 1 / span 2;
}
```


### CSS Inline Level Grid

``css
#grid-container {
    display: inline-grid;
}
```


### minmax() Функция

```css {.wrap}
.grid {
    display: grid;
    grid-template-columns: 100px minmax(100px, 500px) 100px;
}

```


### grid-row-start & grid-row-end

Синтаксис CSS:
- grid-row-start: auto|row-line;<br>
- grid-row-end: auto|row-line|span n;

#### Пример
``css
grid-row-start: 2;
grid-row-end: span 2;
```


### CSS grid-row-gap

``css
grid-row-gap: length;
```
Любое законное значение длины, например px или %. По умолчанию используется значение 0


### CSS grid-area

``css
.item1 {
    grid-area: 2 / 1 / span 2 / span 3;
}
```


### Обоснование элементов

```css
#container {
    display: grid;
    justify-items: center;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr 1fr 1fr;
    grid-gap: 10px;
}
```

### CSS grid-template-areas

``css
.item {
    grid-area: nav;
}
.grid-container {
    display: grid;
    grid-template-areas:
    'nav nav . .'
    'nav nav . .';
}
```


### Обосновать себя

```css
#grid-container {
    display: grid;
    justify-items: start;
}

.grid-items {
    justify-self: end;
}
```
Элементы сетки позиционируются справа (в конце) от строки.

### Выравнивание элементов

``css
#container {
    display: grid;
    align-items: start;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr 1fr 1fr;
    grid-gap: 10px;
}
```



Динамическое содержимое CSS
------------

### Переменная

Определение переменной CSS
``css
:root {
  --first-color: #16f;
  --second-color: #ff7;
}
```
Использование переменных
``css
#firstParagraph {
  background-color: var(--first-color);
  color: var(--second-color);
}
```
См. также: [CSS Variable](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)

### Счетчик

``css
/* Установить значение "my-counter" равным 0 */
counter-set: my-counter;
```

```css
/* Увеличение "my-counter" на 1 */
counter-increment: my-counter;
```

```css
/* Уменьшение "my-counter" на 1 */
counter-increment: my-counter -1;
```

```css
/* Сбросить значение "my-counter" в 0 */
counter-reset: my-counter;
```

См. также: [Counter set](https://developer.mozilla.org/en-US/docs/Web/CSS/counter-set)

### Использование счетчиков
``css
body { counter-reset: section; }

h3::before {
  counter-increment: section;
  content: "Раздел.", counter(section);
}
```

``css
ol {
  counter-reset: section;
  list-marker-type: none;
}

li::before {
  счетчик-инкремент: section;
  content: counters(section, ".") " ";
}
```


Хитрости Css 3
------------

### Сглаживание полосы прокрутки
``css
html {
    scroll-behavior: smooth;
}
```
[Нажмите на меня](#css-getting-started), страница будет плавно прокручиваться до раздела Getting started




См. также {.cols-1}
---------

- [CSS selectors cheatsheet](https://frontend30.com/css-selectors-cheatsheet/) _(frontend30.com)_
- [MDN: Using CSS flexbox](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Flexible_boxes)
- [Ultimate flexbox cheatsheet](http://www.sketchingwithcss.com/samplechapter/cheatsheet.html)
- [GRID: простая визуальная шпаргалка](http://grid.malven.co/)
- [CSS Tricks: A Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [Поддержка браузеров](https://caniuse.com/#feat=css-grid)
