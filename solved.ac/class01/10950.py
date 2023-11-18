#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    turn = int(input())

    for _ in range(turn):
        nums = map(int, input().split())
        print(sum(nums))

if __name__ == "__main__":
    main()