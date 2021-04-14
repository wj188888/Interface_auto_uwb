#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
本章主题: 应用相关单接口的用例
'''

import requests
# from requests.auth import HTTPBasicAuth
import pytest
import yaml
import os
import sys
path = os.path.dirname(sys.path[0])
import json
from business.common import http_header,http_host,search_org_list,search_app_list

# 调用common.py中http_header,http_host函数获取,,请求头和host
Headers = http_header()
host = http_host()
org_id = search_org_list()
# print(org_id.json()['data'])
org_id_dict = []
org_id_dict = org_id.json()['data']
# print(org_id_dict['data'][0]['id'])
org_Id = org_id_dict['data'][-1]['id']


data1 = [
    ({"name": "大汇网络服务应用_wj","id": org_Id, "description": "大汇网络服务"}, 200, "添加应用成功"),
    ({"name": "安全冲锋衣应用_wj", "id": org_Id, "description": "安全冲锋衣"}, 200, "添加应用成功")
]

# @pytest.mark.skip
@pytest.mark.parametrize('topic_data, code, msg', data1, ids=["新增 大汇网络服务应用_wj,","新增 安全冲锋衣应用_wj"])
def test_create_application(topic_data, code, msg):

    api = '/v1/application/' + str(topic_data['id']) # 这里跟的是: 组织id
    urls = host + api
    my_body = {
          "description": topic_data['description'],
          "name": topic_data['name']
    }
    my_body = json.dumps(my_body)
    rp = requests.post(headers=Headers, url=urls, data=my_body)
    print(rp.json())

    assert rp.json()['code'] == code
    assert rp.json()['msg'] == msg
    assert rp.json()['data']['enabled'] is True
    assert rp.json()['data']['name'] is not None

def test_get_application():
    # 查询应用
    al = search_app_list(org_Id)
    bl = al.json()['data']
    api = '/v1/application/' + str(bl['data'][0]['id']) # 这里跟的是: 应用id
    urls = host + api
    rp = requests.request(method='get', url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_update_application():
    # 修改更新应用信息
    al = search_app_list(org_Id)
    bl = al.json()['data']
    api = '/v1/application/' + str(bl['data'][0]['id']) # 这里跟的是:应用id
    urls = host + api
    my_body = {
        "description": "安全冲锋衣-修改更新",
        "name": "安全冲锋衣应用_wj"
    }
    my_body = json.dumps(my_body)
    rp =requests.put(headers=Headers, url=urls, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
enable_data = [
    {"enable": "false"},{"enable": "true"}
]
@pytest.mark.parametrize("able", enable_data, ids=["先禁用", "再启用"])
def test_enabled_application(able):
    # 禁用/启用应用
    al = search_app_list(org_Id)
    bl = al.json()['data']
    api = '/v1/application/enable/' + str(bl['data'][0]['id']) + '/' + able['enable'] # ./应用id/enabled 的id,,false作为参数
    urls = host + api
    rp = requests.put(url=urls, headers=Headers)
    # if able['enbale'] == "true":
    #     print("应用启用成功!!!")
    # elif able['enbale'] == "false":
    #     print("应用禁用成功!!!")
    # else: print("========")
    rp_dict = json.loads(rp.text)
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def test_search_oneorg_allapp():
    # 查询组织的所有应用
    api = '/v1/application/all/' + str(org_Id) # 这里是组织id
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    # assert rp.json()['data'][0]['name'] is not None # 断言name不为空
model_data = [
    {"modelType": 1},
    {"modelType": 2}
]
@pytest.mark.parametrize('id', model_data, ids=["基站类型", "帽子类型"])
def test_search_application_list(id):
    # 查询应用列表和型号列表
    api = '/v1/application/list/model/' + str(org_Id) + '/' + str(id['modelType']) # 组织 id;->model id;
    urls = host + api
    my_params = {
        'id': 1, #
        'page': None,
        'pageSize': None,
        'searchKey': None
    }
    rp = requests.get(url=urls, headers=Headers, params=my_params)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200


def test_del_application():
    # 删除应用
    for i in range(-2,0):
        al = search_app_list(org_Id)
        bl = al.json()['data']
        xid = bl['data'][0]['id']
        api = '/v1/application/' + str(xid)# 应用id
        urls = host + api
        rp = requests.delete(headers=Headers, url=urls)
        assert rp.status_code == 200
        assert rp.json()['code'] == 200
        assert rp.json()['msg'] == "删除应用成功"

