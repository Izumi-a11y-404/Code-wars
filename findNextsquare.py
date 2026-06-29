# def find_next_square(sq):
#   # Return the next square if sq is a square, -1 otherwise
#   base_num = sq**(1/2)
#   if base_num % 1 == 0:
#     next_num = int(base_num) + 1
#     new_num = next_num**(2)
#     return new_num
  
#   return -1

def find_next_square(sq):
  return ((sq**(0.5))+1)**2 if (sq**(0.5)) % 1 == 0 else -1 
  
print(find_next_square(123))