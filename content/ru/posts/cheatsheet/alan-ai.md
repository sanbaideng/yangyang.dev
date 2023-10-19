---
title: Алан ИИ
date: 2023-03-03 6:00:00
фон: bg-[#4aa181]
теги:
    - ИИ
    - AlanAI
    - Подсказки
    - Советы
категории:
    - Инструментарий
введение: Эта шпаргалка охватывает все основные концепции сценариев, методы клиентского API, обработчики и другие инструменты для создания мультимодального разговорного опыта с Alan AI
---

### Легенда

- ``паттерн'' - фраза, вызывающая голосовую/текстовую команду или воспроизводимый ответ
- ``значение`` - указанное значение
- ``параметры`` - передаваемые параметры
- ``действие`` - действие, которое должно быть выполнено
- ``output`` - результат обработки данных
- ``[...]`` - необязательные данные или параметры

Скрипт диалога
-------------

### Намерения и шаблоны

Определение голосовой/текстовой команды для воспроизведения ответа

``` {.wrap}
intent('pattern'[, 'patternN'], reply('pattern'))
```

Определение голосовой/текстовой команды для воспроизведения ответа или выполнения действия
``` {.wrap}
intent('pattern'[, 'patternN'], p => { action })
```

Определение альтернатив
``` {.wrap}
intent('phrase1|phrase2')
```

Определение необязательных слов и фраз
``` {.wrap}
intent('pattern (optional phrase|)')
```



### Функции ответа

Воспроизведение ответа (в случае нескольких шаблонов ответ выбирается случайным образом)
``` {.wrap}
reply('pattern'[, 'patternN'])
```

Воспроизведение ответа
``` {.wrap}
p.play('pattern')
```

Задание голосовых настроек для ответа ассистента: ``акцент (en, fr, de, it, ru, es)``, ``гендер (мужской/женский)``, ``тип голоса``, ``высота тона речи``, ``темп речи``.
`` {.wrap}
p.play([voice(code, gender, type, pitch, rate), ]'pattern')
```

Определяем параметры воспроизведения: ``force:true`` (выполнить, если кнопка неактивна), ``activate:true`` (активировать кнопку до), ``deactivate:true`` (деактивировать кнопку после)
``` {.wrap}
p.play('pattern'[, opts(options)])
```

Отправляем команду в приложение
``` {.wrap}
p.play({команда:data})
```

### Слоты, определяемые пользователем

Определяют статический список значений, ожидаемых на входе

``` {.wrap}
$(SLOTNAME value1|value2) => p.SLOTNAME.value
```

Предоставление меток для классификации или идентификации значений слотов

``` {.wrap}
$(SLOTNAME value1~label1|value2~label2) => p.SLOTNAME.label
```

Включить нечеткое сопоставление для выявления похожих вариантов

``` {.wrap}
$(SLOTNAME~ value1|value2) => p.SLOTNAME.value
```

Сделать слот необязательным

``` {.wrap}
$(SLOTNAME value1|value2|)
```

Захват нескольких значений слотов

``` {.wrap}
intent('$(SLOTNAME value1|value2) и $(SLOTNAME value1|value2 )') => p.SLOTNAME_ (array), p.SLOTNAME_[0].value, p.SLOTNAME_[1].value
```

### Предопределенные слоты

Захват значений даты

``` {.wrap}
$(DATE) => p.DATE.value, p.DATE.moment, p.DATE.luxon
```

Захват значений времени

``` {.wrap}
$(TIME) => p.TIME.value, p.TIME.moment
```

Захват кардинальных чисел

``` {.wrap}
$(NUMBER) => p.NUMBER.value, p.NUMBER.number
```

Захват порядковых номеров

``` {.wrap}
$(ORDINAL) => p.ORDINAL.value, p.ORDINAL.number
```

Захват местоположений

``` {.wrap}
$(LOC) => p.LOC.value
```

Захват имен

``` {.wrap}
$(NAME) => p.NAME.value
```

### Динамические слоты

Определение динамического слота на уровне проекта

``` {.wrap}
project.name = {en: "value1|value2|value3"}
$(SLOTNAME p:name) => p.SLOTNAME.value
```

Определение динамического слота на уровне диалоговой сессии

``` {.wrap}
p.userData.name = {en: "value1|value2|value3"}
$(SLOTNAME u:name) => p.SLOTNAME.value
```

Получение данных для динамического слота с визуальным состоянием

``` {.wrap}
let name = ["value1|value2|value3"]
p.visual.data = {en: name};
$(SLOTNAME v:name) => p.SLOTNAME.value
```

Определение динамического слота в короткой форме

``` {.wrap}
project.name = {en: "value1|value2|value3"}
$(p:name) => p.SLOTNAME.value
```

Определение меток для динамических слотов: см. раздел [User-defined slots](#user-defined-slots).

Включить нечеткое соответствие для динамических слотов: см. раздел [User-defined slots](#user-defined-slots).

Сделать динамический слот необязательным: см. раздел [User-defined slots](#user-defined-slots).

Захват нескольких значений слотов: см. раздел [User-defined slots](#user-defined-slots).


### Слоты RegEx

Захват комбинации цифр и/или букв

``` {.wrap}
const reg = "([A-Za-z]{1}\\\s?){6}"
$(SLOTNAME* ${reg}) => p.SLOTNAME.value
```

Перехватываем любой пользовательский ввод

``` {.wrap}
$(SLOTNAME* .+) => p.SLOTNAME.value
```

### Контексты

Определение контекста

``` {.wrap}
let contextName = context(() => { action })
```

Активация контекста

``` {.wrap}
intent('pattern', p => {..., p.then(contextName)}
```

Передача данных в контекст

``` {.wrap}
p.then(contextName, state: {data:yourData}) => p.state.data
```

Разрешить контекст

``` {.wrap}
p.resolve([data:yourData])
```


Сброс контекста

``` {.wrap}
p.resetContext()
```

Определение намерений, которые могут быть сопоставлены в любой момент времени без переключения текущего контекста

``` {.wrap}
intent(noctx, 'pattern', ...) или noContext(() => {intent(...)})
```

Воспроизведение подсказки для ожидаемого ввода

``` {.wrap}
fallback('pattern1'[, 'patternN'])
```

Заголовок контекста

``` {.wrap}
title('contextName')
```

### Предопределенные объекты

Хранят статические данные об устройстве и пользователе, передаваемые из клиентского приложения

``` {.wrap}
authData.data => p.authData.data
```

Храним данные о состоянии, чтобы они были доступны глобально в масштабе проекта

``` {.wrap}
project.info = {data:yourData} => project.info.data
```

Хранение оценки совпадения намерений

``` {.wrap}
p.score
```

Хранение данных для передачи между контекстами

``` {.wrap}
p.state.data
```

Хранить данные визуального контекста, которые будут передаваться из клиентского приложения с помощью ``setVisualState()``.

``` {.wrap}
p.visual.data
```

Хранит данные о состоянии пользователя, доступные во время сеанса диалога

``` {.wrap}
p.userData.data
```

### Предопределенные обратные вызовы

Определяют действия, которые будут выполняться при сохранении скрипта и построении диалоговой модели

``` {.wrap}
onCreateProject(() => { action })
```

Определите действия, которые будут выполняться при запуске сеанса диалога

``` {.wrap}
onCreateUser((p) => { action })
```

Определите действия, которые будут выполняться при завершении сеанса диалога

``` {.wrap}
onCleanupUser((p) => { action })
```

Определяем действия, которые будут выполняться при установке визуального состояния

``` {.wrap}
onVisualState((p, s) => { action })
```

Определите действия, которые будут выполняться при возникновении пользовательского события в клиентском приложении: ``buttonReady``, ``buttonClicked``, ``micPermissionPrompt``, ``micAllowed``, ``firstActivate``, ``showPopup``, ``popupCloseClicked``, ``recognized``.

`` {.wrap}
onUserEvent((p, e) => { action })
```

Определение действий, которые будут выполняться при активации контекста

``` {.wrap}
onEnter((p) => { action })
```


### Сервис вопросов и ответов

Определение URL-адреса индексируемого ресурса

``` {.wrap}
corpus({url: url, depth: depthLevel})
```

Определение корпуса текстов, который будет использоваться ассистентом в диалоге
``` {.wrap}
corpus('text')
```

### Встроенные JS-библиотеки

Выполнение вызовов API

``` {.wrap}
axios, request
```

Работа со временем

``` {.wrap}
moment-timezone, luxon
```

Работа с массивами, числами, объектами, строками и т.д.

``` {.wrap}
lodash
```

### Другое

Приведите список подсказок, помогающих распознать конкретные термины

``` {.wrap}
recognitionHints('hint'[, 'hintN'])
```

Запись информационных сообщений в журналы Alan Studio

``` {.wrap}
console.log(data)
```

Запись сообщений об ошибках в журналы Alan Studio

``` {.wrap}
console.error(data)
```

Клиентский SDK
----------

### Методы клиентского API

Передача информации о визуальном состоянии из клиентского приложения в скрипт диалога

``` {.wrap}
setVisualState(visualStateData:object)
```

Передача данных или выполнение действий без голосовой/текстовой команды

``` {.wrap}
projectAPI.method = function(p, param, callback) {
  p.userData.data = param.data;
  callback();
};

callProjectApi(method:string, data:object, callback:function)
```

Воспроизведение текстового сообщения в клиентском приложении

``` {.wrap}
playText(text:string)
```

Передача текстового сообщения в Alan в качестве входного сигнала пользователя

``` {.wrap}
sendText(text:string)
```

Выполнение команды в клиентском приложении

``` {.wrap}
playCommand(command:object)
```

### Методы клиентского API (продолжение)

Программная активация кнопки Alan

``` {.wrap}
activate()
```

Деактивировать кнопку Alan программно

``` {.wrap}
deactivate()
```

Проверка состояния кнопки Alan

``` {.wrap}
isActive()
```

Удаление кнопки Alan из родительского элемента, страницы (поддерживается в Web, Ionic)

``` {.wrap}
remove()
```

Проверка состояния слова wake (поддерживается на iOS, Android)

``` {.wrap}
getWakewordEnabled()
```

Установка состояния слова пробуждения (поддерживается на iOS, Android)

``` {.wrap}
setWakewordEnabled(enabled:boolean)
```

### Обработчики

// Примеры приведены для Web-платформы

Обработка команд, передаваемых из сценария диалога в клиентское приложение

`` {.wrap}
onCommand: function (commandData) { action }
```

Обработка изменений состояния кнопки Alan

``` {.wrap}
onButtonState: function (e) { action }
```

Обработка состояния подключения к проекту виртуального помощника в Alan Cloud

``` {.wrap}
onConnectionStatus: function (e) { action }
```

Обработка событий, полученных от Alan

``` {.wrap}
onEvent: function (e) { action }
```




Также см.
--------

- [Сайт Alan AI](https://alan.app)
- [О платформе Alan](https://alan.app/platform)
- [Документация Alan AI](https://alan.app/docs)



<style>
em { font-size: 0.785em; }
strong { font-weight: 400;}
ul.collapsible > li > pre { padding-left: 0; padding-right: 0; font-size: 0.925em;}
</style>
