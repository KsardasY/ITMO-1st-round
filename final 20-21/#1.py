for x in range(4, 100):
    for y in range(5, 100):
        if 36 * x + 4 * y + 40 == 12 * (x ** 2 - 1):
            print(x, y)
