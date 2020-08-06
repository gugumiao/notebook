#!/usr/bin/env python
# encoding: utf-8

import time

start = time.perf_counter()
s = ''
for n in range(100000):
    s += str(n)
end = time.perf_counter()
print(f's+=... : {end-start}')


start = time.perf_counter()
l = []
for n in range(100000):
    l.append(str(n))
s = ''.join(l)
end = time.perf_counter()
print(f'..join: {end-start}')

start = time.perf_counter()
s = ''.join(map(str, range(100000)))
end = time.perf_counter()
print(f'map : {end-start}')

