---
title: PhpStorm
date: 2022-11-23 16:23:31.703719
background: bg-gradient-to-r from-[#be4fe9] to-[#715bef] hover:from-emerald-400 hover:to-blue-500
label:
tags:
    - jetbrains
категории:
    - Клавиатурные сокращения
intro: |
    Наглядная шпаргалка по 96 сочетаниям клавиш в JetBrains PhpStorm
---



Клавиатурные сокращения
------------------



### Редактирование {.row-span-4}

Ярлык | Действие
---|---
`Ctrl` `Space` | Базовое завершение кода
`Alt` `Enter` | Показать действия по намерениям и быстрые исправления
`Ctrl` `P` | Информация о параметрах (в аргументах вызова метода)
`Ctrl` `Q` | Быстрый поиск документации
`Ctrl` `(навести курсор мыши на код)` | Краткая информация
`Alt` `Insert` | Сгенерировать код... (геттеры, сеттеры, конструкторы)
`Ctrl` `O` | Переопределение методов
`Ctrl` `I` | Реализовать методы
`Ctrl` `Alt` `T` | Окружить... (if..else, try..catch, for и т.д.)
`Ctrl` `/` | Комментировать/некомментировать с помощью комментария строки
`Ctrl` `Shift` `/` | Комментировать/некомментировать с блочным комментарием
`Ctrl` `W` | Выделить последовательно увеличивающиеся блоки кода
`Ctrl` `Shift` `W` | Уменьшить текущее выделение до предыдущего состояния
`Ctrl` `Alt` `L` | Переформатировать код
`Ctrl` `Alt` `I` | Автоматический отступ от строки (строк)
`Ctrl` `D` | Дублировать текущую строку или выделенный блок
`Ctrl` `Y` | Удалить строку по каретке
`Ctrl` `Shift` `J` | Интеллектуальное объединение строк (только для HTML и JavaScript)
`Ctrl` `Enter` | Интеллектуальное разделение строк (только для HTML и JavaScript)
`Shift` `Enter` | Начать новую строку
`Ctrl` `Shift` `U` | Переключение регистра для слова у каретки или выделенного блока
`Ctrl` `Shift` `[` | Выделить до начала блока кода
`Ctrl` `Shift` `]` | Выделить до конца блока кода
`Ctrl` `Delete` | Удалить до конца слова
`Ctrl` `Backspace` | Удалить до начала слова
`Ctrl` `+/-` | Развернуть/свернуть блок кода
`Ctrl` `F4` | Закрыть активную вкладку редактора
`Ctrl` `Shift` `V` | Вставить из истории
{.shortcuts}


### Отладка

Ярлык | Действие
---|---
`F8` | Step over
`F7` | Шаг в
`Shift` `F8` | Шаг наружу
`Alt` `F8` | Оценить выражение
`F9` | Возобновить программу
`Ctrl` `F8` | Переключить точку останова
`Ctrl` `Shift` `F8` | Просмотр точек останова
{.shortcuts}


### Running

Ярлык | Действие
---|---
`Shift` `F10` | Run
`Shift` `F9` | Отладка
`Ctrl` `Shift` `F10` | Запуск контекстной конфигурации из редактора
`Ctrl` `Shift` `X` | Запуск командной строки
{.shortcuts}


### Поиск/Замена

Ярлык | Действие
---|---
`Ctrl` `F/R` | Найти/Заменить
`F3` | Найти следующий
`Shift` `F3` | Найти предыдущий
`Ctrl` `Shift` `F/R` | Найти/заменить в пути
{.shortcuts}


### Использование Поиск

Ярлык | Действие
---|---
`Alt` `F7` | Найти употребления
`Ctrl` `F7` | Найти использования в файле
`Ctrl` `Shift` `F7` | Подчеркнуть использования в файле
`Ctrl` `Alt` `F7` | Show usages
{.shortcuts}


### Навигация {.row-span-2}

Ярлык | Действие
---|---
`Ctrl` `N` | Перейти к классу
`Ctrl` `Shift` `N` | Переход к файлу
`Ctrl` `Shift` `Alt` `N` | Переход к символу
`Ctrl` `G` | Переход к строке
`Alt` `Left/Right` | Переход на следующую/предыдущую вкладку редактора
`Esc` | Переход к редактору (из окна инструментов)
`Ctrl` `E` | Всплывающее окно Последние файлы
`Ctrl` `Alt` `Лево/Право` | Навигация назад/вперед
`Ctrl` `Shift` `Backspace` | Переход к последнему месту редактирования
`Alt` `F1` | Выбрать текущий файл или символ в любом представлении
`Ctrl` `B` | Переход к декларации
`Ctrl` `Alt` `B` | Переход к реализации(ям)
`Ctrl` `Shift` `I` | Открыть быстрый поиск определений
`Ctrl` `Shift` `B` | Переход к объявлению типа
`Ctrl` `U` | Переход к суперметоду/суперклассу
`Alt` `Up/Down` | Переход к предыдущему/следующему методу
`Ctrl` `]/[` | Переход к концу/началу блока кода
`F2` | Следующая выделенная ошибка
`Shift` `F2` | Предыдущая выделенная ошибка
`F4` | Редактировать/просмотреть источник
{.shortcuts}


### Рефакторинг

Ярлык | Действие
---|---
`F5/F6` | Копировать/переместить
`Alt` `Delete` | Безопасное удаление
`Shift` `F6` | Переименовать
`Ctrl` `Alt` `N` | Встроенная переменная
`Ctrl` `Alt` `M/V/F/C` | Извлечь метод/переменную/поле/константу
`Ctrl` `Alt` `Shift` `T` | Refactor This (показывает все доступные рефакторинги)
{.shortcuts}


### VCS/Local History

Ярлык | Действие
---|---
`Alt` <code>\`</code> | Быстрое всплывающее окно VCS
`Ctrl` `K` | Зафиксировать проект в VCS
`Ctrl` `T` | Обновить проект из VCS
`Alt` `Shift` `C` | Просмотр последних изменений
{.shortcuts}


### Общие сведения

Ярлык | Действие
---|---
`Shift x2` | Поиск везде
`Ctrl` `Shift` `A` | Найти действие
`Alt` `1-9` | Открыть окно соответствующего инструмента
`Ctrl` `Alt` `F11` | Переключение в полноэкранный режим
`Ctrl` `Shift` `F12` | Включить режим максимизации редактора
`Alt` `Shift` `F` | Добавить в избранное
`Alt` `Shift` `I` | Просмотреть текущий файл с текущим профилем
`Ctrl` `Alt` `S` | Открыть диалог настроек
`Ctrl` `Tab` | Переключение между вкладками и окном инструментов
{.shortcuts}


### Живые шаблоны/ сниппеты

Ярлык | Действие
---|---
`Ctrl` `J` | Вставить живой шаблон
`eco` | 'echo' statement
`fore` | foreach(iterable_expr as $value) {...}
`forek` | foreach(iterable_expr as $key => $value) {...}
`inc/inco` | Утверждение 'include'/'include_once'
`prif` | private function
`prof` | protected function
`pubf` | public function
`rqr/rqro` | 'require'/'require_once' statement
{.shortcuts}



### Misc

Ярлык | Действие
---|---
`Ctrl` `Shift` `A` | Find Action
{.shortcuts}




Также см.
--------
- [Клавиатурные сокращения для PhpStorm](https://resources.jetbrains.com/storage/products/phpstorm/docs/PhpStorm_ReferenceCard.pdf) _(resources.jetbrains.com)_