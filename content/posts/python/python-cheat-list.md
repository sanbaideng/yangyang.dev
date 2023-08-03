---
title: "python 常用操作cheat sheet"
date: 2023-08-03T08:30:12+08:00
draft: false
tags: ["python", "cheat sheet"]

---
# python 常用操作cheat sheet
## 遍历目录文件
```

import os
for root, dirs, files in os.walk('dist', topdown=False):
    for name in files:
        file_path = os.path.join(root, name)
        file_dirname = os.path.dirname(file_path)
        print(file_path,file_dirname)
```
## python 获取当前时间       
```
from datetime import datetime
currentDateAndTime = datetime.now()

print("The current date and time is", currentDateAndTime)
# Output: The current date and time is 2023-08-03 10:05:39.482383

currentTime = currentDateAndTime.strftime("%H:%M:%S")
print("The current time is", currentTime)
# The current time is 10:06:55
```
### python 日期前一天
```
from datetime import date
    today = date.today()
    end_time = today + datetime.timedelta(days = -1)
```
## peewee 出现 MySQL driver not installed!
安装peewee后，需要手动安装mysql 驱动
```
pip install pymysql
```
## python urllib.request包如何添加请求头headers
```
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
```
## python如何使用urllib.request包调用post请求 
```
from urllib.request import Request, urlopen 
req = Request(url=url, method='POST',data=bytes(json.dumps(datas), encoding="utf-8") )
response = urlopen(req)
html = response.read()
print(html)
```
## python 判断当前时间 是否不超过12点 : datetime.datetime.now().hour
```
now_time = datetime.datetime.now()   

if now_time.hour<=12:
    print('当前时间小于12点')
```
