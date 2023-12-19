#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    counts = int(input())
    stack = []
    for _ in range(counts):
        num = int(input())
        if num > 0:
            stack.append(num)
        else:
            stack.pop()
    print(sum(stack))


if __name__ == "__main__":
    main()