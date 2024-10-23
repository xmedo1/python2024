roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


# Inny sposob:
# roman_dict = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])


def roman2int(string):
    suma = 0
    previous_value = 0

    for c in reversed(string):
        value = roman_dict[c]
        if value < previous_value:
            suma -= value
        else:
            suma += value
        previous_value = value

    return suma


print(roman2int("MMXXIV"))
print(roman2int("XXV"))
print(roman2int("CXI"))
