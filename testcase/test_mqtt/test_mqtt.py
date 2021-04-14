#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
本章主题:创建一个mqtt推送,状态:未完成,等王洋那边和硬件进行联调时完善mqtt
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

def test_mqtt_ac1():
    # 权限认证
    api = '/v1/mqtt/acl'
    urls = host + api
    my_params = {
        'access': 1,    # int
        'topic': "da ",
        'username': "z"
    }
    rp = requests.get(url=urls, header=Headers, params=my_params)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_mqtt_auth():
    # mqtt认证
    api = '/v1/mqtt/auth'
    urls = host + api
    my_body = {
      "clientid": "string",
      "password": "string",
      "username": "string"
    }
    my_body = json.dumps(my_body)
    rp = requests.post(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_mqtt_superauth():
    # mqtt超级用户认证
    api = '/v1/mqtt/super'
    urls = host + api
    my_body = {
        "clientid": "string",
        "password": "string",
        "username": "string"
    }
    my_body = json.dumps(my_body)
    rp = requests.post(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200