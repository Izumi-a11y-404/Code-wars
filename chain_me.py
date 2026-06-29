from functools import reduce

def chain(init_val, functions):
  # for function in functions:
  #   init_val = function(init_val)
  # return init_val

  # Pythonic solution
  return reduce(lambda x, f: f(x), functions, init_val)


def add10(x): return x + 10
def mul30(x): return x * 30
def main():
  print(chain(50, [add10, mul30]))

if __name__ == '__main__':
  main()
