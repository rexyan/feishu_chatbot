from chatbot.api import ChatBotAPI, Builder
from voluptuous import Required


class MediaChatBot(ChatBotAPI, metaclass=Builder):
    # 视频消息 https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json#54406d84
    _templates = {
        "basic": {
            Required("msg_type"): "media",
            Required("content"): {
                Required("file_key"): str,
                Required("image_key"): str
            },
            "receive_id": str
        }
    }
