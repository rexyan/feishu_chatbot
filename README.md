### 简介
基于[飞书官方文档](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json#5d353271)，封装的飞书消息机器人接口。支持简单的消息格式校验，获取发送消息所需 file_key, image_key 等。更多使用示例，可参考[接口文档](./docs/docs.md)。



### 使用示例
**安装**

```shell
pip install -U feishu-chatbot
```

**发送文本**
```python
from chatbot import ChatBotClient, TextChatBot

client = ChatBotClient(app_id="xxx", app_secret='xxx')
user = client.get_user_id_by_email("jack@gmail.com")

data = {
    "msg_type": "text",
    "content": {"text": "示例文本消息"},
    "receive_id": user["open_id"],
}
chatbot = TextChatBot.set_client(client).set_data(data).build()
chatbot.send()
```
