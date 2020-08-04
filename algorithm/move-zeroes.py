#!/usr/bin/env python
# encoding: utf-8
# https://leetcode.com/problems/move-zeroes

from tests import int_list_dup
from time_counter import time_counter
from copy import deepcopy

class Solution(object):

    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    @time_counter
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


    @time_counter
    def moveZeroes2(self, nums):
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.append(nums.pop(i))


if __name__ == '__main__':
    max_range = int(input('max_range 测试数组长度位数(1-9 9=亿): '))
    dup = int(input('dup 数组重复度(min(len(array)//10, dup)): '))
    s = Solution()
    for i in range(max_range):
        print(f'测试用例长度: {format(10**i, ",")}')
        test = int_list_dup(i, dup)
        test1 = deepcopy(test)
        test2 = deepcopy(test)
        s.moveZeroes(test1)
        s.moveZeroes2(test2)

