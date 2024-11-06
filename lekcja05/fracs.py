# Zadanie 5.2

def gcd(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    return abs(a)


def simplify(frac):
    licznik = frac[0]
    mianownik = frac[1]
    if mianownik < 0:
        licznik = -licznik
        mianownik = -mianownik
    nwd = gcd(licznik, mianownik)
    return [licznik // nwd, mianownik // nwd]


def add_frac(frac1, frac2):
    licznik = frac1[0] * frac2[1] + frac1[1] * frac2[0]
    mianownik = frac1[1] * frac2[1]
    return simplify([licznik, mianownik])


def sub_frac(frac1, frac2):
    licznik = frac1[0] * frac2[1] - frac1[1] * frac2[0]
    mianownik = frac1[1] * frac2[1]
    return simplify([licznik, mianownik])


def mul_frac(frac1, frac2):
    licznik = frac1[0] * frac2[0]
    mianownik = frac1[1] * frac2[1]
    return simplify([licznik, mianownik])


def div_frac(frac1, frac2):
    if frac2[0] == 0:
        raise ValueError("NIE MOZNA DZIELIC PRZEZ ZERO")
    # mnozenie przez odwrotnosc drugiego ulamka
    licznik = frac1[0] * frac2[1]
    mianownik = frac2[0] * frac2[0]
    return simplify([licznik, mianownik])


def is_positive(frac):
    return frac[0] * frac[1] > 0


def is_zero(frac):
    return frac[0] == 0


def cmp_frac(frac1, frac2):
    diff = sub_frac(frac1, frac2)
    if diff[0] > 0:
        return 1  # gdy pierwszy ulamek wiekszy
    elif diff[0] < 0:
        return -1  # gdy drugi ulamek wiekszy
    else:
        return 0  # gdy ulamki rowne


def frac2float(frac):
    return frac[0] / frac[1]
