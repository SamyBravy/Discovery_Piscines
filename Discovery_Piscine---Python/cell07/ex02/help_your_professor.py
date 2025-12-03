#!/usr/bin/env python3

def average(dictionary):
    sum = 0
    if len(dictionary) == 0:
    	return 0
    for key in dictionary:
        sum += dictionary[key]
    return sum / len(dictionary)

class_3B =      {
                    "marine": 18,
                    "jean": 15,
                    "coline": 8,
                    "luc": 9
                }
class_3C =      {
                    "quentin": 17,
                    "julie": 15,
                    "marc": 8,
                    "stephanie": 13
                }
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
