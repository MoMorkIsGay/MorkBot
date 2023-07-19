# MorkBot&Fumo
极简的qq群聊chatgpt&fumo机器人。

输入前缀“fumo ”或“Fumo ”与其进行互动：

`Fumo 世界上最高的山是哪座`

`fumo ///`（重置对话用）

`Fumo 怪故事`

# 使用

## 安装go-cqhttp

https://github.com/Mrs4s/go-cqhttp/releases

选择`0: HTTP通信`。设置好相关信息后转到第96行：

```yaml
  - http: # HTTP 通信设置
      address: 0.0.0.0:5700 # HTTP监听地址
      timeout: 0      # 反向 HTTP 超时时间, 单位秒，<5 时将被忽略
      long-polling:   # 长轮询拓展
        enabled: false       # 是否开启
        max-queue-size: 2000 # 消息队列大小，0 表示不限制队列大小，谨慎使用
      middlewares:
        <<: *default # 引用默认中间件
      post:           # 反向HTTP POST地址列表
      - url: http://127.0.0.1:5701/                # 地址
      #  secret: ''             # 密钥
        max-retries: 0         # 最大重试，0 时禁用
      #  retries-interval: 1500 # 重试时间，单位毫秒，0 时立即
      #- url:  # 地址
      #  secret: ''                  # 密钥
      #  max-retries: 10             # 最大重试，0 时禁用
      #  retries-interval: 1000      # 重试时间，单位毫秒，0 时立即
```

## 安装依赖

`pip3 install -r requirements.txt`

## 运行

填写好`handlemsg.py`中的api key和相关必填内容后后运行`main.py`和`go-cqhttp.bat`。

## 功能和特色

# 上传fumo

使用格式`fumo 上传fumo [图片]`
就会自动截取后面的图片CQ码存储到`fumo.txt`里，并自动换行

发送原理：发送图片的CQ码，QQ会自动识别并发送图片
后面的语音发送也是同理

# fumo

当群里有人发送“fumo”或者消息里带有“fumo”的时候就有概率执行“fumo fumo”或发送`record.txt`的一条语音

# 保护措施

当你的网络代理很差以至于连接不到ChatGPT时，就会执行保护措施：与“fumo 说点怪话”相同的功能（防止大家知道你的机器人炸了）

# 相关链接

https://github.com/acheong08/ChatGPT

https://docs.go-cqhttp.org/

https://platform.openai.com/docs/api-reference/chat/create?lang=python

如何注册OpenAI账号: https://sms-activate.org/cn/info/ChatGPT
