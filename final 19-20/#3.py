from itertools import product
a = lambda x, y, z: int(((x and y) <= z) == ((not x) <= (y and z)))
b = lambda x, y, z: int(((y and z) <= x) == ((not y) <= (x and z)))
c = lambda x, y, z: int(((x and z) <= y) == ((not z) <= (x and y)))
d = lambda x, y, z: int(x and (y <= z) or y and (x <= z))
f = (0, 1)
print('x', 'y', 'z', '1', '2', '3', 'f', sep='\t')
for x, y, z in product(f, repeat=3):
  print(x, y, z, a(x, y, z), b(x, y, z), c(x, y, z), d(x, y, z), sep='\t')
