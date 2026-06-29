from typing import Iterable, Callable

# Iterable, Callable defines that the arguments we are passing should be a sequence and a function [..., bool]
# defines that it should return a boolean value
def one(xs: Iterable, predicate: Callable[..., bool]) -> bool:
  True_count = 0
  for num in xs:
    if predicate(num):
      True_count += 1
      if True_count > 1:
        return False
      
  return True_count == 1

def main():
  equals_9 = lambda x: x == 9
  # the above one is same as writing
  # def equals_9(some_num):
  #   if some_num == 9:
  #     return True
  print(one([6, 7, 8, 9, 10, 11], equals_9)) # Returns True cuz only one number is 9 in the sequence

if __name__ == '__main__':
  main()