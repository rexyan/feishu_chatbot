from chatbot.api import ChatBotAPI, Builder
from voluptuous import Required


class TextChatBot(ChatBotAPI, metaclass=Builder):
    # 文本消息 https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN#756b882f
    _templates = {
        "basic": {
            Required("msg_type"): "text",
            Required("content"): {
                Required("text"): str
            },
            "receive_id": str
        }
    }