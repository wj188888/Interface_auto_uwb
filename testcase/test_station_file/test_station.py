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

# reg_Id是区域id
reg_id= search_region_list(org_Id)
reg_id_dict = []
reg_id_dict = reg_id.json()['data']
reg_Id = reg_id_dict['data'][0]['id'] # 取区域返回的最新建的区域id,reg_id

def test_create_station():
    # 添加基站
    api = '/v1/station'
    urls = host + api
    my_body = {
      "altitude": 100,
      "coordinateType": 2,
      "latitude": 30.616,
      "longitude": 101.356,
      "modelId": 1,
      "name": "大坝基站_wj",
      "regionId": reg_Id,
      "securityCode": "25452412164545",
      "serialNumber": "1013132129"
    }
    my_body = json.dumps(my_body)
    rp = requests.post(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_update_station():
    # 修改基站
    s_id = search_station_list(org_Id, reg_Id)
    api = '/v1/station/' + str(s_id)
    urls = host + api
    my_body = {
      "altitude": 200,
      "coordinateType": 2,
      "latitude": 30.616,
      "longitude": 101.356,
      "modelId": 1,
      "name": "大坝基坑-修改",
      "regionId": reg_Id,
      "securityCode": "25452412164545",
      "serialNumber": "1013132126"
    }
    my_body = json.dumps(my_body)
    rp = requests.put(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200


def test_search_station_info():
    # 获取基站信息
    s_id = search_station_list(org_Id, reg_Id)
    api = '/v1/station/' + str(s_id) # 序列号id
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code']

@pytest.mark.skipif
def test_search_station_list():
    # 搜索(查询)基站列表
    api = '/v1/station/search/' + str(org_Id)
    urls = host + api
    my_params = {
        "page": 1,
        "pageSize": 100,
        "regionId": reg_Id,
        "searchKey": "基站"
    }
    rp = requests.get(url=urls, headers=Headers, params=my_params)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

sta_data = [
    {"enable": "false"},
    {"enable": "true"}
]
@pytest.mark.parametrize('able', sta_data, ids=["先禁用","再启用"])
def test_enabled_station(able):
    # 先禁用,再启用基站
    s_id = search_station_list(org_Id, reg_Id)
    api = '/v1/station/enable/' + str(s_id) + '/' + str(able['enable']) # 序列号id
    urls = host + api
    rp = requests.put(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200


def test_del_station():
    # 删除基站
    s_id = search_station_list(org_Id, reg_Id)
    api = '/v1/station/' + str(s_id) # 序列号id
    urls = host + api
    rp = requests.delete(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code']
