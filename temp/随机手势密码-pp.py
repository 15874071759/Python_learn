#!/usr/bin/env python3

"""
输入位数（1-9），生成9宫格密码，要求
1. 数字只能相邻
2. 不可重复

思路：
正向推导时，有可能随机取数时因重复导致重算，所以考虑：
1. 算出1-9位的所有可用密码
2. 输入位数后从对应的密码中随机返回一个

"""

import random
import argparse


# 每个数字和可用的相邻数字，分"可走对角"和"不走对角"两种方式

# 不走对角使用：
# base_dict = {1: [2, 4], 2: [1, 3, 5], 3: [2, 6], 4: [1, 5, 7], 5: [2, 4, 6, 8],
#              6: [3, 5, 9], 7: [4, 8], 8: [5, 7, 9], 9: [6, 8]}
# 可走对角使用：
base_dict = {1: [2, 4, 5], 2: [1, 3, 4, 5, 6], 3: [2, 5, 6], 4: [1, 2, 5, 7, 8], 5: [1, 2, 3, 4, 6, 7, 8, 9],
             6: [2, 3, 5, 8, 9], 7: [4, 5, 8], 8: [4, 5, 6, 7, 9], 9: [5, 6, 8]}


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('-l', '--long', type=int, default=4, help="定义密码长度")
    return p.parse_args()


def make_one():
    """
    1位密码就是1-9随机选一个数
    """
    pw = [[i] for i in range(1, 10)]
    return pw


def make_more(pre_pw):
    """
    2位和以上的密码，依赖前一次生成的密码，最后一位相邻的所有组合
    然后排重
    """
    pw_dup = []

    for i in pre_pw:
        for j in base_dict[i[-1]]:
            temp = i[:]
            temp.append(j)
            pw_dup.append(temp)

    pw = [i for i in pw_dup if len(set(i)) == len(i)]  # 去重

    return pw


def make_all_pw():
    """
    循环将生成所有位数的密码并存为dict
    """
    all_pw = dict()
    all_pw[1] = make_one()
    for i in range(2, 10):
        all_pw[i] = make_more(all_pw[i-1])

    return all_pw


def main():

    args = parse_args()
    pw_l = args.long

    if 0 < pw_l < 10:
        my_all_pw = make_all_pw()
        my_pw = random.choice(my_all_pw[pw_l])
        print("".join(str(i) for i in my_pw))
    else:
        print("错误的位数")


if __name__ == '__main__':
    main()
