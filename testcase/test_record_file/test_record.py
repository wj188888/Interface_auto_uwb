#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
# from requests.auth import HTTPBasicAuth
import pytest
import os
import sys
path = os.path.dirname(sys.path[0])
import json
import yaml
from business.common import *

# 调用common.py中http_header,http_host函数获取,,请求头和host
Headers = http_header()
host = http_host()

def test_record():
    # 查询操作日志
    api = '/v1/record/search'
    urls = host + api
    my_params = {
        "startTime": "2021-04-16 17:17:05",
        "endTime": "2021-05-12 17:17:05",
        "page": 1,
        "pageSize": 100,
        "searchKey": " "
    }
    rp = requests.get(url=urls, headers=Headers, params=my_params)
    json_rp = json.dumps(rp.json())
    with open('./operate_record.yaml', 'w+', encoding='utf-8') as f:
        yaml.dump(json_rp, f)
    assert rp.status_code == 200
    assert rp.json()['code'] == 200