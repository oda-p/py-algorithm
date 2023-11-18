#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    for line in sys.stdin:
        nums = map(int, line.split())
        print(sum(nums))

if __name__ == "__main__":
    main()