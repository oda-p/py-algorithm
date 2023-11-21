#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    owned_len_count, split_count = map(int, input().split())
    sizes = [int(input()) for _ in range(owned_len_count)]

    
    start = 1
    end = max(sizes)

    while start <= end:
        mid = (end + start) // 2
        if sum([size // mid for size in sizes]) < split_count:
            end = mid - 1
        else:
            start = mid + 1

    print(end)



if __name__ == "__main__":
    main()