from chatbot.api import ChatBotAPI, Builder
from voluptuous import Required


class PostChatBot(ChatBotAPI, metaclass=Builder):
    # 富文本消息 https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN#f62e72d5
    _templates = {
        "zh_cn": {
            Required("msg_type"): "post",
            Required("content"): {
                Required("post"): {
                    Required("zh_cn"): {
                        Required("title"): str,
                        Required("content"): list
                    }
                }
            },
            "receive_id": str
        },
        "en_us": {
            Required("msg_type"): "post",
            Required("content"): {
                Required("post"): {
                    Required("zh_cn"): {
                        Required("title"): str,
                        Required("content"): list
                    }
                }
            },
            "receive_id": str
        }
    }
