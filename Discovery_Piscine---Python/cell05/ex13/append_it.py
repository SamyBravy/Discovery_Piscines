#!/usr/bin/env python3

import sys, re

if len(sys.argv) - 1 == 0:
    print("none")
    sys.exit()

for argument in sys.argv[1:]:
    if not re.search("ism$", argument):
        print(argument + "ism")
