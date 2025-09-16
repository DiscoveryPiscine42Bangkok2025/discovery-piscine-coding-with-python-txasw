#!/usr/bin/env python3

chars = list(input())
for i in range(len(chars)):
    if chars[i].isupper():
        print(chars[i].lower(), end="")
    elif chars[i].islower():
        print(chars[i].upper(), end="")
    else:
        print(chars[i], end="")