---
title: "# Wordpress use rest Api post Articals 用rest api 推送文章到wordpress"
date: 2023-10-11T11:26:58+08:00
draft: false
tags: ["wordpress","rest api"]
---

# Wordpress use rest Api post Articals

## SETTING

### 1# Install jwt plugin

from here:

https://wordpress.org/plugins/jwt-authentication-for-wp-rest-api/



ps: minimun php version:7.4.0

### PHP HTTP AUTHORIZATION HEADER ENABLE 

#### 1.1#    .htaccess 

change from --->

```
# SGS XMLRPC Disable Service
<Files xmlrpc.php>
	order deny,allow
	deny from all
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
  Header unset Vary
# SGO Unset Vary END
```

to---->

```
# SGS XMLRPC Disable Service
<Files xmlrpc.php>
	order deny,allow
	deny from all
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
 SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
</IfModule>
# END WordPress

# SGO Unset Vary
  Header unset Vary
# SGO Unset Vary END

```

#### CONFIGURATE THE SECRET KEY 

The JWT needs a **secret key** to sign the token this **secret key** must be unique and never revealed.
JWT需要一个秘钥来签署令牌，这个秘钥必须是唯一的且永不泄露。

To add the **secret key** edit your wp-config.php file and add a new constant called **JWT_AUTH_SECRET_KEY**
要添加密钥，请编辑您的wp-config.php文件，并添加一个名为JWT_AUTH_SECRET_KEY的新常量。

```
define('JWT_AUTH_SECRET_KEY', 'your-top-secret-key');
```

You can use a string from here  你可以从这里使用一个字符串 https://api.wordpress.org/secret-key/1.1/salt/


#### CONFIGURATE CORS SUPPORT 配置CORS支持

The **wp-api-jwt-auth** plugin has the option to activate [CORs](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) support.
wp-api-jwt-auth插件有激活CORs支持的选项。

To enable the CORs Support edit your wp-config.php file and add a new constant called **JWT_AUTH_CORS_ENABLE**
要启用CORs支持，请编辑您的wp-config.php文件并添加一个名为JWT_AUTH_CORS_ENABLE的新常量。

```
define('JWT_AUTH_CORS_ENABLE', true);
```



### Usage 

#### get jwt token

post https://example.com/wp-json/jwt-auth/v1/token

data:

```
 {"username": "xxx@gmail.com",   "password": "xxxx" }
```

will get the response like this:

```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2dlbmcudG9kYXkiLCJpYXQiOjE2OTY5OTE0NjIsIm5iZiI6MTY5Njk5MTQ2MiwiZXhwIjoxNjk3NTk2MjYyLCJkYXRhIjp7InVzZXIiOnsiaWQiOiIxIn19fQ.VxdjEmKdqZShrHqzponvgHmHnp1HpkJaIgOqMj7G6Ggxxx",
    "user_email": "xxx@gmail.com",
    "user_nicename": "xxxgmail-com",
    "user_display_name": "xxx@gmail.com"
}
```

![](https://imagedelivery.net/L3derMyVP1V9uWRu-KGKdg/c3bbf81a-deaf-440a-d1fe-c83fd0a0a400/public)





and then , add request header Authorization: Bearer 

```
POST /resource HTTP/1.1
Host: server.example.com
Authorization: Bearer mF_s9.B5f-4.1JqM
```

and json data:

```
{
	"title": "44433x-Hello World",
	"status": "publish", 
	"content": "aaa", 
	"date": "2023-10-09T10:00:00"
}
```

![](https://imagedelivery.net/L3derMyVP1V9uWRu-KGKdg/0948fcda-1fdd-4f42-68b5-9822016e7e00/public)

### errors



some error you can meet:

```
{
    "code": "rest_cannot_create",
    "message": "Sorry, you are not allowed to create posts as this user.",
    "data": {
        "status": 401
    }
}

```

you need to add config in .htaccess

```
 SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
```

