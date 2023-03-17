
###Goal of this little script is to give me a calculator where I can enter a cocktail, work out the total cost, and the mls of whatever single missing ingredient when something is eg. top with soda

##Glassware types by mileage, note, rough mileage required after ice:
glassware = {"Old Fash": 125, "Jug": 2000}

##Cocktail ingredients + mls dictionaries
#Note, always put mixer(top with) ingredient last for mls calculator to work
kentucky_buck = {"Scotch": 45, "Lemon Juice": 22.5, "Bitters": 2, "Strawberry Syrup": 10, "Ginger Beer": 45}
paloma = {"Tequila": 45, "Ruby Red Grapefruit Juice": 25, "Lime Juice": 10, "Pink Grapefruit Syrup": 15, "Soda Water": 30}

#Ingredient and price per ml dictionary
#This will need to be manually updated each time prebatch is being made (i think)
#For lemons and limes assumption is made that each lemon will give 45mls juice, and each lime 30mls
#Below for 2023/18/03 cocktails, always dollars/total mls(or quantity for lemons)/mls
ingredient_pp_ml = {"Scotch": 0/700, "Lemon Juice": 20.74/16/30, "Bitters": 14/700, "Strawberry Syrup": 17.50/1000, "Ginger Beer": 12.50/3750, "Tequila": 0/700, "Ruby Red Grapefruit Juice": 6.25/1500, "Lime Juice": 5.33/8/30, "Pink Grapefruit Syrup": 17.50/1000, "Soda Water": (4.20/1100)}

print("$" + str((ingredient_pp_ml["Lime Juice"])) + " per ml")
print(450*ingredient_pp_ml["Ginger Beer"])

##Function for calculating the total mls of an item
def mls_calculator(cocktail_dictionary):
  total_mls = 0
  for mls in cocktail_dictionary.keys():
    total_mls += cocktail_dictionary[mls]
  return float(total_mls)

##Function for calculating the amount of mls needed to finish the cocktail, just change glassware type within function
def mls_missing(glassware, cocktail_dictionary):
  missing_mls = glassware - mls_calculator(cocktail_dictionary)
  print(str(missing_mls) + "mls required to complete cocktail")

#Test mls_missing function
#mls_missing(glassware["Old Fash"], kentucky_buck)

#Calculate percent of cocktail which carbonated mixer takes up (to be added after prebatch mix poured)
def carbonated_mixer_percent(cocktail_dictionary):
  mixer_mls = mls_calculator(cocktail_dictionary)
  mixer_percent = round((list(kentucky_buck.values())[-1]) / mixer_mls * 100, 2)
  print("Top with " + str(mixer_percent) + "% " + (list(cocktail_dictionary.keys())[-1]))

##Calculator for mls of each cocktail ingredient in pre-batch
#Two versions, one where all ingredients are going into pre-batch, one without last ingredient (eg. carbonated mixer)
carbonated_mixer = False
def pre_batch_ingredient_mls(cocktail_dictionary, carbonated_mixer, glassware, quantity=1):
  cocktails_per_pre_batch = glassware*quantity / mls_calculator(cocktail_dictionary)
  print("Each cocktail will be " + str(mls_calculator(cocktail_dictionary)) + "mls once complete (not including ice or dilution if relevant)")
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
  total_cost_per = 0
  for key in cocktail_dictionary:
    key = (ingredient_pp_ml[key] * cocktail_dictionary[key])
    total_cost_per += key
  print("Cost per cocktail $" + str(total_cost_per))
  total_cost = total_cost_per * cocktails_per_pre_batch 
  print("Total cost per batched jug : $" + str(total_cost))    

pre_batch_ingredient_mls(paloma, carbonated_mixer, glassware["Jug"])

##Below seperated function for the prebatch calculator cost calculator, not used because function scope
# def total_cost_per_cocktail(ingredient_pp_ml, cocktail_dictionary):
#   total_cost_per = 0
#   for key in cocktail_dictionary:
#     key = (ingredient_pp_ml[key] * cocktail_dictionary[key])
#     print(key)
#     total_cost_per += key
#   print("Cost per cocktail $" + str(total_cost_per))
#   total_cost = total_cost_per * cocktails_per_pre_batch 
#   print("Total cost per batched jug : $" + str(total_cost))    
# total_cost_per_cocktail(ingredient_pp_ml, kentucky_buck)


  

#Print mls totals here - No longer needed, working
# print(mls_calculator(kentucky_buck))
# print(mls_calculator(paloma))


