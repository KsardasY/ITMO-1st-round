n = int(input())
for b in range(n):
    k = 0
    a = ['.' * 20] + [input() for _ in range(10)] + ['.' * 20]
    i = 1
    while i < 11:
        if a[i].count('#') == 20:
            if a[i - 1].count('.') == 20:
                j = i + 1
                while j < 11 and a[j].count('#') == 20:
                    j += 1
                if a[j].count('.') == 20:
                    k += 1
                    i = j + 1
                else:
                    i = j + 2
            else:
                i += 2
        else:
            i += 1
    if b != n - 1:
        _ = input()
    if k == 1:
        print('Negative')
    elif k == 3:
        print('Positive')
    else:
        print('Incorrect')
