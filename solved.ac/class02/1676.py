#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_zero(num):
    cnt = 0

    while num % 10 == 0:
        num //= 10
        cnt += 1
    
    return cnt

def main():
    num = int(input())
    factorial = 1
    total_zero_count = 0
    while num > 0:
        zero_count = count_zero(num)
        total_zero_count += zero_count
        factorial *= num // 10 ** zero_count
        num -= 1

    total_zero_count += count_zero(factorial)

    print(total_zero_count)


def main2():
    num = int(input())

    zero_count = 0
    while num != 0:
        num //= 5
        zero_count += num

    print(zero_count)
    
if __name__ == "__main__":
    main()
