#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    num = int(input())
    for _ in range(num):
        string = input()
        stack = 0
        for chr in string:
            if chr == '(':
                stack += 1
            else:
                stack -= 1
            if stack < 0:
                break
        if stack == 0:
            print('YES')
        else:
            print('NO')

if __name__ == "__main__":
    main()