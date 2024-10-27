def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        temp = b
        b = a + b
        a = temp
    return b


for i in range(11):
    print(f"{i}-liczba ciagu Fibonacciego: {fibonacci(i)}")
