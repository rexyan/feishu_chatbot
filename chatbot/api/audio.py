from chatbot.api import ChatBotAPI, Builder
from voluptuous import Required


class AudioChatBot(ChatBotAPI, metaclass=Builder):
    # 语音消息 https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json#5d353271
    _templates = {
        "basic": {
            Required("msg_type"): "audio",
            Required("content"): {
                Required("file_key"): str
            },
            "receive_id": str,
        }
    }
