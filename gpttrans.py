import os
import openai
import markdown
import os


# 读取 markdown 文件
# Load your API key from an environment variable or secret management service
openai.api_key = "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"
prompt_format_system = "你是一个翻译专家，SEO专家，我将给你一篇Markdown格式的博客，请将博客翻译成{}，可以适当扩充、润色内容，代码片段不用翻译，代码中的注释可以翻译，请添加相关SEO友好的标题 h1,h2等，内容如下:"

#br,de,dk,en,eo,es,fr,hr,it,ja,ko,lmo,nb,nl,pl,ru,tr,zh-CN,zh-TW
language_prompt_list = [
    {"br":"巴西语"},
    {"de":"德语"},
    {"dk":"丹麦语"},
    {"en":"英语"},
    # {"eo":"世界语"},
    # {"es":"西班牙语"},
    # {"fr":"法语"},
    # {"hr":"克罗地亚语"},
    # {"it":"意大利语"},
    # {"ja":"日语"},
    # {"ko":"韩语"},
    # {"lmo":"伦巴第语"},
    # {"nb":"挪威语"},
    # {"nl":"荷兰语"},
    # {"pl":"波兰语"},
    # {"ru":"俄语"},
    # {"tr":"土耳其语"},
    # {"zh-CN":"中文"},
    # {"zh-TW":"中文"}
]

for root, dirs, files in os.walk('content/posts', topdown=False):
    for name in files:
        file_path = os.path.join(root, name)
        file_dirname = os.path.dirname(file_path)
        nottrans = ['artists.md','help.md']
        # print(file_path,file_dirname)
        if name in nottrans:
            print('不翻译：',name)
            continue
        with open(file_path, "r",encoding='utf-8') as f:
            data = f.read()
            # print(len(data))
            if len(data) > 5000:
                print('   大文件-> 长度 ',len(data),file_path)
            else:
                print('小文件-> 长度 ',len(data),file_path)

def onefiletest(file_path):
    with open(file_path, "r",encoding='utf-8') as f:
        data = f.read()
        # print(len(data))
        if len(data) > 5000:
            print('   大文件-> 长度 ',len(data),file_path)
        else:
            print('小文件-> 长度 ',len(data),file_path)
        print(data)
        for lang in language_prompt_list:
            for k,v in lang.items():
                message = []
                print(k,v)
                systemmsg = prompt_format_system.format(v) 
                message.append({"role": "system", "content": systemmsg})
                message.append({"role": "user", "content": data})
                print(message)
                newpath = create_new_lang_folder(file_path,k)
                filename = os.path.basename(file_path)

                chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)
                print(chat_completion.choices[0].message.content)
                content_after_trans = chat_completion.choices[0].message.content

                print('写文件',newpath+filename)
                f = open(newpath+filename, "w",encoding='utf-8')
                f.write(content_after_trans)

                f.close()
def create_new_lang_folder(file_path,lang_shortname):
    last_index_of_slant = file_path.rfind('/')
    oldpath = file_path[0:last_index_of_slant]
    print('老路径',oldpath)

    
    index_of_insert = oldpath.find('/')
    head  =   oldpath[0:index_of_insert]
    tail = oldpath[index_of_insert:]
    newpath = head + '/' + lang_shortname + tail
    if not os.path.exists(newpath):
        print(newpath)
        os.makedirs(newpath)
    return newpath+'/'

onefiletest('content/posts/ai/gpt/gpt_proxy.md')                 
        

def get_trans(msg,language):
    prompt = '{}'.format(language) + msg
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    return response.choices[0].text

def puretest():
        
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "你是一个翻译专家，SEO专家，我将给你一篇Markdown格式的博客，请将博客翻译成巴西语，可以适当扩充、润色内容，添加相关SEO友好的标题，tag中的内容不翻译"},
                                                                                    {"role": "user", "content": '''
    ---
    title: "how to use copilot"
    date: 2023-03-13T10:04:55+08:00
    draft: false
    tags: ["copilot","AI"]
    ---
    官方quickstart文档
    https://docs.github.com/zh/copilot/quickstart

    Copilot 也提供了一些快捷键，可以很方便地使用。

    ```

    接受建议：Tab
    拒绝建议：Esc
    打开Copilot：Ctrl + Enter （会打开一个单独的面板，展示10个建议）
    下一条建议：Alt/Option + ]
    上一条建议：Alt/Option + [
    触发行内Copilot：Alt/Option + \ （Coplit还没有给出建议或者建议被拒绝了，希望手工触发它提供建议）

    ```

    idea 认证，
    如果vscode已认证，而且已经打开，
    idea下载plugin后重启，右下角提示登录，跳转github，出现8位验证码输入框，直接粘贴（密码已有vscode自动复制） 相关链接：
    https://github.com/community/community/discussions/8468#discussioncomment-4818526
    '''
                                                                                                                                    }])
    print(chat_completion.choices[0].message.content)

# puretest()    