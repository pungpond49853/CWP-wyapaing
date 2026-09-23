#!/usr/bin/env python3

import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    while len(string) < 8:
        string += "Z"
    print(string)

if len(sys.argv) == 1:
    print("none")
else:
    for parameter in sys.argv[1:]:
        if len(parameter) > 8:
            shrink(parameter)
        elif len(parameter) < 8:
            enlarge(parameter)
        else:
            print(parameter)