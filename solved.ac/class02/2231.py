#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    num = int(input())
    result = 0
    for n in range(num):
        tmp = n
        sum = n
        
        while tmp > 0:
            sum += tmp % 10
            tmp = int(tmp/10)
        
        if num == sum:
            result = n
            break
        
    print(result)
    

if __name__ == "__main__":
    main()
