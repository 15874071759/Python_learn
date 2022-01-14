#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-02 19:28 
# @Author : huff 
# @File : mypy_3.py 
# @Software: PyCharm
import pytest

# @pytest.fixture()  # 默认参数，每个测试方法前调用
# def before():
#    print('before each test')
#    a= 'kk'
#    return a
#
# def test_1(before):
#    print('test_1()')
#    print(before)
#
# @pytest.mark.usefixtures("before")
# def test_2():
#    print('test_2()')
#    print(before)


class Foo(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def echo(self):
        print(self.a, self.b, self.c)
        return True

@pytest.fixture(params=[["1", "2", "3"], ["x", "y", "z"]])
def foo(request):
    return Foo(*request.param)

def test_foo(foo):
    assert foo.echo()