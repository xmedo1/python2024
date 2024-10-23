while True:
    x = input("Podaj liczbe rzeczywista (stop, aby zakonczyc): ")
    if x == "stop":
        break
    try:
        x = float(x)
        print(f"x={x} x^3={x ** 3}")
    except ValueError:
        print("Blad wejscia")
