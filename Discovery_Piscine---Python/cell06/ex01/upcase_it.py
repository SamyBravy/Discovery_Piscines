#!/usr/bin/env python3

import sys

def upcase_it(string: str):
    return string.upper()

try:
    print(upcase_it("hello"))
except:
    sys.exit()
