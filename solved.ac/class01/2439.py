#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    stars = int(input())

    for i in range(1, stars+1):
        print(' '*(stars - i) + '*'*(i))

if __name__ == "__main__":
    main()