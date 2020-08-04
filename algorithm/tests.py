#!/usr/bin/env python
# encoding: utf-8

# 测试数据

import random

def ranges(max_range):
    return [1*10**i for i in range(max_range)]


def int_list_dup(max_range):
    r = ranges(max_range)
    tests = [[random.randint(0, max(10, r[i]//10)) for _ in range(r[i])] for i in range(len(r))]
    return tests


def int_list_dup_sorted(max_range):
    return list(map(sorted, int_list_dup(max_range)))


def int_list_dedup(max_range):
    pass


def int_list_dedup_sorted(max_range):
    pass


if __name__ == '__main__':
    print(int_list_dup(4))
    print(int_list_dup_sorted(4))

