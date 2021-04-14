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


def test_add_terminal():
    # 添加终端
    api = '/v1/terminal'
    urls = host + api
    my_body = {
        "applicationId": app_Id,
        "modelId": 2,
        "name": "刘飞儿",
        "properties": {
        "key": "12332"
        },
        "serialNumber": "1234563789"
    }
    my_body = json.dumps(my_body)
    rp = requests.post(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['msg'] == "添加成功"

def test_update_terminal():
    # 修改终端
    t_Id = search_terminal(app_Id,org_Id)
    api = '/v1/terminal/' + str(t_Id)
    urls = host + api
    my_body = {
        "applicationId": app_Id,
        "modelId": 2,
        "name": "地底探险家",
        "properties": {
            "key": "12332"
        },
        "serialNumber": "1234563789"
    }
    my_body = json.dumps(my_body)
    rp = requests.put(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_search_terminal():
    # 搜索终端列表
    api = '/v1/terminal/search'
    urls = host + api
    my_params = {
        "applicationId": app_Id,
        "organizationId": org_Id,
        "page": 1,
        "pageSize": 100,
        "searchKey": " "
    }
    rp = requests.get(url=urls, headers=Headers, params=my_params)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_select_terminal():
    # 查看终端
    t_Id = search_terminal(app_Id, org_Id)
    api = '/v1/terminal/' + str(t_Id)
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
ter_data = [
    {"enable": "false"},
    {"enable": "true"}
]
@pytest.mark.parametrize('able', ter_data, ids=["先禁用","再启用"])
def test_enabled_terminal(able):
    # 先禁用,再启用
    t_Id = search_terminal(app_Id, org_Id)
    api = '/v1/terminal/enable/' + str(t_Id) + '/' +str(able['enable'])
    urls = host + api
    rp = requests.put(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['msg'] == "操作成功"

def test_del_terminal():
    # 删除终端
    t_Id = search_terminal(app_Id, org_Id)
    api = '/v1/terminal/' + str(t_Id)
    urls = host + api
    rp = requests.delete(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200