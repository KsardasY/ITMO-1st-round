from itertools import product
for i in range(11, 20):
    k = 0
    for x in product('01', repeat=i):
        z = ''.join(x)
        k += not '111' in z and not '000' in z
    if k == 1220:
        print(i)
        break
