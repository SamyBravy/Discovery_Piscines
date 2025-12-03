#!/usr/bin/env python3

import sys

try:
    n = int(input("Enter a number less than 25\n"))
except:
    sys.exit()

if n > 25:
    print("Error")
    sys.exit()

while n <= 25:
    print("Inside the loop, my variable is", n)
    n += 1
