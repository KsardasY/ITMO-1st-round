from math import ceil, log2
for n in range(1, 50):
    if 5624 % n == 0:
        for m in range(n + 1, 51):
            if 5624 % n == 0 and 5624 // n * ceil(log2(139 ** n)) - 5624 // m * ceil(log2(139 ** m)) == 128:
                print(n, m)
