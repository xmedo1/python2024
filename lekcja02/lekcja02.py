# 2.10
line="""Lorem ipsum dolor       sit amet.
 In amet consequatur                 ut amet praesentium ut dicta autem ea   voluptatibus autem et dolores saepe.
 Ut repellendus aspernatur nam           atque amet est quaerat earum et tempore galisum.
 GvR"""
print("Tekst:\n" + line)
print("\n2.10:\nIlosc wyrazow: " + str(len(line.split())))

# 2.11
word="PrzykladowyTekst"

print("\n2.11:\n" + str("_".join(word)))

# 2.12
pierwszeZnaki="".join(slowo[0] for slowo in line.split())
ostatnieZnaki="".join(slowo[-1] for slowo in line.split())

print("\n2.12:\nSlowo z pierwszych znakow: " + pierwszeZnaki)
print("Slowo z ostatnich znakow: " + ostatnieZnaki)

# 2.13
sumaDlgWyrazow = sum(len(slowo) for slowo in line.split())

print("\n2.13\nLaczna dlugosc napisow w line: " + str(sumaDlgWyrazow))

# 2.14
najdluzszeSlowo = max(line.split(),key=len)

print("\n2.14\nNajdluzsze slowo w line: " + najdluzszeSlowo)
print("Dlugosc tego slowa: " + str(len(najdluzszeSlowo)))

# 2.15
L=list(range(1,10))
print("\n2.15\nLista: " + str(L))
print("Slowo z elementow listy: " + str("".join(str(liczba) for liczba in L)))

# 2.16
kopia = str(line)
kopia = kopia.replace("GvR","Guido van Rossum")

print("\n2.16\nTekst z zastapionym GvR:\n" + kopia)
