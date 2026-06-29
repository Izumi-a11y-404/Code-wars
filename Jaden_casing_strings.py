def to_jaden_case(string):
  # new_string = ""
  # for i in range(len(string)):
  #   if i == 0:
  #     new_string += string[i].upper()
  #   elif string[i - 1] == ' ':
  #     new_string += string[i].upper()
  #   else:
  #     new_string += string[i]
  # return new_string

  return (" ").join(word.capitalize() for word in string.split())
    

def main():
  string = "how can mirrors be real if our eyes aren't real"
  print(to_jaden_case(string))

if __name__ == '__main__':
  main()