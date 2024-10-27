# Linijka
def make_ruler(dlugosc):
    miarka_up = ""
    miarka_down = "0"
    for i in range(dlugosc):
        miarka_up += "|...."
    miarka_up += "|"

    for i in range(1, dlugosc + 1):
        miarka_down += f"{str(i):>{5}}"

    return miarka_up + "\n" + miarka_down


# Prostokat
def make_grid(x, y):
    vertEdge = "|" + "   |" * y
    horEdge = "+" + "---+" * y
    grid = ""

    for i in range(x):
        grid += horEdge + "\n"
        grid += vertEdge + "\n"
    grid += horEdge
    return grid


ruler = make_ruler(20)
print(ruler)
print("\n")
prostokat = make_grid(4, 3)
print(prostokat)
