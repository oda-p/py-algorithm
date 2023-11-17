#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    UNICODE_A = 97
    alphabets = [-1]*26

    text = input()
    length = len(text)
    unique_cnt = 0

    for i in range(length):
        alphabet_unicode = ord(text[i]) - UNICODE_A
        if alphabets[alphabet_unicode] < 0:
            alphabets[alphabet_unicode] = i
            unique_cnt += 1
        if unique_cnt == 26:
            break

    for alphabet in alphabets:
        print(alphabet, end=' ')


if __name__ == "__main__":
    main()