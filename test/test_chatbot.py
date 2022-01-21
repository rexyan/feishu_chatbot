import json
from chatbot.client import ChatBotClient
from chatbot.api.file import FileChatBot


def test_file_chatbot():
    client = ChatBotClient(app_id="xxx", app_secret='xxx')
    user = client.get_user_id_by_email(email="user_email")

    f = open('1.ppt', 'rb')
    mp4 = f.read()
    file_key = client.get_file_key(mp4, "1.ppt", "ppt")

    data = {
        "receive_id": user["open_id"],
        "content": json.dumps({"file_key": file_key}),
        "msg_type": "file"
    }

    FileChatBot.set_client(client).set_data(data).build().send()
