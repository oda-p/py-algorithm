#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    for line in sys.stdin:
        nums = map(int, line.split())
        result = sum(nums)
        if result == 0:
            break
        print(result)

if __name__ == "__main__":
    main()