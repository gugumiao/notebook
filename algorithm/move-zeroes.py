#!/usr/bin/env python
# encoding: utf-8
# https://leetcode.com/problems/move-zeroes

from time_counter import time_counter
import random


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
    count = [100*10**i for i in range(6)]
    s = Solution()
    for i in count:
        test = [random.randint(0, 9) for _ in range(i)]
        print(f'测试用例长度: {format(len(test), ",")}')
        s.moveZeroes(test)
        s.moveZeroes2(test)

