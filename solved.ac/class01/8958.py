#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    TOTAL_TURN = int(input())

    scores = [0] * TOTAL_TURN
    for turn in range(TOTAL_TURN):
        test_case = map(lambda x: len(x), input().split('X'))
        for answer in test_case:
            scores[turn] += int(answer * (answer + 1) / 2)

    for score in scores:
        print(score)
        

if __name__ == "__main__":
    main()