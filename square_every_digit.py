def square_digits(num):
  # num_str = str(num)
  # new_num = ""
  # for num in num_str:
  #   new_num += str(int(num)**2)
  # return int(new_num)

  return ("").join(str(int(x)**2) for x in str(num))


def main():
  print(square_digits(9119))

if __name__ == '__main__':
  main()