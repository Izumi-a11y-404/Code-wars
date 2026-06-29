from collections import Counter

def histogram(values: list[int], bin_width: int) -> list[int]:
  if values:
    values.sort()
    bin_count = []
    result_count = []
    for item in values:
      bin = item // bin_width
      bin_count.append(bin)
    counts = Counter(bin_count)
    for i in range(values[(len(values)-1)//bin_width]):
      if i in counts:
        result_count.append(counts[i])
      else:
        result_count.append(0)
      return result_count
    else:
      return []

def main():
  print(histogram([1,1,0,1,3,2,6], 2))

if __name__ == '__main__':
  main()