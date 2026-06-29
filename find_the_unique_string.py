from collections import Counter

def find_uniq(arr):
  normalised = [frozenset(s.lower()) for s in arr]
  # frozenset is a dictionary that is immutable -> we used frozenset because we need a key for a dictionary that shoudnt be immutable 
  # As keys in a dictionary must be immutable or hashable
  counts = Counter(normalised)
  for string in arr:
    if counts[frozenset(string.lower())] == 1:
      return string
  return -1

def main():
  print(find_uniq([ '', '', '', 'a', '', '' ]))

if __name__ == '__main__':
  main()