#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_num = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    numbers = []
    for char in roman_string:
        numbers.append(roman_num[char])
    if len(roman_string) == 1:
        return numbers[0]
    res = 0
    fnum = 0
    snum = 0
    for fnum, snum in zip(numbers, numbers[1:]):
        if fnum >= snum:
            res += fnum
        else:
            res -= fnum
    return res + snum
