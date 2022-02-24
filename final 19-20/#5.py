a = 'abcdef'
s = 'abcdef'
b = list()
for i in range(2, 1001):
    d = len(a) // 2
    a = a[d - 1:d + 1] + a
    if i == 90 or i == 200 or i == 300 or i == 1000:
        b.append(a[0])
print(a)
b = {'a': b[0], 'b': b[1], 'd': b[2], 'c': b[3]}
for i in range(4):
    print(b[s[i]], end='')
