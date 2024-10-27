# Wersja iteracyjna
def odwracanie_iter(L, left, right):
    while left < right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        left += 1
        right -= 1
    return L


# Wersja rekurencyjna
def odwracanie_rek(L, left, right):
    if left >= right:
        return L
    temp = L[left]
    L[left] = L[right]
    L[right] = temp
    return odwracanie_rek(L, left + 1, right - 1)


L = list(range(10))
L_copy = L.copy()

print("Lista odwrocona iteracyjnie:")
odwracanie_iter(L, 2, 5)
print(L)
print("\nLista odwrocona rekurencyjnie:")
odwracanie_rek(L_copy, 2, 5)
print(L_copy)

czy_rowne = L == L_copy
print(f"\nCzy listy sa sobie rowne?: {czy_rowne}")
