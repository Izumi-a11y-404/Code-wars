def hydrate(drink_string):
  string_list = drink_string.split()
  water_needed = sum([int(string) for string in string_list if string.isdigit()])
  return "{} {} of water.".format(water_needed, "glasses") if water_needed > 1 else "{} {} of water.".format(water_needed, "glass")

def main():
  print(hydrate("1 shot, 0 beers, 0 shots, 0 glass of wine, 0 beer"))

if __name__ == "__main__":
  main()