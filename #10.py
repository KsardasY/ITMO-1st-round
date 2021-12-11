k = 0
for i in range(1000, 1500 + 1):
    n = i
    r = n
    while r >= 100:
        r = 0
        while n > 0:
            r += n % 100
            n //= 100
        n = r
    if r % 11 == 0:
        k += 1
print(k)
