#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_order(docs, docs_count, target_index):

    stack = sorted(docs)
    print_seq = 1
    index = -1
    while stack:

        index = (index + 1) % docs_count
        
        if docs[index] != stack[-1]:
            continue
        
        if index == target_index:
            break

        print_seq += 1
        stack.pop()
        
    print(print_seq)        

    


def main():
    test_case = int(input())

    for _ in range(test_case):
        docs_count, target_index = map(int, input().split())
        docs = list(map(int, input().split()))

        get_order(docs, docs_count, target_index)

if __name__ == "__main__":
    main()