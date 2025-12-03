#!/usr/bin/env python3

numbers = [2, 8, 9, 48, 8, 22, -12, 2]
new_numbers = [number + 2 for number in numbers if number > 5]	# potevo usare new_numbers.append(number + 2) in un ciclo for

print(numbers)
print(new_numbers)
