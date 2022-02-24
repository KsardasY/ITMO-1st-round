b = [[0] * 9 for _ in range(6)]
b[1][0] = b[1][-1] = 1
b[2][1] = b[2][-2] = 1
b[3][2] = b[3][-3] = 1
b[4][3] = b[4][-4] = 1
b[5][4] = 1
for h in range(1, 10000):
    x = h
    a = [[0] * 9 for _ in range(6)]
    n = 6
    k = 0
    h = h ** 2
    while h > 0:
        a[h % n][k] = 1
        h //= n
        k += 1
    if b == a:
        print(x)
        break
