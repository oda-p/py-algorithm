#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import Counter

def avg(nums, length):
    return round(sum(nums)/length)

def mid(nums, length):
    temp = sorted(nums)
    return temp[length//2]

def mode(nums, length):
    counter = Counter(nums)
    most_common = counter.most_common()
    if length > 1 : 
        if most_common[0][1] == most_common[1][1]:
            mod = most_common[1][0]
        else : 
            mod = most_common[0][0]
    else : 
        mod = most_common[0][0]
    
    return mod

def bound(nums):
    return max(nums) - min(nums)



def main():
    length = int(sys.stdin.readline())
    nums = [int(sys.stdin.readline()) for _ in range(length)]
    print(avg(nums, length))
    print(mid(nums, length))
    print(mode(sorted(nums), length))
    print(bound(nums))


if __name__ == "__main__":
    main()