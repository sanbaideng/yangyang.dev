--- 
title: "Простой javascript-код для предотвращения отладки F12 на сайте" 
date: 2023-09-14T10:39:58+08:00
tags: ["js complementary environments"] 
--- 
# Простой javascript-код для 
предотвращения отладки F12 на сайте На нашем сайте, если нам нужно предотвратить просмотр исходного кода другими пользователями, мы можем отключить F12 и перехватить его с помощью javascript. мы можем отключить F12 и перехватывать его через javascript и выдавать запрос, когда кто-то нажимает F12.


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