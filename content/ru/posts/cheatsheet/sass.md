---
Название: Sass
дата: 2020-12-20 22:15:43
background: bg-[#ba6993]
label: CSS
теги:
    - css
категории:
    - Программирование
intro: |
      Это краткая шпаргалка, в которой перечислены наиболее полезные возможности [SASS](https://sass-lang.com).
плагины:
    - copyCode
---

Основы Sass
--------

### Введение

- [Документация](https://sass-lang.com/documentation) _(sass-lang.com)_
- [Learn X in Y minutes](https://learnxinyminutes.com/docs/sass/) _(learnxinyminutes.com)_


### Переменные

```scss
$defaultLinkColor: #46EAC2;

a {
  color: $defaultLinkColor;
}
```

### Интерполяция строк

```scss
$wk: -webkit-;

.rounded-box {
  #{$wk}border-radius: 4px;
}
```



### Комментарии

``css
/*
 Блочные комментарии
 Блочные комментарии
 Блочные комментарии
*/

// Комментарии к строкам
```




### Миксины

```css
@mixin heading-font {
    font-family: sans-serif;
    font-weight: bold;
}
h1 {
    @include heading-font;
}
```
См: [Миксины](#sass-mixins)



### Вложенность {.row-span-2}

```css
.markdown-body {
    a {
      цвет: синий;
      &:hover {
        цвет: красный;
      }
    }
}
```

#### к свойствам
```scss
text: {
    // как text-align: center
    align: center;
    // как text-transform: uppercase
    transform: uppercase;
}
```


### Расширение

```scss
.button {
    ---
}
```

``css
.push-button {
    @extend .button;
}
```

### @import

```scss
@import './other_sass_file';
@import '/code', 'lists';

// Обычный CSS @imports
@import "theme.css";
@import url(theme);
```

Расширение `.sass` или `.sass` является необязательным.


Миксины Sass
------


### Параметры

```css.
@mixin font-size($n) {
    font-size: $n * 1.2em;
}
```

```scss
body {
    @include font-size(2);
}
```

### Значения по умолчанию

```scss
@mixin pad($n: 10px) {
    padding: $n;
}
```

```scss
body {
    @include pad(15px);
}
```

### Переменная по умолчанию

```scss
$default-padding: 10px;

@mixin pad($n: $default-padding) {
    padding: $n;
}

body {
    @include pad(15px);
}
```


Функции Sass Color {.cols-2}
--------

### rgba

``css
rgb(100, 120, 140)
rgba(100, 120, 140, .5)
rgba($color, .5)
```

### Смешивание

```scss
mix($a, $b, 10%) // 10% a, 90% b
```

### Модификация HSLA

```scss
затемнить($color, 5%)
lighten($color, 5%)
```

```scss
saturate($color, 5%)
desaturate($color, 5%)
grayscale($color)
```

```css
adjust-hue($color, 15deg)
complement($color) // как adjust-hue(_, 180deg)
invert($color)
```

```css
fade-in($color, .5) // aka opacify()
fade-out($color, .5) // она же transparentize()
rgba($color, .5) // устанавливает альфу на .5
```

### Получение индивидуальных значений

#### HSLA

```scss
hue($color) // 0deg..360deg
насыщенность($color) // 0%..100%
светлота($color) // 0%..100%
alpha($color) // 0..1 (aka opacity())
```

#### RGB

```scss
красный($color) // 0..255
зеленый($color)
синий($color)
```

См: [hue()](http://sass-lang.com/documentation/Sass/Script/Functions.html#hue-instance_method), [red()](http://sass-lang.com/documentation/Sass/Script/Functions.html#red-instance_method)

### Корректировки

```css''
// Изменение на фиксированную величину
adjust-color($color, $blue: 5)
adjust-color($color, $lightness: -30%) // затемнение(_, 30%)
adjust-color($color, $alpha: -0.4) // затухание(_, .4)
adjust-color($color, $hue: 30deg) // adjust-hue(_, 15deg)
```

```css
// Изменение через процент
scale-color($color, $lightness: 50%)
```

```scss
// Полностью изменяет одно свойство
change-color($color, $hue: 180deg)
change-color($color, $blue: 250)
```

Поддерживаются: `$red`, `$green`, `$blue`, `$hue`, `$saturation`, `$lightness`, `$alpha`

Sass Другие функции {.cols-2}
--------

### Строки

```css
unquote('hello')
цитата(hello)
```

```scss
to-upper-case(hello)
to-lower-case(hello)
```

```scss
str-length(hello world)
str-slice(hello, 2, 5) // "ello" - он основан на 1, а не на 0
str-insert("abcd", "X", 1) // "Xabcd"
```

### Единицы

```scss
unit(3em) // 'em'
unitless(100px) // false
```

### Числа

```scss
floor(3.5)
ceil(3.5)
round(3.5)
abs(3.5)
```

```css
min(1, 2, 3)
max(1, 2, 3)
```

```scss
percentage(.5) // 50%
random(3) // 0..3
```

### Misc

```scss
variable-exists(red) // проверяет наличие $red
mixin-exists(red-text) // проверяет наличие @mixin red-text
function-exists(redify)
```

```css
global-variable-exists(red)
```

```scss
selector-append('.menu', 'li', 'a') // .menu li a
selector-nest('.menu', '&:hover li') // .menu:hover li
selector-extend(...)
selector-parse(...)
selector-replace(...)
selector-unify(...)
```

Проверки Sass Feature {.cols-2}
--------

### Проверка возможностей

```css
feature-exists(global-variable-shadowing)
```

### Особенности

* global-variable-shadowing
* extend-selector-pseudoclass
* units-level-3
* at-error

Циклы Sass
--------

### Циклы For

```scss
@for $i from 1 to 4 {
    .item-#{$i} { left: 20px * $i; }
}
```

### Циклы Each (простые)

```css
$menu-items: home about contact;

@each $item in $menu-items {
    .photo-#{$item} {
      background: url('#{$item}.jpg');
    }
}
```

### Каждый цикл (вложенный)
```scss
$backgrounds: (home, 'home.jpg'),
              (about, 'about.jpg');

@each $id, $image in $backgrounds {
    .photo-#{$id} {
      background: url($image);
    }
}
```

### Циклы While

```scss
$i: 6;
@while $i > 0 {
    .item-#{$i} { width: 2em * $i; }
    $i: $i - 2;
}
```

Другие возможности Sass
--------

### Условные обозначения {.row-span-2}

```scss
@if $position == 'left' {
     position: absolute;
     left: 0;
}
@else if $position == 'right' {
     позиция: абсолютная;
     right: 0;
}
@else {
     position: static;
}
```

### Интерполяция

```css
.#{$klass} { ... }      // Класс
call($function-name) // Функции

@media #{$tablet}
font: #{$size}/#{$line-height}
url("#{$background}.jpg")
```

### Списки

```scss
$list: (a b c);

nth($list, 1) // начинается с 1
length($list)

@each $item in $list { ... }
```

### Карты {.col-span-2}

```scss
$map: (key1: value1, key2: value2, key3: value3);

map-get($map, key1)
```


