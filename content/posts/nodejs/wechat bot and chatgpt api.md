---
title: "wechat bot and chatgpt api"
date: 2023-02-16T15:20:12+08:00
draft: false
---
# 个人微信接入chatgpt

  - ```微信机器人 和 chatgpt接口 、 openai图片生成api```


简要架构
---

![avatar](https://res.cloudinary.com/dkmuoufxh/image/upload/v1676598390/wecgatbot3_slru5x.jpg)

涉及内容：

- wechat bot：
https://github.com/wechaty/puppet-xp
- npm chatgpt:
https://www.npmjs.com/package/chatgpt#demos
- openai 
https://platform.openai.com/docs/guides/images/usage

注意点：
- (请使用小号或不重要的微信号，防止被封，根据本人使用经验，puppet-xp暂时没啥问题，不排除后面微信有动作)
- 微信必须是指定版本，请查看查看项目readme
- 回复功能需要自己写一部分代码（在onRecvMsg方法中编写）
- openai 画图是收费的，免费账户有18美金额度。
```
   
  const onRecvMsg = async (args: any) => {
    .
    .
    const questiontext = text.replace('@fakegpt_x','')
    try{
      if(talkerId && text.startsWith('@fakegpt_x') ){
        const res = await api.sendMessage(questiontext)
        await sidecar.sendMsg(toId, questiontext + '\n--------\n' +res.text)
        console.log(res)
      }
    }catch(ex){
      var result=(ex as Error).message
      console.info('------err----'+result)    
      await sidecar.sendMsg(toId, questiontext + '\n--------\n' +'这个问题可能超时或出错了。')

    }
    .
    .
    .    
  }
```

相关截图：
 - 1.收消息
  ---
  ![微信机器人收消息](https://res.cloudinary.com/dkmuoufxh/image/upload/v1676590010/message1_vyaizv.jpg)
  
  ---

 - 2.收消息，调用gpt api ，再发消息
  ---
  ![微信机器人收消息，调用gpt api ，再发消息](https://res.cloudinary.com/dkmuoufxh/image/upload/v1676590762/message2_rkjpqj.jpg)
  
  ---
 
- 3.收到画图消息，调用openai的接口，存储图片，再转发图片到微信
  ---
  ![微信机器人收消息，调用gpt api ，再发消息](https://res.cloudinary.com/dkmuoufxh/image/upload/v1676598565/wecgatbot4_pnrfsv.jpg)
  
  ---
待解决：
在vscode中调试puppet-xp项目（typescript）