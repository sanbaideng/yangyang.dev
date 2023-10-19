---
Название: MongoDB
дата: 2023-04-05
background: bg-gradient-to-r from-green-900 via-green-600 to-green-400 hover:from-green-900 hover:via-green-700 hover:to-green-500
теги:
  - NoSQL
  - БД
категории:
  - Базы данных
intro: Шпаргалка по MongoDB содержит наиболее часто используемые команды и запросы к MongoDB для справки. шпаргалка взята с сайта разработчиков mongodb
плагины:
  - подсказка
  - copyCode
---

## Начало работы {.cols-2}

### Подключение оболочки MongoDB

``mongosh
mongo # по умолчанию подключается к mongodb://127.0.0.1:27017
```

```mongosh
mongo --host <host> --port <port> -u <user> -p <pwd> # опустите пароль, если хотите получить подсказку
```

``mongosh
mongo "mongodb://192.168.1.1:27017"
```

```mongosh
mongo "mongodb+srv://cluster-name.abcde.mongodb.net/<dbname>" --username <username> # MongoDB Atlas
```

### Помощники

show dbs :

``mongosh
db // выводит текущую базу данных
```

Переключить базу данных :

``mongosh
использовать <имя_базы_данных>
```

Показать коллекции :

``mongosh
показать коллекции
```

Запустить файл JavaScript :

``mongosh
load("myScript.js")
```

---

## Crud

### Создать

``mongosh
db.coll.insertOne({имя: "Макс"})
db.coll.insert([{имя: "Макс"}, {имя: "Алекс"}]) // заказная массовая вставка
db.coll.insert([{имя: "Макс"}, {имя: "Алекс"}], {ordered: false}) // неупорядоченная массовая вставка
db.coll.insert({date: ISODate()})
db.coll.insert({name: "Max"}, {"writeConcern": {"w": "majority", "wtimeout": 5000}})
```

### Удалить

``Монгош
db.coll.remove({name: "Max"})
db.coll.remove({name: "Max"}, {justOne: true})
db.coll.remove({}) // ВНИМАНИЕ! Удаляются все документы, но не сама коллекция и определения ее индексов
db.coll.remove({name: "Max"}, {"writeConcern": {"w": "majority", "wtimeout": 5000}})
db.coll.findOneAndDelete({"name": "Max"})
```

### Обновление

``Монгош
db.coll.update({"_id": 1}, {"year": 2016}) // ВНИМАНИЕ! Заменяет весь документ
db.coll.update({"_id": 1}, {$set: {"year": 2016, name: "Max"}})
db.coll.update({"_id": 1}, {$unset: {"year": 1}})
db.coll.update({"_id": 1}, {$rename: {"year": "date"} })
db.coll.update({"_id": 1}, {$inc: {"year": 5}})
db.coll.update({"_id": 1}, {$mul: {price: NumberDecimal("1.25"), qty: 2}})
db.coll.update({"_id": 1}, {$min: {"imdb": 5}})
db.coll.update({"_id": 1}, {$max: {"imdb": 8}})
db.coll.update({"_id": 1}, {$currentDate: {"lastModified": true}})
db.coll.update({"_id": 1}, {$currentDate: {"lastModified": {$type: "timestamp"}}})
```

### Массив { .row-span-2 }

``mongosh
db.coll.update({"_id": 1}, {$push :{"array": 1}})
db.coll.update({"_id": 1}, {$pull :{"array": 1}})
db.coll.update({"_id": 1}, {$addToSet :{"array": 2}})
db.coll.update({"_id": 1}, {$pop: {"array": 1}}) // последний элемент
db.coll.update({"_id": 1}, {$pop: {"array": -1}}) // первый элемент
db.coll.update({"_id": 1}, {$pullAll: {"array" :[3, 4, 5]}})
db.coll.update({"_id": 1}, {$push: {scores: {$each: [90, 92, 85]}}})
db.coll.updateOne({"_id": 1, "grades": 80}, {$set: {"grades.$": 82}})
db.coll.updateMany({}, {$inc: {"grades.$[]": 10}})
db.coll.update({}, {$set: {"grades.$[element]": 100}}, {multi: true, arrayFilters: [{"element": {$gte: 100}}]})
```

### Обновление множества { .row-span-1 }

``mongosh
db.coll.update({"year": 1999}, {$set: {"decade": "90's"}}, {"multi":true})
db.coll.updateMany({"year": 1999}, {$set: {"decade": "90's"}})
```

### FindOneAndUpdate { .row-span-1 }

```mongosh
db.coll.findOneAndUpdate({"name": "Max"}, {$inc: {"points": 5}}, {returnNewDocument: true})
```

### Upsert { .row-span-1 }

``mongosh
db.coll.update({"_id": 1}, {$set: { item: "apple"}, $setOnInsert: {defaultQty: 100}}, {upsert: true})
```

### Заменить { .row-span-1 }

```mongosh
db.coll.replaceOne({"name": "Max"}, {"firstname": "Maxime", "surname": "Beugnet"})
```

