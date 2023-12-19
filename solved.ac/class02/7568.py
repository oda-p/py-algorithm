#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def compare(a: tuple, b: tuple) -> bool:
    return a[0] < b[0] and a[1] < b[1]

def main():
    num = int(input())
    peoples = [tuple(map(int, input().split())) for _ in range(num)]

    for people in peoples:
        rank = 1
        for comparator in peoples:
            if compare(people, comparator):
                rank += 1
        print(rank, end=' ')
        


if __name__ == "__main__":
    main()