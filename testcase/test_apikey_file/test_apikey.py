#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
本章主题:创建一个apikey,已完成,可使用
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

def test_create_apikey():
    # 创建apikey
    api = '/v1/apikey/' + str(org_Id)
    urls = host + api
    my_body = {
        "applicationId": app_Id, # 应用级别添加这个应用id
        "name": "高精度定位API_wj",
        "whiteLists": [
            "192.168.10.125",
            "192.168.10.144"
        ]
    }
    my_body = json.dumps(my_body)
    rp = requests.post(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_update_apikey():
    # 修改apikey
    api_id = search_apikey_list(org_Id)
    api = '/v1/apikey/' + str(api_id)
    urls = host + api
    my_body = {
        "applicationId": app_Id,
        "name": "大汇的key",
        "whiteLists": [
        "192.168.10.6", "192.168.10.2", "192.168.10.5"
        ]
    }
    my_body = json.dumps(my_body)
    rp = requests.put(url=urls, headers=Headers, data=my_body)
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

data2 = [
    {"enable": "false"},
    {"enable": "true"}
]
@pytest.mark.parametrize('able', data2, ids=["先禁用Apikey","启用Apikey"])
def test_enable_apikey(able):
    # 禁用/启用apikey
    api_id = search_apikey_list(org_Id)
    api = '/v1/apikey/enable/' + str(api_id) + '/' + str(able['enable'])
    urls = host + api
    rp = requests.put(url=urls, headers=Headers)
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_select_apikey():
    # 查询apikey
    api_id = search_apikey_list(org_Id)
    api = '/v1/apikey/' + str(api_id)
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_select_apikeylist():
    # 查询apikey列表
    api = '/v1/apikey/search/' + str(org_Id)
    urls = host + api
    my_params = {
        "page": 1,
        "pageSize": 100,
        "searchKey": " "
    }
    rp = requests.get(url=urls, headers=Headers)
    # print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_delete_apikey():
    # 删除apikey
    api_id = search_apikey_list(org_Id)
    api = '/v1/apikey/' + str(api_id)
    urls = host + api
    rp = requests.delete(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200