### 简介
基于[飞书官方文档](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json#5d353271)，封装的飞书消息机器人接口。支持简单的消息格式校验，获取发送消息所需 file_key, image_key 等。



### 使用示例
**安装**
```shell
pip install -U feishu-chatbot
```

**发送文本**
```python
client = ChatBotClient(app_id="xxx", app_secret='xxx')
user = client.get_user_id_by_email("user_email")
data = {
    "msg_type": "text",
    "content": json.dumps({"text": "测试文本"}),
    "receive_id": user["open_id"],  # or user["user_id"]
}
TextChatBot.set_client(client).set_data(data).build().send()  # receive_id 默认使用 open_id
TextChatBot.set_client(client).set_receive_id_type("user_id").set_data(data).build().send()  # receive_id 默认使用 user_id
```

**发送视频**

```python
client = ChatBotClient(app_id="xxx", app_secret='xxx')
user = client.get_user_id_by_email("user_email")

# 上传图片和文件获取对应的 key 信息
image_key = client.get_image_key("...")
file_key = client.get_file_key("...")

data = {
    "msg_type": "media",
    "content": json.dumps({"file_key": file_key, "image_key": image_key}),
    "receive_id": user["open_id"],
}
MediaChatBot.set_client(client).set_data(data).build().send()
```



