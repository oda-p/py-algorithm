#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    asc, desc, top = map(int, input().split())

    top -= asc

    degree = asc - desc
    count = top // degree + 1
    if top % degree > 0:
        count += 1
    
    print(count)



if __name__ == "__main__":
    main()