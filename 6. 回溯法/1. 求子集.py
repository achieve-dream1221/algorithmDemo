#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 10:18
# @Author  : achieve_dream
# @File    : 1. 求子集.py
# @Software: Pycharm

def print_line():
    """
    打印分割行
    :return:
    """
    print("-" * 40)


def print_result(a: list, x: list):
    """
    打印满足条件的子集
    :param a: 求解的数组
    :param x: 是否选中的状态数组
    :return:
    """
    print_line()
    result = []
    for i in range(len(a)):
        if x[i] == 1:
            result.append(a[i])
    print(result)


def dfs(a: list, i: int, x: list):
    """
    深度优先遍历搜索子集树
    :param a: 求解数组
    :param i: 下标
    :param x: 状态数组
    :return:
    """
    if i >= len(a):  # 结束条件
        print_result(a, x)
    else:  # 深度遍历搜索
        x[i] = 0  # 不选择当前元素
        dfs(a, i + 1, x)
        x[i] = 1  # 选择当前元素
        dfs(a, i + 1, x)


if __name__ == "__main__":
    a = [*range(1, 4)]  # 1, 2, 3
    x = [0] * len(a)  # 子集树: 是否选择0, 1 初始均为0
    print("求解集合: ", a)
    dfs(a, 0, x)
