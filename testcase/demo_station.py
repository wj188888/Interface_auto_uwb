#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
本章主题: 基站相关单接口用例
'''
import  requests
import pytest
import yaml
import json
from requests.auth import HTTPBasicAuth

with open('E:/wj/saas/UwbNetworkServer/common/YamlFile/MyHeaders.yaml','r',encoding='utf-8') as f:
    Headers = yaml.safe_load(f)
with open('E:/wj/saas/UwbNetworkServer/common/YamlFile/uwb_network_api.yaml','r',encoding='utf-8') as f:
    my_host = yaml.safe_load(f)
host = my_host['host1']

def test_add_station():
    # 创建一个应用
    api = '/v1/station'
    urls = host + api
    my_data = {
        "altitude": {},
        "coordinateType": {},
        "latitude": {},
        "longitude": {},
        "name": {},
        "regionId": {},
        "securityCode": {},
        "stationEui": {}
    }
    my_data = json.dumps(my_data)
    rp = requests.request(method='post', url=urls, headers=Headers, auth=HTTPBasicAuth('1511564082@qq.com','12345678'), data=my_data)
    print(rp.text)
    assert rp.status_code == 200

def test_get_station():
    api = '/v1/station/{stationId}'
    urls = host + api
    rp = requests.request(method='get', url=urls, headers=Headers, auth=HTTPBasicAuth('1511564082@qq.com','12345678'))
    print(rp.text)
    assert rp.status_code == 200

def test_update_station():
    api = '/v1/station/enabled/{stationId}/{enabled}'
    urls = host + api
    rp = requests.request(method='put', url=urls, headers=Headers, auth=HTTPBasicAuth('1511564082@qq.com','12345678'))
    print(rp.text)
    assert rp.status_code == 200
def test_del_station():
    api = '/v1/station/{stationId}'
    urls = host + api
    rp = requests.request(method='delete', url=urls, headers=Headers, auth=HTTPBasicAuth('1511564082@qq.com','12345678'))
    print(rp.text)
    assert rp.status_code == 200

def test_select_apikeylist():
    # 查询apikey列表
    api = '/v1/apikey/search/' + str(org_Id)
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    # print(rp.text)
    with open(r'./wj.txt', 'w', encoding='utf-8') as f:
        yaml.dump(rp.text, f, allow_unicode=True)
    assert rp.status_code == 200
    assert json.loads(rp.text)['code'] == 200