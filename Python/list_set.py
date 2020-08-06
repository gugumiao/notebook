#!/usr/bin/env python
# encoding: utf-8

import time

id = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(id, price))


def find_unique_price_using_list(product):
    unique_price_list = []
    for _, price in products:
        if price not in unique_price_list:
            unique_price_list.append(price)
    return len(unique_price_list)


def find_unique_price_using_set(product):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)


# 计算列表版本的时间
start = time.perf_counter()
find_unique_price_using_list(products)
end = time.perf_counter()
print(f'time elapse using list: {end-start}')


# 计算集合版本的时间
start = time.perf_counter()
find_unique_price_using_set(products)
end = time.perf_counter()
print(f'time elapse using set: {end-start}')

