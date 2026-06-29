from collections import Counter

def most_frequent_item_count(collection):
  # if collection: # as empty list is considered False
  #   collection_set = list(set(collection))
  #   counts = []
  #   for i in range(len(collection_set)):
  #     counter = 0
  #     for j in range(len(collection)):
  #       if collection_set[i] == collection[j]:
  #         counter += 1
  #     counts.append(counter)
  #   return max(counts)
  # else:
  #   return 0

  # Short form by Me
  # if collection:
  #   counts = Counter(collection)
  #   return max([counts[count] for count in counts])
  # else:
  #   return 0
  
  # More short
  return max(Counter(collection).values(), default=0)

def main():
  print(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]))
  print(most_frequent_item_count([3, -1, -1]))

if __name__ == '__main__':
  main()