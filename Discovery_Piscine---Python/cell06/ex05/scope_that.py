#!/usr/bin/env python3

def add_one(number):
    number += 1

n = 42
print(n)
add_one(n)
print(n)    # uguale perché la funzione modifica n solo all'interno di sé stessa
