---
Название: GraphQL
дата: 2021-07-15 20:51:44
фон: bg-[#cc44a2]
теги:
    - запрос
    - API
категории:
    - Программирование
intro: |
    Эта краткая шпаргалка содержит краткий обзор GraphQL.
плагины:
    - copyCode
---


Начало работы
--------

### Обзор

- Альтернативный подход к RESTful API
- GraphQL - это язык запросов для API.
- Легко описать форму API GraphQL с помощью понятных общих терминов.
- Клиенты выполняют запросы/мутации для чтения и обновления данных
- Синтаксис GraphQL может выражать сложные отношения между сущностями
- Библиотеки для реализации GraphQL на [различных языках](https://graphql.org/code/)

[GraphQL](https://graphql.org/)
{.link-arrow}


### Схема

| | |
|----------------|----------------------------------|
| `schema` | Определение схемы GraphQL |
| `query` | Чтение и просмотр данных |
| `мутация` | Изменение данных или инициирование действия |
| `subscription` | Запуск запроса при наступлении события |



### Встроенные скалярные типы

| | |
|-----------|----------------------------------------------|
| `Int` | Подписанное 32-битное целое число |
| `Float` | Подписанное значение с плавающей точкой двойной точности |
| `String` | Последовательность символов в формате UTF-8 |
| `Boolean` | true или false |
| `ID` | Уникальный идентификатор |



### Определения типов

| | |
|-------------|-------------------|
| | `scalar` | Скалярный тип |
| `type` | Object Type |
| `интерфейс` | Тип интерфейса |
| `union` | Union Type |
| `enum` | Enum Type |
| `input` | Input Object Type |



### Модификаторы типов

| | |
|--------------|-----------------------------------|
| `String` | Нулевая строка |
| `String!` | Non-null String |
| `[String]` | Список нулевых строк |
| | `[String]!` | Не нулевой список нулевых строк |
| `[String!]!` | Ненулевой список ненулевых строк |


### Входные аргументы {.row-span-2}
#### Основной ввод
``js
тип Query {
    users(limit: Int): [User]
}
```

#### Вход со значением по умолчанию
``js
тип Query {
    users(limit: Int = 10): [User]
}
```


#### Ввод с несколькими аргументами
``js
тип Query {
    users(limit: Int, sort: String): [User]
}
```


#### Ввод с несколькими аргументами и значениями по умолчанию

``js {.wrap}
тип Query {
    users(limit: Int = 10, sort: String): [User]
}
type Query {
    users(limit: Int, sort: String = "asc"): [User]
}
type Query {
    users(limit: Int = 10, sort: String = "asc"): [User]
}
```


### Типы ввода


``js
input ListUsersInput {
    лимит: Int
    since_id: ID
}
```

``js
тип Мутация {
    users(params: ListUsersInput): [User]!
}
```

### Пользовательские скаляры


``js
scalar Url
тип Пользователь {
    имя: String
    домашняя страница: Url
}
```


### Интерфейсы

``js
интерфейс Foo {
    is_foo: Boolean
}
интерфейс Goo {
    is_goo: Boolean
}
тип Bar реализует Foo {
    is_foo: Boolean
    is_bar: Boolean
}
type Baz implements Foo, Goo {
    is_foo: Boolean
    is_goo: Boolean
    is_baz: Boolean
}
```
Объект, реализующий один или несколько интерфейсов


### Союзы

``js
тип Foo {
    имя: String
}
тип Bar {
    is_bar: String
}
союз SingleUnion = Foo
union MultipleUnion = Foo | Bar
тип Root {
    single: SingleUnion
    множественный: MultipleUnion
}
```
Объединение одного или нескольких объектов


### Enums

``js {.wrap}
enum USER_STATE {
    НЕ_НАЙДЕН
    ACTIVE
    НЕАКТИВНЫЙ
    SUSPENDED
}
тип Root {
    stateForUser(userID: ID!): USER_STATE!
    users(state: USER_STATE, limit: Int = 10): [User]
}
```



Также см.
-------
* [GraphQL Schema Language Cheat Sheet](https://github.com/sogko/graphql-schema-language-cheat-sheet) _(github.com)_
