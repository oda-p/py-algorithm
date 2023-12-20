#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    MAX = 10001
    size = int(input())
    tmp = [0 for _ in range(MAX)]

    for _ in range(size):
        index = int(sys.stdin.readline())
        tmp[index] += 1
    
    for num in range(MAX):
        if tmp[num] < 0:
            continue
        for _ in range(tmp[num]):
            print(num)


if __name__ == "__main__":
    main()