### Сохранить { .row-span-1 }

``mongosh
db.coll.save({"item": "book", "qty": 40})
```

### Write concern { .row-span-1 }

``mongosh
db.coll.update({}, {$set: {"x": 1}}, {"writeConcern": {"w": "majority", "wtimeout": 5000}})
```

### Найти { .row-span-2 }

``mongosh
db.coll.findOne() // возвращает один документ
db.coll.find() // возвращает курсор - показать 20 результатов - "это" для отображения большего количества
db.coll.find().pretty()
db.coll.find({имя: "Макс", возраст: 32}) // неявное логическое "И".
db.coll.find({date: ISODate("2020-09-25T13:57:17.180Z")})
db.coll.find({имя: "Макс", возраст: 32}).explain("executionStats") // или "queryPlanner", или "allPlansExecution"
db.coll.distinct("name")
```

### Count

```монгош
db.coll.count({age: 32}) // оценка на основе метаданных коллекции
db.coll.estimatedDocumentCount() // оценка на основе метаданных коллекции
db.coll.countDocuments({age: 32}) // псевдоним для конвейера агрегации - точный подсчет
```

### Сравнение

```монгош
db.coll.find({"год": {$gt: 1970}})
db.coll.find({"год": {$gte: 1970}})
db.coll.find({"год": {$lt: 1970}})
db.coll.find({"год": {$lte: 1970}})
db.coll.find({"год": {$ne: 1970}})
db.coll.find({"год": {$in: [1958, 1959]}})
db.coll.find({"год": {$nin: [1958, 1959]}})
```

### Логический

```монгош
db.coll.find({name:{$not: {$eq: "Max"}}})
db.coll.find({$or: [{"год" : 1958}, {"год" : 1959}]})
db.coll.find({$nor: [{price: 1.99}, {sale: true}]})
db.coll.find({
$and: [
    {$or: [{qty: {$lt :10}}, {qty :{$gt: 50}}]}
{ $or: [{sale: true}, {price: {$lt: 5 }}]}
]
})
```

### Элемент

```монгош
db.coll.find({name: {$exists: true}})
db.coll.find({"zipCode": {$type: 2 }})
db.coll.find({"zipCode": {$type: "string"}})
```

### Конвейер агрегации

```монгош
db.coll.aggregate([
{$match: {status: "A"}},
{$group: {_id: "$cust_id", total: {$sum: "$amount"}}},
{$sort: {total: -1}}
])
```

### Текстовый поиск с индексом "text"

```монгош
db.coll.find({$text: {$search: "cake"}}, {score: {$meta: "textScore"}}).sort({score: {$meta: "textScore"}})
```

### Regex

```монгош
db.coll.find({name: /^Max/}) // regex: начинается на букву "М"
db.coll.find({имя: /^Max$/i}) // регекс нечувствителен к регистру
```

### Массив

``Монгош
db.coll.find({tags: {$all: ["Realm", "Charts"]}})
db.coll.find({field: {$size: 2}}) // индексировать невозможно - лучше хранить размер массива и обновлять его
db.coll.find({results: {$elemMatch: {product: "xyz", score: {$gte: 8}}}})
```

### Прогнозы

``Монгош
db.coll.find({"x": 1}, {"actors": 1}) // актеры + \_id
db.coll.find({"x": 1}, {"actors": 1, "\_id": 0}) // актеры
db.coll.find({"x": 1}, {"actors": 0, "summary": 0}) // все, кроме "actors" и "summary"
```

### Сортировка, пропуск, ограничение

``Монгош
db.coll.find({}).sort({"год": 1, "рейтинг": -1}).skip(10).limit(3)
```

### Читательский концерн

```монгош
db.coll.find().readConcern("большинство")
```


## Базы данных и коллекции { .cols-2 }

### Drop { .row-span-1 }

``mongosh
db.coll.drop() // удаляет коллекцию и определения ее индексов
db.dropDatabase() // дважды проверьте, что вы *NOT* на кластере PROD... :-)
```

### Создаем коллекцию { .row-span-2}

``mongosh
db.createCollection("contacts", {
   validator: {$jsonSchema: {
      bsonType: "object",
      required: ["phone"],
      properties: {
         phone: {
            bsonType: "string",
            описание: "must be a string and is required"
         },
         email: {
            bsonType: "string",
            pattern: "@mongodb\.com$",
            описание: "должно быть строкой и соответствовать шаблону регулярного выражения"
         },
         status: {
            enum: ["Unknown", "Incomplete" ],
            описание: "может быть только одно из значений перечисления"
         }
      }
   }}
})
```

### Другие функции коллекции { .row-span-1}

``mongosh
db.coll.stats()
db.coll.storageSize()
db.coll.totalIndexSize()
db.coll.totalSize()
db.coll.validate({full: true})
db.coll.renameCollection("new_coll", true) // 2-й параметр для удаления целевой коллекции, если она существует
```


## Индексы {.cols-2}

### Основы

#### Список

``mongosh
db.coll.getIndexes()
db.coll.getIndexKeys()
```

