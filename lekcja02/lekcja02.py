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

# 2.17
slowa = line.split()
posortowaneAlfabetycznie = sorted(slowa,key=str.lower)
posortowaneDlugoscia = sorted(slowa,key=len)

print("\n2.17\nTekst posortowany alfabetycznie:\n" + str(" ".join(posortowaneAlfabetycznie)))
print("Tekst posortowany pod wzgledem dlugosci slow:\n" + str(" ".join(posortowaneDlugoscia)))

# 2.18

duzaLiczba = 372175000923810205017050024812094
iloscZer = str(duzaLiczba).count('0')

print("\n2.18\nLiczba: " + str(duzaLiczba))
print("Ilosc zer w tej liczie: " + str(iloscZer))

# 2.19
L = [312,61,38,8,395,613,666,373,213,7,633,991,123,321]
# wyraz oddzielony kropkami dla lepszej czytelnosci
wyraz = ".".join(str(liczba).zfill(3) for liczba in L)

print("\n2.19\nWyraz z 3-cyfrowych blokow: " + str(wyraz))