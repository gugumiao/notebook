#!/usr/bin/env python
# encoding: utf-8

#https://leetcode.com/problems/generate-parentheses/

from time_counter import time_counter


def solution1(n):

    def add(left, right, p):
        if left == n and right == n:
            result.append(p)
        if left < n:
            p += '('
            left += 1
            add(left, right, p)
        if right < left:
            p += ')'
            right += 1
            add(left, right, p)

    result = []
    add(0, 0, '')
    return result


if __name__ == '__main__':
    print(solution1(3))

