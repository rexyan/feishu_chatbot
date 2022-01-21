import json

import requests

from chatbot import ChatBotClientException, openapi_callback
from chatbot.enums import OpenAPI
from chatbot.http_client import HttpClient


class ChatBotClient:
    def __init__(self, app_id=None, app_secret=None):
        if not app_id or not app_secret:
            raise ChatBotClientException("init client error, app_id, app_secret parameter is required")

        self.app_id = app_id
        self.app_secret = app_secret
        self.client = HttpClient()

    @classmethod
    def init_client(cls, app_id, app_secret):
        return cls(app_id, app_secret)

    def send(self, message, **kwargs):
        """
        发送消息
        :param message:
        :param kwargs:
        :return:
        """
        access_token = self._get_access_token()
        return self.client.post(
            url_params=kwargs,
            content_type="data",
            data=json.dumps(message),
            path=OpenAPI.SEND_MESSAGE.value,
            response_data_extractor=openapi_callback,
            headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json; charset=utf-8"}
        )

    def _get_access_token(self):
        """
        获取 access token
        :return:
        """
        data = self.client.post(
            OpenAPI.ACCESS_TOKEN.value,
            response_data_extractor=openapi_callback,
            data={"app_id": self.app_id, "app_secret": self.app_secret},
            headers={"Content-Type": "application/json; charset=utf-8"}
        )
        print(data.get("tenant_access_token"))
        return data.get("tenant_access_token")

    def get_image_key(self, image, image_type="message"):
        """
        上传图片获取 image key
        :param image:
        :param image_type:
        :return:
        """
        access_token = self._get_access_token()
        data = self.client.post(
            content_type="data",
            path=OpenAPI.GET_IMAGE_KEY.value,
            response_data_extractor=openapi_callback,
            data={"image_type": image_type},
            files={'image': image},
            headers={"Authorization": f"Bearer {access_token}"}
        )
        return data["data"]["image_key"]

    def get_file_key(self, file, file_name, file_type):
        """
        上传文件获取 file key
        :param file: 二进制文件
        :param file_name: 带后缀的文件名称。例；测试视频.mp4
        :param file_type: 文件类型.
            opus：上传opus音频文件；其他格式的音频文件，请转为opus格式后上传，转换方式可参考：ffmpeg -i SourceFile.mp3 -acodec libopus -ac 1 -ar 16000 TargetFile.opus
            mp4：上传mp4视频文件
            pdf：上传pdf格式文件
            doc：上传doc格式文件
            xls：上传xls格式文件
            ppt：上传ppt格式文件
            stream：上传stream格式文件。以上类型之外，可以使用stream格式
        :return:
        """
        access_token = self._get_access_token()
        data = self.client.post(
            content_type="data",
            files={'file': file},
            path=OpenAPI.GET_FILE_KEY.value,
            response_data_extractor=openapi_callback,
            data={"file_name": file_name, "file_type": file_type},
            headers={"Authorization": f"Bearer {access_token}"}
        )
        return data["data"]["file_key"]

    def get_user_id_by_email(self, email: str = None):
        """
        根据邮箱获取用户 openid，userid
        :param email:
        :return:
        """
        return self._get_user_id(email=email)

    def get_user_id_by_mobile(self, mobile: str = None):
        """
        根据电话获取用户 openid，userid
        :param mobile:
        :return:
        """
        return self._get_user_id(mobile=mobile)

    def _get_user_id(self, email: str = None, mobile: str = None):
        """
        获取用户 openid，userid
        :param email:
        :param mobile:
        :return:
        """
        url_params = dict()
        access_token = self._get_access_token()

        if email:
            url_params.update({"emails": email})
        if mobile:
            url_params.update({"mobiles": mobile})
        data = self.client.get(
            url_params=url_params,
            path=OpenAPI.GET_USER_ID.value,
            response_data_extractor=openapi_callback,
            headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json; charset=utf-8"}
        )
        if email:
            return list(data["data"]['email_users'].values())[0][0]
        return list(data["data"]['mobile_users'].values())[0][0]

    def get_group_robot_id(self):
        """
        获取机器人所在群列表
        :return:
        """
        access_token = self._get_access_token()
        data = self.client.get(
            OpenAPI.GET_GROUP_ROBOT_ID.value,
            response_data_extractor=openapi_callback,
            headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json; charset=utf-8"}
        )
        return data["data"]["items"]
