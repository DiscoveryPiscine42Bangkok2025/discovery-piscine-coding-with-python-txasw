#!/usr/bin/env python3

first = input("Enter the first number:\n")
second = input("Enter the second number:\n")
result = int(first) * int(second)
print("{} x {} = {}".format(first, second, result))
if result < 0:
    print("The result is negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is both positive and negative.")