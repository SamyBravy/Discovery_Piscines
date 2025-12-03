#!/usr/bin/env python3

import sys, re

if len(sys.argv) - 1 != 2:
    print("none")
    sys.exit()

n = len(re.findall(sys.argv[1], sys.argv[2]))

if n == 0:
    print("none")
else:
    print(n)
