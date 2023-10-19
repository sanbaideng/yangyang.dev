---
title: Emmet
date: 2020-12-14 18:28:43
latar belakang: bg-[#95c844]
tags:
    - cuplikan
    - pengkodean
    - html
    - css
    - abbr
kategori:
    - Toolkit
intro: |
    [Emmet](https://emmet.io/) adalah toolkit pengembang web untuk meningkatkan penulisan kode HTML & CSS, yang memungkinkan Anda untuk menulis blok kode HTML yang besar dengan kecepatan cahaya menggunakan selektor CSS yang terkenal.
pengaya (plugin):
    - copyCode
---


Sintaks Emmet
---------------


### Memulai

Mari kita mulai untuk meningkatkan perkembangan Anda dengan kecepatan cahaya.

- [Emmet di Visual Studio Code](https://code.visualstudio.com/docs/editor/emmet) _(code.visualstudio.com)_
- [Emmet 2 untuk Sublime Text](https://github.com/emmetio/sublime-text-plugin) _(github.com)_
- [Emmet untuk Coda](https://emmet.io/download/coda/) _(emmet.io)_
- [Emmet untuk Atom](https://github.com/emmetio/emmet-atom#readme) _(github.com)_


### Perkalian: *

ul>li*5

```html
<ul>
    <li></li>
    <li></li> <li></li>
    <li></li> <li></li>
    <li></li> <li></li>
    <li></li> <li></li>
</ul>
```



### Anak: >
`nav>ul>li`

```html
<nav>
    <ul>
        <li></li>
    </ul>
</nav>
```


### Atribut khusus {.col-span-2}

p [title = "Halo dunia"]

```html
<p title = "Halo dunia"></p>
```

td [rowspan=2 colspan=3 title]

```html
<td rowspan="2" colspan="3" title=""></td
```

[a = 'nilai1' b = "nilai2"]

```html
<div a="value1" b="value2"></div>
```





### Teks: {}

a{Klik saya}

```html
<a href="">Klik saya</a>
```

p>{Klik }+a{di sini}+{ untuk melanjutkan}

```html {.wrap}
<p>Klik <a href="">di sini</a> untuk melanjutkan</p>
```


### Atribut ID dan CLASS {.row-span-2}

`#header`

```html
<div id="header"></div>
```

.title

``` .html
<div class="title"></div> </div>
```


form#search.wide

```html
<form id="search" class="wide"></form>
```

p.class1.class2.class3

```html
<p class="class1 class2 class3"></p>
```


### Nama tag implisit {.row-span-2}
.class

```html
<div class="class"></div>
```

em>.class

```html
<em><span class="class"></span></em>
```


ul>.class
```html
<ul>
    <li class="class"></li>
</ul>
```


table>.row>.col

```html
<tabel>
    <tr class="row">
        <td class="col"></td>
    </tr>
</table>
```


### Saudara kandung: +

div + p + bq

```html
<div> </div>
<p></p>
<kutipan blok </kutipan blok>
```


### Memanjat: ^

div+div>p>span+em^bq


```html
<div></div> </div
<div>
    <p><span></span><em></em></p>
    <kutipan blok></kuotasi blok>
</div> </div>
```


div+div>p>span+em^^bq

```html
<div></div> </div
<div>
    <p><span></span><em></em></p>
</div> </div>
<kutipan blok></kuotasi blok>
```


### Pengelompokan: ()

div>(header>ul>li*2>a)+footer>p

```html
<div>
    <header>
        <ul>
            <li><a href=""></a></li>
            <li><a href=""></a></li>
        </ul>
    </header>
    <footer>
        <p></p>
    </footer>
</div> </div>
```

(div>dl>(dt+dd)*4)+footer>p
```html
<div>
    <dl>
        <dt></dt>
        <dd></dd>
        <dt></dt>
        <dd></dd>
        <dt></dt>
        <dt></dd>
        <dt></dt>
        <dd></dd>
    </dl>
</div>
<footer>
    <p></p>
</footer>
```


### $ {.row-span-2}

ul>li.item$*3

```html
<ul>
    <li class="item1"></li>
    <li class="item2"></li>
    <li class="item3"></li>
</ul>
```

h$[judul=item$]{Header $}*3

```html
<h1 title = "item1">Header 1</h1>
<h2 title = "item2">Header 2</h2>
<h3 title="item3">Header 3</h3>
```

ul>li.item$$$*3

```html
<ul>
    <li class="item001"></li>
    <li class="item002"></li>
    <li class="item003"></li>
</ul>
```

ul>li.item$@-*3
```html
<ul>
    <li class="item3"></li>
    <li class="item2"></li>
    <li class="item1"></li>
</ul>
```

ul>li.item$@2*3
```html
<ul>
    <li class="item2"></li>
    <li class="item3"></li>
    <li class="item4"></li>
</ul>
```

Lihat juga {.cols-1}
--------

* [Lembar contekan Emmet] (https://docs.emmet.io/cheat-sheet/) _(docs.emmet.io)_
