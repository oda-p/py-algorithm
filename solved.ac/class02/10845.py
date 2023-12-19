#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input = sys.stdin.readline
class Queue:

    buffer = []

    def push(self, el):
        self.buffer.append(el)
    
    def pop(self):
        if not self.buffer:
            print(-1)
            return
        print(self.buffer.pop(0))
    
    def size(self):
        print(len(self.buffer))

    def empty(self):
        print(int(not bool(self.buffer)))

    def front(self):
        print(self.buffer[0] if self.buffer else -1)

    def back(self):
        print(self.buffer[-1] if self.buffer else -1)

def main():
    N = int(input())
    queue = Queue()

    for _ in range(N):
        command = input().split()
        if command[0] == 'push':
            queue.push(int(command[1]))
            continue
        if command[0] == 'pop':
            queue.pop()
        if command[0] == 'size':
            queue.size()
        if command[0] == 'empty':
            queue.empty()
        if command[0] == 'front':
            queue.front()
        if command[0] == 'back':
            queue.back()
        

if __name__ == "__main__":
    main()