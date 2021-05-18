#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json

# 获取token
def get_token():
    token = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2NiIsImF1dGhUeXBlIjoiMSIsInN1YiI6IjE4NDI4MzMzNjU4IiwiaWF0IjoxNjIxMjIwODM0LCJleHAiOjE2MjM4MTI4MzR9.RygFiczKDCA1u0_vvcfENXIePmtU652NbXXNEkM4eB8"
    return token
def current_token():
    head = {"Content-Type": "application/json"}
    api = '/v1/authorization/login'
    urls = http_host() + api
    my_body = {
        "name": "18428333658",
        "password": "12345678"
    }
    my_body = json.dumps(my_body)
    rp = requests.post(headers=head, url=urls, data=my_body)
    print(rp.json())
    ref_Token = rp.json()['data']['refreshToken']
    return ref_Token
# 请求头

def refresh():
    # 账户认证,刷新认证,什么情况下会刷新认证
    api = '/v1/authorization/refresh'
    urls = http_host() + api
    my_body = {
        "refreshToken": current_token()
    }
    my_body = json.dumps(my_body)
    rp = requests.post(url=urls, headers=Headers, data=my_body)
    return rp


def http_header():
    head_data = {
      "Content-Type": "application/json",
      "Authorization": get_token(),
      "Connection": "keep-alive",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    return head_data

def http_host():
    my_host = "http://192.168.10.70:5052"
    return my_host

def search_org_list():
    # head = http_header()
    api = '/v1/organization/search'
    urls = http_host() + api
    my_params = {
        'page': 1,
        'pageSize': 100, # 限制为100以内,是每一页显示列表数据条数
        'searchKey': None
    }
    rp = requests.get(headers=http_header(), url=urls, params=my_params)
    # print(rp.json())
    return rp

def search_app_list(orgID):
    # 查询应用列表,返回响应的应用列表
    api = '/v1/application/search/' + str(orgID)
    urls = http_host() + api
    my_params = {
        "page": 1,
        "pageSize": 20,
        "searchKey": ""
    }
    rp = requests.get(headers=http_header(), url=urls, params=my_params)
    return rp

def search_region_list(orgID):
    # 搜索(查询)区域列表
    api = '/v1/region/search/' + str(orgID)
    urls = http_host() + api
    my_params = {
        'page': 1,
        'pageSize': 100,  # 限制为100以内,是每一页显示列表数据条数
        'searchKey': None
    }
    rp = requests.get(headers=http_header(), url=urls, params=my_params)
    return rp

# 平台用户模块
def search_user():
    # 搜索平台用户
    api = '/v1/user/search'
    urls = http_host() + api
    my_params = {
        'page': 1,
        'pageSize': 100,  # 限制为100以内,是每一页显示列表数据条数
        'searchKey': None
    }
    rp = requests.get(url=urls, headers=http_header(), params=my_params)
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    return rp

def search_org_user(org_id):
    # 搜索组织内用户
    api = '/v1/user/organization/search/' + str(org_id)
    urls = http_host() + api
    my_params = {
        'page': 1,
        'pageSize': 100,  # 限制为100以内,是每一页显示列表数据条数
        'searchKey': None
    }
    rp = requests.get(url=urls, headers=http_header(), params=my_params)
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    return rp

def update_username(name):
    # 修改当前平台用户  "姓名"
    api = '/v1/user/userinfo/username/' + str(name)
    urls = host + api
    rp = requests.put(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def update_phone(newphone):
    # 修改当前平台用户  "手机号"
    api = '/v1/user/userinfo/phone/' + str(newphone)
    url = host + api
    rp = requests.put(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
def update_password(new,old):
    # 修改平台用户  "密码"
    api = '/v1/user/userinfo/password'
    urls = host + api
    my_body = {
      "newPassword": new,
      "oldPassword": old
    }
    my_body = json.dumps(my_body)
    rp = requests.put(url=urls, headers=Headers, data=my_body)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200

def update_email(newmail):
    # 修改平台用户    "邮箱"
    api = '/v1/user/userinfo/email/' + str(newmail)
    urls = host + api
    rp = requests.put(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code']

def search_station_list(org_id, reg_id):
    # 搜索(查询)基站列表
    api = '/v1/station/search/' + str(org_id)
    urls = http_host() + api
    my_params = {
        "page": 1,
        "pageSize": 100,
        "regionId": reg_id,
        "searchKey": " "
    }
    rp = requests.get(url=urls, headers=http_header(), params=my_params)
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    # sta_Id是基站id
    snum_id_dict = []
    snum_id_dict = rp.json()['data']
    snum_Id= snum_id_dict['data'][0]['serialNumber']
    return snum_Id

def add_model(type):
    # 添加型号
    api = '/v1/model/' + str(type)
    urls = http_host() + api
    my_body = {
        "description": "新增的通信基站",
        "name": "智能安全帽通信基站2"
    }
    my_body = json.dumps(my_body)
    rp = requests.post(url=urls, headers=http_header(), data=my_body)
    return rp

def search_terminal(app_id,org_id):
    # 搜索终端列表
    api = '/v1/terminal/search'
    urls = http_host() + api
    my_params = {
        "applicationId": app_id,
        "organizationId": org_id,
        "page": 1,
        "pageSize": 100,
        "searchKey": " "
    }
    rp = requests.get(url=urls, headers=http_header(), params=my_params)
    t_id = rp.json()['data']
    t_Id = t_id['data'][0]['serialNumber']
    return t_Id

def search_apikey_list(org_id):
    # 查询apikey列表
    api = '/v1/apikey/search/' + str(org_id)
    urls = http_host() + api
    my_params = {
        "page": 1,
        "pageSize": 100,
        "searchKey": " "
    }
    rp = requests.get(url=urls, headers=http_header())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    api_id = rp.json()['data']
    api_Id = []
    api_Id = api_id['data'][-1]['id'] # 返回最新(新建)的api_id
    return api_Id

def search_http(app_id):
    # 查询http
    api = '/v1/integrate/1/' + str(app_id)
    urls = http_host() + api
    rp = requests.get(url=urls, headers=http_header())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    jc_id = rp.json()['data']
    jc_Id = jc_id['data']['id']
    return jc_Id

def search_mqtt(app_id):
    # 查询应用
    api = '/v1/integrate/mqtt/' + str(app_id)
    urls = http_host() + api
    rp = requests.get(url=urls, headers=http_header())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200
    return rp.json()['data']['id']