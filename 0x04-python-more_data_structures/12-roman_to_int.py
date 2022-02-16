#!/usr/bin/python3


def roman_to_int(rom_str):
    if rom_str and type(rom_str) is str:
        ro_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for j in range(len(rom_str)):
            if j > 0 and ro_num[rom_str[j]] > ro_num[rom_str[j - 1]]:
                sum += ro_num[rom_str[j]] - 2 * ro_num[rom_str[j - 1]]
            else:
                sum += ro_num[rom_str[j]]
        return sum
    return (0)
