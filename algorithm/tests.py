#!/usr/bin/env python
# encoding: utf-8

# 简单测试数据

import random


def int_list_dup(max_range, dup):
    r = 10 ** max_range
    dup = min(r//10, dup) if r > 1 else 1
    return [random.randint(-r//dup, r//dup) for _ in range(r)]


def int_list_dup_sorted(max_range, dup):
    return list(map(sorted, int_list_dup(max_range, dup)))


def int_list_dedup(max_range):
    r = 10 ** max_range
    return random.sample(range(-r, r), r)


def int_list_dedup_sorted(max_range):
    return list(map(sorted, int_list_dedup(max_range)))


if __name__ == '__main__':
    pass

