# def find_short(s):
#   # your code here
#   word_lst = s.strip('.').split(" ")
#   shortest = len(word_lst[0])

#   for word in word_lst:
#     if len(word) < shortest:
#       shortest = len(word)
#   l = shortest
#   return l # l: shortest word length

# using min function
# def find_short(s):
#   return min(x for x in s.strip('.').split(' '))

# using min function with key
def find_short(s):
  words = s.strip('.').split(' ')
  return len(min(words, key=len))
print(find_short("The quick brown fox jumps over the lazy dog."))