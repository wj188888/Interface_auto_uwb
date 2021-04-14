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
org_Id_new = org_id_dict['data'][0]['id'] # 取最新组织的id
org_Id = org_id_dict['data'][-1]['id'] # 取第一个组织的id
# usr_id
usr_id = search_user()
usr_id_dict = []
usr_id_dict = usr_id.json()['data']
usr_Id = usr_id_dict['data'][-1]['id']  # 取最新(近)的用户id

def test_normal_user_list():
    # 分页查询所有普通用户列表
    api = '/v1/user/list/normal'
    urls = host + api
    my_params = {
        'organizationId': org_Id,
        'page': 1,
        'pageSize': 20,  # 限制为100以内,是每一页显示列表数据条数
        'searchKey': None
    }
    rp = requests.get(url=urls, headers=Headers, params=my_params)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    # assert rp.json()['data]['data'][0]['granted'] is True # 授权与否

def test_search_org_user():
    # 搜索组织内用户
    api = '/v1/user/organization/search/' + str(org_Id_new)
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

def test_select_alluser():
    # 查询所有的用户
    api = '/v1/user/all/' + str(org_Id)
    urls = host + api
    rp = requests.request(method='get', url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_userinfo():
    # 个人中心信息
    api = '/v1/user/userinfo/' + str(usr_Id)
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_del_org_user():
    # 删除组织用户
    org_usr_id = search_org_user(org_Id_new)
    org_usr_iddt = []
    org_usr_iddt = org_usr_id.json()['data']
    org_usr_Id = org_usr_iddt['data'][-1]['grantId']

    api = '/v1/user/organization/' + str(org_usr_Id) # 组织内的用户的id
    urls = host + api
    rp = requests.delete(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_add_org_user():
    # 添加组织用户
    api = '/v1/user/organization/' + str(org_Id_new) + '/' +str(usr_Id)
    urls = host + api
    rp = requests.post(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

