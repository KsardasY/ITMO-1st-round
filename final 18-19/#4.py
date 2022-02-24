for i in range(1, 10000):
    x = str(i)
    k = 0
    while k < 3 and x != x[::-1]:
        x = str(int(x) + int(x[::-1]))
        k += 1
    if k == 3 and x == x[::-1] == '13431':
        print(i)
        break
