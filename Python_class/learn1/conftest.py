#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-03-24 17:21 
# @Author : huff 
# @File : conftest.py 
# @Software: PyCharm
import pytest

@pytest.fixture(scope="function")
def aa():
    a = 1
    return a