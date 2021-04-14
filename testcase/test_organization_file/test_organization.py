#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
# from requests.auth import HTTPBasicAuth
import pytest
import os
import sys
path = os.path.dirname(sys.path[0])
import time
import json
from business.common import http_header,http_host,search_org_list,search_app_list

# 调用common.py中http_header,http_host函数获取,,请求头和host
Headers = http_header()
host = http_host()

org_id = search_org_list()
org_id_dict = []
org_id_dict = org_id.json()['data']
org_Id = org_id_dict['data'][0]['id'] # 取第一个组织的id

def test_create_organization():
    # 添加组织
    api = '/v1/organization'
    urls = host + api
    my_body = {
            "contactName": "王杰",
            "contactPhone": "18428333658",
            "maxApplicationCount": 20,
            "description": "",
            "maxGatewayCount": 20,
            "maxRegionCount": 20,
            "maxTerminalCount": 20,
            "maxStationCount": 30,
            "name": "大汇-科技"
    }
    my_body = json.dumps(my_body)
    rp = requests.post(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['data']['name'] == "大汇-科技"
    assert rp.json()['data']['enabled'] is True
time.sleep(1)
def test_update_organization():
    # 修改组织
    org_id_del = search_org_list()
    org_id_dict1 = []
    org_id_dict1 = org_id_del.json()['data']
    org_Id_del = org_id_dict1['data'][0]['id'] # 之前是-1,现在改为0
    api = '/v1/organization/' + str(org_Id_del) # 修改最后(最新)一个组织
    urls = host + api
    my_body = {
        "contactName": "王杰",
        "contactPhone": "18428333658",
        "maxApplicationCount": 40,
        "description": "修改更新wj的组织",
        "maxGatewayCount": 40,
        "maxRegionCount": 40,
        "maxTerminalCount": 40,
        "maxStationCount": 100,
        "name": "促进经济发展-小队"
    }
    my_body = json.dumps(my_body)
    rp = requests.put(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.json()['code'] == 200
    assert rp.json()['msg'] == "修改组织成功"
    assert rp.json()['data']['enabled'] is True
def test_get_organization():
    # 查询某一个组织的详情
    api = '/v1/organization/' + str(org_Id) # 返回列表的第一个组织
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.json()['code'] == 200
    assert rp.json()['msg'] == "查询组织信息成功"
    assert rp.json()['data'] is not None

def test_getall_organization():
    # 查询所有组织简要信息列表
    api = '/v1/organization/all'
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    assert rp.json()['data'] is not None

def test_delete_organization():
    # 删除组织
    org_id_del = search_org_list()
    # print(org_id.json()['data'])
    org_id_dict1 = []
    org_id_dict1 = org_id_del.json()['data']
    # print(org_id_dict['data'][0]['id'])
    org_Id_del = org_id_dict1['data'][0]['id'] # 之前是-1
    api = '/v1/organization/' + str(org_Id_del) # 删除最后(最新)新建的一个组织
    urls = host + api
    rp = requests.delete(url=urls, headers=Headers)
    print(rp.json())
    assert rp.json()['code'] == 200
    assert rp.json()['msg'] == "删除组织成功"