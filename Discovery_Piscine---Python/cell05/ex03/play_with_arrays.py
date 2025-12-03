#!/usr/bin/env python3

numbers = [2, 8, 9, 48, 8, 22, -12, 2]
new_numbers = {number + 2 for number in numbers if number > 5}	# e' come scrivere new_numbers = set(number + 2 for number in numbers if number > 5)

print(numbers)
print(new_numbers)
