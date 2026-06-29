def tower_builder(n_floor):
  # tower = []
  # for i in range(n_floor):
  #   floor = ''
  #   for _ in range(n_floor - i - 1):
  #     floor += ' '
  #   for _ in range(2*i + 1):
  #     floor += '*'
  #   for _ in range(n_floor - i - 1):
  #     floor += ' '
  #   tower.append(floor)
  # print(tower)

  # tower = []
  # for i in range(n_floor):
  #   stars = "*" * (2 * i + 1)
  #   space = " " * (n_floor - i - 1)
  #   tower.append(space + stars + space)
  #   print(space + stars + space)
  # print(tower)

  # tower = []
  # for i in range(n_floor):
  #   stars = "*" * (2 * i + 1)
  #   floor = stars.center(n_floor * 2 - 1)
  #   tower.append(floor)
  #   print(floor)
  # print(tower)

  # return [("*" * (2 * i + 1)).center(n_floor*2 - 1) for i in range(n_floor)]
  tower = []
  for i in range(n_floor):
    star = '*'*(2 * i + 1)
    space = ' '*(n_floor - i - 1)
    tower.append(space+star+space)
  return tower

  
    


def main():
  print(tower_builder(4))
  for floor in tower_builder(4):
    print(floor)

if __name__ == '__main__':
  main()