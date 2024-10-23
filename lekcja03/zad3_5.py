def miarka(dlugosc):
    miarka_up = ""
    miarka_down = "0"
    for i in range(dlugosc):
        miarka_up += "|...."
    miarka_up += "|"

    for i in range(1,dlugosc+1):
        miarka_down += f"{str(i):>{5}}"

    print(miarka_up)
    print(miarka_down)

miarka(20)