---
title: "网站防止F12调试的简单javascript代码"
date: 2023-09-14T10:39:58+08:00
draft: false
tags: ["js补环境"]
---
# 网站防止F12调试的简单javascript代码
我们的网站如果需要防止别人查看源码，可以禁止F12，当别人按下F12的时候，通过javascript拦截，并提示。

```
<script>
		document.onkeydown = function(){

	    if(window.event && window.event.keyCode == 123) {
	        alert("Hi,欢迎来到xx！");
	        event.keyCode=0;
	        event.returnValue=false;
	    }
	    if(window.event && window.event.keyCode == 13) {
	        window.event.keyCode = 505;
	    }
	    if(window.event && window.event.keyCode == 8) {
	        alert(str+"\n请使用Del键进行字符的删除操作！");
	        window.event.returnValue=false;
	    }
		}
	</script>
```