#### Drop Indexes

``mongosh
db.coll.dropIndex("name_1")
```

#### Скрытие/скрытие индексов

``mongosh
db.coll.hideIndex("name_1")
db.coll.unhideIndex("name_1")
```

### Создание индексов

```mongosh
// Типы индексов
db.coll.createIndex({"имя": 1}) // индекс по одному полю
db.coll.createIndex({"имя": 1, "дата": 1}) // составной индекс
db.coll.createIndex({foo: "text", bar: "text"}) // текстовый индекс
db.coll.createIndex({"$**": "text"}) // текстовый индекс с подстановочными знаками
db.coll.createIndex({"userMetadata.$**": 1}) // индекс подстановочных знаков
db.coll.createIndex({"loc": "2d"}) // индекс 2d
db.coll.createIndex({"loc": "2dsphere"}) // индекс 2dsphere
db.coll.createIndex({"_id": "hashed"}) // хэшированный индекс

// Параметры индекса
db.coll.createIndex({"lastModifiedDate": 1}, {expireAfterSeconds: 3600}) // TTL-индекс
db.coll.createIndex({"name": 1}, {unique: true})
db.coll.createIndex({"name": 1}, {partialFilterExpression: {age: {$gt: 18}}}) // частичный индекс
db.coll.createIndex({"name": 1}, {collation: {locale: 'en', strength: 1}}) // индекс, нечувствительный к регистру, с strength = 1 или 2
db.coll.createIndex({"name": 1 }, {sparse: true})
```

## Другие { .cols-2 }

### Удобные команды { .row-span-3 }

``mongosh
использовать администратора
db.createUser({ "user": "root", "pwd": passwordPrompt(), "roles": ["root"]})
db.dropUser("root")
db.auth("user", passwordPrompt() )

использовать тест
db.getSiblingDB("dbname")
db.currentOp()
db.killOp(123) // opid

db.fsyncLock()
db.fsyncUnlock()

db.getCollectionNames()
db.getCollectionInfos()
db.printCollectionStats()
db.stats()

db.getReplicationInfo()
db.printReplicationInfo()
db.isMaster()
db.hostInfo()
db.printShardingStatus()
db.shutdownServer()
db.serverStatus()

db.setSlaveOk()
db.getSlaveOk()

db.getProfilingLevel()
db.getProfilingStatus()
db.setProfilingLevel(1, 200) // 0 == OFF, 1 == ON with slowms, 2 == ON

db.enableFreeMonitoring()
db.disableFreeMonitoring()
db.getFreeMonitoringStatus()

db.createView("viewName", "sourceColl", [{$project:{department: 1}}])
```

### Набор реплик { .row-span-2}

```mongosh
rs.status()
rs.initiate({"_id": "replicaTest",
  members: [
    { _id: 0, host: "127.0.0.1:27017" },
    { _id: 1, host: "127.0.0.1:27018" },
    { _id: 2, host: "127.0.0.1:27019", arbiterOnly:true }]
})
rs.add("mongodbd1.example.net:27017")
rs.addArb("mongodbd2.example.net:27017")
rs.remove("mongodbd1.example.net:27017")
rs.conf()
rs.isMaster()
rs.printReplicationInfo()
rs.printSlaveReplicationInfo()
rs.reconfig(<valid_conf>)
rs.slaveOk()
rs.stepDown(20, 5) // (stepDownSecs, secondaryCatchUpPeriodSecs)
```

### Sharded Cluster { .row-span-2 }

```mongosh
sh.status()
sh.addShard("rs1/mongodbd1.example.net:27017")
sh.shardCollection("mydb.coll", {zipcode: 1})

sh.moveChunk("mydb.coll", { zipcode: "53187" }, "shard0019")
sh.splitAt("mydb.coll", {x: 70})
sh.splitFind("mydb.coll", {x: 70})
sh.disableAutoSplit()
sh.enableAutoSplit()

sh.startBalancer()
sh.stopBalancer()
sh.disableBalancing("mydb.coll")
sh.enableBalancing("mydb.coll")
sh.getBalancerState()
sh.setBalancerState(true/false)
sh.isBalancerRunning()

sh.addTagRange("mydb.coll", {state: "NY", zip: MinKey }, { state: "NY", zip: MaxKey }, "NY")
sh.removeTagRange("mydb.coll", {state: "NY", zip: MinKey }, { state: "NY", zip: MaxKey }, "NY")
sh.addShardTag("shard0000", "NYC")
sh.removeShardTag("shard0000", "NYC")

sh.addShardToZone("shard0000", "JFK")
sh.removeShardFromZone("shard0000", "NYC")
sh.removeRangeFromZone("mydb.coll", {a: 1, b: 1}, {a: 10, b: 10})
```
### Изменение потоков {.row-span-1 }

```mongosh
watchCursor = db.coll.watch( [ { $match : { "operationType" : "insert" } } ] )

while (!watchCursor.isExhausted()){
   if (watchCursor.hasNext()){
      print(tojson(watchCursor.next()));
   }
}
```