def return_operand(a, b, res):
  # Pythonic solution
  # return {a + b: 'addition', a - b: 'subtraction', a * b: 'multiplication', a / b: 'division'}[res]

  if a + b == res:
    return 'addition'
  elif a - b == res:
    return 'subtraction'
  elif a * b == res:
    return 'multiplication'
  elif b != 0 and a / b == res:
    return 'division'
  else:
    return -1

def main():
  print(return_operand(1, 3, 4))

if __name__ == '__main__':
  main()