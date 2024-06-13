#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fizzbuzz(num:int):
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return str(num)

def main():
    num = 0
    for i in range(3):
        value = input()
        if value.isdigit():
            num = int(value)
        else:
            num += 1
    print(fizzbuzz(num+1))

if __name__ == "__main__":
    main()