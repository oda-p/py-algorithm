#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def round(val):
  if val - int(val) >= 0.5:
    return int(val)+1
  else:
    return int(val)

def main():
    count = int(sys.stdin.readline().rstrip())
    drop_count = round(count * 0.15)
    if count <= drop_count * 2:
       print(0)
       return

    nums = []
    for _ in range(count):
        nums.append(int(sys.stdin.readline().rstrip()))

    
    if drop_count > 0:
        nums = sorted(nums)[drop_count:-drop_count]
        
    print(round(sum(nums)/len(nums)))

if __name__ == "__main__":
    main()