def prostokat(x, y):
    vertEdge = "|" + "   |" * y
    horEdge = "+" + "---+" * y
    prostokat = ""

    for i in range(x):
        prostokat += horEdge + "\n"
        prostokat += vertEdge + "\n"
    prostokat += horEdge
    print(prostokat)


prostokat(4, 3)
