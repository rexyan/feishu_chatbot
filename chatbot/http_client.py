"""
自定义 http 请求类：支持设置重试次数，重试退避规则，强制重试的一组 HTTP 状态代码，支持数据请求成功 callback

使用示例：
    def func(data):
        return data["resultcode"]

    http = HttpClient()
    print(http.get("http://xxx/api"))
    print(http.get("http://apis.juhe.cn/ip/ipNew"))
    print(http.get("http://apis.juhe.cn/ip/ipNew", response_data_extractor=func))
"""

import requests
from requests import Response
from requests.exceptions import (
    RetryError,
    HTTPError,
    ConnectionError,
    Timeout,
    ConnectTimeout,
    RequestException,
)
from urllib3 import Retry
from collections import defaultdict
from collections.abc import Callable
from requests.adapters import HTTPAdapter


class HttpClient:
    __slots__ = ()

    def __requests_retry_session(
        self,
        retries: int = 3,
        backoff_factor: float = 0.3,
        status_forcelist: tuple = (500, 502, 504),
        session: object = None,
    ) -> requests.Session:
        """
        获取 session 对象
        @param retries: 重试次数
        @param backoff_factor: 重试退避规则
        @param status_forcelist: 强制重试 HTTP 状态代码
        @param session:
        @return:
        """
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def get(
        self,
        path: str,
        headers: dict = None,
        url_params: dict = None,
        data: dict = None,
        response_data_extractor: Callable = lambda x: x,
        verify: bool = False,
    ) -> object or Response:
        """
        get 请求
        @param path: 请求路径
        @param headers: 请求头
        @param url_params: 请求数据
        @param data: 请求头
        @param response_data_extractor: 回调函数
        @param verify: 是否校验证书
        @return:
        """
        params = defaultdict()
        params["url"] = path
        params["verify"] = verify
        if headers:
            params["headers"] = headers
        if data:
            params["params"] = data
        if url_params:
            params["params"] = url_params
        try:
            response = self.__requests_retry_session().get(**params)
            response.raise_for_status()
            result = response_data_extractor(response)
        except (RetryError, HTTPError, ConnectionError, Timeout, ConnectTimeout) as e:
            raise RequestException(f"HttpClient Request Error: {e}, {e.response.text}")
        except Exception as e:
            raise RequestException(f"HttpClient Error: {e}")
        else:
            return result

    def post(
        self,
        path: str,
        data: dict or str = None,
        headers: dict = None,
        files=None,
        url_params: dict = None,
        response_data_extractor: Callable = lambda x: x,
        content_type: str = "json",
        verify: bool = False,
    ) -> object or Response:
        """
        post 请求
        @param path: 请求路径
        @param data: 请求数据
        @param url_params: 请求数据
        @param headers: 请求头
        @param files: 文件
        @param response_data_extractor: 回调函数
        @param content_type: 请求类型
        @param verify: 是否校验证书
        @return:
        """
        params = defaultdict()
        params["url"] = path
        params["verify"] = verify
        if headers:
            params["headers"] = headers
        if data:
            params[content_type] = data
        if url_params:
            params["params"] = url_params
        if files:
            params["files"] = files
        try:
            response = self.__requests_retry_session().post(**params)
            response.raise_for_status()
            result = response_data_extractor(response)
        except (RetryError, HTTPError, ConnectionError, Timeout, ConnectTimeout) as e:
            raise RequestException(f"HttpClient Request Error: {e}, {e.response.text}")
        except Exception as e:
            raise RequestException(f"HttpClient Error: {e}")
        else:
            return result

    def put(
        self,
        path: str,
        data: dict = None,
        headers: dict = None,
        response_data_extractor: Callable = lambda x: x,
        verify: bool = False,
    ) -> object or Response:
        """
        post 请求
        @param path: 请求路径
        @param data: 请求数据
        @param headers: 请求头
        @param response_data_extractor: 回调函数
        @param verify: 是否校验证书
        @return:
        """
        params = defaultdict()
        params["url"] = path
        params["verify"] = verify
        if headers:
            params["headers"] = headers
        if data:
            params["data"] = data
        try:
            response = self.__requests_retry_session().put(**params)
            response.raise_for_status()
            result = response_data_extractor(response)
        except (RetryError, HTTPError, ConnectionError, Timeout, ConnectTimeout) as e:
            raise RequestException(f"HttpClient Request Error: {e}, {e.response.text}")
        except Exception as e:
            raise RequestException(f"HttpClient Error: {e}")
        else:
            return result
