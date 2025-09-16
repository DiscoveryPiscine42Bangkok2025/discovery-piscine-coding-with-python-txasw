#!/usr/bin/env python3

import sys

def shrink(str):
     print(str[:8])

def enlarge(str):
    while len(str) < 8:
        str += 'Z'
    print(str)

if len(sys.argv) == 1:
    print("none")
else:
    for word in sys.argv[1:]:
        if len(word) > 8:
            shrink(word)
        else:
            enlarge(word)