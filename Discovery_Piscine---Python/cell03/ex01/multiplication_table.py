#!/usr/bin/env python3

import sys

try:
    n = float(input("Enter a number\n"))
except:
    sys.exit()

if n.is_integer():
    n = int(n)

i = 0
while i <= 9:
    print(i, "x", n, '=', i * n)
    i += 1
