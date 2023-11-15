#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    num1, num2 = map(int, input().split())

    if num1 < num2:
        print("<")
    elif num1 == num2:
        print("==")
    else:
        print(">")
        
if __name__ == "__main__":
    main()