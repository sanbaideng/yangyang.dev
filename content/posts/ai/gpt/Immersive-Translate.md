---
title: "Immersive Translate"
date: 2024-04-30T09:11:55+08:00
draft: false
tags: ["GPT","Immersive Translate"]
---
# 沉浸式翻译插件 国内用法
不需要太好的效果，直接看第二步->第六步->第四步，即可。

## 先获取山寨gpt账号

进入https://www.gptapi.us/register?aff=gs5O 注册 登录，然后充值。（注：这个链接带了我的邀请码，我可以获得一元）



### 先看怎么充值50元



图一 兑换码充值页面，这时候咱还没有兑换码，需要去买。

![image-20240430083912499](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430083912499.png)



点击获取兑换码之后，跳到图二 ，如下，点击50元。

![image-20240430083936796](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430083936796.png)

跳到图三，付款，注意填下邮箱。

![image-20240430084003540](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430084003540.png)

注意填邮箱，充值完成后得到卡密，

卡密填到 图一，获取额度。

### 再看怎么获取api key（gpt官方的中转）

点击令牌->新建令牌，随意输入名称，保持永不过期，无限额度(充的50元是上限)，其他不管，点击提交。



图三 新建令牌：

![image-20240430084822289](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430084822289.png)

然后得到下面的这一行内容，  有复制、聊天按钮。

复制是复制一串密文，相当于调用gpt的钥匙。



图四： 令牌列表：

![image-20240430084947365](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430084947365.png)

到这里 准备工作就完成了。



## 二、再获取chrome插件： Immersive Translate

安装插件这步需要魔法，打开网址：https://chromewebstore.google.com/?utm_source=ext_app_menu

(ps:无魔法的可以用Microsoft Edge 浏览器,名字叫：沉浸式翻译)



搜索 Immersive Translate，

找到第一个，图标如图所示

![image-20240430085338470](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430085338470.png)

点进去，然后获取安装。



## 三、再结合上面两个，将gpt的key，配置到插件里面。

找到刚安装的chrome插件：



图五：点击插件，找到插件配置选项

![image-20240430085928596](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430085928596.png)

先去图四，点击复制，得到key，下面步骤需要

图六 关键步骤：进入翻译插件配置页，选择openai作为翻译引擎，然后填入再图四中复制的key，模型选择gpt-3.5-turbo,这个便宜。效果需要更好的就选择gpt-4-turbo,更贵。

![image-20240430090420969](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430090420969.png)

然后需要展开更多配置：



图七：更多配置



![image-20240430090508834](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430090508834.png)

填写openai的调用地址，因为我们是山寨的，需要填写山寨地址https://api.gptapi.us/v1/chat/completions，而不是官方的。



图八：配置api的地址：

![image-20240430090611899](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430090611899.png)





## 四、测试

到这里就完成了配置，

打开https://example.com/，去点击插件，点击翻译。查看效果，有时候慢一点，可能是用的人多，资源不够。



图九：效果测试。

![image-20240430091005522](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430091005522.png)



图十：效果：

![image-20240430091027581](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430091027581.png)

## 五、文件翻译功能,配置还是之前的配置，不用动（gpt-4耗费可能较多，需要注意下； 而gpt-3.5很便宜，加上山寨有折扣，一般耗费很低）

图十一： 点击插件，点击左下角 pdf/epub

![image-20240430091855981](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430091855981.png)



图十二：跳转到文件翻译页，点击上传需要翻译的文件：

![image-20240430091936475](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430091936475.png)



图十二：上传了epub后的效果，此时还没有点击翻译 ，插件只是把文件文章节展示了：（ps：上传的文档最好能复制文字，效果更好）

![image-20240430092222155](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430092222155.png)



图十三：点击翻译：需要一点时间，看到文字后面转圈圈就是在调用gpt了。

![image-20240430092359309](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430092359309.png)





## 六、不需要太好的效果，只想试一下，就可以选择微软的翻译，不用充值第一步的平台，是免费的。

![image-20240430092551994](https://markdowna.oss-cn-shenzhen.aliyuncs.com/articalimage-20240430092551994.png)

