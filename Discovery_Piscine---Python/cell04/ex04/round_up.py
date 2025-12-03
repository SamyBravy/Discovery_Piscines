#!/usr/bin/env python3

import sys, math

try:
    n = float(input("Give me a number: "))
except:
    sys.exit()

n = math.ceil(n)
print(n)
