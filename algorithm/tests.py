#!/usr/bin/env python
# encoding: utf-8

# 简单测试数据

import random


def int_list_dup(max_range, dup=1, is_sort=False):
    r = 10 ** max_range
    dup = min(r//10, dup) if r > 1 else 1
    l = [random.randint(-r//dup, r//dup) for _ in range(r)]
    return sorted(l) if is_sort else l


def int_list_dedup(max_range, is_sort=False):
    r = 10 ** max_range
    l = random.sample(range(-r, r), r)
    return sorted(l) if is_sort else l


if __name__ == '__main__':
    pass

