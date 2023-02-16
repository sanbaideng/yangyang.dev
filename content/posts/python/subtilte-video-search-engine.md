---
title: "subtitle(local) and video(online)  search system"
date: 2023-02-12T08:30:12+08:00
draft: true
---
# 视频搜索系统

  - ```爬取全网字幕，然后根据字幕时间戳，查找视频并下载相应片段（这里还没有自动操作，需人工查看时间戳是否对准）```


简要架构
---

![avatar](https://res.cloudinary.com/dkmuoufxh/image/upload/v1676537068/result_uqaito.jpg)

涉及内容：

- 前端项目：
https://github.com/PanJiaChen/vue-element-admin/
- fastapi:
https://github.com/tiangolo/fastapi
- kingshard:
https://github.com/flike/kingshard
- 字幕爬虫
- zip解压
- 字幕提取
- 写入字幕到mysql
- mysql-写入elasticsearch
- 视频地址爬虫
- 视频下载
https://github.com/nilaoda/N_m3u8DL-CLI
