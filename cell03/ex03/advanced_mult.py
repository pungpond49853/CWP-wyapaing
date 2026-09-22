#!/usr/bin/env python3

import sys

if len(sys.argv) != 1:
    print("none")
else:
    table = 0

    while table <= 10:
        number = 0
        line = f"Table de {table}:"

        while number <= 10:
            line += f" {table * number}"
            number += 1

        print(line)
        table += 1