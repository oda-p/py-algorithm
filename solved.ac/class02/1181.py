#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    word_count = int(input())
    bag_of_words = set(input() for _ in range(word_count))

    sorted_bag_of_words = sorted(bag_of_words, key=lambda x: (len(x), x))

    for word in sorted_bag_of_words:
        print(word)

if __name__ == "__main__":
    main()