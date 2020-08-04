#!/usr/bin/env python
# encoding: utf-8

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


from time_counter import time_counter
import random


@time_counter
def solution1(nums):
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            nums.pop(i)
    return len(nums)


@time_counter
def solution2(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1


if __name__ == '__main__':
    count = [1*10**i for i in range(9)]
    for i in count:
        test = [random.randint(0, 10) for _ in range(i)]
        test.sort()
        print(f'测试用例长度: {format(len(test), ",")}')
        solution1(test)
        solution2(test)

