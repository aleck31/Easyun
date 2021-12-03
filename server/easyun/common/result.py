# -*- coding: UTF-8 -*-
'''
@Description: Standardization for return.
@LastEditors: 
'''
from apiflask import Schema, abort
from apiflask.fields import String, Integer, Field, Nested
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
from typing import Union, Tuple


def generate_payload(data: any = None,
                     message: str = "success",
                     status_code: int = 200) -> dict:
    """生成格式化的响应体

    Args:
        data (any, optional): 响应的数据. Defaults to None.
        message (str, optional): 响应的消息. Defaults to "success".
        status_code (int, optional): 业务状态码. Defaults to 200.

    Returns:
        dict: 格式化好的载体
    """
    return {'message': message, 'status_code': status_code, 'data': data}


def make_resp(data: any = None,
              message: str = "success", status_code: int = 200,
              http_status_code: int = 200) -> Tuple[dict, int]:
    """make a views function response

            The return value should match the base response schema
            and the data key should match

    Args:
        data (any, optional): 响应的数据. Defaults to None.
        message (str, optional): 响应的消息. Defaults to "success".
        status_code (int, optional): 业务状态码. Defaults to 200.
        http_status_code (int, optional): http状态码. Defaults to 200.

    Returns:
        Tuple[dict, int]: 格式化好的字典与http状态码
    """
    return generate_payload(data=data, message=message, status_code=status_code), http_status_code



def error_resp(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message):
    return error_resp(400, message)


class Result:

    # 构造函数
    def __init__(self, code, msg, data):
        self.__code = code
        self.__msg = msg
        self.__data = data

    # getter
    @property
    def code(self):
        return self.__code

    # settter
    @code.setter
    def code(self, code):
        self.__code = code

    # getter
    @property
    def msg(self):
        return self.__msg

    # setter
    @msg.setter
    def msg(self, msg):
        self.__msg = msg

    # getter
    @property
    def data(self):
        return self.__data

    # settter
    @data.setter
    def code(self, data):
        self.__data = data
