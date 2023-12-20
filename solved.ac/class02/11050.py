#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def combination(n, k):

    if k == 0 or k == n:
        return 1

    return combination(n-1, k-1) + combination(n-1, k)

def main():
    n, k = map(int, input().split())
    result = combination(n, k)
    print(result)

if __name__ == "__main__":
    main()