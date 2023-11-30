#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input = sys.stdin.readline

def main():
    MAX_ADDRESS = 14

    test_case = int(input())
    for _ in range(test_case):
        apartment = [[number for number in range(1, MAX_ADDRESS+1)] for _ in range(2)]
        FLOOR = int(input())
        ADDRESS = int(input())

        for floor in range(FLOOR+1):
            for address in range(ADDRESS):
                apartment[(floor+1)%2][address] = sum(apartment[floor%2][:address+1])
        
        print(apartment[FLOOR%2][ADDRESS-1])



if __name__ == "__main__":
    main()
