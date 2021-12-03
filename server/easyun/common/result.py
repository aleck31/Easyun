# -*- coding: UTF-8 -*-
'''
@Description: Standardization for return.
@LastEditors: 
'''
from apiflask import Schema, abort
from apiflask.fields import String, Integer, Field, Nested
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def make_resp(message, status_code, data):
    # the return value should match the base response schema
    # and the data key should match
    return {'message': message, 'status_code': status_code, 'data': data}


def error_resp(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message):
    return error_resp(400, message)



class Result :
 
    #构造函数
    def __init__(self, code, msg, data):
        self.__code = code
        self.__msg = msg
        self.__data = data
 
    #getter
    @property
    def code(self):
        return self.__code
 
    #settter
    @code.setter
    def code(self, code):
        self.__code = code
 
    #getter
    @property
    def msg(self):
        return self.__msg

    #setter
    @msg.setter
    def msg(self, msg):
        self.__msg = msg
 
    #getter
    @property
    def data(self):
        return self.__data
 
    #settter
    @data.setter
    def code(self, data):
        self.__data = data

