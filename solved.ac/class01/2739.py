#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    MAX_NUM = 9
    num = int(input())

    for i in range(1, MAX_NUM+1):
        print(f'{num} * {i} = {num * i}')

if __name__ == "__main__":
    main()