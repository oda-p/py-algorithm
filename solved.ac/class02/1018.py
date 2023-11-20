#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    player = ('W', 'B')
    ROW, COL = 8, 8
    white_first = [[player[i%2] for i in range(r%2, COL+r%2)] for r in range(ROW)]
    black_first = [[player[i%2] for i in range(r%2, COL+r%2)] for r in range(1,ROW+1)]
    
    input_row, input_col = map(int, input().split())

    board = [[cell for cell in input()] for _ in range(input_row)]


    min_changed = 50 * 50
    for i in range(input_row - ROW+1):
        for j in range(input_col - COL+1):
            changed_count_white_first = 0
            changed_count_black_first = 0
            for r in range(ROW):
                for c in range(COL):
                    if white_first[r][c] != board[r+i][c+j]:
                        changed_count_white_first += 1
                    if black_first[r][c] != board[r+i][c+j]:
                        changed_count_black_first += 1
            min_changed = min(min_changed, changed_count_white_first, changed_count_black_first)
    
    print(min_changed)

if __name__ == "__main__":
    main()