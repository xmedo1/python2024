def sum_seq(sequence):
    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum += sum_seq(item)
        else:
            sum += item
    return sum


sekwencja = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(f"Sekwencja: {sekwencja}")
print(f"Suma sekwencji: {sum_seq(sekwencja)}")
