#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    for (num1, num2) in sorted(arr, key=lambda x: (x[1], x[0])):
        print(num1, num2)

if __name__ == "__main__":
    main()