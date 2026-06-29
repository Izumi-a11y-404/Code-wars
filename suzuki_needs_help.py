def sort_names(string):
  # name_list = string.split()
  # for i in range(len(name_list)):
  #   temp = ''
  #   for j in range(i + 1, len(name_list)):
  #     if len(name_list[i]) <= len(name_list[j]):
  #       temp = name_list[i]
  #       name_list[i] = name_list[j]
  #       name_list[j] = temp
  # return name_list

  # Find the largest number first then swap once
  # name_list = string.split()
  # for i in range(len(name_list)):
  #   max_index = i
  #   for j in range(i + 1, len(name_list)):
  #     if len(name_list[j]) > len(name_list[max_index]):
  #       max_index = j
  #   name_list[i], name_list[max_index] = name_list[max_index], name_list[i]
  # return name_list

  # simple solution
  name_list = string.split()
  name_list.sort()
  sorted_list = sorted(name_list, key=len)
  return sorted_list[::-1]

  # Pythonic solution
  # return sorted(string.split(), key=lambda name: (len(name), name), reverse=True)

def main():
  names = 'Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi'
  result = sort_names(names)
  print(result)

if __name__ == '__main__':
  main()