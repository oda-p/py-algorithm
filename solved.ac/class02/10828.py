#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input = sys.stdin.readline
class Stack:

    buffer = []

    def push(self, el):
        self.buffer.append(el)
    
    def pop(self):
        if not self.buffer:
            print(-1)
            return
        print(self.buffer.pop())
    
    def size(self):
        print(len(self.buffer))

    def empty(self):
        print(int(not bool(self.buffer)))

    def top(self):
        print(self.buffer[-1] if self.buffer else -1)

def main():
    N = int(input())
    stack = Stack()

    for _ in range(N):
        command = input().split()
        if command[0] == 'push':
            stack.push(int(command[1]))
            continue
        if command[0] == 'pop':
            stack.pop()
        if command[0] == 'size':
            stack.size()
        if command[0] == 'empty':
            stack.empty()
        if command[0] == 'top':
            stack.top()
        

if __name__ == "__main__":
    main()