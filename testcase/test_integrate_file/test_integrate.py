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

# org_Id是组织id
org_id = search_org_list()
org_id_dict = []
org_id_dict = org_id.json()['data']
org_Id = org_id_dict['data'][-1]['id'] # 取第一个组织的id
org_Id_new = org_id_dict['data'][0]['id'] # 取最新的一个组织id

# 应用id
app_id = search_app_list(org_Id)
app_id_dict = app_id.json()['data']
app_Id = app_id_dict['data'][0]['id'] # 取最新的一个应用id

@pytest.mark.skip
def test_create_integrate():
    # 添加一个集成推送
    api = '/v1/integrate/http/' + str(app_Id) # 应用id:4
    urls = host + api
    my_body = {
        "enabled": False,
        "headers": {
        "token": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxIiwiYXV0aFR5cGUiOiIxIiwic3ViIjoiMTY4NTU1NDExMjIiLCJpYXQiOjE2MTcyNDM0"
        },
        "httpMethod": 1, # 请求Method 1 GET 2 POST 3 PUT 4 DELETE
        "url": "https://www.json.cn/"
    }
    my_body = json.dumps(my_body)
    rp = requests.post(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_update_integrate():
    # 修改HTTP集成推送
    jc_id = search_http(app_Id)
    api = '/v1/integrate/http/' + str(jc_id)
    urls = host + api
    my_body = {
        "enabled": True,
        "headers": {
        "token": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxIiwiYXV0aFR5cGUiOiIxIiwic3ViIjoiMTY4NTU1NDExMjIiLCJpYXQiOjE2MTcyNDM0"
        },
        "httpMethod": 1,
        "url": "https://www.json.cn/"
    }
    my_body = json.dumps(my_body)
    rp = requests.put(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['data']['enabled'] is True

# 已经放入common.py文件
# @pytest.mark.skip
def test_search_http():
    # 查询http
    api = '/v1/integrate/1/' + str(app_Id)
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

# 已经放入common.py文件
def test_search_mqtt():
    # 查询应用
    api = '/v1/integrate/mqtt/' + str(app_Id)
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_update_mqtt():
    # 修改mqtt密码
    mqtt_id = search_mqtt(app_Id)
    api = '/v1/integrate/mqtt/' + str(mqtt_id)
    urls = host + api
    rp = requests.put(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['msg'] == "修改成功"
    assert rp.json()['data'] is not None
able_data = [
    {"enable": "false"},
    {"enable": "true"}
]
@pytest.mark.parametrize('able', able_data, ids=["先禁用","再启用"])
def test_enabled_integrate(able):
    # 先禁用,再启用
    mqtt_id = search_mqtt(app_Id)
    api = '/v1/integrate/enable/' + str(mqtt_id) + '/' + str(able['enable'])
    urls = host + api
    rp = requests.put(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['msg'] == "操作成功"