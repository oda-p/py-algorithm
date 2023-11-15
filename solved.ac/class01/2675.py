#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    tries = int(input())

    buffer = []
    for _ in range(tries):
        repeat, string = input().split()
        tmp = ''
        for char in string:
            tmp += char * int(repeat)
        buffer.append(tmp)

    for b in buffer:
        print(b)

if __name__ == "__main__":
    main()