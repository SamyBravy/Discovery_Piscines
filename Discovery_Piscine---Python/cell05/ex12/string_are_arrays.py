#!/usr/bin/env python3

import sys, re

if len(sys.argv) - 1 != 1 or len(re.findall('z', sys.argv[1])) == 0:
    print("none")
    sys.exit()

for z in re.findall('z', sys.argv[1]):
    print(z, end='')
