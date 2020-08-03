#!/usr/bin/env python
# encoding: utf-8

import time


def time_counter(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        func(*args, **kwargs)
        end = time.perf_counter_ns()
        print(f'{func.__name__} 耗时: {end-start}ns')
    return wrapper

