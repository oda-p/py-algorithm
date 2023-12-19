#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    num = int(input())

    count = num // 5
    rest = num % 5

    while True:
        if rest % 3 == 0:
            count += rest // 3
            break
        rest += 5
        count -= 1
        if count < 0:
            break
    
    print(count)
    
        
        

if __name__ == "__main__":
    main()