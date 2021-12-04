# -*- coding: UTF-8 -*-
'''
@Description: Standardization for return.
@LastEditors: 
'''
from apiflask import Schema, abort
from apiflask.fields import String, Integer, Field, Nested
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES, http_date
from typing import Any, Union, Tuple

{
    "detail": {  # 存放data
        # "api_msg": "", 
        # "api_status_code": 200 
        # "api_detail": {}
    },
    "message": "Not Found",  # 响应消息
    "status_code": 200  # 业务码
    # "error": {}, # 存放错误内容
}


def generate_payload(data: Any = None,
                     message: str = "success",
                     status_code: int = 200) -> dict:
    """生成格式化的响应体

    Args:
        data (Any, optional): 响应的数据. Defaults to None.
        message (str, optional): 响应的消息. Defaults to "success".
        status_code (int, optional): 业务状态码. Defaults to 200.

    Returns:
        dict: 格式化好的载体
    """
    return {'message': message, 'status_code': status_code, 'data': data}


def make_resp(data: Any = None,
              message: str = "success", status_code: int = 200,
              http_status_code: int = 200) -> Tuple[dict, int]:
    """make a views function response

            The return value should match the base response schema
            and the data key should match

    Args:
        data (Any, optional): 响应的数据. Defaults to None.
        message (str, optional): 响应的消息. Defaults to "success".
        status_code (int, optional): 业务状态码. Defaults to 200.
        http_status_code (int, optional): http状态码. Defaults to 200.

    Returns:
        Tuple[dict, int]: 格式化好的字典与http状态码
    """
    return generate_payload(data=data, message=message, status_code=status_code), http_status_code


def error_resp(status_code, message=None):
    abort(status_code=status_code, message=message)
    # payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    # if message:
    #     payload['message'] = message
    # response = jsonify(payload)
    # response.status_code = status_code
    # return response


def bad_request(message):
    return error_resp(400, message)


class Result:

    # 构造函数
    def __init__(self,
                 data: Any = None, status_code: int = 200,
                 message: str = "success", http_status_code: int = 200) -> None:
        """初始化响应数据类

        Args:
            data (Any, optional): 响应的数据. Defaults to None.
            status_code (int, optional): 业务状态码. Defaults to 200.
            message (str, optional): 响应消息. Defaults to "success".
            http_status_code (int, optional): HTTP状态码. Defaults to 200.
        """
        self.status_code = status_code
        self.message = message
        self.data = data
        self.http_status_code = http_status_code

    def make_resp(self) -> Tuple[dict, int]:
        # 调用上面的make_resp函数，确定方式后合并
        return make_resp(self.data, self.message, self.status_code, self.http_status_code)

    def err_resp(self) -> None:
        # 是否需要这样处理error?
        # error 响应体格式?
        # 通用响应体中是否需要新增一个 'error' 字段？
        abort(self.http_status_code,
              self.message,
              extra_data={
                  "data": self.data,
                  "status_code": self.status_code
              })
        # apiflask 的错误响应格式:
        # {
        #     "detail": {

        #     },
        #     "message": "Not Found"
        # }

    # 是否需要 setter 与 getter？
    # getter
    # @property
    # def code(self):
    #     return self.__code

    # # settter
    # @code.setter
    # def code(self, code):
    #     self.__code = code

    # # getter
    # @property
    # def msg(self):
    #     return self.__msg

    # # setter
    # @msg.setter
    # def msg(self, msg):
    #     self.__msg = msg

    # # getter
    # @property
    # def data(self):
    #     return self.__data

    # # settter
    # @data.setter
    # def code(self, data):
    #     self.__data = data
