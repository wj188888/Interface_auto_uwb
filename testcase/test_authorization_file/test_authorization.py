#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
本章主题:授权相关的接口
'''
import requests
# from requests.auth import HTTPBasicAuth
import pytest
import os
import sys
path = os.path.dirname(sys.path[0])
import json
from business.common import *

# 调用common.py中http_header,http_host函数获取,,请求头和host
Headers = http_header()
host = http_host()

data1 = [
    {'name': '','password': ''},
    {'name': '1312d','password': 'ddad'},
    {'name': '','password': '12345678'},
    {'name': '16855541122','password': ''}
]
@pytest.mark.skip
@pytest.mark.xfail
@pytest.mark.parametrize('input', data1, ids =["账户密码都为空,登录失败",
                                               "账户密码都错误,登录失败",
                                               "账户为空,密码正确,登录失败",
                                               "账号正确,密码为空,登录失败"])
def test_authorization_login0(input):
    # 账户登录,反用例验证
    api = '/v1/authorization/login'
    urls = host + api
    my_body = {
      "name": input['name'],
      "password": input['password']
    }
    my_body = json.dumps(my_body)
    rp = requests.post(url=urls, headers=Headers, data=my_body)
    # print(rp.text)
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_authorization_login1():
    # 账户登录,正用例验证
    api = '/v1/authorization/login'
    urls = host + api
    my_body = {
      "name": '18428333658',
      "password": '12345678'
    }
    my_body = json.dumps(my_body)
    rp = requests.post(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    return rp


def test_refresh():
    # 账户认证,刷新认证,shenmeqingkaungxia会刷新认证
    retoken_id = test_authorization_login1()
    retorkn_dict = []
    retorkn_dict = retoken_id.json()['data']['refreshToken']
    api = '/v1/authorization/refresh'
    urls = host + api
    my_body = {
      "refreshToken": retorkn_dict
    }
    my_body = json.dumps(my_body)
    print(rp.json())
    rp = requests.post(url=urls, headers=Headers, data=my_body)
    assert rp.json()['code'] == 200
