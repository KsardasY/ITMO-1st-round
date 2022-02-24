for n in range(1, 'AABBAABBAABBAABBAABBAABB'.count('A')):
    a = 'AABBAABBAABBAABBAABBAABB'
    for _ in range(14):
        x = len(a) - 1
        d = x
        k = 0
        while x >= 0 and k < n:
            if a[x] == 'A':
                k += 1
            x -= 1
        a = (2 * a)[:d + x + 2]
    if a.count('A') == 98310:
        print(n)
        break
