#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if roman_string:
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string[-2:] == 'IX' or roman_string[-2:] == 'IV':
        for i in roman_string[:-2]:
            total += rom[i]
        if roman_string[-2:] == 'IX':
            total += 9
        if roman_string[-2:] == 'IV':
            total += 4
    else:
        for i in roman_string:
            total += rom[i]
    return total
