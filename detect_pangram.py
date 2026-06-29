import string

def is_pangram(st):
  # alpha = 'abcdefghijklmnopqrstuvwxyz'
  # already_stored_letters = []
  # count = 0
  # for ch in st.lower():
  #   if ch in already_stored_letters or ch.isalpha() == False:
  #     continue
  #   if ch in alpha:
  #     already_stored_letters.append(ch)
  #     count += 1
  # if count == len(alpha):
  #   return True
  # return False
  print(set(string.ascii_lowercase))
  print(st.lower())
  return set(string.ascii_lowercase).issubset(st.lower())

def main():
  st = "The quick brown fox jumps over the lazy dog."
  print(is_pangram(st))

if __name__ == '__main__':
  main()