from enum import Enum


class OpenAPI(Enum):
    ACCESS_TOKEN = 'https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/'
    SEND_MESSAGE = 'https://open.feishu.cn/open-apis/im/v1/messages'
    REPLY_MESSAGE = 'https://open.feishu.cn/open-apis/im/v1/messages/{message_id}/reply'
    GET_USER_ID = 'https://open.feishu.cn/open-apis/user/v1/batch_get_id'
    GET_GROUP_ROBOT_ID = 'https://open.feishu.cn/open-apis/im/v1/chats'
    GET_IMAGE_KEY = 'https://open.feishu.cn/open-apis/im/v1/images'
    GET_FILE_KEY = 'https://open.feishu.cn/open-apis/im/v1/files'
