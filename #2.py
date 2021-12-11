from itertools import product
s = '123456789'
k = 1
for i in range(1, 10):
    k += i - 1
    for x in product(s[:10 - i], repeat=i):
        c = sum(list(map(int, list(x))))
        c += int(x[-1])
        if c <= 11:
            k += 1
print(k)
