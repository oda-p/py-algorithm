#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# nCr = n-1Cr + n-1Cr-1

# TODO: 다양한 방식의 순열 조합 구현방법 숙지 필요

def nested_for_loop(arr: list, length: int, maximum: int):
    result = 0
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                value = arr[i]+arr[j]+arr[k]
                if value > maximum:
                    continue
                else:
                    result = max(result, value)
    return result

def main():
    length, maximum = map(int, input().split())
    arr = list(map(int, input().split()))
    result = nested_for_loop(arr, length, maximum)
    print(result)

if __name__ == "__main__":
    main()
    assert nested_for_loop([93, 181, 245, 214, 315, 36, 185, 138, 216, 295], 10, 500) == 497
    assert nested_for_loop([5, 6, 7, 8, 9], 5, 21) == 21