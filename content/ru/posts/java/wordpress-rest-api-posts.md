---
title: "Wordpress use rest Api post Articals"
date: 2023-10-11T11:26:58+08:00
черновик: false
tags: ["wordpress", "rest api"]
---

# Wordpress use rest Api post Articals 用rest api 推送文章到wordpress

## УСТАНОВКА

### 1# Установите плагин jwt

отсюда:

https://wordpress.org/plugins/jwt-authentication-for-wp-rest-api/



ps: минимальная версия php:7.4.0

### PHP HTTP AUTHORIZATION HEADER ENABLE

#### 1.1# .htaccess

изменить с --->

```
# SGS XMLRPC Disable Service
<Файлы xmlrpc.php
	запретить, разрешить
	запретить для всех
</Files>
# SGS XMLRPC Disable Service END


# BEGIN WordPress
<IfModule mod_rewrite.c>
 RewriteEngine On
 RewriteBase /
 RewriteRule ^index\.php$ - [L]
 RewriteCond %{REQUEST_URI} !/(wp-content\/uploads/.*)$
 RewriteCond %{REQUEST_FILENAME} !-f
 RewriteCond %{REQUEST_FILENAME} !-d
 RewriteRule . /index.php [L]
</IfModule>
# END WordPress

# SGO Unset Vary
  Заголовок не установлен Vary
# SGO Unset Vary END
```

to---->

```
# SGS XMLRPC Disable Service
<Файлы xmlrpc.php
	порядок: запретить, разрешить
	запретить для всех
</Files>
# SGS XMLRPC Disable Service END


# BEGIN WordPress
<IfModule mod_rewrite.c>
 RewriteEngine On
 RewriteBase /
 RewriteRule ^index\.php$ - [L]
 RewriteCond %{REQUEST_URI} !/(wp-content\/uploads/.*)$
 RewriteCond %{REQUEST_FILENAME} !-f
 RewriteCond %{REQUEST_FILENAME} !-d
 RewriteCond %{HTTP:Authorization} ^(.*)
 RewriteRule . /index.php [L]
 RewriteRule ^(.*) - [E=HTTP_AUTHORIZATION:%1]
 SetEnvIf Авторизация "(.*)" HTTP_AUTHORIZATION=$1
</IfModule>
# END WordPress

# SGO Unset Vary
  Заголовок не установлен Vary
# SGO Unset Vary END

```

#### НАСТРОЙКА СЕКРЕТНОГО КЛЮЧА

JWT требует **секретного ключа** для подписи токена. Этот **секретный ключ** должен быть уникальным и никогда не раскрываться.
JWT需要一个秘钥来签署令牌，这个秘钥必须是唯一的且永不泄露。

Для добавления **секретного ключа** отредактируйте файл wp-config.php и добавьте новую константу **JWT_AUTH_SECRET_KEY**.
要添加密钥，请编辑您的wp-config.php文件，并添加一个名为JWT_AUTH_SECRET_KEY的新常量。

```
define('JWT_AUTH_SECRET_KEY', 'your-top-secret-key');
```

Вы можете использовать строку отсюда 你可以从这里使用一个字符串 https://api.wordpress.org/secret-key/1.1/salt/.


#### CONFIGURATE CORS SUPPORT 配置CORS支持

В плагине **wp-api-jwt-auth** появилась возможность активировать поддержку [CORs](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing).
wp-api-jwt-auth插件有激活CORs支持的选项。

Чтобы включить поддержку CORs, отредактируйте файл wp-config.php и добавьте новую константу **JWT_AUTH_CORS_ENABLE**.
要启用CORs支持，请编辑您的wp-config.php文件并添加一个名为JWT_AUTH_CORS_ENABLE的新常量。

```
define('JWT_AUTH_CORS_ENABLE', true);
```



### Использование

#### получить jwt-токен

разместить https://example.com/wp-json/jwt-auth/v1/token

данные:

```
 {"username": "xxx@gmail.com", "password": "xxxx" }
```

получим ответ следующим образом:

```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2dlbmcudG9kYXkiLCJpYXQiOjE2OTY5OTE0NjIsIm5iZiI6MTY5Njk5MTQ2MiwiZXhwIjoxNjk3NTk2MjYyLCJkYXRhIjp7InVzZXIiOnsiaWQiOiIxIn19fQ.VxdjEmKdqZShrHqzponvgHmHnp1HpkJaIgOqMj7G6Ggxxx",
    "user_email": "xxx@gmail.com",
    "user_nicename": "xxxgmail-com",
    "user_display_name": "xxx@gmail.com"
}
```

![](https://imagedelivery.net/L3derMyVP1V9uWRu-KGKdg/c3bbf81a-deaf-440a-d1fe-c83fd0a0a400/public)





а затем добавьте заголовок запроса Authorization: Bearer

```
POST /resource HTTP/1.1
Хост: server.example.com
Авторизация: Bearer mF_s9.B5f-4.1JqM
```

и json-данные:

```
{
	"title": "44433x-Hello World",
	"status": "publish",
	"content": "aaa",
	"date": "2023-10-09T10:00:00"
}
```

![](https://imagedelivery.net/L3derMyVP1V9uWRu-KGKdg/0948fcda-1fdd-4f42-68b5-9822016e7e00/public)

### ошибки



некоторая ошибка, с которой можно встретиться:

```
{
    "code": "rest_cannot_create",
    "message": "Извините, вам не разрешено создавать сообщения от имени этого пользователя",
    "data": {
        "status": 401
    }
}

```

необходимо добавить конфигурацию в .htaccess

```
 SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
```

