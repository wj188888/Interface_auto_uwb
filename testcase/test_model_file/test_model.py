#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

m_id = add_model(1)
m_Id = m_id.json()['data']['id']

# 基站:1 帽子:2

def test_update_model():
    # 修改型号
    api = '/v1/model/' + str(m_Id)
    urls = host + api
    my_body = {
        "description": "修改后-的通信基站",
        "name": "智能安全帽通信基站X"
    }
    my_body = json.dumps(my_body)
    rp = requests.put(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['msg'] == "修改型号成功"
    assert rp.json()['data'] is not None

def test_search_model():
    api = '/v1/model/' + str(m_Id)
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_del_model():
    print("删除型号")