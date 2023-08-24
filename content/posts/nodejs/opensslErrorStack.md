---
title: "npm install error:opensslErrorStack error 03000086 digital envelope routines initialization error "
date: 2023-08-24T15:20:12+08:00
draft: false
tags: ["nodejs", "error info"]
---
# npm install error:opensslErrorStack: [ 'error:03000086:digital envelope routines::initialization error' ]

//https://stackoverflow.com/questions/74726224/opensslerrorstack-error03000086digital-envelope-routinesinitialization-e
切换到node v18的时候，npm install 出现如下错误
```
 {
 opensslErrorStack: [ 'error:03000086:digital envelope routines::initialization error' ],
  library: 'digital envelope routines',
  reason: 'unsupported',
  code: 'ERR_OSSL_EVP_UNSUPPORTED'
 }
```
## 解决办法有两种：
### 1 尝试卸载 Node.js 版本 17+，然后重新安装 Node.js 版本 16+
使用nmv时，直接
```
nvm use 16 #16相关版本
```
### 2 打开终端并按照说明粘贴以下内容：
#### Linux和macOS（Windows Git Bash）-
```
export NODE_OPTIONS=--openssl-legacy-provider
```
#### Windows PowerShell- Windows PowerShell
```
$env:NODE_OPTIONS = "--openssl-legacy-provider"
```
