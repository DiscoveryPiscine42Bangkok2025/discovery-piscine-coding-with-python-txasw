#!/usr/bin/env python3

def add_one():
    global num
    num += 1

num = 0
print(num)
add_one()
print(num)