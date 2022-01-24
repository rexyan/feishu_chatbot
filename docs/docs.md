### 发送文本消息

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



### 发送语音消息

```python
from chatbot import ChatBotClient, AudioChatBot

client = ChatBotClient(app_id="xxx", app_secret='xxx')
user = client.get_user_id_by_email("jack@gmail.com")

with open("1.opus", "rb") as f:
    file_key = client.get_file_key(f.read(), "1.opus", "opus")

data = {
    "msg_type": "audio",
    "content": {"file_key": file_key},
    "receive_id": user["open_id"],
}
chatbot = AudioChatBot.set_client(client).set_data(data).build()
chatbot.send()
```



### 发送文件消息

```python
from chatbot import ChatBotClient, FileChatBot

client = ChatBotClient(app_id="xxx", app_secret='xxx')
user = client.get_user_id_by_email("jack@gmail.com")

with open("1.mp4", "rb") as f:
    file_key = client.get_file_key(f.read(), "1.mp4", "mp4")

data = {
    "msg_type": "file",
    "content": {"file_key": file_key},
    "receive_id": user["open_id"],
}
chatbot = FileChatBot.set_client(client).set_data(data).build()
chatbot.send()
```



### 发送图片消息

```python
from chatbot import ChatBotClient, ImageChatBot

client = ChatBotClient(app_id="xxx", app_secret='xxx')
user = client.get_user_id_by_email("jack@gmail.com")

with open("1.png", "rb") as f:
    image_key = client.get_image_key(f.read())
    
data = {
    "msg_type": "image",
    "content": {"image_key": image_key},
    "receive_id": user["open_id"],
}
chatbot = ImageChatBot.set_client(client).set_data(data).build()
chatbot.send()
```



### 发送卡片消息

```python
from chatbot import ChatBotClient, PostChatBot

client = ChatBotClient(app_id="xxx", app_secret='xxx')
user = client.get_user_id_by_email("jack@gmail.com")

data = {
    "msg_type": "post",
    "content": {"post": {"zh_cn": {"title": "消息标题", "content": "消息正文"}}},
    "receive_id": user["open_id"],
}
chatbot = PostChatBot.set_client(client).set_data(data).build()
chatbot.send()
```



### 发送视频消息

```python
from chatbot import ChatBotClient, MediaChatBot

client = ChatBotClient(app_id="xxx", app_secret='xxx')
user = client.get_user_id_by_email("jack@gmail.com")

with open("1.mp4", "rb") as f:
    file_key = client.get_file_key(f.read(), "1.mp4", "mp4")
with open("1.png", "rb") as f:
    image_key = client.get_image_key(f.read())

data = {
    "msg_type": "media",
    "content": {"file_key": file_key, "image_key": image_key},
    "receive_id": user["open_id"],
}
chatbot = MediaChatBot.set_client(client).set_data(data).build()
chatbot.send()
```



### 发送名片消息

```python
from chatbot import ChatBotClient, ShareChatBot

client = ChatBotClient(app_id="xxx", app_secret='xxx')
user = client.get_user_id_by_email("jack@gmail.com")

data = {
    "msg_type": "share_user",
    "content": {"user_id": user["user_id"]},
    "receive_id": user["open_id"],
}
chatbot = ShareChatBot.set_client(client).set_data(data).build()
chatbot.send()
```



### 发送表情包消息

```python
from chatbot import ChatBotClient, StickerChatBot

client = ChatBotClient(app_id="xxx", app_secret='xxx')
user = client.get_user_id_by_email("jack@gmail.com")

with open("1.png", "rb") as f:
    file_key = client.get_file_key(f.read(), "1.png", "png")

data = {
    "msg_type": "sticker",
    "content": {"file_key": file_key},
    "receive_id": user["open_id"],
}
chatbot = StickerChatBot.set_client(client).set_data(data).build()
chatbot.send()
```

