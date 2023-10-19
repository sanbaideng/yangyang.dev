---
title: Google Search
date: 2023-01-10 09:51:44
фон: bg-[#d3594a]
теги:
категории:
  - Другое
intro:  |
    В этой краткой справочной шпаргалке перечислены операторы расширенного поиска Google.
---

Начало работы {.cols-2}
----


### Операторы расширенного поиска Google
| Оператор | Описание | Категория |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
 Отдельное слово не допускает синонимов | Basic,Mail |
| `OR`/`AND` | Булевая функция поиска для поиска OR, так как Google по умолчанию использует AND между словами - должно быть все заглавные буквы | Basic,Mail |
| `\` | Реализует функцию OR | Basic |
| | `()` | Позволяет группировать операторы и диктовать порядок | Basic, Mail |
| `-` | Исключает слово из результатов | Basic,Mail |
| `*` | Действует как подстановочный знак и будет соответствовать любому слову или фразе | Basic |
| `#..#` | # в данном случае обозначает число. Используется для поиска чисел в серии.                                                                                                                      Базовый | Базовый |
| | `$` | Позволяет искать в долларах США | Базовый |
| | `€` | Позволяет искать евро | Basic |
| | `in` | Позволяет искать конвертацию единиц измерения (валюты, единицы или меры) | Basic |
| | `~` | Префикс - включение синонимов (потенциально устаревших) | Базовый |
| `+` | Префикс - Принудительное точное совпадение по одной фразе | Basic,Mail |
| `AROUND(X)` | Это вставка между двумя словами, причем X определяет, через сколько слов они должны быть упомянуты. Например, если это (4), то два ключевых слова должны быть упомянуты в пределах 4 слов друг от друга. | Дополнительно |
| `_` | Действует как подстановочный знак для автозаполнения | Дополнительно |


### Поиск по url
| Оператор | Описание | Категория |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `inurl:` | Возвращает только те результаты, в которых запрашиваемое ключевое слово(а) присутствует в URL | Дополнительно |
| `allinurl:` | Как и выше, но только содержащие все указанные слова в URL | Дополнительно |
| | `blogurl:` | Поиск URL-адресов блогов под определенным доменом. Эта функция используется в поиске блогов Google, но я обнаружил, что она дает некоторые результаты и в обычном поиске. | Дополнительно |
| `site:` | Ограничить результаты только результатами с одного сайта | Дополнительно |
| ``related:`` | Поиск доменов, схожих с запрашиваемым доменом | Дополнительно |


### Поиск по датам
Оператор | Оператор | Описание | Категория |
|--------------|------------------------------------------------------------------------------------------------------|------------|
| `daterange:` | Возвращает результаты в указанном диапазоне (требует юлианских дат) | Дополнительно |
| `after:` | Позволяет искать на диске или в почте измененные файлы или отправленные/полученные письма в любое время после заданной даты | Drive,Mail |
| `before:` | Позволяет искать на диске или в почте файлы, измененные или отправленные/полученные до определенной даты | Drive,Mail |
| `older:` | Поиск сообщений старше определенной даты | Mail |
| `newer:` | Поиск сообщений, более новых, чем определенная дата | Mail |


### Поиск файлов
| Оператор | Описание | Категория |
|-----------------|------------------------------------------------------------------------------------------------------|------------|
| `filename:` | Поиск сообщений с прикрепленным файлом определенного типа или точным именем файла | Mail |
| `type:` | Позволяет искать диск по типу файла | Drive |
| `owner:` | Позволяет искать диск по владельцу файла или папки | Drive |
| `to:` | Позволяет искать на диске файлы, которыми поделился определенный человек | Диск |
| `title:` | Позволяет искать на диске файлы, в названии которых присутствует только ключевое слово | Drive |
| `source:domain` | Позволяет искать файлы или папки, общие для всех в вашем бизнесе | Drive |
| `filetype:` | Возвращает только файлы определенного типа, связанные с искомым ключевым словом | Advanced |
| `ext:` | Как и выше, на основе расширения | Дополнительно |
| `after:` | Позволяет искать на диске или в почте измененные файлы или отправленные/полученные письма в любое время после заданной даты | Drive,Mail |
| `before:` | Позволяет искать на диске или в почте файлы, измененные или отправленные/полученные до определенной даты | Drive,Mail |
| `is:trash` | Поиск элемента в корзине диска | Drive |


### Поиск с использованием содержимого страницы
| Оператор | Описание | Категория |
|----------------|---------------------------------------------------------------------------------------------------------------------|----------|
| `link:` | Поиск страниц, ссылающихся на целевой домен | Дополнительно |
| `inanchor:` | Найти страницы, на которые ссылается указанный якорный текст/фраза. Данные сильно дискретизированы.                               | Дополнительно |
| `allinanchor:` | Найти страницы со всеми отдельными терминами после "inanchor:" в тексте входящей ссылки.                                  Дополнительно | |
| `intitle:` | Возвращает страницы, в заголовке которых встречается искомый запрос.
| `allintitle:` | Аналогично intitle:, но возвращает только те заголовки, в которых все слова в заголовке совпадают | Дополнительно |
| `inposttile:` | Находит страницы с ключевыми словами в заголовках постов (например, для изучения блогов) | &nbsp; |
| `intext:` | Находит страницы, на которых ключевое слово (слова) упоминаются в содержимом страницы.                                             | Дополнительно |
| `allintext:` | Аналогично "intext", но возвращаются только результаты, содержащие все указанные слова на странице. Расширенные | | |


### Ключевые слова
| Оператор | Описание | Категория |
|-------------------|--------------------------------------------------------------------------------------------------|----------|
| `Бизнес` | тип Например, кафе, ресторан, бар и т.д. вернет выборку соответствующих предприятий в данном районе | Карты |
| `Бензин/зарядка` | Станция EV рядом со мной или станция perol рядом со мной | Карты |
| `Поиск` | для сообщения с прикрепленной таблицей google | Почта |
| `Поиск` | для сообщения с прикрепленной google презентацией | Mail |


### Поиск по электронной почте
| Оператор | Описание | Категория |
|-------------------|-------------------------------------------------------------------------------------------------------|------------|
| `+` | Префикс - принудительное точное совпадение по одной фразе | Basic,Mail |
| | `()` | Позволяет группировать операторы и диктовать порядок | Basic,Mail |
| `-` | Исключает слово из результатов | Basic,Mail |
| | `""` | Позволяет искать конкретную фразу - точный поиск. Отдельное слово исключает синонимы | Basic,Mail |
| `OR`/`AND` | Булевая функция поиска для поиска OR, так как Google по умолчанию использует AND между словами - должно быть все заглавными буквами | Basic,Mail |
| `after:` | Позволяет искать на диске или в почте измененные файлы или отправленные/полученные письма в любое время после заданной даты | Drive, Mail |
| `before:` | Позволяет искать на диске или в почте файлы, измененные или отправленные/полученные до определенной даты | Drive, Mail |
| `is:starred` | Ищет только те элементы, которые были отмечены звездочками на диске | Drive,Mail |
| `from:` | Указывает отправителя в почте google | Mail |
| `to:` | Укажите получателя в google mail | Mail |
| `cc:` | Поиск по адресату, который был скопирован в письмо | Mail |
| `bcc:` | Поиск по адресату, который был скопирован в письмо вслепую | Mail |
| `older:` | Поиск сообщений старше определенной даты | Mail |
| `newer:` | Поиск сообщений, более новых, чем определенная дата | Mail |
| `Поиск` | для сообщения с прикрепленным google sheet | Mail |
| `Поиск` | для сообщения с прикрепленной google-презентацией | Mail |
| `AROUND` | Аналогично обычной функции поиска Google, позволяет искать ключевые слова рядом друг с другом.      Mail | |
| `subject:` | Поиск по ключевым словам в теме письма | Mail |
| | `{}` | Используется в почте вместо функции ИЛИ | Mail |
| `label:` | Поиск сообщений, имеющих определенный ярлык | Mail |
| | `has:attachment` | Поиск сообщений, к которым прикреплен элемент | Mail |
| `has:drive` | Поиск сообщений с прикрепленным google-диском | Mail |
| `has:document` | Поиск сообщений, к которым прикреплен google doc | Mail |
| `has:youtube` | Поиск сообщений, содержащих видео с youtube | Mail |
| `list:` | Поиск всех сообщений из определенного списка рассылки | Mail |
| | `в:везде` | Включает в поиск все папки, включая спам и корзину | Mail |
| `is:important` | Поиск сообщений, которые были помечены как важные | Mail |
| `label:important` | То же, что и is:important | Mail |
| | `is:snoozed` | Поиск сообщений, которые были отложены | Mail |
| `is:unread` | Поиск непрочитанных сообщений | Mail |
| `is:read` | Поиск только прочитанных сообщений | Mail |
| `has:yellow-star` | Поиск сообщений с цветным значком звезды | Mail |
| `has:blue-info` | Поиск сообщений с цветным значком | Mail |
| `is:chat` | Поиск сообщений из чата | Mail |
| `deliveredto:` | Поиск доставленных сообщений по адресу электронной почты | Mail |
| | `category:` | Поиск сообщений по категориям. После двоеточия следует название категории, т.е. category:primary | Mail |
| ``размер:`` | Сообщения, превышающие определенный размер в байтах | Mail |
| ``больше:`` | Сообщения, превышающие определенный размер в байтах | Mail |
| `smaller:` | Сообщения меньше определенного размера в байтах | Mail |
| | `has:userlabels` | Поиск сообщений, имеющих пользовательские метки | Mail |
| ` ` | Поиск сообщений, не имеющих пользовательских меток | Mail |


### Некоторые другие полезные операторы поиска
Оператор | Оператор | Описание | Категория |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| `define:` | Извлекает из Google карточку-ответ, отображающую словарное определение слова или словосочетания | Advanced |
| `cache:` | Возвращает наиболее актуальный кэш проиндексированной веб-страницы | Дополнительно |
| `weather:` | Выводит на экран фрагмент с погодой для данного места | Дополнительно |
| `stocks:` | Возвращает информацию об акциях для указанного тикера | Дополнительно |
| `map:` | Принудительное отображение результатов google map для определенного запроса | Дополнительно |
| `movie:` | Поиск информации по указанному фильму (особенно полезно, когда фильм имеет неоднозначное название). Если фильм еще идет в кинотеатрах, то будет также показано время показа | Дополнительно |
| `source:` | Используется в google news, возвращает результаты из указанного источника | Дополнительно |
| `loc:` | Возвращает результаты для определенного места | Дополнительно |
| `location:` | Как указано выше, но с новостями Google | Дополнительно |
| `info:` | Возвращает информацию, связанную с доменом (страницы с текстом домена, похожие страницы сайта, кэш и т.д.) | Дополнительно |
| `near` | Часть ленивого поиска в google maps, например, книжные магазины рядом с работой | Карты |



Также см.
--------

- [Шпаргалка по поисковым операторам Google](https://static.semrush.com/blog/uploads/files/39/12/39121580a18160d3587274faed6323e2.pdf) _(static.semrush.com)_