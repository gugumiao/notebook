#!/usr/bin/env python
# encoding: utf-8
# https://leetcode-cn.com/problems/move-zeroes
from time_counter import time_counter


class Solution(object):

    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    @time_counter
    def moveZeroes(self, nums):
        pass


    @time_counter
    def moveZeroes2(self, nums):
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.append(nums.pop(i))
        print(nums)


if __name__ == '__main__':
    test = [0, 1, 0, 3, 12]
    s = Solution()
    s.moveZeroes(test)
    s.moveZeroes2(test)

