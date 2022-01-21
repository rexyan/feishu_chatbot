from chatbot.api import ChatBotAPI, Builder
from voluptuous import Required


class InteractiveChatBot(ChatBotAPI, metaclass=Builder):
    # 卡片消息 https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN#4996824a
    _templates = {
        "basic": {
            Required("msg_type"): "interactive",
            Required("content"): {
                Required("config"): dict,
                Required("elements"): list,
                Required("header"): dict
            },
            "receive_id": str
        }
    }
