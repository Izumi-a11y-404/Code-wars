def moser():
  n = 1
  while True:
    regions = (24 + (n**4) - (6*(n**3)) + (23*(n**2)) - 18*n)//24
    yield regions
    n += 1
  

g = moser()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))