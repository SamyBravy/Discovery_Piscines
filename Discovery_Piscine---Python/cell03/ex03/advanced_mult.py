#!/usr/bin/env python3

import sys

if len(sys.argv) != 1:
    sys.exit("none")

table = 0
while table <= 10:
    print("Table de {table}:", end=" ")
    i = 0
    while i <= 10:
        print(table * i, end=" ")
        i += 1
    if table != 10:
        print("")
    table += 1
