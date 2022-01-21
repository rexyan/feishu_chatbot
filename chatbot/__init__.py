__version__ = '1.0.0'


class ChatBotClientException(Exception):
    pass


def openapi_callback(response):
    response_data = response.json()
    if response.status_code != 200 or response_data.get("code") != 0:
        raise ChatBotClientException(f"openapi return error, code: {response_data.get('code')}, msg: {response_data.get('msg')}")
    return response_data
