#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    n, m, b = map(int, sys.stdin.readline().rstrip().split())
    
    land = []
    
    for _ in range(n):
        tmp = list([int(i) for i in sys.stdin.readline().rstrip().split()])
        assert len(tmp) == m
        land.append(tmp)

    min_count = int(1e9)
    min_floor = min([min(floor) for floor in land])
    max_floor = max([max(floor) for floor in land])

    for floor in range(min_floor, max_floor+1):
        used_block = 0
        inventory = 0
        for row in range(n):
            for col in range(m):
                block = land[row][col]
                if block > floor:
                    inventory += block - floor
                else:
                    used_block += floor - block
        
        if used_block > inventory + b:
            continue
        
        
        count = inventory * 2 + used_block
        if count <= min_count:
            min_count = count
            max_floor = floor

    print(min_count, max_floor)
    
if __name__ == "__main__":
    main()