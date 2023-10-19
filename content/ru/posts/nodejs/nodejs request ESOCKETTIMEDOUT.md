---
title: "nodejs request ESOCKETTIMEDOUT"
date: 2023-08-11T16:13:12+08:00
черновик: false
tags: ["nodejs", "ESOCKETTIMEDOUT"]
---
# NodeJS запрос ESOCKETTIMEDOUT
在请求gpt-4的completions接口时，request请求经常报错 ESOCKETTIMEDOUT

在请求options中，加入forever: true, 解决
```

  let options = {
    method: 'POST',
    url:account_config.hostUrl,
    body: data,
    заголовки: {
      // 'Accept': '*/*',
      // 'Connection': 'keep-alive',
      'Authorization': account_config.Authorization
    },
    forever: true,
    timeout: 1200000,
     json: true
  }
```