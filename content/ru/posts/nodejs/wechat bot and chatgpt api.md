---
title: "wechat bot и chatgpt api"
date: 2023-02-16T15:20:12+08:00
tag: ["nodejs", "wechat"]
---
# личный доступ к wechat chatgpt

  - ``Интерфейс бота WeChat и chatgpt, openai image generation api``.


Краткая архитектура
---

! [avatar](https://res.cloudinary.com/dkmuoufxh/image/upload/v1676598390/wecgatbot3_slru5x.jpg)

Задействован контент:

- wechat-бот:
https://github.com/wechaty/puppet-xp
- npm chatgpt.
https://www.npmjs.com/package/chatgpt#demos
- openai
https://platform.openai.com/docs/guides/images/usage

Внимание:
- (Пожалуйста, используйте небольшой или неважный микросигнал, чтобы предотвратить блокировку, согласно моему опыту использования, puppet-xp временно не имеет проблем, не исключайте, что сзади микроканал имеет действие)
- WeChat должен быть указанной версии, пожалуйста, проверьте, чтобы увидеть проект readme
- Для функции ответа необходимо написать свою часть кода (пишется в методе onRecvMsg)
- розыгрыш openai платный, на бесплатном счете кредит $18.
``

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
      await sidecar.sendMsg(toId, questiontext + '\n--------\n' + 'Этот вопрос мог прерваться по времени или пойти не так')

    }
    .
    .
    .
  }
```

Похожие скриншоты:
 - 1. Получение сообщений
  ---
  ! [Бот WeChat собирает сообщения](https://res.cloudinary.com/dkmuoufxh/image/upload/v1676590010/message1_vyaizv.jpg)

  --- !

 - 2. Получение сообщения, вызов gpt api и отправка сообщения
  ---
  ! [WeChat-бот собирает сообщение, вызывает gpt api, снова отправляет сообщение](https://res.cloudinary.com/dkmuoufxh/image/upload/v1676590762/message2_rkjpqj.jpg)

  --- !

- 3. получить сообщение о рисунке, вызвать интерфейс openai, сохранить рисунок, затем переслать рисунок в WeChat
  ---
  ! [Wechat-бот получает сообщение, вызывает gpt api, затем отправляет сообщение](https://res.cloudinary.com/dkmuoufxh/image/upload/v1676598565/wecgatbot4_pnrfsv.jpg)

  --- !
Решить:
Отладка проекта puppet-xp в vscode (typescript)