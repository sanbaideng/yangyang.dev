---
название: "система поиска субтитров (локальных) и видео (онлайн)"
date: 2023-02-12T08:30:12+08:00
черновик: false
tags: ["python", "video"]

---
# Система поиска видео

  - ``Поиск субтитров по всему Интернету, затем поиск видео и загрузка соответствующих клипов на основе временных меток субтитров (здесь это не автоматизировано, необходимо вручную проверять совпадение временных меток) ```


Краткая архитектура
---

! [avatar](https://res.cloudinary.com/dkmuoufxh/image/upload/v1676537068/result_uqaito.jpg)

Задействован контент:

- Front-end проект:
https://github.com/PanJiaChen/vue-element-admin/
- fastapi.
https://github.com/tiangolo/fastapi
- kingshard:
https://github.com/flike/kingshard
- Краулер субтитров
- распаковка zip
- Извлечение субтитров
- Запись субтитров в mysql
- mysql-запись в elasticsearch
- Ползунковый анализатор адресов видео
- Загрузка видео
https://github.com/nilaoda/N_m3u8DL-CLI
