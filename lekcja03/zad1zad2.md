# Zadanie 3.1

```python
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
```
Ten kod zadziała poprawnie, ale średniki na końcach linii oraz nawiasy przy `if` są zbędne.

---
```python
for i in "axby": if ord(i) < 100: print (i)
```
Ten fragment kodu nie zadziała, ponieważ w jednej linii nie mogą być umieszczone instrukcje `for` i `if`. Poprawna wersja tego kodu wyglądałaby następująco:
```python
for i in "axby":
    if ord(i) < 100: print (i)
```

---
```python
for i in "axby": print (ord(i) if ord(i) < 100 else i)
```
Ten kod jest poprawny.

---
# Zadanie 3.2

```python
L = [3, 5, 4] ; L = L.sort()
```
Ten kod podstawia pod listę `L` wartość zwracaną przez metodę `sort()`, czyli `None`.
Poprawnie wyglądający kod powinien tylko wywołać metodę `sort()` na liście `L`.

```python
L = [3, 5, 4]
L.sort()
```

---

```python
x, y = 1, 2, 3
```
Po lewej stronie operatora przypisania mamy dwie zmienne, a po prawej stronie trzy wartości.

---
```python
X = 1, 2, 3 ; X[1] = 4
```
`X` jest krotką, więc nie można zmieniać jej elementów po utworzeniu. Instrukcja `X[1] = 4` byłaby poprawna, gdyby `X` było listą.

---

```python
X = [1, 2, 3] ; X[3] = 4
```
Listy są indeksowane od zera, więc indeks `3` w tej liście nie istnieje. Ostatni element listy `X` (o wartości 3) ma indeks `2`. Chcąc dodać element do tej listy możemy użyć przykładowo metody `append()`.

---
```python
X = "abc" ; X.append("d")
```
Metoda `append()` jest dostępna tylko dla list, a nie dla typu `string`.

---
```python
L = list(map(pow, range(8)))
```
Metoda `pow()` nie otrzymała żadnych argumentów.