#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# reference
# - https://mlerma54.github.io/problem_solving/solutions/josephus.pdf
# - https://velog.io/@error_io/%EB%B0%B1%EC%A4%80-2164-%EC%B9%B4%EB%93%9C2-Python

import math

def main():
    N = int(input())
    M = 2 ** math.floor(math.log2(N))
    last_card = 2 * (N - M)
    print(last_card if last_card != 0 else N)

if __name__ == "__main__":
    main()