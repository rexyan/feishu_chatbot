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
ImageChatBot.set_client(client).set_data(data).build().send()
