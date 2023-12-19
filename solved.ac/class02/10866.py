#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input = sys.stdin.readline
class Deque:

    buffer = []

    def push(self, index, el):
        if index < 0:
            self.buffer.append(el)
        else:
            self.buffer.insert(index, el)
    
    def pop(self, index):
        if not self.buffer:
            print(-1)
            return
        print(self.buffer.pop(index))
    
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
    queue = Deque()

    for _ in range(N):
        command = input().split()
        if command[0] == 'push_front':
            queue.push(0, int(command[1]))
        if command[0] == 'push_back':
            queue.push(-1, int(command[1]))
            
        if command[0] == 'pop_front':
            queue.pop(0)
        if command[0] == 'pop_back':
            queue.pop(-1)
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