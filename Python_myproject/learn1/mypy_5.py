#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-17 15:16 
# @Author : huff 
# @File : mypy_5.py 
# @Software: PyCharm
import pytest
# a = [{'a','b'}, ('b'), ('c')]
# b = [{'a','b'}, ('b')]
# print(set(a))
# print(set(a).intersection(set(b)))

# a={1,"ok",[1,2]}
# print(a)

# 增加可读性
data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]

# ids
#ids = ["a:{} + b:{} = expect:{}".format(a, b, expect) for a, b, expect in data_1]


@pytest.mark.parametrize('a, b, expect', data_1, ids=['1','2'])
class TestParametrize(object):

    def test_parametrize_1(self, a, b, expect):
        print('测试函数1测试数据为{}-{}'.format(a, b))
        assert a + b == expect

    def test_parametrize_2(self, a, b, expect):
        print('测试函数2数据为{}-{}'.format(a, b))
        assert a + b == expect