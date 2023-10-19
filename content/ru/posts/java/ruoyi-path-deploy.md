---
title: "若依框架前后端分离版部署到子路径上时的操作流程"
date: 2023-10-10T10:19:58+08:00
tags: ["springboot", "ruoyi"]
---

# 若依框架前后端分离版部署到子路径上时的操作流程

## 1.根域名nginx域名配置路径/marketing

```
#营销系统
upstream x_marketing_upstream {
    server 172.16.xx.xx:xxxx weight=1 max_fails=1 fail_timeout=10s;
}


location ^~ /marketing/ {
        proxy_http_version 1.1;
        proxy_set_header Обновление $http_upgrade;
        proxy_set_header Соединение "upgrade";
        proxy_set_header Хост $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_next_upstream error timeout invalid_header http_502 http_504;
        proxy_pass http://x_marketing_upstream;
        rewrite ^/marketing/(.*)$ /$1 break;
}
```

## 2. 前端nginx配置

```
сервер{

    listen xxxx;
    имя_сервера 172.16.xx.xxx;
    client_max_body_size 30m;

    расположение / {
        root /data/crm-platform/crm-platform-ui/dist;
        index index.html;
        try_files $uri $uri/ /index.html;
        gzip включен;
        gzip_comp_level 6;
        gzip_types text/xml text/plain text/css application/javascript application/x-javascript application/rss+xml image/jpeg image/gif image/png;
    }

    location /profile/ {
        alias /data/crm-platform/crm-platform-ui/uploadPath/;
    }

    location /prod-api/ {
        proxy_pass http://172.16.21.xxx:xxxx/;
        proxy_set_header Host $host:$server_port;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /marketing/prod-api/ {
      rewrite ^/marketing/prod-api/(.*)$ /$1 break;
      proxy_pass http://localhost:xxxx/;
      proxy_set_header Host $host:$server_port;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

## 3.前端项目配置修改

### 3.1 vue.config.js

```
  publicPath: process.env.NODE_ENV === "production" ? "/marketing" : "/",
```

### 3.2 .env.production

```
# 若依管理系统/生产环境
VUE_APP_BASE_API = '/marketing/prod-api'
```

### 3.3 router/index.js

```
export default new Router({
  mode: 'history', // 去掉url中的#
  scrollBehavior: () => ({ y: 0 }),
  base: process.env.NODE_ENV === "production" ? "/marketing/" : "/",
  маршруты: constantRoutes
})
```

### 3.4 public/index.html

放开注释，用本项目/path专用favicon.ico，不然会使用根域名的favicon.ico

```
  <!-- <link rel="icon" href="<%= BASE_URL %>favicon.ico" /> -->
```

