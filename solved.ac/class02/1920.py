#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_exists(arr, length, val):
    start = 0
    end = length - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == val:
            return 1
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid - 1

    return 0
        

def main():
    answers_count = int(input())
    answers = sorted(map(int, input().split()))

    tests_count = int(input())
    tests = list(map(int, input().split()))

    for test in tests:
        print(is_exists(answers, answers_count, test))

if __name__ == "__main__":
    main()
    