from collections import Counter

def find_unique(arr):
  counts = Counter(arr)
  print(counts)
  for count in counts:
    if counts[count] == 1:
      return  count
  return -1


def main():
  print(find_unique([1, 1, 1, 2, 1]))

if __name__ == '__main__':
  main()