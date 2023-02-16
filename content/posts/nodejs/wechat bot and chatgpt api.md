---
title: "wechat bot and chatgpt api"
date: 2023-02-16T15:20:12+08:00
draft: true
---
# 个人微信接入chatgpt

  - ```微信机器人 和 chatgpt接口```


简要架构
---

![avatar](https://i.328888.xyz/2023/02/16/mqFS3.png)

涉及内容：

- wechat bot：
https://github.com/wechaty/puppet-xp
- npm chatgpt:
https://www.npmjs.com/package/chatgpt#demos


注意点：
- (请使用小号或不重要的微信号，防止被封，根据本人使用经验，puppet-xp暂时没啥问题，不排除后面微信有动作)
- 微信必须是指定版本，请查看查看项目readme
- 回复功能需要自己写一部分代码（在onRecvMsg方法中编写）
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
待解决：
在vscode中调试puppet-xp项目（typescript）