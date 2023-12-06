#!/usr/bin/python3
def roman_to_int(roman_string):
    z_number = []
    for z in roman_string:
        if type(roman_string) != str or type(roman_string) is None:
            return 0
        elif z == "i" or z == "I":
            z_number.append(1)
        elif z == "v" or z == "V":
            z_number.append(5)
        elif z == "x" or z == "X":
            z_number.append(10)
        elif z == "l" or z == "L":
            z_number.append(50)
        elif z == "c" or z == "C":
            z_number.append(100)
        elif z == "d" or z == "D":
            z_number.append(500)
        elif z == "m" or z == "M":
            z_number.append(1000)
        else:
            print("Wrong Character")
    return sum(z_number)
