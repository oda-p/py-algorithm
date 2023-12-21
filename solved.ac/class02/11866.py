#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    n, k = map(int, input().split())
    arr = [num for num in range(1, n+1)]

    tmp = []
    index = 0
    while arr:
        index = (index + k - 1) % len(arr)
        tmp.append(str(arr.pop(index)))

    print(f"<{', '.join(tmp)}>")


if __name__ == "__main__":
    main()