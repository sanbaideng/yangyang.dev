---
название: jQuery
дата: 2020-12-24 21:08:21
фон: bg-[#2c63a2]
теги:
    - веб
    - js
    - javascript
    - библиотека
категории:
    - Программирование
intro: |
    Эта шпаргалка по [jQuery](https://jquery.com/) является отличным пособием как для начинающих, так и для опытных разработчиков.
плагины:
    - tooltip
    - copyCode
---


Начало работы
------------



### Включение jQuery

``javascript {.wrap}
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
```
#### Официальный CDN
``javascript {.wrap}
<script src="https://code.jquery.com/jquery-3.5.1.min.js" crossorigin="anonymous"></script>
```


### Синтаксис jQuery
``javascript

$(selector).methodOrFunction();

```
#### Пример:
``javascript
$('#menu').on('click', () =>{
  $(this).hide();
});

$("body").css("background", "red");
```


### jQuery document ready

``javascript

$(document).ready(function() {
  // Выполняется после загрузки DOM.
  alert('DOM полностью загружен!');
});
```

``javascript
$(function(){
  // Выполняется после загрузки DOM.
  alert('DOM полностью загружен!');
});
```




Селекторы jQuery
----------

### Примеры {.secondary}
``javascript
$("button").click(() => {
    $(":button").css("color", "red");
});
```
#### Комбинирование селекторов
``javascript
$("selector1, selector2 ...selectorn")
```



### Основы
- [*](https://api.jquery.com/all-selector/){data-tooltip="Выбирает все элементы."}
- [.class](https://api.jquery.com/class-selector/){data-tooltip="Выбирает все элементы с заданным классом. "}
- [element](https://api.jquery.com/element-selector/){data-tooltip="Выбирает все элементы с заданным именем тега."}
- [#id](https://api.jquery.com/id-selector/){data-tooltip="Выбирает один элемент с заданным атрибутом id. "}
- [:hidden](https://api.jquery.com/hidden-selector/){data-tooltip="Выбирает все элементы, которые скрыты."}
- [:visible](https://api.jquery.com/visible-selector/){data-tooltip="Выбирает все элементы, которые видны."}
- [:contains()](https://api.jquery.com/contains-selector/){data-tooltip="Выбрать все элементы, содержащие указанный текст."}
- [:empty](https://api.jquery.com/empty-selector/){data-tooltip="Выбирает все элементы, у которых нет дочерних элементов (включая текстовые узлы)."}
- [:has()](https://api.jquery.com/has-selector/){data-tooltip="Выбирает элементы, содержащие хотя бы один элемент, соответствующий указанному селектору."}
- [:parent](https://api.jquery.com/parent-selector/){data-tooltip="Выбирает все элементы, имеющие хотя бы один дочерний узел (либо элемент, либо текст)."}
- [parent &gt; child](https://api.jquery.com/child-selector/){data-tooltip="Выбирает все прямые дочерние элементы, указанные через child, элементов, указанных через parent."}
- [ancestor descendant](https://api.jquery.com/descendant-selector/){data-tooltip="Выбирает все элементы, являющиеся потомками данного предка."}
- [prev + next](https://api.jquery.com/next-adjacent-Selector/){data-tooltip="Выбирает все следующие элементы, соответствующие next, которым непосредственно предшествует братский элемент prev."}
- [prev ~ siblings](https://api.jquery.com/next-siblings-selector/){data-tooltip="Выбирает все элементы-сестры, которые следуют после элемента prev, имеют того же родителя и соответствуют селектору фильтрации siblings."} {.col-span-2}
{.marker-none .cols-3}


### Основные фильтры
- [:animated](https://api.jquery.com/animated-selector/){data-tooltip="Выбираются все элементы, находящиеся в процессе анимации на момент выполнения селектора."}
- [:eq()](https://api.jquery.com/eq-selector/){data-tooltip="Выберите элемент с индексом n в сопоставленном наборе."}
- [:even](https://api.jquery.com/even-selector/){data-tooltip="Выбирает четные элементы с нулевым индексом.  См. также :odd."}
- [:first](https://api.jquery.com/first-selector/){data-tooltip="Выбирает первый найденный элемент DOM."}
- [:gt()](https://api.jquery.com/gt-selector/){data-tooltip="Выбирает все элементы с индексом, большим, чем индекс, в пределах найденного набора."}
- [:header](https://api.jquery.com/header-selector/){data-tooltip="Выбирает все элементы, которые являются заголовками, например h1, h2, h3 и т.д."}
- [:lang()](https://api.jquery.com/lang-selector/){data-tooltip="Выбирает все элементы указанного языка."}
- [:last](https://api.jquery.com/last-selector/){data-tooltip="Выбирает последний найденный элемент."}
- [:lt()](https://api.jquery.com/lt-selector/){data-tooltip="Выбирает все элементы с индексом меньше индекса в пределах найденного множества."}
- [:not()](https://api.jquery.com/not-selector/){data-tooltip="Выбирает все элементы, которые не соответствуют заданному селектору."}
- [:odd](https://api.jquery.com/odd-selector/){data-tooltip="Выбирает нечетные элементы с нулевым индексом.  См. также :even."}
- [:root](https://api.jquery.com/root-selector/){data-tooltip="Выбирает элемент, являющийся корнем документа."}
- [:target](https://api.jquery.com/target-selector/){data-tooltip="Выбирает целевой элемент, указанный идентификатором фрагмента URI документа&apos;}.
{.marker-none .cols-3}


### Атрибут
- [[name|="value"]](https://api.jquery.com/attribute-contains-prefix-selector/){data-tooltip="Выбирает элементы, у которых указанный атрибут имеет значение, либо равное заданной строке, либо начинающееся с этой строки, за которой следует дефис (-)."}
- [[name*="value"]](https://api.jquery.com/attribute-contains-selector/){data-tooltip="Выбирает элементы, у которых указанный атрибут имеет значение, содержащее заданную подстроку."}
- [[name~="value"]](https://api.jquery.com/attribute-contains-word-selector/){data-tooltip="Выбирает элементы, у которых указанный атрибут имеет значение, содержащее заданное слово, разделенное пробелами."}
- [[name$="value"]](https://api.jquery.com/attribute-ends-with-selector/){data-tooltip="Выбирает элементы, у которых указанный атрибут имеет значение, заканчивающееся точно на заданную строку. Сравнение чувствительно к регистру."}
- [[name="value"]](https://api.jquery.com/attribute-equals-selector/){data-tooltip="Выбирает элементы, у которых указанный атрибут имеет значение, точно равное определенному значению."}
- [[name!="value"]](https://api.jquery.com/attribute-not-equal-selector/){data-tooltip="Выбирает элементы, которые либо не имеют указанного атрибута, либо имеют его, но не с определенным значением."}
- [[name^="value"]](https://api.jquery.com/attribute-starts-with-selector/){data-tooltip="Выбирает элементы, у которых указанный атрибут имеет значение, начинающееся точно с заданной строки."}
- [[name]](https://api.jquery.com/has-attribute-selector/){data-tooltip="Выбирает элементы, имеющие указанный атрибут с любым значением. "}
- [[name="value"][name2="value2"]](https://api.jquery.com/multiple-attribute-selector/){data-tooltip="Выбирает элементы, соответствующие всем заданным фильтрам атрибутов."} {.col-span-2}
{.marker-none .cols-2}


### Фильтры дочерних элементов
- [:first-child](https://api.jquery.com/first-child-selector/){data-tooltip="Выбирает все элементы, которые являются первыми дочерними элементами своего родителя."}
- [:first-of-type](https://api.jquery.com/first-of-type-selector/){data-tooltip="Выбирает все элементы, которые являются первыми среди братьев и сестер с одинаковым именем элемента."}
- [:last-child](https://api.jquery.com/last-child-selector/){data-tooltip="Выбирает все элементы, которые являются последними дочерними элементами своего родителя."}
- [:last-of-type](https://api.jquery.com/last-of-type-selector/){data-tooltip="Выбирает все элементы, которые являются последними среди братьев и сестер с одинаковым именем элемента."}
- [:nth-child()](https://api.jquery.com/nth-child-selector/){data-tooltip="Выбирает все элементы, которые являются nth-child своего родителя."}
- [:nth-last-child()](https://api.jquery.com/nth-last-child-selector/){data-tooltip="Выбирает все элементы, являющиеся n-ыми дочерними элементами своего родителя, считая от последнего элемента к первому."}
- [:nth-last-of-type()](https://api.jquery.com/nth-last-of-type-selector/){data-tooltip="Выбирает все элементы, которые являются n-ым ребенком своего родителя по отношению к братьям и сестрам с тем же именем элемента, считая от последнего элемента к первому."}
- [:nth-of-type()](https://api.jquery.com/nth-of-type-selector/){data-tooltip="Выбирает все элементы, которые являются n-ым дочерним элементом своего родителя по отношению к братьям и сестрам с одинаковым именем элемента."}
- [:only-child](https://api.jquery.com/only-child-selector/){data-tooltip="Выбирает все элементы, которые являются единственными дочерними элементами своего родителя."}
- [:only-of-type()](https://api.jquery.com/only-of-type-selector/){data-tooltip="Выбирает все элементы, у которых нет братьев и сестер с одинаковым именем элемента."}
{.marker-none .cols-2}


### Формы
- [:button](https://api.jquery.com/button-selector/){data-tooltip="Выбирает все элементы button и элементы типа button."}
- [:checkbox](https://api.jquery.com/checkbox-selector/){data-tooltip="Выбирает все элементы типа checkbox."}
- [:checked](https://api.jquery.com/checked-selector/){data-tooltip="Выбирает все элементы, которые отмечены или выбраны."}
- [:disabled](https://api.jquery.com/disabled-selector/){data-tooltip="Выбирает все элементы, которые отключены."}
- [:enabled](https://api.jquery.com/enabled-selector/){data-tooltip="Выбирает все элементы, которые включены."}
- [:focus](https://api.jquery.com/focus-selector/){data-tooltip="Выбирает элемент, если он в данный момент сфокусирован."}
- [:file](https://api.jquery.com/file-selector/){data-tooltip="Выбирает все элементы типа file."}
- [:image](https://api.jquery.com/image-selector/){data-tooltip="Выбирает все элементы типа image."}
- [:input](https://api.jquery.com/input-selector/){data-tooltip="Выбирает все элементы типа input, textarea, select и button."}
- [:password](https://api.jquery.com/password-selector/){data-tooltip="Выбирает все элементы типа password."}
- [:radio](https://api.jquery.com/radio-selector/){data-tooltip="Выбирает все элементы типа radio."}
- [:reset](https://api.jquery.com/reset-selector/){data-tooltip="Выбирает все элементы типа reset."}
- [:selected](https://api.jquery.com/selected-selector/){data-tooltip="Выбирает все элементы, которые выбраны."}
- [:submit](https://api.jquery.com/submit-selector/){data-tooltip="Выбирает все элементы типа submit."}
- [:text](https://api.jquery.com/text-selector/){data-tooltip="Выбирает все элементы ввода типа text."}
{.marker-none .cols-3}



Атрибуты jQuery
------------


### Примеры {.secondary .row-span-2}

``javascript
$('h2').css({
  color: 'blue',
  backgroundColor: 'gray',
  fontSize: '24px'
});
```
#### jQuery addClass
``javascript
$('.button').addClass('active');
```
#### jQuery removeClass
``javascript
$('.button').on('mouseleave', evt => {
   let e = evt.currentTarget;
   $(e).removeClass('active');
});
```
#### jQuery .toggleClass
``javascript
$('.choice').toggleClass('highlighted');
```



### Атрибуты
- [.attr()](https://api.jquery.com/attr/){data-tooltip="Получить значение атрибута для первого элемента в наборе найденных элементов."}
- [.prop()](https://api.jquery.com/prop/){data-tooltip="Получить значение свойства для первого элемента в наборе найденных элементов."}
- [.removeAttr()](https://api.jquery.com/removeAttr/){data-tooltip="Удалить атрибут из каждого элемента в наборе найденных элементов."}
- [.removeProp()](https://api.jquery.com/removeProp/){data-tooltip="Удалить свойство для набора найденных элементов."}
- [.val()](https://api.jquery.com/val/){data-tooltip="Получить текущее значение первого элемента в наборе подобранных элементов."}
{.marker-none .cols-2}

#### Data
- [jQuery.data()](https://api.jquery.com/jQuery.data/){data-tooltip="Хранит произвольные данные, связанные с указанным элементом. Возвращает заданное значение."}
- [.data()](https://api.jquery.com/data/){data-tooltip="Хранит произвольные данные, связанные с заданными элементами."}
- [jQuery.hasData()](https://api.jquery.com/jQuery.hasData/){data-tooltip="Определяет, есть ли у элемента какие-либо данные jQuery, связанные с ним."}
- [jQuery.removeData()](https://api.jquery.com/jQuery.removeData/){data-tooltip="Удалить ранее сохраненный фрагмент данных."}
- [.removeData()](https://api.jquery.com/removeData/){data-tooltip="Удалить ранее сохраненный фрагмент данных."}
{.marker-none .cols-2}

### CSS
- [.addClass()](https://api.jquery.com/addClass/){data-tooltip="Добавляет указанный класс(ы) к каждому элементу в наборе найденных элементов."}
- [.hasClass()](https://api.jquery.com/hasClass/){data-tooltip="Определяет, присвоен ли какому-либо из найденных элементов заданный класс."}
- [.removeClass()](https://api.jquery.com/removeClass/){data-tooltip="Удалить один класс, несколько классов или все классы из каждого элемента в наборе сопоставленных элементов."}
- [.toggleClass()](https://api.jquery.com/toggleClass/){data-tooltip="Добавляет или удаляет один или несколько классов из каждого элемента в наборе сопоставленных элементов в зависимости от наличия класса или значения аргумента state."}
- [.css()](https://api.jquery.com/css/){data-tooltip="Получить вычисленные свойства стиля для первого элемента в наборе сопоставленных элементов."}
- [jQuery.cssHooks](https://api.jquery.com/jQuery.cssHooks/){data-tooltip="Вставьте крючок непосредственно в jQuery, чтобы переопределить получение или установку определенных CSS-свойств, нормализовать именование CSS-свойств или создать пользовательские свойства."}
- [jQuery.cssNumber](https://api.jquery.com/jQuery.cssNumber/){data-tooltip="Объект, содержащий все CSS-свойства, которые могут использоваться без единицы измерения. Метод .css() использует этот объект для определения возможности добавления px к значениям без единиц измерения."}
- [jQuery.escapeSelector()](https://api.jquery.com/jQuery.escapeSelector/){data-tooltip="Выводит любой символ, имеющий особое значение в CSS-селекторе."}
{.marker-none .cols-2}

### Размеры
- [.height()](https://api.jquery.com/height/){data-tooltip="Получает текущую вычисленную высоту для первого элемента в наборе сопоставленных элементов."}
- [.innerHeight()](https://api.jquery.com/innerHeight/){data-tooltip="Получить текущую вычисленную высоту для первого элемента в наборе сопоставленных элементов, включая padding, но не border."}
- [.innerWidth()](https://api.jquery.com/innerWidth/){data-tooltip="Получить текущую вычисленную внутреннюю ширину для первого элемента в наборе сопоставленных элементов, включая padding, но не border."}
- [.outerHeight()](https://api.jquery.com/outerHeight/){data-tooltip="Получить текущую вычисленную внешнюю высоту (включая padding, border и, опционально, margin) для первого элемента в наборе сопоставленных элементов."}
- [.outerWidth()](https://api.jquery.com/outerWidth/){data-tooltip="Получить текущую вычисленную внешнюю ширину (включая padding, border и, опционально, margin) для первого элемента в наборе сопоставленных элементов."}
- [.width()](https://api.jquery.com/width/){data-tooltip="Получить текущую вычисленную ширину для первого элемента в наборе сопоставленных элементов."}
{.marker-none .cols-2}

### Смещение
- [.offset()](https://api.jquery.com/offset/){data-tooltip="Получить текущие координаты первого элемента в наборе найденных элементов относительно документа."}
- [.offsetParent()](https://api.jquery.com/offsetParent/){data-tooltip="Получить ближайший позиционируемый элемент-предок."}
- [.position()](https://api.jquery.com/position/){data-tooltip="Получить текущие координаты первого элемента из набора сопоставленных элементов, относительно смещенного родителя."}
- [.scrollLeft()](https://api.jquery.com/scrollLeft/){data-tooltip="Получить текущее горизонтальное положение полосы прокрутки для первого элемента в наборе сопоставленных элементов."}
- [.scrollTop()](https://api.jquery.com/scrollTop/){data-tooltip="Получить текущее вертикальное положение полосы прокрутки для первого элемента в наборе найденных элементов или установить вертикальное положение полосы прокрутки для каждого найденного элемента."}
{.marker-none .cols-2}



Манипуляции jQuery
------------

### Примеры {.secondary .row-span-3}

``javascript
/*<span>Span.</span>*/
$('span').after('<p>Параграф.</p>');
/*<span>Span.</span><p>Paragraph.</p>*/

/*<span>Span.</span>*/
$('<span>Span.</span>').replaceAll('p');
/*<p>Span.</p>*/

/*<span>Это span.</span>*/
$('span').wrap('<p></p>');
/*<p><span>Это span.</span></p>*/
```

### Копирование
- [.clone()](https://api.jquery.com/clone/){data-tooltip="Создать глубокую копию набора совпадающих элементов."}
{.marker-none .cols-3}

### DOM Insertion, Around
- [.wrap()](https://api.jquery.com/wrap/){data-tooltip="Обернуть HTML-структуру вокруг каждого элемента в наборе найденных элементов."}
- [.wrapAll()](https://api.jquery.com/wrapAll/){data-tooltip="Обернуть HTML-структуру вокруг всех элементов в наборе найденных элементов."}
- [.wrapInner()](https://api.jquery.com/wrapInner/){data-tooltip="Обернуть HTML-структуру вокруг содержимого каждого элемента в наборе найденных элементов."}
{.marker-none .cols-3}

### DOM Insertion, Inside
- [.append()](https://api.jquery.com/append/){data-tooltip="Вставьте содержимое, указанное параметром, в конец каждого элемента из набора найденных элементов."}
- [.appendTo()](https://api.jquery.com/appendTo/){data-tooltip="Вставьте каждый элемент из набора сопоставленных элементов в конец цели."}
- [.html()](https://api.jquery.com/html/){data-tooltip="Получить HTML-содержимое первого элемента из набора найденных элементов."}
- [.prepend()](https://api.jquery.com/prepend/){data-tooltip="Вставить содержимое, указанное параметром, в начало каждого элемента в наборе найденных элементов."}
- [.prependTo()](https://api.jquery.com/prependTo/){data-tooltip="Вставить каждый элемент из набора сопоставленных элементов в начало цели."}
- [.text()](https://api.jquery.com/text/){data-tooltip="Получить объединенное текстовое содержимое каждого элемента в наборе найденных элементов, включая их потомков."}
{.marker-none .cols-3}

### DOM Insertion, Outside
- [.after()](https://api.jquery.com/after/){data-tooltip="Вставьте содержимое, указанное параметром, после каждого элемента из набора найденных элементов."}
- [.before()](https://api.jquery.com/before/){data-tooltip="Вставьте содержимое, указанное параметром, перед каждым элементом из набора подобранных элементов."}
- [.insertAfter()](https://api.jquery.com/insertAfter/){data-tooltip="Вставьте каждый элемент из набора сопоставленных элементов после цели."}
- [.insertBefore()](https://api.jquery.com/insertBefore/){data-tooltip="Вставьте каждый элемент из набора найденных элементов перед целью."}
{.marker-none .cols-3}

### DOM Removal
- [.detach()](https://api.jquery.com/detach/){data-tooltip="Удалить набор найденных элементов из DOM."}
- [.empty()](https://api.jquery.com/empty/){data-tooltip="Удалите из DOM все дочерние узлы набора совпадающих элементов."}
- [.remove()](https://api.jquery.com/remove/){data-tooltip="Удалить набор совпадающих элементов из DOM."}
- [.unwrap()](https://api.jquery.com/unwrap/){data-tooltip="Удалить из DOM родителей набора совпадающих элементов, оставив на их месте совпадающие элементы."}
{.marker-none .cols-3}

### Замена DOM
- [.replaceAll()](https://api.jquery.com/replaceAll/){data-tooltip="Замените каждый целевой элемент на набор совпадающих элементов."}
- [.replaceWith()](https://api.jquery.com/replaceWith/){data-tooltip="Замените каждый элемент в наборе найденных элементов новым содержимым и верните набор элементов, который был удален."}
{.marker-none .cols-3}


jQuery Traversing
------------


### Фильтрация
- [.eq()](https://api.jquery.com/eq/){data-tooltip="Сокращает набор найденных элементов до элемента с указанным индексом."}
- [.filter()](https://api.jquery.com/filter/){data-tooltip="Сократите набор найденных элементов до тех, которые соответствуют селектору или прошли проверку функцией&apos;s. "}
- [.first()](https://api.jquery.com/first/){data-tooltip="Сократите набор найденных элементов до первого в наборе."}
- [.has()](https://api.jquery.com/has/){data-tooltip="Сократите набор найденных элементов до тех, у которых есть потомок, соответствующий селектору или элементу DOM."}
- [.is()](https://api.jquery.com/is/){data-tooltip="Проверяет текущий набор элементов на соответствие селектору, элементу или объекту jQuery и возвращает true, если хотя бы один из этих элементов соответствует заданным аргументам."}
- [.last()](https://api.jquery.com/last/){data-tooltip="Уменьшить набор найденных элементов до последнего в наборе."}
- [.map()](https://api.jquery.com/map/){data-tooltip="Пропускаем каждый элемент из текущего найденного набора через функцию, создавая новый объект jQuery, содержащий возвращаемые значения."}
- [.not()](https://api.jquery.com/not/){data-tooltip="Удалить элементы из набора найденных элементов."}
- [.slice()](https://api.jquery.com/slice/){data-tooltip="Сократить множество найденных элементов до подмножества, заданного диапазоном индексов."}
{.marker-none .cols-3}

### Разное обход
- [.add()](https://api.jquery.com/add/){data-tooltip="Создать новый объект jQuery с элементами, добавленными в набор найденных элементов."}
- [.addBack()](https://api.jquery.com/addBack/){data-tooltip="Добавляет предыдущий набор элементов в стеке к текущему набору, опционально отфильтрованный селектором."}
- [.andSelf()](https://api.jquery.com/andSelf/){data-tooltip="Добавить предыдущий набор элементов в стеке к текущему набору."}
- [.contents()](https://api.jquery.com/contents/){data-tooltip="Получить дочерние элементы каждого элемента из набора сопоставленных элементов, включая узлы текста и комментариев."}
- [.each()](https://api.jquery.com/each/){data-tooltip="Итерация по объекту jQuery с выполнением функции для каждого найденного элемента. "}
- [.end()](https://api.jquery.com/end/){data-tooltip="Завершает последнюю операцию фильтрации в текущей цепочке и возвращает набор найденных элементов в предыдущее состояние."}
{.marker-none .cols-3}

### Обход дерева
- [.children()](https://api.jquery.com/children/){data-tooltip="Получить дочерние элементы каждого элемента в наборе найденных элементов, отфильтрованные селектором."}
- [.closest()](https://api.jquery.com/closest/){data-tooltip="Для каждого элемента в наборе получите первый элемент, соответствующий селектору, проверив сам элемент и пройдя вверх по его предкам в дереве DOM."}
- [.find()](https://api.jquery.com/find/){data-tooltip="Получите потомков каждого элемента в текущем наборе совпадающих элементов, отфильтрованных по селектору, объекту jQuery или элементу."}
- [.next()](https://api.jquery.com/next/){data-tooltip="Получает ближайшего родственника каждого элемента в наборе сопоставленных элементов. Если указан селектор, то следующий брат и сестра будут получены только в том случае, если они соответствуют этому селектору."}
- [.nextAll()](https://api.jquery.com/nextAll/){data-tooltip="Получает всех следующих братьев и сестер каждого элемента из набора сопоставленных элементов, дополнительно отфильтрованных селектором."}
- [.nextUntil()](https://api.jquery.com/nextUntil/){data-tooltip="Получить все следующие братья и сестры каждого элемента до элемента, сопоставленного с переданным селектором, узлом DOM или объектом jQuery, но не включая его."}
- [.parent()](https://api.jquery.com/parent/){data-tooltip="Получить родителя каждого элемента в текущем наборе найденных элементов, дополнительно отфильтрованных селектором."}
- [.parents()](https://api.jquery.com/parents/){data-tooltip="Получить предков каждого элемента в текущем наборе сопоставленных элементов, отфильтрованных селектором."}
- [.parentsUntil()](https://api.jquery.com/parentsUntil/){data-tooltip="Получение предков каждого элемента в текущем наборе сопоставленных элементов, вплоть до элемента, сопоставленного селектором, узлом DOM или объектом jQuery, но не включая его."}
- [.prev()](https://api.jquery.com/prev/){data-tooltip="Получение непосредственно предшествующего брата или сестры каждого элемента в наборе сопоставленных элементов. Если указан селектор, то предыдущий сиблинг будет получен только в том случае, если он соответствует этому селектору."}
- [.prevAll()](https://api.jquery.com/prevAll/){data-tooltip="Получить всех предшествующих братьев и сестер каждого элемента в наборе сопоставленных элементов, дополнительно отфильтрованных селектором."}
- [.prevUntil()](https://api.jquery.com/prevUntil/){data-tooltip="Получить всех предшествующих братьев и сестер каждого элемента до элемента, сопоставленного с селектором, узлом DOM или объектом jQuery, но не включая его."}
- [.siblings()](https://api.jquery.com/siblings/){data-tooltip="Получение братьев и сестер каждого элемента в наборе сопоставленных элементов, дополнительно отфильтрованных селектором."}
{.marker-none .cols-3}


jQuery Events
------------


### Примеры {.secondary .row-span-6}

``javascript
// Событие мыши 'click'
$('#menu-button').on('click', () => {
  $('#menu').show();
});

// Событие клавиатуры 'keyup'
$('#textbox').on('keyup', () => {
  $('#menu').show();
});

// Событие прокрутки 'scroll'
$('#menu-button').on('scroll', () => {
  $('#menu').show();
});
```
#### Объект Event
```javascript
$('#menu').on('click', event => {
  $(event.currentTarget).hide();
});
```
#### Цепочка методов
``javascript
$('#menu-btn').on('mouseenter', () => {
  $('#menu').show();
}).on('mouseleave', () => {
  $('#menu').hide();
});
```
#### Предотвращает событие
``javascript
$("p" ).click(function( event ) {
  event.stopPropagation();
  // Сделайте что-нибудь
});
```



### События браузера
- [.error()](https://api.jquery.com/error/){data-tooltip="Привязать обработчик события к JavaScript-событию error."}
- [.resize()](https://api.jquery.com/resize/){data-tooltip="Привязать обработчик события к JavaScript-событию resize или запустить это событие на элементе."}
- [.scroll()](https://api.jquery.com/scroll/){data-tooltip="Привязать обработчик события к JavaScript-событию прокрутки или запустить это событие на элементе."}
{.marker-none .cols-3}



### Объект события {.row-span-6}
- [event.currentTarget](https://api.jquery.com/event.currentTarget/){data-tooltip=" Текущий DOM-элемент в фазе всплытия события.  "}
- [event.delegateTarget](https://api.jquery.com/event.delegateTarget/){data-tooltip="Элемент, к которому был присоединен вызванный в данный момент обработчик события jQuery."}
- [event.data](https://api.jquery.com/event.data/){data-tooltip="Необязательный объект данных, передаваемых методу события при привязке текущего выполняющегося обработчика.  "}
- [event.isDefaultPrevented()](https://api.jquery.com/event.isDefaultPrevented/){data-tooltip="Возвращает, вызывалась ли когда-либо функция event.preventDefault() для этого объекта события. "}
- [event.isImmediatePropagationStopped()](https://api.jquery.com/event.isImmediatePropagationStopped/){data-tooltip="Возвращает, вызывалась ли когда-либо функция event.stopImmediatePropagation() для данного объекта события. "}
- [event.isPropagationStopped()](https://api.jquery.com/event.isPropagationStopped/){data-tooltip="" Возвращает, вызывалась ли когда-либо функция event.stopPropagation() для данного объекта события. "}
- [event.metaKey](https://api.jquery.com/event.metaKey/){data-tooltip="Указывает, была ли нажата клавиша META в момент срабатывания события."}
- [event.namespace](https://api.jquery.com/event.namespace/){data-tooltip="Пространство имен, указанное при срабатывании события."}
- [event.pageX](https://api.jquery.com/event.pageX/){data-tooltip="Положение мыши относительно левого края документа."}
- [event.pageY](https://api.jquery.com/event.pageY/){data-tooltip="Положение мыши относительно верхнего края документа."}
- [event.preventDefault()](https://api.jquery.com/event.preventDefault/){data-tooltip="Если вызвать этот метод, то действие по умолчанию события не будет вызвано."}
- [event.relatedTarget](https://api.jquery.com/event.relatedTarget/){data-tooltip="Другой элемент DOM, вовлеченный в событие, если таковой имеется."}
- [event.result](https://api.jquery.com/event.result/){data-tooltip="Последнее значение, возвращенное обработчиком события, которое было вызвано этим событием, если только значение не было неопределенным."}
- [event.stopImmediatePropagation()](https://api.jquery.com/event.stopImmediatePropagation/){data-tooltip="Задерживает выполнение остальных обработчиков и предотвращает распространение события по дереву DOM."}
- [event.stopPropagation()](https://api.jquery.com/event.stopPropagation/){data-tooltip="Предотвращает распространение события по дереву DOM, не позволяя родительским обработчикам получить уведомление о событии."}
- [event.target](https://api.jquery.com/event.target/){data-tooltip="Элемент DOM, инициировавший событие.  "}
- [event.timeStamp](https://api.jquery.com/event.timeStamp/){data-tooltip="Разница в миллисекундах между моментом создания события браузером и 1 января 1970 года."}
- [event.type](https://api.jquery.com/event.type/){data-tooltip="Описывает характер события."}
- [event.which](https://api.jquery.com/event.which/){data-tooltip="Для событий, связанных с клавишами или мышью, это свойство указывает на конкретную клавишу или кнопку, которая была нажата."}
{.marker-none .cols-1}



### Загрузка документа
- [.load()](https://api.jquery.com/load-event/){data-tooltip="Привяжите обработчик события к JavaScript-событию load."}
- [.ready()](https://api.jquery.com/ready/){data-tooltip="Укажите функцию, которая будет выполняться после полной загрузки DOM."}
- [.unload()](https://api.jquery.com/unload/){data-tooltip="Привязать обработчик события к событию unload JavaScript."}
{.marker-none .cols-3}


### Привязка обработчика события
- [.bind()](https://api.jquery.com/bind/){data-tooltip="Прикрепить обработчик к событию для элементов."}
- [.delegate()](https://api.jquery.com/delegate/){data-tooltip="Прикрепить обработчик к одному или нескольким событиям для всех элементов, соответствующих селектору, сейчас или в будущем, на основе определенного набора корневых элементов."}
- [.die()](https://api.jquery.com/die/){data-tooltip="Удалить с элементов обработчики событий, ранее закрепленные с помощью .live()."}
- [.live()](https://api.jquery.com/live/){data-tooltip="Прикрепить обработчик событий для всех элементов, соответствующих текущему селектору, сейчас и в будущем."}
- [.off()](https://api.jquery.com/off/){data-tooltip="Удалить обработчик события."}
- [.on()](https://api.jquery.com/on/){data-tooltip="Прикрепить к выбранным элементам функцию-обработчик одного или нескольких событий."}
- [.one()](https://api.jquery.com/one/){data-tooltip="Прикрепить обработчик к событию для элементов. Обработчик выполняется не более одного раза на элемент для каждого типа события."}
- [.trigger()](https://api.jquery.com/trigger/){data-tooltip="Выполнить все обработчики и поведения, прикрепленные к найденным элементам для данного типа события."}
- [.triggerHandler()](https://api.jquery.com/triggerHandler/){data-tooltip="Выполнить все обработчики, прикрепленные к элементу для данного события."}
- [.unbind()](https://api.jquery.com/unbind/){data-tooltip="Удалить ранее прикрепленный обработчик события из элементов."}
- [.undelegate()](https://api.jquery.com/undelegate/){data-tooltip="Удалить обработчик из события для всех элементов, соответствующих текущему селектору, на основе определенного набора корневых элементов."}
{.marker-none .cols-3}

### События формы
- [.blur()](https://api.jquery.com/blur/){data-tooltip="Привязать обработчик события к JavaScript-событию blur или запустить это событие на элементе."}
- [.change()](https://api.jquery.com/change/){data-tooltip="Привязать обработчик события к JavaScript-событию change или запустить это событие на элементе."}
- [.focus()](https://api.jquery.com/focus/){data-tooltip="Привязать обработчик события к JavaScript-событию focus или запустить это событие на элементе."}
- [.focusin()](https://api.jquery.com/focusin/){data-tooltip="Привязать обработчик события к событию focusin."}
- [.focusout()](https://api.jquery.com/focusout/){data-tooltip="Привязать обработчик события к JavaScript-событию focusout."}
- [.select()](https://api.jquery.com/select/){data-tooltip="Привязать обработчик события к JavaScript-событию select или вызвать это событие на элементе."}
- [.submit()](https://api.jquery.com/submit/){data-tooltip="Привязать обработчик события к JavaScript-событию submit или вызвать это событие на элементе."}
{.marker-none .cols-3}

### Клавиатурные события
- [.keydown()](https://api.jquery.com/keydown/){data-tooltip="Привязать обработчик события к JavaScript-событию keydown или запустить это событие на элементе."}
- [.keypress()](https://api.jquery.com/keypress/){data-tooltip="Привязать обработчик события к JavaScript-событию keypress или запустить это событие на элементе."}
- [.keyup()](https://api.jquery.com/keyup/){data-tooltip="Привязать обработчик события к JavaScript-событию keyup или запустить это событие на элементе."}
{.marker-none .cols-3}

### События мыши
- [.click()](https://api.jquery.com/click/){data-tooltip="Привязать обработчик события к JavaScript-событию click или запустить это событие на элементе."}
- [.contextMenu()](https://api.jquery.com/contextmenu/){data-tooltip="Привязать обработчик события к JavaScript-событию contextmenu или запустить это событие на элементе."}
- [.dblclick()](https://api.jquery.com/dblclick/){data-tooltip="Привязать обработчик события к JavaScript-событию dblclick или запустить это событие на элементе."}
- [.hover()](https://api.jquery.com/hover/){data-tooltip="Привяжите к сопоставленным элементам два обработчика, которые будут выполняться при входе и выходе указателя мыши из элементов."}
- [.mousedown()](https://api.jquery.com/mousedown/){data-tooltip="Привяжите обработчик события к JavaScript-событию mousedown или запустите это событие на элементе."}
- [.mouseenter()](https://api.jquery.com/mouseenter/){data-tooltip="Привязать обработчик события к событию входа мыши в элемент или запустить этот обработчик на элементе."}
- [.mouseleave()](https://api.jquery.com/mouseleave/){data-tooltip="Привязать обработчик события, которое будет запускаться при выходе мыши из элемента, или запустить этот обработчик на элементе."}
- [.mousemove()](https://api.jquery.com/mousemove/){data-tooltip="Привязать обработчик события к JavaScript-событию mousemove или запустить это событие на элементе."}
- [.mouseout()](https://api.jquery.com/mouseout/){data-tooltip="Привязать обработчик события к JavaScript-событию mouseout или запустить это событие на элементе."}
- [.mouseover()](https://api.jquery.com/mouseover/){data-tooltip="Привязать обработчик события к JavaScript-событию mouseover или запустить это событие на элементе."}
- [.mouseup()](https://api.jquery.com/mouseup/){data-tooltip="Привязать обработчик события к JavaScript-событию mouseup или запустить это событие на элементе."}
- [.toggle()](https://api.jquery.com/toggle-event/){data-tooltip="Привязать к сопоставленным элементам два или более обработчиков, которые будут выполняться при поочередном щелчке мыши."}
{.marker-none .cols-3}



Эффекты jQuery
------------

### Примеры {.secondary .row-span-2}

``javascript
$('#menu-button').on('click', () => {
  // $('#menu').fadeIn(400, 'swing')
  $('#menu').fadeIn();
});
```
#### Эффект fadeOut
```javascript
$('#menu-button').on('click', () => {
  // $('#menu').fadeOut(400, 'swing')
  $('#menu').fadeOut();
});
```



### Основы
- [.hide()](https://api.jquery.com/hide/){data-tooltip="Скрыть найденные элементы."}
- [.show()](https://api.jquery.com/show/){data-tooltip="Показать найденные элементы."}
- [.toggle()](https://api.jquery.com/toggle/){data-tooltip="Отображать или скрывать найденные элементы."}
{.marker-none .cols-3}


### Скольжение
- [.slideDown()](https://api.jquery.com/slideDown/){data-tooltip="Отображать найденные элементы скользящим движением."}
- [.slideToggle()](https://api.jquery.com/slideToggle/){data-tooltip="Отображать или скрывать найденные элементы скользящим движением."}
- [.slideUp()](https://api.jquery.com/slideUp/){data-tooltip="Скрыть найденные элементы скользящим движением."}
{.marker-none .cols-3}


### Custom
- [.animate()](https://api.jquery.com/animate/){data-tooltip="Выполнить пользовательскую анимацию набора CSS-свойств."}
- [.clearQueue()](https://api.jquery.com/clearQueue/){data-tooltip="Удалить из очереди все элементы, которые еще не были запущены."}
- [.delay()](https://api.jquery.com/delay/){data-tooltip="Установите таймер для задержки выполнения последующих элементов в очереди."}
- [.dequeue()](https://api.jquery.com/dequeue/){data-tooltip="Выполнить следующую функцию в очереди для найденных элементов."}
- [jQuery.dequeue()](https://api.jquery.com/jQuery.dequeue/){data-tooltip="Выполнить следующую функцию в очереди для найденного элемента."}
- [.finish()](https://api.jquery.com/finish/){data-tooltip="Остановить текущую анимацию, удалить все анимации из очереди и завершить все анимации для найденных элементов."}
- [jQuery.fx.interval](https://api.jquery.com/jQuery.fx.interval/){data-tooltip="Скорость (в миллисекундах) срабатывания анимации."}
- [jQuery.fx.off](https://api.jquery.com/jQuery.fx.off/){data-tooltip="Глобально отключить все анимации."}
- [jQuery.speed](https://api.jquery.com/jQuery.speed/){data-tooltip="Создает объект, содержащий набор свойств, готовых к использованию при определении пользовательских анимаций."}
- [.queue()](https://api.jquery.com/queue/){data-tooltip="Показать очередь функций, которые будут выполняться над найденными элементами."}
- [jQuery.queue()](https://api.jquery.com/jQuery.queue/){data-tooltip="Показать очередь функций, которые будут выполняться над найденным элементом."}
- [.stop()](https://api.jquery.com/stop/){data-tooltip="Остановить текущую анимацию на подобранных элементах".}
{.marker-none .cols-3}


### Затухание
- [.fadeIn()](https://api.jquery.com/fadeIn/){data-tooltip="Отобразите найденные элементы, сделав их непрозрачными."}
- [.fadeOut()](https://api.jquery.com/fadeOut/){data-tooltip="Скрыть найденные элементы, сделав их прозрачными."}
- [.fadeTo()](https://api.jquery.com/fadeTo/){data-tooltip="Регулировка непрозрачности сопоставленных элементов."}
- [.fadeToggle()](https://api.jquery.com/fadeToggle/){data-tooltip="Отображать или скрывать подобранные элементы, анимируя их непрозрачность."}
{.marker-none .cols-3}



jQuery Ajax
------------

### Примеры {.secondary .row-span-2}
``javascript
$.ajax({
  url: this.action,
  type: this.method,
  data: $(this).serialize()
}).done(function(server_data){
  console.log("success" + server_data);
}).fail(function(jqXHR, status, err){
  console.log("fail" + err);
});
```


### Глобальные обработчики событий Ajax
- [.ajaxComplete()](https://api.jquery.com/ajaxComplete/){data-tooltip="Зарегистрируйте обработчик, который будет вызываться при завершении Ajax-запросов. Это событие AjaxEvent."}
- [.ajaxError()](https://api.jquery.com/ajaxError/){data-tooltip="Зарегистрируйте обработчик, который будет вызываться при завершении Ajax-запросов с ошибкой. Это Ajax-событие."}
- [.ajaxSend()](https://api.jquery.com/ajaxSend/){data-tooltip="Прикрепить функцию, которая будет выполняться перед отправкой Ajax-запроса. Это событие Ajax Event."}
- [.ajaxStart()](https://api.jquery.com/ajaxStart/){data-tooltip="Зарегистрируйте обработчик, который будет вызываться при начале первого Ajax-запроса. Это событие Ajax Event."}
- [.ajaxStop()](https://api.jquery.com/ajaxStop/){data-tooltip="Зарегистрируйте обработчик, который будет вызываться после завершения всех Ajax-запросов. Это Ajax-событие."}
- [.ajaxSuccess()](https://api.jquery.com/ajaxSuccess/){data-tooltip="Прикрепить функцию, которая будет выполняться при успешном завершении Ajax-запроса. Это событие Ajax Event."}
{.marker-none .cols-2}

### Вспомогательные функции
- [jQuery.param()](https://api.jquery.com/jQuery.param/){data-tooltip="Создает сериализованное представление массива, обычного объекта или объекта jQuery, пригодное для использования в строке запроса URL или Ajax-запросе. В случае передачи объекта jQuery он должен содержать элементы ввода со свойствами имя/значение."}
- [.serialize()](https://api.jquery.com/serialize/){data-tooltip="Закодировать набор элементов формы в виде строки для отправки."}
- [.serializeArray()](https://api.jquery.com/serializeArray/){data-tooltip="Закодировать набор элементов формы в виде массива имен и значений."}
{.marker-none .cols-2}

### Низкоуровневый интерфейс
- [jQuery.ajax()](https://api.jquery.com/jQuery.ajax/){data-tooltip="Выполнить асинхронный HTTP (Ajax) запрос."}
- [jQuery.prefilter()](https://api.jquery.com/jQuery.ajaxPrefilter/){data-tooltip="Обработка пользовательских Ajax-опций или модификация существующих опций перед отправкой каждого запроса и перед их обработкой в $.ajax()."}
- [jQuery.ajaxSetup()](https://api.jquery.com/jQuery.ajaxSetup/){data-tooltip="Устанавливает значения по умолчанию для будущих Ajax-запросов. Его использование не рекомендуется."}
- [jQuery.ajaxTransport()](https://api.jquery.com/jQuery.ajaxTransport/){data-tooltip="Создает объект, который обрабатывает фактическую передачу Ajax-данных."}
{.marker-none .cols-2}

### Краткие методы
- [jQuery.get()](https://api.jquery.com/jQuery.get/){data-tooltip="Загрузка данных с сервера с помощью HTTP GET-запроса."}
- [jQuery.getJSON()](https://api.jquery.com/jQuery.getJSON/){data-tooltip="Загрузка JSON-кодированных данных с сервера с помощью HTTP-запроса GET."}
- [jQuery.getScript()](https://api.jquery.com/jQuery.getScript/){data-tooltip="Загрузка JavaScript-файла с сервера с помощью GET HTTP-запроса, а затем его выполнение."}
- [jQuery.post()](https://api.jquery.com/jQuery.post/){data-tooltip="Отправить данные на сервер с помощью HTTP POST-запроса."}
- [.load()](https://api.jquery.com/load/){data-tooltip="Загрузите данные с сервера и поместите возвращенный HTML в соответствующие элементы."}
{.marker-none .cols-2}




Разное
------------


### jQuery Object
- [jQuery()](https://api.jquery.com/jQuery/){data-tooltip="Принимает строку, содержащую CSS-селектор, который затем используется для подбора набора элементов."}
- [jQuery.noConflict()](https://api.jquery.com/jQuery.noConflict/){data-tooltip="Передать jQuery&apos;контроль над переменной $."}
- [jQuery.sub()](https://api.jquery.com/jQuery.sub/){data-tooltip="Создает новую копию jQuery, свойства и методы которой могут быть изменены без влияния на исходный объект jQuery."}
- [jQuery.holdReady()](https://api.jquery.com/jQuery.holdReady/){data-tooltip="Удерживает или освобождает выполнение события jQuery&apos;s ready."}
- [jQuery.when()](https://api.jquery.com/jQuery.when/){data-tooltip="Предоставляет способ выполнения функций обратного вызова на основе нуля или более объектов Thenable, обычно объектов Deferred, которые представляют асинхронные события."}
{.marker-none .cols-2}

### Отложенный объект {.row-span-2}
- [jQuery.Deferred()](https://api.jquery.com/jQuery.Deferred/){data-tooltip=""Фабричная функция, которая возвращает цепочечный полезный объект с методами для регистрации нескольких обратных вызовов в очередях обратных вызовов, вызова очередей обратных вызовов и передачи состояния успеха или неудачи любой синхронной или асинхронной функции."}
- [deferred.always()](https://api.jquery.com/deferred.always/){data-tooltip=""Добавить обработчики, которые будут вызываться, когда объект Deferred будет либо разрешен, либо отклонен. "}
- [deferred.done()](https://api.jquery.com/deferred.done/){data-tooltip=" Добавить обработчики, которые будут вызываться при разрешении объекта Deferred. "}
- [deferred.fail()](https://api.jquery.com/deferred.fail/){data-tooltip=" Добавить обработчики, которые будут вызываться при отклонении объекта Deferred. "}
- [deferred.isRejected()](https://api.jquery.com/deferred.isRejected/){data-tooltip="" Определить, был ли отклонен объект Deferred. "}
- [deferred.isResolved()](https://api.jquery.com/deferred.isResolved/){data-tooltip=" Определить, был ли разрешен объект Deferred. "}
- [deferred.notify()](https://api.jquery.com/deferred.notify/){data-tooltip="" Вызов progressCallbacks на объекте Deferred с заданными args. "}
- [deferred.notifyWith()](https://api.jquery.com/deferred.notifyWith/){data-tooltip=" Вызов progressCallbacks для объекта Deferred с заданным контекстом и args. "}
- [deferred.pipe()](https://api.jquery.com/deferred.pipe/){data-tooltip="" Утилитарный метод для фильтрации и/или цепочки Deferred'ов.  "}
- [deferred.progress()](https://api.jquery.com/deferred.progress/){data-tooltip="Добавить обработчики, которые будут вызываться, когда объект Deferred генерирует уведомления о ходе выполнения."}
- [deferred.promise()](https://api.jquery.com/deferred.promise/){data-tooltip=" Возвращает объект Deferred&apos;s Promise. "}
- [deferred.reject()](https://api.jquery.com/deferred.reject/){data-tooltip=" Отклонить объект Deferred и вызвать любые failCallbacks с заданными args. "}
- [deferred.rejectWith()](https://api.jquery.com/deferred.rejectWith/){data-tooltip="" Отклонить объект Deferred и вызвать любые failCallbacks с заданным контекстом и args. "}
- [deferred.resolve()](https://api.jquery.com/deferred.resolve/){data-tooltip=" Разрешить объект Deferred и вызвать любые doneCallbacks с заданными args. "}
- [deferred.resolveWith()](https://api.jquery.com/deferred.resolveWith/){data-tooltip=" Разрешить объект Deferred и вызвать любые doneCallbacks с заданными контекстом и args. "}
- [deferred.state()](https://api.jquery.com/deferred.state/){data-tooltip="Определить текущее состояние объекта Deferred. "}
- [deferred.then()](https://api.jquery.com/deferred.then/){data-tooltip="Добавьте обработчики, которые будут вызываться, когда объект Deferred будет разрешен, отклонен или все еще находится в процессе выполнения. "}
- [.promise()](https://api.jquery.com/promise/){data-tooltip="Возвращает объект Promise для наблюдения за завершением всех действий определенного типа, привязанных к коллекции, поставленных в очередь или нет. "}
{.marker-none .cols-2}

### Утилиты {.row-span-3}
- [jQuery.boxModel](https://api.jquery.com/jQuery.boxModel/){data-tooltip="Определяет, отображается ли текущая страница в браузере пользователя&apos;с использованием W3C CSS Box Model."}
- [jQuery.browser](https://api.jquery.com/jQuery.browser/){data-tooltip="Содержит флаги для пользовательского агента, считываемые из navigator.userAgent. Это свойство было удалено в jQuery 1.9 и доступно только через плагин jQuery.migrate. Попробуйте вместо него использовать определение свойств."}
- [jQuery.contains()](https://api.jquery.com/jQuery.contains/){data-tooltip="Проверяет, является ли элемент DOM потомком другого элемента DOM."}
- [jQuery.each()](https://api.jquery.com/jQuery.each/){data-tooltip="Обобщенная функция итератора, которая может быть использована для плавного итерационного перехода как по объектам, так и по массивам. Массивы и массивоподобные объекты со свойством length (например, объект аргументов функции&apos;s) итерируются по числовому индексу, от 0 до length-1. Другие объекты итерируются по их именованным свойствам."}
- [jQuery.extend()](https://api.jquery.com/jQuery.extend/){data-tooltip="Объединить содержимое двух или более объектов в первый объект."}
- [jQuery.globalEval()](https://api.jquery.com/jQuery.globalEval/){data-tooltip="Выполнить некоторый JavaScript-код глобально."}
- [jQuery.grep()](https://api.jquery.com/jQuery.grep/){data-tooltip="Находит элементы массива, удовлетворяющие функции фильтра. Исходный массив не затрагивается."}
- [jQuery.inArray()](https://api.jquery.com/jQuery.inArray/){data-tooltip="Поиск заданного значения в массиве и возврат его индекса (или -1, если значение не найдено)."}
- [jQuery.isArray()](https://api.jquery.com/jQuery.isArray/){data-tooltip="Определить, является ли аргумент массивом."}
- [jQuery.isEmptyObject()](https://api.jquery.com/jQuery.isEmptyObject/){data-tooltip="Проверяет, не является ли объект пустым (не содержит перечислимых свойств)."}
- [jQuery.isFunction()](https://api.jquery.com/jQuery.isFunction/){data-tooltip="Определяет, является ли его аргумент вызываемой функцией."}
- [jQuery.isNumeric()](https://api.jquery.com/jQuery.isNumeric/){data-tooltip="Определяет, представляет ли его аргумент число JavaScript."}
- [jQuery.isPlainObject()](https://api.jquery.com/jQuery.isPlainObject/){data-tooltip="Проверяет, является ли объект обычным объектом."}
- [jQuery.isWindow()](https://api.jquery.com/jQuery.isWindow/){data-tooltip="Определить, является ли аргумент окном."}
- [jQuery.isXMLDoc()](https://api.jquery.com/jQuery.isXMLDoc/){data-tooltip="Проверяет, находится ли узел DOM внутри XML-документа (или является ли он XML-документом)."}
- [jQuery.makeArray()](https://api.jquery.com/jQuery.makeArray/){data-tooltip="Преобразование массивоподобного объекта в настоящий массив JavaScript."}
- [jQuery.map()](https://api.jquery.com/jQuery.map/){data-tooltip="Преобразовать все элементы массива или объекта в новый массив элементов."}
- [jQuery.merge()](https://api.jquery.com/jQuery.merge/){data-tooltip="Объединить содержимое двух массивов в первый массив. "}
- [jQuery.noop()](https://api.jquery.com/jQuery.noop/){data-tooltip="Пустая функция."}
- [jQuery.now()](https://api.jquery.com/jQuery.now/){data-tooltip="Возвращает число, представляющее текущее время."}
- [jQuery.parseHTML()](https://api.jquery.com/jQuery.parseHTML/){data-tooltip="Разбирает строку в массив узлов DOM."}
- [jQuery.parseJSON()](https://api.jquery.com/jQuery.parseJSON/){data-tooltip="Принимает правильно сформированную строку JSON и возвращает полученное значение JavaScript."}
- [jQuery.parseXML()](https://api.jquery.com/jQuery.parseXML/){data-tooltip="Разбирает строку в XML-документ."}
- [jQuery.proxy()](https://api.jquery.com/jQuery.proxy/){data-tooltip="Берет функцию и возвращает новую, которая всегда будет иметь определенный контекст."}
- [jQuery.support](https://api.jquery.com/jQuery.support/){data-tooltip="Коллекция свойств, отражающих наличие различных возможностей или ошибок браузера. Предназначен для внутреннего использования jQuery&apos; определенные свойства могут быть удалены, когда они больше не нужны для улучшения производительности запуска страницы. Для определения особенностей вашего проекта мы настоятельно рекомендуем использовать внешнюю библиотеку, такую как Modernizr, вместо зависимости от свойств в jQuery.support."}
- [jQuery.trim()](https://api.jquery.com/jQuery.trim/){data-tooltip="Удаление пробельных символов из начала и конца строки."}
- [jQuery.type()](https://api.jquery.com/jQuery.type/){data-tooltip="Определить внутренний JavaScript [[Класс]] объекта."}
- [jQuery.unique()](https://api.jquery.com/jQuery.unique/){data-tooltip="Сортирует массив элементов DOM по месту, удаляя дубликаты. Обратите внимание, что это работает только с массивами DOM-элементов, а не со строками или числами."}
- [jQuery.uniqueSort()](https://api.jquery.com/jQuery.uniqueSort/){data-tooltip="Сортирует массив элементов DOM на месте с удалением дубликатов. Обратите внимание, что это работает только с массивами DOM-элементов, а не со строками или числами."}
{.marker-none .cols-2}

### Методы DOM-элементов
- [.get()](https://api.jquery.com/get/){data-tooltip="Получить один из элементов, соответствующих объекту jQuery."}
- [.index()](https://api.jquery.com/index/){data-tooltip="Поиск заданного элемента среди сопоставленных элементов."}
- [.size()](https://api.jquery.com/size/){data-tooltip="Возвращает количество элементов в объекте jQuery."}
- [.toArray()](https://api.jquery.com/toArray/){data-tooltip="Получить все элементы, содержащиеся в наборе jQuery, в виде массива."}
{.marker-none .cols-2}

### Внутренние компоненты
- [.jquery](https://api.jquery.com/jquery-2/){data-tooltip="Строка, содержащая номер версии jQuery."}
- [.context](https://api.jquery.com/context/){data-tooltip="Контекст узла DOM, изначально переданный в jQuery(); если контекст не был передан, то контекстом, скорее всего, будет документ."}
- [jQuery.error()](https://api.jquery.com/jQuery.error/){data-tooltip="Принимает строку и выбрасывает содержащее ее исключение."}
- [.length](https://api.jquery.com/length/){data-tooltip="Количество элементов в объекте jQuery."}
- [.pushStack()](https://api.jquery.com/pushStack/){data-tooltip="Добавляет коллекцию элементов DOM в стек jQuery."}
- [.selector](https://api.jquery.com/selector/){data-tooltip="Селектор, представляющий собой селектор, переданный в jQuery(), если таковой имелся при создании исходного набора."}
{.marker-none .cols-2}

### Объект обратных вызовов
- [jQuery.Callbacks()](https://api.jquery.com/jQuery.Callbacks/){data-tooltip="Многоцелевой объект списка обратных вызовов, обеспечивающий мощный способ управления списками обратных вызовов."}
- [callbacks.add()](https://api.jquery.com/callbacks.add/){data-tooltip="Добавить обратный вызов или коллекцию обратных вызовов в список обратных вызовов."}
- [callbacks.disable()](https://api.jquery.com/callbacks.disable/){data-tooltip="Отключить список обратных вызовов от выполнения дополнительных действий" }
- [callbacks.disabled()](https://api.jquery.com/callbacks.disabled/){data-tooltip="Определить, был ли отключен список обратных вызовов."}
- [callbacks.empty()](https://api.jquery.com/callbacks.empty/){data-tooltip="Удалить все обратные вызовы из списка."}
- [callbacks.fire()](https://api.jquery.com/callbacks.fire/){data-tooltip="Вызвать все обратные вызовы с заданными аргументами."}
- [callbacks.fired()](https://api.jquery.com/callbacks.fired/){data-tooltip="Определите, вызывались ли уже эти обратные вызовы хотя бы один раз."}
- [callbacks.fireWith()](https://api.jquery.com/callbacks.fireWith/){data-tooltip="Вызов всех обратных вызовов в списке с заданным контекстом и аргументами."}
- [callbacks.has()](https://api.jquery.com/callbacks.has/){data-tooltip="Определите, есть ли в списке обратные вызовы. Если в качестве аргумента указан обратный вызов, определите, находится ли он в списке."}
- [callbacks.lock()](https://api.jquery.com/callbacks.lock/){data-tooltip="Зафиксировать список обратных вызовов в его текущем состоянии."}
- [callbacks.locked()](https://api.jquery.com/callbacks.locked/){data-tooltip="Определить, был ли заблокирован список обратных вызовов."}
- [callbacks.remove()](https://api.jquery.com/callbacks.remove/){data-tooltip="Удалить обратный вызов или коллекцию обратных вызовов из списка обратных вызовов."}
{.marker-none .cols-2}




