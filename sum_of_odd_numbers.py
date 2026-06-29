def row_sum_odd_numbers(n):
  odd = 1
  for i in range(1, n+1):
    for _ in range(i):
      print(odd, end=" ")
      odd += 2
    print()
def main():
  row_sum_odd_numbers(4)

if __name__ == '__main__':
  main()