#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    memory = {
        ')': '(', 
        ']': '[' 
    }
    while True:
        string = input()
        if string == '.':
            break

        stack = []
        for chr in string:
            if chr in memory.values():
                stack.append(chr)
                continue

            if chr in memory.keys():
                if stack and stack[-1] == memory[chr]:
                    stack.pop()
                    continue
                stack.append('.')
                break
        if stack:
            print('no')
        else:
            print('yes')



if __name__ == "__main__":
    main()