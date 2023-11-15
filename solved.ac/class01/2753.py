#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    year = int(input())

    print(int(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)))

if __name__ == "__main__":
    main()