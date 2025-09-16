#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    found = False
    for c in list(sys.argv[1]):
        if c == 'z' :
            print('z', end='')
            found = True
    if not found:
        print("none")
    print()