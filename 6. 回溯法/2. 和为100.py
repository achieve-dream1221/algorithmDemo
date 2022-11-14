#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 11:24
# @Author  : achieve_dream
# @File    : 2. 和为100.py
# @Software: Pycharm

def print_with_line(*args):
    print(*args, sep='')


def print_no_line(*args):
    print(*args, end='')


def solve(ops: list, sum: int, prev_add: int, a: list, index: int):
    """
    解决从1-9的数字的加减操作使其和为100的方案
    :param ops: 操作符数组
    :param sum: 当前求和
    :param prev_add: 上一次执行的操作数子
    :param a: 1-9的数组
    :param index: 当前的位置索引
    :return:
    """
    if index == len(a):  # 用完所有数字, 则判断最终结果
        if sum == 100:  # 和为100, 则输出解
            print_no_line(a[0])  # 打印第一个数字
            for i in range(1, len(a)):  # 打印剩余的数字
                if ops[i] != " ":  # 不为空则打印操作符
                    print_no_line(ops[i])
                print_no_line(a[i])  # 打印数字
            print_with_line("=100")
        return  # 结束当前方案

    # + 操作
    ops[index] = "+"
    sum += a[index]  # 加上当前的数据
    solve(ops, sum, a[index], a, index + 1)  # 解决下一个数字的状态
    sum -= a[index]  # 回溯, 减去之前加上的数据

    # - 操作
    ops[index] = "-"
    sum -= a[index]  # 减去当前的数据
    solve(ops, sum, -a[index], a, index + 1)  # 解决下一个
    sum += a[index]  # 回溯, 加上减去的数据

    # 空操作, 不在之间加入+或者-
    ops[index] = ' '
    sum -= prev_add
    tmp = prev_add * 10 + (a[index] if prev_add > 0 else -a[index])
    sum += tmp
    solve(ops, sum, tmp, a, index + 1)
    sum -= tmp
    sum += prev_add


if __name__ == '__main__':
    a = [*range(1, 10)]
    ops = [""] * len(a)
    solve(ops, a[0], a[0], a, 1)
