---
Название: Pandoc
дата: 2023-03-21 13:26:00
фон: bg-red-400
теги:
    - конвертировать
    - документ
    - утилита
категории:
    - Linux Command
ввод: |
    [Pandoc](https://pandoc.org) - это конвертер документов, эта шпаргалка по pandoc содержит команды pandoc и некоторые распространенные трюки pandoc.
плагины:
    - copyCode
---

Начало работы
---------------

### Использование Pandoc

Синтаксис
Шелл-скрипт
$ pandoc -s [исходный файл] -o [выходной файл]
```


Примеры Pandoc
----------


### LaTeX в MS Word {.col-span-2}

Простой перевод .tex в .docx
Шелевой сценарий
$ pandoc -s file.tex -o file.docx
```

Преобразование .tex в .docx с цитированием по умолчанию
командный сценарий
$ pandoc -s file.tex --citeproc --bibliography=bib_library.bib -o file.docx
```

Перевод .tex в .docx с определенными цитатами
``Основной сценарий
$ pandoc -s file.tex --citeproc --bibliography=bib_library.bib --csl=apa.csl -o file.docx
```
Получить файл `.csl` с сайта [здесь](https://github.com/citation-style-language/styles)

.tex в .docx с перекрестными ссылками
командный сценарий
$ pandoc -s file.tex --filter pandoc-crossref -o file.docx
```
Получить фильтр `pandoc-crossref` из [здесь](https://github.com/lierdakil/pandoc-crossref/releases)





Также см. {.cols-1}
----------
- [примеры pandoc](https://pandoc.org/demos.html)


