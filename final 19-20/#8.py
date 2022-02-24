s = 0
for x in range(1, 1000):
    a = [[0] * 3 for _ in range(10001)]
    a[0][0] = 5236
    a[0][1] = x
    for i in range(1, 10001):
        if a[i - 1][1] < a[i - 1][0]:
            a[i][0] = a[i - 1][0] - a[i - 1][1]
        else:
            a[i][0] = a[i - 1][0]
        if a[i - 1][1] > a[i - 1][0]:
            a[i][1] = a[i - 1][1] - a[i - 1][0]
        else:
            a[i][1] = a[i - 1][1]
        if a[i][0] == a[i][1]:
            a[i][2] = a[i][1]
    c = max(a, key=lambda x: x[2])[2]
    if c == 187:
        s += x
print(s)
