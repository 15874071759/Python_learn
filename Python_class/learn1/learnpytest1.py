#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020-10-30 16:13 
# @Author : huff 
# @File : learn_pytest_1.py 
# @Software: PyCharm

import requests
import pytest
from config.settings import HTTP_HOST,HEADERS

@pytest.fixture()
def con_db():
    print('预处理')
    yield
    print('后处理')

#@pytest.mark.skip
def test_withdraw_banks():
    url = HTTP_HOST + '/v1/portfolio/withdraw/banks'
    payload = {}
    headers = HEADERS
    try:
        response = requests.request("GET", url, headers=headers, data=payload, allow_redirects=False)
        print(response.json())
        print(response.json()['code'])
        print(response.status_code)
        assert response.status_code == 200
        assert response.json()['code'] == 0
   # except BaseException as e:
    except AssertionError as e:
        print(e)
        raise

#@pytest.mark.skip
def test_func1():
    # with pytest.raises(Exception):
    #     assert 1 == 2
    try:
        assert 200 == 200
   # except BaseException as e:
    except AssertionError as e:
        print(e)
        raise

#test_withdraw_banks()

