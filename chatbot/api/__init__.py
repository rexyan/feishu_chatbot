import copy
import json
from voluptuous import Schema, ALLOW_EXTRA

from chatbot.client import ChatBotClient


class ChatBotAPI:
    def __init__(self, builder):
        self._data = builder.data
        self._client = builder.client
        self._receive_id_type = builder.receive_id_type

    def send(self):
        return self._client.send(self._data, **{"receive_id_type": self._receive_id_type})


class Builder(type):
    receive_id_type = "open_id"
    client, data = None, None

    def __new__(mcs, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        cls = type.__new__(mcs, *args, **kwargs)
        return cls

    def set_client(self, client):
        if not isinstance(client, ChatBotClient):
            raise ChatBotException("client must be a concrete implementation of ChatBotClient")
        self.client = client
        return self

    def set_data(self, data):
        if not self._check_message_struct(data):
            raise ChatBotException("message struct error!")
        data["content"] = json.dumps(data["content"])
        self.data = data
        return self

    def set_receive_id_type(self, receive_id_type):
        if receive_id_type not in ["open_id", "user_id", "union_id", "email", "chat_id"]:
            raise ChatBotException(f"Invalid receive_id_type: {receive_id_type}")
        self.receive_id_type = receive_id_type
        return self

    def build(self):
        if not self.client or not self.data:
            raise ChatBotException("build error, client, data, receive_id_type parameter is required")
        return self(self)

    def _check_message_struct(self, message):
        check_success_count = 0
        for _, _schema in self._templates.items():
            try:
                schema = Schema(_schema, True, ALLOW_EXTRA)
                schema(message)
                check_success_count += 1
            except Exception as e:
                print(e)
        return check_success_count > 0


class ChatBotException(Exception):
    pass
