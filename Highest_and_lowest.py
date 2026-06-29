def high_and_low(numbers):
  num_list = numbers.split()
  highest = int(num_list[0])
  lowest = int(num_list[0])
  for num in num_list:
    if int(num) > highest:
      highest = int(num)
    if int(num) < lowest:
      lowest = int(num)
  numbers = f"{highest} {lowest}"
  return numbers


  # Using min(), max() functions
  # num_list = [int(num) for num in numbers.split()]
  # return f"{max(num_list)} {min(num_list)}"
  
  # Using key=int for sorting out the elements of the string
  # num_list = sorted(numbers.split(), key=int) # key=int -> Temporarily convers the string to an integer for comparison
  # return "{} {}".format(num_list[-1], num_list[0])

def main():
  num_str = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
  print(high_and_low(num_str))

if __name__ == '__main__':
  main()