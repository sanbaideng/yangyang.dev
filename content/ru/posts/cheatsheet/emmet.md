---
название: Emmet
дата: 2020-12-14 18:28:43
фон: bg-[#95c844]
теги:
    - сниппеты
    - кодирование
    - html
    - css
    - аббревиатура
категории:
    - Инструментарий
intro: |
    [Emmet](https://emmet.io/) - это инструментарий веб-разработчика для ускорения написания HTML и CSS кода, который позволяет писать большие блоки HTML кода со скоростью света, используя известные CSS селекторы.
плагины:
    - copyCode
---


Синтаксис эммета
---------------


### Начало работы

Давайте начнем улучшать вашу разработку до скорости света.

- [Emmet в Visual Studio Code](https://code.visualstudio.com/docs/editor/emmet) _(code.visualstudio.com)_
- [Emmet 2 для Sublime Text](https://github.com/emmetio/sublime-text-plugin) _(github.com)_
- [Emmet для Coda](https://emmet.io/download/coda/) _(emmet.io)_
- [Emmet для Atom](https://github.com/emmetio/emmet-atom#readme) _(github.com)_


### Умножение: *

ul>li*5

``html
<ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ul>
```



### Child: >
`nav>ul>li`

``html
<nav>
    <ul>
        <li></li>
    </ul>
</nav>
```


### Пользовательские атрибуты {.col-span-2}

p[title="Hello world"]

``html
<p title="Hello world"></p>
```

td[rowspan=2 colspan=3 title]

``html
<td rowspan="2" colspan="3" title=""></td>
```

[a="value1" b="value2"]

``html
<div a="value1" b="value2"></div>
```





### Текст: {}

a{Нажмите на меня}

``html
<a href="">Нажмите на меня</a>
```

p>{Кликните }+a{here}+{ для продолжения}

``html {.wrap}
<p>Нажмите <a href="">здесь</a>, чтобы продолжить</p>
```


### Атрибуты ID и CLASS {.row-span-2}

`#header`

``html
<div id="header"></div>
```

.title

``html
<div class="title"></div>
```


form#search.wide

``html
<form id="search" class="wide"></form>
```

p.class1.class2.class3

``html
<p class="class1 class2 class3"></p>
```


### Неявные имена тегов {.row-span-2}
.class

``html
<div class="class"></div>
```

em>.class

``html
<em><span class="class"></span></em>
```


ul>.class
``html
<ul>
    <li class="class"></li>
</ul>
```


table>.row>.col

``html
<table>
    <tr class="row">
        <td class="col"></td>
    </tr>
</table>
```


### Родные братья и сестры: +

div+p+bq

``html
<div></div>
<p></p>
<blockquote></blockquote>
```


### Восхождение: ^

div+div>p>span+em^bq


``html
<div></div>
<div>
    <p><span></span><em></em></p>
    <blockquote></blockquote>
</div>
```


div+div>p>span+em^^bq

``html
<div></div>
<div>
    <p><span></span><em></em></p>
</div>
<blockquote></blockquote>
```


### Группировка: ()

div>(header>ul>li*2>a)+footer>p

``html
<div>
    <заголовок>
        <ul>
            <li><a href=""></a></li>
            <li><a href=""></a></li>
        </ul>
    </header>
    <footer>
        <p></p>
    </footer>
</div>
```

(div>dl>(dt+dd)*4)+footer>p
``html
<div>
    <dl>
        <dt></dt>
        <dd></dd>
        <dt></dt>
        <dd></dd>
        <dt></dt>
        <dd></dd>
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

``html
<ul>
    <li class="item1"></li>
    <li class="item2"></li>
    <li class="item3"></li>
</ul>
```

h$[title=item$]{Заголовок $}*3

``html
<h1 title="item1">Заголовок 1</h1>
<h2 title="item2">Заголовок 2</h2>
<h3 title="item3">Заголовок 3</h3>
```

ul>li.item$$$*3

``html
<ul>
    <li class="item001"></li>
    <li class="item002"></li>
    <li class="item003"></li>
</ul>
```

ul>li.item$@-*3
``html
<ul>
    <li class="item3"></li>
    <li class="item2"></li>
    <li class="item1"></li>
</ul>
```

ul>li.item$@2*3
``html
<ul>
    <li class="item2"></li>
    <li class="item3"></li>
    <li class="item4"></li>
</ul>
```

Также см. {.cols-1}
--------

* [Шпаргалка Эммета](https://docs.emmet.io/cheat-sheet/) _(docs.emmet.io)_
