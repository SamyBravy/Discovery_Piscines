#!/usr/bin/env python3

import sys

if len(sys.argv) - 1 != 2:
    print("none")
    sys.exit()

if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    sys.exit()

array = [n for n in range(int(sys.argv[1]), int(sys.argv[2]) + 1)]
print(array)
