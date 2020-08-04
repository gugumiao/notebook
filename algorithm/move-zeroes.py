#!/usr/bin/env python
# encoding: utf-8
# https://leetcode.com/problems/move-zeroes

from tests import int_list_dup
from time_counter import time_counter


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
        #print(nums)


    @time_counter
    def moveZeroes2(self, nums):
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.append(nums.pop(i))
        #print(nums)


if __name__ == '__main__':
    max_range = 9
    s = Solution()
    for i in range(max_range):
        test = int_list_dup(i, dup=10)
        print(f'测试用例长度: {format(len(test), ",")}')
        s.moveZeroes(test)
        s.moveZeroes2(test)

