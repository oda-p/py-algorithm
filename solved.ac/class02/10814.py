#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    counts = int(input())
    memory = []
    for i in range(counts):
        el = input().split()
        memory.append((int(el[0]), el[1], i))
    memory.sort(key=lambda x: (x[0], x[2]))
    for m in memory:
        print(m[0], m[1])
        


if __name__ == "__main__":
    main()