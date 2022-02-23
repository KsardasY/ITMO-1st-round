from itertools import product
for a, b, c in product((True, False), repeat=3):
    if not (((a and b or c) != (not a and c or not b)) or (a and not b or c) != (a and not c or b)):
        print(int(a), int(b), int(c))
