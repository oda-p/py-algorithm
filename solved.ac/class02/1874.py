#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Stack:
    
    PUSH = '+'
    POP = '-'
    _arr = []
    _cmd = []

    def peek(self):
        return self._arr[-1]
    
    def push(self, val):
        self._cmd.append(self.PUSH)
        self._arr.append(val)

    def pop(self):
        self._cmd.append(self.POP)
        return self._arr.pop()
    
    def history(self):
        for cmd in self._cmd:
            print(cmd)
def main():
    stack = Stack()
    PUSH = '+'
    POP = '-'
    
    nums = int(input())
    sequence = [int(input()) for _ in range(nums)]

    offset = 1
    for num in sequence:
        while offset <= num:
            stack.push(offset)
            offset += 1

        if stack.peek() != num:
            print('NO')
            return
        
        stack.pop()

    stack.history()

if __name__ == "__main__":
    main()
