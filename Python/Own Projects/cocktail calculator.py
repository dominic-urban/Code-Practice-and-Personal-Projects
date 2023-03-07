#This program will use simple lists to check which cocktails we can make.
#The idea will be to input a list containing the items we have in stock, and then creating a list of cocktail names which we can make.
#As a stretch goal we can query the database for the cocktail's recipe and directions

# stock = ["Egg White", "Blueberries", "Strawberries", "Vanilla Essence", "Vodka", "Passionfruit", "Lemons", "Meringue"]
# print("Stock on hand = " + str(stock))
# Cocktails = ["Pavlovs_Dom"]
# Pavlovs_Dom = ["Egg White", "Vodka", "Lemon Juice", "Passionfruit", "Vanilla Essence", "Strawberries", "Blueberries", "Meringue"] 
# Pavlovs_Dom_Recipe = ["20ml Egg White", "30ml lemon juice", "4 Blueberries", "1 medium-large strawberry", "30ml passionfruit pulp", "30ml Vodka", "5ml Vanilla Essence", "Crushed meringue"] 
# Pavlovs_Dom_Directions = ["Place egg white, lemon juice, passionfruit pulp, blueberries, and strawberries into shaker and muddle. Add remaining ingredientes and dry shake. Add ice, shake and double strain into cocktail glass. Garnish with crushed meringue."]



#Plan below:
#Basically I want the program to have a dictionary/list database of my cocktails, their ingredients and their recipes.
#I want to be able to write in what i have on hand via an input, and have it give me back the cocktails that i am able to make with the items on hand.
#It would be best for this to include a value with items that are 'always' on hand (eg. my current spirits list) that i update manually through the program
#Step 1: Give ingredients + value(spirits_list)(?)
#Step 2: Returns possible cocktails from cocktail list
#Step 3: Requests entry of which cocktail I would like to make
#Step 4: Returns relevant cocktail + ingredients + recipe
#Note, can have something where if i just need a rum, it requires just something to be in the relevant list. Rum = True or something
#Later can adjust to include more specifics (eg, white rum vs dark)

#Types of rum set as value in key:value pair - - Dark, Gold, White, Spiced, Rhum Agricole
rums_on_hand = {'Dead Reckoning Barbados Tawny Cask': 'Dark', 'Phraya Elements Thai': 'Dark', 'Plantation 20YO XO': "Dark", 'Dead Reckoning Mhoba South African Wine Cask': "Dark", 'Killik Gold Ferntree Gully': "Gold", 'Ron Zacapa Solera': "Dark", 'Plantation Pineapple': "Dark", 'Privateer': "Dark", 'Plantation 3 Star': "White", 'Plantation Fiji': 'Dark', "Sampan Overproof Vietnamese": 'Rhum Agricole', "Bundaberg Spiced": "Spiced", "Kraken Black Spiced": "Spiced", "Buckeye Spiced (Custom mixed cheap rums)": "Spiced", "Ron Medellin Columbian": "Dark", "Cargo Cult Spiced": "Spiced"}
#Types: London Dry, Sloe, Specific Flavour, Japanese, etc
gins_on_hand = {'Hendricks': "Cucumber", "Gordons": "London Dry", "Malfy Gin Rosa": "Grapefruit", "Four Pillars Yuzu": "Yuzu", "Tanqueray Sevilla": "Sevilla Oranges", "Tanqueray Rangpur": "Indian Lime", "Etsu": "Japanese", "Ki No Bi Navy Strength": "Japanese", "Ki No Bi": "Japanese", "Larios": "London Dry", "Yuzu Gin": "Japan", "Tanqueray": "London Dry"}
#Types: Smooth, Harsh
vodkas_on_hand = {"Grey Goose": "Smooth", "Russian Standard": "Smooth"}
#Types: Reposado, Blanco, Anejo
tequilas_on_hand = {"Jose Cuervo": "Reposado"}
#Types of whiskies: - - Blended, Single Malt, Bourbon
whiskies_on_hand = {"Canadian Club 12YO Blended": "Blended", "Canadian Club 20YO": "Blended", "Glenlivet 12YO": "Single Malt", "Johnnie Walker Small Batch Coffee": "Blended", "Bulleit Bourbon": "Bourbon"}
#liqueurs and syrups will have the flavour as the value pair
liqueurs_on_hand = {"Fireball": "Cinnamon Whisky", "Soho": "Lychee", "Canpari": "Bitter Italian Oranges", "Aperol": "Bitter Italian Oranges", "Midori": "Melon", "Steinbock Watermelon": "Watermelon", "Marionette Apricot": "Apricot", "86 Peach Schnapps": "Peach", "86 Apple Schnapps": "Apple", "Jagermeister": "Herbal", "Vok dark creme de cacao": "Creme de cacao", "Butterscotch Schnapps": "Butterscotch", "Frangelico": "Hazelnut", "Baileys Red Velvet": "Red Velvet Cake", "Baileys": "Irish Cream", "White Creme de Cacao": "Creme de cacao", "Kahlua": "Coffee", "Vok Blue Curacao": "Blue Curacao", "Cointreau": "Italian Orange", "Disaronno Amaretto": "Almond", "Limoncello": "Limoncello", "Massenez Creme de Mure": "Creme de mure", "Galliano White Sambucca": "Anise"}
syrups_on_hand = {"Crawsey's Grenadine": "Grenadine", "Homemade Simple Syrup": "Simple Syrup", "Monin Vanilla": "Vanilla", "Monin Coconut": "Coconut"}
#Wines will have the general type, vermouths will have sweet, dry, etc
wine_and_vermouth_on_hand = {"Cinzano Rosso": "Sweet Vermouth", "Galway Pipe": "Port"}
other_on_hand = {"Choya Umeshu": "Umeshu", "Choya Yuzu": "Yuzu Sake"}

#Section for combined lists
#spirits_on_hand = {rums_on_hand + gins_on_hand + vodkas_on_hand + tequilas_on_hand + whiskies_on_hand + liqueurs_on_hand}
##Above gives error: Unsupported operand type for dict and dict
stock_on_hand = {}

for rum in rums_on_hand:
    if rums_on_hand 


additional_items = []