#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    MAX_NUMS = 9
    max_num = 0
    max_index = -1
    for i in range(MAX_NUMS):
        num = int(input())
        if max_num < num:
            max_num = num
            max_index = i+1

    print(max_num)
    print(max_index)

if __name__ == "__main__":
    main()

    