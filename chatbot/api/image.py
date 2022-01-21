from chatbot.api import ChatBotAPI, Builder
from voluptuous import Required


class ImageChatBot(ChatBotAPI, metaclass=Builder):
    # 图片消息 https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN#132a114c
    _templates = {
        "basic": {
            Required("msg_type"): "image",
            Required("content"): {
                Required("image_key"): str
            },
            "receive_id": str
        }
    }
