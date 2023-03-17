
###Goal of this little script is to give me a calculator where I can enter a cocktail, work out the total cost, and the mls of whatever single missing ingredient when something is eg. top with soda

##Glassware types by mileage, note, rough mileage required after ice:
glassware = {"Old Fash": 125, "Jug": 2000}

##Cocktail ingredients + mls dictionaries
#Note, always put mixer(top with) ingredient last for mls calculator to work
kentucky_buck = {"Scotch": 45, "Lemon Juice": 22.5, "Bitters": 2, "Strawberry Syrup": 10, "Ginger Beer": 45}
paloma = {"Tequila": 45, "Ruby Red Grapefruit Juice": 25, "Lime Juice": 10, "Pink Grapefruit Syrup": 15, "Soda Water": 30}

#Ingredient price, mls and price per ml

##Function for calculating the total mls of an item
def mls_calculator(cocktail_dictionary):
  total_mls = 0
  for mls in cocktail_dictionary.keys():
    total_mls += cocktail_dictionary[mls]
  return float(total_mls)

#Calculate percent of cocktail which carbonated mixer takes up (to be added after prebatch mix poured)
def carbonated_mixer_percent(cocktail_dictionary):
  mixer_mls = mls_calculator(cocktail_dictionary)
  mixer_percent = round((list(kentucky_buck.values())[-1]) / mixer_mls * 100, 2)
  print((list(kentucky_buck.keys())[-1]) + " should be " + str(mixer_percent) + "% of the final cocktail")

##Calculator for mls of each cocktail ingredient in pre-batch
#Two versions, one where all ingredients are going into pre-batch, one without last ingredient (eg. carbonated mixer)
carbonated_mixer = False
def pre_batch_ingredient_mls(cocktail_dictionary, carbonated_mixer, glassware, quantity=1):
  cocktails_per_pre_batch = glassware*quantity / mls_calculator(cocktail_dictionary)
  print("Each cocktail will be " + str(mls_calculator(cocktail_dictionary)) + "mls once complete")
  print("Cocktails per " + str(glassware) + "mls: " + str(cocktails_per_pre_batch))
  ingredient = []
  mls_of_ingredient = []
  if carbonated_mixer == False:
    for item in cocktail_dictionary.keys():
      ingredient.append(item)    
    for mls in cocktail_dictionary.keys():
      mls_of_ingredient.append(mls)
  else:
    for item in cocktail_dictionary.keys():
      ingredient.append(item)
    for mls in cocktail_dictionary.keys():
      mls_of_ingredient.append(mls)
    del ingredient[-1]
    del mls_of_ingredient[-1]
  carbonated_mixer_percent(cocktail_dictionary)

pre_batch_ingredient_mls(kentucky_buck, carbonated_mixer, glassware["Jug"])
  

#Print mls totals here - No longer needed, working
# print(mls_calculator(kentucky_buck))
# print(mls_calculator(paloma))

##Working out how much Soda Water to put into Paloma (top with Soda) - Used to finish of paloma list with 30mls Soda Water
def mls_missing(glassware, cocktail_dictionary):
  missing_mls = glassware["Old Fash"] - mls_calculator(cocktail_dictionary)
  print(missing_mls)

print(mls_missing)
