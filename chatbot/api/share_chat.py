from chatbot.api import ChatBotAPI, Builder
from voluptuous import Required


class ShareChatBot(ChatBotAPI, metaclass=Builder):
    # 分享名片消息 https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN#756b882f
    _templates = {
        "chat_id": {
            Required("msg_type"): "share_chat",
            Required("content"): {
                Required("chat_id"): str,
            },
            "receive_id": str
        },
        "user_id": {
            Required("msg_type"): "share_user",
            Required("content"): {
                Required("user_id"): str,
            },
            "receive_id": str
        }
    }
