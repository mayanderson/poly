def calculate_damage(your_type, opponent_type, attack, defense):
  # Build effectiveness dictionary
  superEffective = {
    "fire" : "grass",
    "water" : "fire",
    "grass" : "water",
    "electric" : "water"
  }
  
  multiplier = 1
  if superEffective.get(your_type) == opponent_type:
    multiplier = 2
  elif superEffective.get(opponent_type) == your_type or your_type == opponent_type :
    multiplier = 0.5
  
  return 50 * (attack / defense) * multiplier


print (calculate_damage("fire", "grass", 100, 100))
  
    