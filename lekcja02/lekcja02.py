# 2.10
line="""Lorem ipsum dolor       sit amet.
 In amet consequatur                 ut amet praesentium ut dicta autem ea   voluptatibus autem et dolores saepe.
 Ut repellendus aspernatur nam           atque amet est quaerat earum et tempore galisum."""

print("2.10:\nIlosc wyrazow: " + str(len(line.split())))

# 2.11
word="PrzykladowyTekst"

print("\n2.11:\n" + str("_".join(word)))

# 2.12
pierwszeZnaki="".join(slowo[0] for slowo in line.split())
ostatnieZnaki="".join(slowo[-1] for slowo in line.split())

print("\n2.12:\nSlowo z pierwszych znakow: " + pierwszeZnaki)
print("Slowo z ostatnich znakow: " + ostatnieZnaki)
