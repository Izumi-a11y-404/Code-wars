def add_binary(a,b):
  # sum = a + b
  # b_sum = ''
  # while True:
  #   rem = sum % 2
  #   quo = sum // 2
  #   b_sum += str(rem)
  #   if quo == 0:
  #     break
  #   sum = quo

  # print(b_sum[len(b_sum)-1::-1])
  # return bin(a+b)[2:]
  return format(a + b, 'b')

print(add_binary(4, 1))