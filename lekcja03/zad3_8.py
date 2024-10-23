def sekwencja(str1, str2):
    # zbiory zapewniaja unikalnosc elementow oraz zdefiniowane operacje sumy i iloczynu zbiorow
    zbior1 = set(str1)
    zbior2 = set(str2)

    mutual_elements = list(zbior1 & zbior2)
    all_elements = list(zbior1 | zbior2)

    print(f"Wspolne elementy: {mutual_elements}")
    print(f"Wszystkie elementy: {all_elements}")


seq1 = input("Podaj pierwsza sekwencje liczb lub znakow: ")
seq2 = input("Podaj druga sekwencje liczb lub znakow: ")
sekwencja(seq1, seq2)
