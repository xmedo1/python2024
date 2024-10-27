def flatten(sequence):
    lista = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            lista.extend(flatten(item))
        else:
            lista.append(item)
    return lista


sekwencja = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(f"Sekwencja: {sekwencja}")
print(f"Splaszczona sekwencja: {flatten(sekwencja)}")
