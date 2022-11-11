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
    if index == len(a):
        if sum == 100:  # 和为100, 则输出解
            print_no_line(a[0])
            for i in range(1, len(a)):
                if ops[i] != " ":
                    print_no_line(ops[i])
                print_no_line(a[i])
            print_with_line("=100")
        return
    ops[index] = "+"
    sum += a[index]
    solve(ops, sum, a[index], a, index + 1)
    sum -= a[index]

    ops[index] = "-"
    sum -= a[index]
    solve(ops, sum, -a[index], a, index + 1)
    sum += a[index]

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
