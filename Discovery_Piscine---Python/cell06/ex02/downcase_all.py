#!/usr/bin/env python3

import sys

def downcase_it(string: str):
    return string.lower()

if len(sys.argv) - 1 == 0:
    print("none")
    sys.exit()

try:
    for argument in sys.argv[1:]:
        print(downcase_it(argument))
except:
    sys.exit()
