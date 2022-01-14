#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-04 19:08 
# @Author : huff 
# @File : learn_allure.py 
# @Software: PyCharm

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-01-29 11:05
# @Author : huff
# @File : test_withdraw_banks.py
# @Software: PyCharm

import pytest
from models.bankcards.withdraw_cards import WithdrawCardsClient
import allure

@pytest.fixture()
def param():
    print('预处理')
    yield
    print('后处理')

#获取区域银行卡
#@pytest.mark.skip
@allure.feature('银行卡模块')
@allure.story('区域银行卡查询')
@allure.title("用例标题2")
@allure.description('简单测试一下')
@allure.step('调用withdraw_banks,请求cannary环境银行区域信息')
@allure.issue('http://baidu.com', name='点击我跳转百度')
@allure.testcase('http://bug.com/user-login-Lw==.html', name='点击我跳转禅道')
def test_withdraw_banks():
    payload = {}
    try:
        temp = WithdrawCardsClient()
        res = temp.query_withdraw_banks(payload=payload)
        print(res.json())
        assert res.status_code == 200
        assert res.json()['code'] == 0
    except AssertionError as e:
        print(e)
        raise

#test_withdraw_banks()
# if __name__ == '__main__':
#     test_withdraw_banks()
