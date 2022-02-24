a = int('4C6D', 16)
d = a // 2 + 1
s = '0123456789ABCDEF'
x = 1
while x < d + 1:
    if a % x == 0:
        z = x
        c = 1
        t = ''
        while z > 0:
            v = z % 16
            t = s[v] + t
            c *= v
            z //= 16
        if c == a // x:
            print(t)
            break
    x += 1
