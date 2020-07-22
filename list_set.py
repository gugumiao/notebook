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
start_using_list = time.perf_counter()
find_unique_price_using_list(products)
end_using_list = time.perf_counter()
print("time elapse using list: {}".format(end_using_list - start_using_list))


# 计算集合版本的时间
start_using_set = time.perf_counter()
find_unique_price_using_set(products)
end_using_set = time.perf_counter()
print("time elapse using set: {}".format(end_using_set - start_using_set))

