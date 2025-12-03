#!/usr/bin/env python3

import sys

n1 = input("Enter the first number:\n")
n2 = input("Enter the second number:\n")
try:
    res = float(n1) * float(n2)
except:
    sys.exit()

if res.is_integer():
    res = int(res)
print(n1, "x", n2, '=', res)
if res < 0:
    print("The result is negative.")
elif res > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")
