def suma_sekwencji(seq):
    result = []
    for s in seq:
        suma = sum(s)
        result.append(suma)
    return result


sekwencja = [[], [4], [1, 2, 3], (1, 2, 3), [9, 9, 9], (77, 1)]
print(suma_sekwencji(sekwencja))
