#!/usr/bin/env python3

import sys

try:
    n = float(input("Give me a number: "))
except:
    sys.exit()

if n.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
