#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    series = int(input())
    end_number = '666'
    title = 665

    while series:
        title += 1
        if end_number in str(title):
            series -= 1

    print(title)

if __name__ == "__main__":
    main()
