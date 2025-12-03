#!/usr/bin/env python3

import sys

try:
    age = int(input("Please tell me your age: "))
except:
    sys.exit()

print("You are currently", age, "years old.")
print("In 10 years, you'll be", age + 10, "years old.")
print("In 20 years, you'll be", age + 20, "years old.")
print("In 30 years, you'll be", age + 30, "years old.")
