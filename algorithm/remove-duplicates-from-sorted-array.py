#!/usr/bin/env python
# encoding: utf-8

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


from time_counter import time_counter
from tests import int_list_dup_sorted
from copy import deepcopy


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
    test = int_list_dup_sorted(3, 10)
    test1 = deepcopy(test)
    test2 = deepcopy(test)
    print(test1)
    print(solution1(test1))
    print(test1)
    print(test2)
    print(solution2(test2))
    print(test2)

