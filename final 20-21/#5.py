t = [7, 77, 7 * 11 * 19, 7 * 11 * 19 * 23]
r = t[0]
i = 1
while i < 4:
    temp = r
    while r != t[i]:
        r += temp
    i += 1
print(r, t[1], t[2])
