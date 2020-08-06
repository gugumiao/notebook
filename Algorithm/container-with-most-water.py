#!/usr/bin/env python
# encoding: utf-8
# https://leetcode.com/problems/container-with-most-water/

from typing import List
from time_counter import time_counter
from tests import int_list_dup


@time_counter
def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        if height[left] < height[right]:
            max_area = max(height[left] * (right-left), max_area)
            left += 1
        else:
            max_area = max(height[right] * (right-left), max_area)
            right -= 1

    return max_area


if __name__ == '__main__':
    height = [abs(i) for i in int_list_dup(1)]
    print(height)
    print(maxArea(height))

