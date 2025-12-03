#!/usr/bin/env python3

import sys

try:
    n1 = float(input("Give me the first number: "))
    n2 = float(input("Give me the second number: "))
except:
    sys.exit()

if n1.is_integer():
    n1 = int(n1)
if n2.is_integer():
    n2 = int(n2)

print("Thank you!")
print(n1, "+", n2, "=", n1 + n2)
print(n1, "-", n2, "=", n1 - n2)
result = n1 / n2
if result.is_integer():
    result = int(result)
print(n1, "/", n2, "=", result)
print(n1, "*", n2, "=", n1 * n2)
