def expand_form(num):
  # divisor = 10 ** (len(str(num)) - 1)
  # expanded_form = []
  # while num > 0:
  #   quotent = num // divisor
  #   print(quotent)
  #   remainder = num % divisor
  #   print(remainder)
  #   print(divisor)
  #   expanded_form.append(f'{quotent * divisor}')
  #   num = remainder
  #   divisor = 10 ** (len(str(remainder)) - 1)
  # print((" + ").join(expanded_form))

  # Using list comprehension
  num = list(str(num))
  # return "+".join([x + '0'*(len(num) - y - 1) for y, x in enumerate(num) if x != '0'])
  num_lst = []
  for y, x in enumerate(num):
    if x != '0':
      get_zeros = '0'*(len(num) - y - 1)
      num_lst.append(x + get_zeros)
      print(num_lst)
  return ' + '.join(num_lst)


def main():
  print(expand_form(12))

if __name__ == '__main__':
  main()