#!/usr/bin/env python3

import sys

if len(sys.argv) - 1 == 0:
    print("none")
    sys.exit()

print("parameters:", len(sys.argv) - 1)
for parameter in sys.argv[1:]:
    print(parameter + ':', len(parameter))
