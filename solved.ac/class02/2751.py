#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input = sys.stdin.readline
print = sys.stdout.write

def main():
    count = int(sys.stdin.readline())
    nums = [int(input()) for _ in range(count)]    

    for i in sorted(nums):
        print(str(i)+'\n')
if __name__ == "__main__":
    main()
