#!/usr/bin/env python3

num = input("Give me a number: ")
if float(num) == int(float(num)):
    print("This number is an integer.")
else:
    print("This number is a decimal.")