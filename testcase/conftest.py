#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
import requests
# @pytest.fixture(scope='function')

# def pytest_collection_modifyitems(items):
#     """
#     测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
#     :return:
#     """
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         print(item.nodeid)
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

# @pytest.fixture(scope="module")
# def setup():
#     print("--------开始执行用例-----------")
#
# @pytest.fixture(scope="module")
# def teardown():
#     print("--------结束执行用例-----------")
# def test_authorization_login1():
#     # 账户登录,正用例
#     api = '/v1/authorization/login'
#     urls = host + api
#     my_body = {
#       "name": '16855541122',
#       "password": '12345678'
#     }
#     my_body = json.dumps(my_body)
#     rp = requests.request(method='post', url=urls, headers=Headers, data=my_body)