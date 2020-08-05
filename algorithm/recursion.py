#!/usr/bin/env python
# encoding: utf-8

def recursion(level, *args):
    # 1. terminator
    if level > MAX_LEVEL:
        return result

    # 2. current level
    process(level, *args)

    # 3. level+1
    recursion(level+1, *args)

    # 4. do sth. if needed

