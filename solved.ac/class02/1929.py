#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    start, end = map(int, input().split())
    tmp = [i > 1 for i in range(end+1)]

    for num in range(2, int(end ** 0.5) + 1):
        for non_prime in range(2*num, end + 1, num):
            tmp[non_prime] = False

    for num in range(start, end + 1):
        if tmp[num]:
            print(num)


if __name__ == "__main__":
    main()
        