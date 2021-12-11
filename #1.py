k = 1
dm = -100000
for i in range(1, 4096):
    x = i
    s1 = 0
    while x > 0:
        s1 += x % 4
        x //= 4
    x = i
    s2 = 0
    while x > 0:
        s2 += x % 16
        x //= 16
    d = s2 - s1
    if d > dm:
        dm = d
        k = 1
    elif d == dm:
        k += 1
print(k)
