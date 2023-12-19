#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    cards = list(map(int, input().split()))
    M = int(input())
    own_cards = list(map(int, input().split()))

    memory = {}
    for card in cards:
        if card not in memory:
            memory[card] = 0
        memory[card] += 1

    for card in own_cards:
        print(memory.get(card, 0), end=' ')
        

if __name__ == "__main__":
    main()