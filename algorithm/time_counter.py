#!/usr/bin/env python
# encoding: utf-8

import time


def time_counter(func):
    def wrapper(*args, **kwargs):
        start = time.process_time_ns()
        func(*args, **kwargs)
        end = time.process_time_ns()
        print(f'{func.__name__} 耗时: {format((end-start), ",")} ns')
    return wrapper

