#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    parameters = sys.argv[1:]

    print(f"parameters: {len(parameters)}")

    for parameter in parameters:
        print(f"{parameter}: {len(parameter)}")