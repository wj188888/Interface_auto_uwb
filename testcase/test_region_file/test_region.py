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

# org_id是组织id
org_id = search_org_list()
org_id_dict = []
org_id_dict = org_id.json()['data']
org_Id = org_id_dict['data'][-1]['id'] # 取第一个组织的id

# reg_id是区域id
reg_id= search_region_list(org_Id)
reg_id_dict = []
reg_id_dict = reg_id.json()['data']
reg_Id = reg_id_dict['data'][0]['id'] # 取区域返回的最新建的区域id,reg_id

def test_create_region():
    # 添加区域
    api = '/v1/region/' + str(org_Id) # 第一个组织id,[0]
    urls = host + api
    my_body = {
        "coordinateSystem": 1,
        "description": "王霸天的区域",
        "locationCount": 3,
        "locationType": 2,
        "organizationId": org_Id,
        "name": "修正wy区域",
        "referenceAltitude": 123.9,
        "filter": False
    }
    my_body = json.dumps(my_body)
    rp = requests.post(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.json()['code'] == 200

def test_update_region():
    # 修改区域
    reg_id_del = search_region_list(org_Id)
    reg_id_dict_del = []
    reg_id_dict_del = reg_id_del.json()['data']
    reg_Id_del = reg_id_dict_del['data'][0]['id']  # 取区域返回的最新建的区域id,reg_id

    api = '/v1/region/' + str(reg_Id_del)
    urls = host + api
    my_body = {
        "coordinateSystem": 1,
        "description": "王霸天的区域-修改更新",
        "locationCount": 3,
        "locationType": 2,
        "organizationId": org_Id,
        "name": "修正区域",
        "referenceAltitude": 200.1,
        "filter": True
    }
    my_body = json.dumps(my_body)
    rp = requests.put(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['data']['enabled'] is True

def test_search_region():
    # 查询某一个区域
    api = '/v1/region/' + str(reg_Id)
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['msg'] == "查询区域成功"
    assert rp.json()['data'] is not None

def test_getall_region_list():
    # 查询当前组织所有区域列表
    api = '/v1/region/all/' + str(org_Id)
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

# 重复使用的接口,放到common去了
def test_search_region_list():
    # 搜索(查询)区域列表
    api = '/v1/region/search/' + str(org_Id)
    urls = host + api
    my_params = {
        'page': 1,
        'pageSize': 100,  # 限制为100以内,是每一页显示列表数据条数
        'searchKey': None
    }
    rp = requests.get(headers=http_header(), url=urls, params=my_params)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

reg_data = [
    {"enable": False},
    {"enable": True}
]
@pytest.mark.parametrize('able', reg_data, ids=["先禁用区域","再启用区域"])
def test_enabled_region(able):
    # 先禁用,再启用我们的区域
    reg_id_del = search_region_list(org_Id)
    reg_id_dict_del = []
    reg_id_dict_del = reg_id_del.json()['data']
    reg_Id_del = reg_id_dict_del['data'][0]['id']  # 取区域返回的最新建的区域id,reg_id

    api = '/v1/region/enable/' + str(reg_Id_del) + '/' + str(able['enable'])
    urls = host + api
    rp = requests.put(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['msg'] == "操作成功"


def test_del_region():
    reg_id_del = search_region_list(org_Id)
    reg_id_dict_del = []
    reg_id_dict_del = reg_id_del.json()['data']
    reg_Id_del = reg_id_dict_del['data'][0]['id']

    api = '/v1/region/' + str(reg_Id_del) # reg_Id_del是区域id
    urls = host + api
    rp = requests.delete(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['msg'] == "删除区域成功"



