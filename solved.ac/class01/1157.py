#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    UNICODE_A = ord('A')
    ALPHABET_COUNT = 26
    alphabet_counter = [0] * ALPHABET_COUNT
    word = map(lambda x: ord(x) - UNICODE_A, input().upper())

    tmp = 0
    for alphabet in word:
        alphabet_counter[alphabet] += 1
        if tmp < alphabet_counter[alphabet]:
            tmp = alphabet_counter[alphabet]
    
    max_count = 0
    most_used_alphabet = ''
    for i in range(ALPHABET_COUNT):
        if alphabet_counter[i] == tmp:
            max_count += 1
            most_used_alphabet = chr(i+UNICODE_A)
    
    print(most_used_alphabet if max_count == 1 else '?')

if __name__ == "__main__":
    main()
    
        
