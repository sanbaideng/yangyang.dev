---
title: "шпаргалка по общим операциям python"
date: 2023-08-03T08:30:12+08:00
tag: ["python", "шпаргалка"]

---
## шпаргалка по общим операциям python
## Итерация по файлам каталога.
``

импортировать os
for root, dirs, files in os.walk('dist', topdown=False)::
    for name in files.
        file_path = os.path.join(root, name)
        file_dirname = os.path.dirname(file_path)
        print(file_path,file_dirname)
``
## python получить текущее время
```
from datetime import datetime
currentDateAndTime = datetime.now()

print("The current date and time is", currentDateAndTime)
# Вывод: текущая дата и время - 2023-08-03 10:05:39.482383

currentTime = currentDateAndTime.strftime("%H:%M:%S")
print("The current time is", currentTime)
# Текущее время 10:06:55
``
### python Дата накануне
``##
from datetime import date
    today = date.today()
    end_time = today + datetime.timedelta(days = -1)
```
## peewee показывает, что драйвер MySQL не установлен!
После установки peewee необходимо установить драйвер mysql вручную.
```
pip install pymysql
```
## Пакет python urllib.request как добавить заголовки запросов
```
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36" )
``
## python как вызвать post-запрос с помощью пакета urllib.request
```
from urllib.request import Request, urlopen
req = Request(url=url, method='POST',data=bytes(json.dumps(datas), encoding="utf-8") )
response = urlopen(req)
html = response.read()
print(html)
```
## python Определить, не превышает ли текущее время 12:00 : datetime.datetime.now().hour
```
now_time = datetime.datetime.now()

if now_time.hour<=12:.
    print('Текущее время меньше 12 часов')
```
## python string to json
```
импортировать json
jsondata = json.loads(jsonstr)
```
## python read txt file
Используйте оператор with для управления открытием файла, end автоматически закроет файл, шаг f.close() можно опустить.
```
#1. Метод read() означает чтение всего содержимого файла за один раз, при этом возвращается строка.
with open("1.txt", "r") as f.
    data = f.read()
    print(data)

#2. Метод readline() Этот метод читает по одной строке за раз, поэтому занимает меньше памяти при чтении и больше подходит для больших файлов, а также этот метод возвращает строковый объект.
with open("test.txt", "r") as f.
    data = f.readline()
    print(data)

#3. метод readlines() Этот метод читает все строки всего файла, сохраненные в переменной list (список), читает по одной строке за раз, но чтение больших файлов будет занимать больше памяти.
with open("test.txt", "r") as f.
    data = f.readlines()
    print(data)
``