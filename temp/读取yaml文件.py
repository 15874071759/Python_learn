#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2/24/22 6:25 PM 
# @Author : huff 
# @File : 读取yaml文件.py 
# @Software: PyCharm

import yaml
import random
import string


def get_data_yaml(test_data_path):
    """从yaml文件获取数据，转换成list返回"""
    case = []  # 存储测试用例名称
    param = []  # 存储测试数据
    # expected = [] #存储预期结果

    with open(test_data_path, 'r', encoding='utf-8') as f:
        file_data = f.read()
    # file = open(test_data_path, 'r', encoding= 'utf-8')
    # file_data = file.read()
    # file.close()

    data = yaml.load(file_data, Loader=yaml.FullLoader)

    test = data['tests']
    for i in test:
        case.append(i.get('case'))
        param.append(i.get('params'))
        # expected.append(i.get('expected'))
    # parameters = zip(case, param, expected)
    parameters = zip(case, param)
    param = list(parameters)
    return param
    # return case, param
    # return case, param, expected


if __name__ == '__main__':
    file_path = './testYaml.yaml'
    param = get_data_yaml(file_path)
    print(param)
