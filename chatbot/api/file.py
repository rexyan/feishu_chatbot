from chatbot.api import ChatBotAPI, Builder
from voluptuous import Required


class FileChatBot(ChatBotAPI, metaclass=Builder):
    # 文件消息 https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json#c92e6d46
    _templates = {
        "basic": {
            Required("msg_type"): "file",
            Required("content"): {
                Required("file_key"): str
            },
            "receive_id": str
        }
    }
