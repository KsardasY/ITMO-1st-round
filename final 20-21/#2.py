from math import log2, ceil
for n in range(6, 10000, 3):
    a = set()
    v1 = n * ceil(log2(3))
    s = 'A'
    s1 = 'ABC'
    s3 = 'AB'
    k = 0
    i = 2
    while len(s) < n:
        s += s1[(i - 1) % 3]
        if i % 2 == 0:
            s += 'A'
        if i % 3 == 0:
            s += s3[k % 2]
            k += 1
        i += 1
    if len(s) == n:
        for i in range(0, n - 1, 3):
            a.add(s[i:i + 3])
        if v1 == n // 3 * ceil(log2(len(a))) + 62:
            print(n)
            break
