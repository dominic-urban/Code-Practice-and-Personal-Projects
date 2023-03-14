letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Adds corresponding letters for lowercase entries
letters += [
  letter.lower() 
  for letter
  in letters
]
#This section of code doubles the points list, essentially adds it to itself. Does not multiply the items together
points *= 2


letter_to_points = {key:value for key,value in zip(letters, points)}

letter_to_points[" "] = 0
##My Answer, which did work but is bulkier than necessary
# def score_word(word):
#   point_total = 0
#   for i in range(len(word)):
#     for letter, points in letter_to_points.items():
#       if letter == word[i]:
#         point_total += letter_to_points[letter]
#       else:
#         point_total += 0
#   return point_total

#actual answer
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}
for player, words, in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)

#This code will update player totals
# def update_point_totals():
#   for player, words in player_to_words.items():
#     player_points = 0
#     for word in words:
#       player_points += score_word(word)
#       player_points[player] = player_points

# update_point_totals()

def play_word(player, word):
  player_to_words[player].append(word)

play_word("player1", "CODE")
print(player_to_words)



print(player_to_points)
