#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import pytest
import yaml
import os
import sys
path = os.path.dirname(sys.path[0])
import json
from business.common import *

# 调用common.py中http_header,http_host函数获取,,请求头和host
Headers = http_header()
host = http_host()

def test_dashboard():
    # 首页数据面板
    api = '/v1/dashboard'
    urls = host + api
    rp = requests.get(url=urls, headers=Headers)
    print(rp.json())
    assert rp.status_code == 200
    assert rp.json()['code'] == 200