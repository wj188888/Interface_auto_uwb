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

# usr_id
usr_id = search_user()
usr_id_dict = []
usr_id_dict = usr_id.json()['data']
usr_Id = usr_id_dict['data'][-1]['id']  # 取最新(近)的用户id

def test_create_user():
    # 必填项测试,正用例
    api = '/v1/user'  # 创建用户
    urls = host + api
    my_data = {
        "admin": True,
        "email": "246456@qq.com",
        "organizationIds": [
            org_Id
        ],
        "password": "12345678",
        "phone": "18428333651",
        "realName": "张三",
        "remark": "张三的高精度平台账号",
        "superAdmin": False
    }
    my_body = json.dumps(my_data)
    rp = requests.post(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_update_userinfo():
    # 修改用户平台信息,正用例
    api = '/v1/user/' + str(usr_Id)
    urls = host + api
    my_body = {
        "admin": True,
        "email": "246515@qq.com",
        "organizationIds": [
        org_Id
        ],
        "password": "12345678",
        "phone": "18428333651",
        "realName": "张三",
        "remark": "修改后操作",
        "superAdmin": False
    }
    my_body = json.dumps(my_body)
    rp = requests.put(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200



def test_search_user():
    # 搜索平台用户
    api = '/v1/user/search'
    urls = host + api
    my_params = {
        'page': 1,
        'pageSize': 100,  # 限制为100以内,是每一页显示列表数据条数
        'searchKey': None
    }
    rp = requests.get(url=urls, headers=Headers, params=my_params)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['msg'] == "搜索成功"
able_user = [
    {"enable": False},
    {"enable": True}
]
@pytest.mark.parametrize('able', able_user, ids=["先禁用", "再启用"])
def test_enabled_user(able):
    # 先禁用,再启用平台用户
    api = '/v1/user/enable/' + str(usr_Id) + '/' + str(able['enable'])
    urls = host + api
    rp = requests.put(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['msg'] == "操作成功"



def test_userinfo():
    # 个人中心信息
    api = '/v1/user/userinfo'
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_userall_org():
    # 查询当前用户可操作的所有组织
    api = '/v1/user/userinfo/all/organization'
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_del_user():
    # 删除平台用户
    api = '/v1/user/' + str(usr_Id)
    urls = host + api
    rp = requests.delete(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200