for n in range(4, 100):
    a = [[0] * n for _ in range(n)]
    t = 0
    i = 0
    j = 0
    a[i][j] = 1
    l = 2
    while True:
        if t == 0:
            if j != n - 1 and a[i][j + 1] == 0:
                j += 1
                a[i][j] = l
            else:
                if a[i + 1][j] != 0:
                    break
                else:
                    i += 1
                    a[i][j] = l
                    t = (t + 1) % 4
        elif t == 1:
            if i != n - 1 and a[i + 1][j] == 0:
                i += 1
                a[i][j] = l
            else:
                if a[i][j - 1] != 0:
                    break
                else:
                    j -= 1
                    a[i][j] = l
                    t = (t + 1) % 4
        elif t == 2:
            if j != 0 and a[i][j - 1] == 0:
                j -= 1
                a[i][j] = l
            else:
                if a[i - 1][j] != 0:
                    break
                else:
                    i -= 1
                    a[i][j] = l
                    t = (t + 1) % 4
        elif t == 3:
            if i != 0 and a[i - 1][j] == 0:
                i -= 1
                a[i][j] = l
            else:
                if a[i][j + 1] != 0:
                    break
                else:
                    j += 1
                    a[i][j] = l
                    t = (t + 1) % 4
        l += 1
    if sum(a[n // 2]) == 13313:
        print(n)
