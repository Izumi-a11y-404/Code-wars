from collections import Counter

def duplicate_encode(word):
  # new_word = ""
  # word = word.lower()
  # for ch in word:
  #   if word.count(ch) > 1:
  #     new_word += ')'
  #   else:
  #     new_word += '('
  # return new_word
  word_lower = word.lower()
  word_count = Counter(word)
  return ("").join('(' if word_count[char] == 1 else ')' for char in word_lower)

def main():
  word = ")((())())"
  print(duplicate_encode(word))

if __name__ == '__main__':
  main()