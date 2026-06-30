def knight_vs_rook(knight, rook):
  print(f"Knight staying position: {knight}")
  print(f"Rook staying position: {rook}")
  columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
  rows = [8, 7, 6, 5, 4, 3, 2, 1]
  knight_covered_positions = []
  rook_covered_positions = []
  knight_covered_numbers = []
  knight_covered_alphas = []
  for position in rook:
    if f"{position}".isdigit():
      for column in columns:
        rook_covered_positions.append((position, column))
    elif f"{position}".isalpha():
      for row in rows:
        rook_covered_positions.append((row, position))
  for position in knight:
    if f"{position}".isdigit():
      starting_position = position - 2
      ending_postion = position + 2
      for i in range(starting_position, ending_postion + 1):
        if i == position:
          continue
        knight_covered_numbers.append(i)
    elif f"{position}".isalpha():
      alpha_starting_position = columns.index(position) - 2
      alpha_ending_position = columns.index(position) + 2
      for i in range(alpha_starting_position, alpha_ending_position + 1):
        if columns[i] == position:
          continue
        knight_covered_alphas.append(columns[i])
      for i, num in enumerate(knight_covered_numbers):
        for j, alp in enumerate(knight_covered_alphas):
          if (i == 1 or i == 2) and j == 0:
            knight_covered_positions.append((num, alp))
          elif (i == 1 or i == 2) and j == 3:
            knight_covered_positions.append((num, alp))
          elif (j == 1 or j == 2) and i == 0:
            knight_covered_positions.append((num, alp))
          elif (j == 1 or j == 2) and i == 3:
            knight_covered_positions.append((num, alp))
  print(f"Knight covered position: {knight_covered_positions}")
  print(f"Rook covered position: {rook_covered_positions}")
  if knight in rook_covered_positions:
    return "Rook wins!"
  elif rook in knight_covered_positions:
    return "Knight wins!"
  else:
    return "No one wins."

def main():
  print(knight_vs_rook((5, 'E'), (4,'C')))

if __name__ == '__main__':
  main()