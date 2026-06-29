# def choose_best_home(places, preferences, priorities):
#   best_house = None
#   highest_score = -1
#   # house = places[place]
#   # typle unpacking
#   for place, house in places.items():
#     current_score = 0
#     for index, priority in enumerate(priorities):
#       # if (priority in house 
#       #   and priority in preferences 
#       #   and house[priority] == preferences[priority]):
#       if house.get(priority) == preferences.get(priority):
#         current_score += 6 - index
#     print(f'{place}: {current_score}')
#     if current_score > highest_score or (highest_score == current_score and (best_house is None or best_house > place)):
#       best_house = place
#       highest_score = current_score
#   return best_house

# def main():
#   places = {
#     "Apartment_A": {"type": "apartment", "cats": "zero_cats"},
#     "House_B":     {"type": "house",     "cats": "many_cats_to_pet"}
#   }
#   preferences = {"type": "apartment", "cats": "many_cats_to_pet"}
#   priorities = ["type", "cats"]
#   print(choose_best_home(places, preferences, priorities))

# if __name__ == '__main__':
#   main()

# def choose_best_house(places, preferences, priorities):
#   weights = {
#     trait: 6 - i
#     for i, trait in enumerate(priorities)
#   }
#   best_name = min(places)
#   best_score = -1
#   for name in places:
#     score = 0
#     house = places[name] # a Dictionary containing traits of the houses
#     for category, preference in preferences.items():
#       if preference == house[category]:
#         score += weights.get(category, 0) # returns a zero if category is not found
#     if score > best_score:
#       best_score = score
#       best_name = name
#     elif score == best_score and best_name > name:
#       best_name = name
#   return best_name
    

# def main():
#   places = {
#     "Apartment_A": {"type": "apartment", "cats": "zero_cats"},
#     "House_B":     {"type": "house",     "cats": "many_cats_to_pet"}
#   }
#   preferences = {"type": "apartment", "cats": "many_cats_to_pet"}
#   priorities = ["type", "cats"]
#   print(choose_best_house(places, preferences, priorities))

# if __name__ == '__main__':
#   main()

def choose_best_house(places, preferences, priorities):
  apartments = list(places.keys())
  score_dict = {apartment: 0 for apartment in apartments}
  max_point = 6
  for priority in priorities:
    for apartment in apartments:
      if places[apartment].get(priority) == preferences.get(priority):
        score_dict[apartment] = max_point
    max_point -= 1 if max_point > 0 else 0

  score_dict = dict(sorted(score_dict.items())) if score_dict else None
  winner = max(score_dict, key=score_dict.get) if score_dict else None

  return winner

def main():
  places = {
    "Apartment_A": {"type": "apartment", "cats": "zero_cats"},
    "House_B":     {"type": "house",     "cats": "many_cats_to_pet"}
  }
  preferences = {"type": "apartment", "cats": "many_cats_to_pet"}
  priorities = ["type", "cats"]
  print(choose_best_house(places, preferences, priorities))

if __name__ == '__main__':
  main()