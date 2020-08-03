#!/usr/bin/env python
# encoding: utf-8

import time

start = time.perf_counter()
i = 0
while i < 100000:
    i += 1
end = time.perf_counter()
print(f'while loop: {end-start}')

start = time.perf_counter()
for i in range(100000):
    pass
end = time.perf_counter()
print(f'for loop: {end-start}')


"""
i是int immutable, i += 1 相当于 i = new int(i+1)
range()是C语言写的, 调用速度非常快
"""

