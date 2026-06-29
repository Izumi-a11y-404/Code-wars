def xo(s):
  s = s.lower()
  x_count = 0
  o_count = 0
  for ch in s:
    if ch == 'x':
      x_count += 1
    elif ch == 'o':
      o_count += 1
  if x_count == o_count:
    return True
  return False

def xo_using_count(s):
  s = s.lower()
  return s.count('x') == s.count('o')


print(xo("xoXo"))
print(xo_using_count("xooo"))