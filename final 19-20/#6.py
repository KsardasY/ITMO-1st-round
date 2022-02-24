def f(x):
    r = 0
    k = 0
    l = 10
    while k < 9:
        m = 0
        s = 0
        while s < 9:
            z = (x // (10 ** s)) % 10
            if m < z < l:
                m = z
                t = s
            s += 1
        if m > 0:
            r = r * 10 + t
            l = m
            k += 1
    return r


print(f(285197364))
