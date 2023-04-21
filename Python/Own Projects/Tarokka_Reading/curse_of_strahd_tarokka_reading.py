import random
import sys
import cv2


# img = cv2.imread(r"E:/15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/1.png", cv2.IMREAD_ANYCOLOR)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

class Cards:
    def __init__(self, name, deck, reading1, dm_info1, reading2, dm_info2, image):
        self.name = name
        self.deck = deck
        self.reading1 = reading1
        self.dm_info1 = dm_info1
        self.reading2 = reading2
        self.dm_info2 = dm_info2
        self.image = image
           
    def __repr__(self):
        if dm == True:
            print(self.name, str(self.deck), self.reading1, self.dm_info1, self.reading2, self.dm_info2)
        else:
            print(self.name, self.reading1, self.reading2)
        img = cv2.imread(self.image, cv2.IMREAD_ANYCOLOR)
        cv2.imshow(self.name,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        

#High Deck cards below
Artifact = Cards("Artifact", "high_deck", "Look for an entertaining man with a monkey. This man is more than he seems.", "This card refers to Rictavio who can be found at the Blue Water inn in Vallaki. Normally reluctant to accompany the characters, Rictavio changes his tune if the characters tell him about the card reading. He sheds his disguise and introduces himself as Dr. Rudolph van Ricten.", "He lurks in the darkness where the morning light once shone - a sacred place", "Strahd faces the characters in the chapel (area K15).", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/3.png")
Beast = Cards("Beast", "high_deck", "A werewolf holds a secret hatred for your enemy. Use her hatred to your advantage. ", "This card refers to the werewolf Zuleika Toranescu. She will accompany the characters if they promise to avenger her mate, Emil, by killing the leader of her pack, Kiril Stoyanovich.", "The beast sits on his dark throne", "Strahd faces the characters in the audience hall (area K25)", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/5.png")
Broken_One = Cards("Broken_One", "high_deck", "I see a man of faith whose sanity hangs by a thread. He has lost someone close to him", "This card refers to Donavich, the priest in the village of Barovia. He will accompany the characters until his son, Doru, is dead and buried", "He haunts the tomb of the man he envied above all.", "Strahd faces the characters in Sergei's tomb (area K85)", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/9.png")
Dark_Lord = Cards("Dark_Lord", "high_deck", "Ah, the worst of all truths! You must face the evil of this land alone!", "There is no NPC who can inspire the characters", "He lurks in the depths of darkness, in the one place to which he must return", "Strahd faces the characters in his tomb (area K86)", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/12.png")
Donjon = Cards("Donjon", "high_deck", "Search for a troubled young man surrounded by wealth and madness. His home is his prison.", "This card refers to Victor Vallakovich. Realizing that the characters are the key to his salvation he enthusiastically leaves home and accompanies them to Castle Ravenloft", "He lurks in a hall of bones, in the dark pits of his castle", "Strahd faces the characters in the hall of bones (area K67)", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/15.png")
Seer = Cards("Seer", "high_deck", "Look for a dusk elf living among the Vistani. He has suffered a great loss and is haunted by dark dreams. Help him, and he will help you in return", "This card refers to Kasimir Velikov. The dusk elf accompanies the characters to Castle Ravenloft only after they lead him to the Amber Temple and help him find the means to resurrect his dead sister Patrina Velikovna", "He waits for you in a place of wisdom, warmth, and despair. Great secrets are there.", "Strahd faces the characters in the study (area K37)", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/42.png")
Ghost = Cards("Ghost", "high_deck", "I see a fallen paladin of a fallen order of knights. He lingers like a ghost in a dead dragon's lair", "This card refers to the revenant Sir Godfrey Gwilym. Althugh initially unwilling to accompany the characters, he will do so if the characters convince him that the honour of the Order of the Silver Dragon can be restored with his help. This will require a successful DC15 charisma (Persuasion) check.", "Look to the father's tomb", "Strahd faces the characters in the tomb of King Barov and Queen Ravenovia (area K88)", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/21.png")
Executioner = Cards("Executioner", "high_deck", "Seek out the brother of the devil's bride. They call him \"the lesser\" but he has a powerful soul", "This refers to Ismark Kolyanovich. Ismark wont accompany the characters to Castle Ravenloft until he knows that his sister Ireena Kolyana is safe.", "I see a dark figure on a balcony, looking down upon this tortured land with a twisted smile", "Strahd faces the characters at the overlook (area K6)", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/20.png")
Horseman = Cards("Horseman", "high_deck", "A man of death named Arrigal will fosake his dark lord to serve your cause. Beware! He has a rotten soul", "This card refers to the Vistani assassin Arrigal. If the characters mention this card reading to him he accepts his fate and accompanies them. If the characters succeed in defeating Strahd, Arrigal betrays and attacks them, believing he is destined to become Barovia's new lord", "He lurks in the one place to which he must return -- a place of death", "Strahd faces the characters in his tomb (area K86)", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/25.png")
Innocent = Cards("Innocent", "high_deck", "Evil's bride is the one you seek!", "This card refers to Ireena Kolyana. Her brother Ismark opposes the idea of her being taken to Castle Ravenloft, but she insists on goignthere once the characters tell her about the card reading. Ireena wont accompany the characters however, until Kolyan Indirovich's body is laid to rest in the cemetary", "He dwells with the one whose blood sealed his doom, a brother of light snuffed out too soon", "Strahd faces the characters in Sergei's tomb (area K85)", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/27.png")
Marionette = Cards("Marionette", "high_deck", "What horror is this? I see a man made by a man. Ageless and alone,it haunts the towers of the castle", "This card refers to Pidlwick II who can be found in area K59 of the castle as well as in appendix D", "Look to great heights. Find the beating heart of the castle. He waits nearby.", "Strahd faces the characters in the north tower peak (area K60)", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/28.png")
Mists = Cards("Mists", "high_deck", "A Vistana wanders this land alone, searching for her mentor. She does not stay in one place for long. Seek her out at Saint Markovia's abbey, near the mists.", "This card refers to Ezmerelda d'Avenir. She can be found in the Abbey of Saint Markovia as well as several other locations throughout Brovia", "The cards can't see where the evil lurks. The mist obscure all!", "This card offers no clue as to where the final showdown with Strahd will occur. You as the DM may choose anywhere within the Castle Ravenloft. Alternatively, Madam Eva tells the characters to return to her after at least three days, and she will consult the cards again for them, but only to dicern the location of their enemy.", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/33.png")
Raven = Cards("Raven", "high_deck", "Find the leader of the feathered ones who live among the vines. Though old he has one more fight left in him", "This card refers to Davian Martikova, the old wereaven. Realizing that he has a chance to end Strahd's tyrannyh he leaves his vineyard and winery in the capable hands of his sons. But before he travels to Castle Ravenloft to face Strahd, Davian insists on reconciling with his third son Urwin (ch.5 area N9)", "Look to the mother's tomb", "Strahd faces the characters in the tomb of King Barov and Queen Ravenovia (area K88)", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/40.png")
Tempter = Cards("Tempter", "high_deck", "I see a child - a Vistana. You must hurry, for her fate hangs in the balacne. Find her at the lake!", "This card refers to Arabelle. She gladly joins the party. But if she returns to her camp, her father, Luvash refuses to let her leave", "I see a secret place -- a vault of temptation hidden behind a woman of great beauty. The evil waits atop his tower of treasure.", "Strahd confronts the characters in the treasury (area K41). A woman of great beauty refers to the portrait of Tatyana hanging in the castle's study (area K37) which contains a secret door leading to the treasury.", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/47.png")

high_deck = [Artifact, Beast, Broken_One, Dark_Lord, Donjon, Seer, Ghost, Executioner, Horseman, Innocent, Marionette, Mists, Raven, Tempter]

#Commmon Deck cards below
Avenger = Cards("Avenger", "common_deck", "The treasure lies in the dragon's house, in the hands once clean - now corrupted", "The treasure is in the possession of Vladimir Horngaard in Argynvostholt", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/4.png")
Paladin = Cards("Paladin", "common_deck", "I see a sleeping prince, a servant of light and the brother of darkness. The treasure lies with him", "The treasure lies in Sergei's tomb (area K85)", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/37.png")
Soldier = Cards("Soldier", "common_deck", "Go to the mountains. Climb the white tower guarded by golden knights", "The treasure lies on the rooftop of the Tsolenka Pass guard tower", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/44.png")
Mercenary = Cards("Mercenary", "common_deck", "The thing you seek lies with the dead, under mountains of gold coins", "The treasure lies in a crypt in Castle Ravenloft (area K84, crypt 31)", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/29.png")
Myrmidon = Cards("Myrmidon", "common_deck", "Look for a den of wolves in the hills overlooking a mountain lake. The treasure belongs to Mother Night", "The treasure lies in a shrine of Mother Night in the werewolf den (ch.15 area Z7)", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/35.png")
Berserker = Cards("Berserker", "common_deck", "Find the Mad Dog's crypt. The treasure lies within,beneath blackened bones", "The treasure lies in the crypt of General Kroval \"Mad Dog\" Grislek (ch4, area K84, crypt 38)", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/7.png")
Hooded_One = Cards("Hooded_One", "common_deck", "I see a faceless god. He awaits you at the end of a long and winding road, deep in the mountains. ", "The treasure is inside the head of the giant statue in the Amber Temple (chapter 13, area X5a). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/24.png")
Dictator = Cards("Dictator", "common_deck", "I see a throne fit for a king. ", "The treasure lies in Castle Ravenloft's audience hall (chapter 4, area K25).", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/13.png")
Torturer = Cards("Torturer", "common_deck", "There is a town where all is not well. There you will find a house of corruption, and within, a dark room full of still ghosts. ", "The treasure is hidden in the attic of the burgomaster's mansion in Vallaki (chapter 4: area N3s)", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/49.png")
Warrior = Cards("Warrior", "common_deck", "That which you seek lies in the womb of darkness, the devil's lair: the one place to which he must return. ", "The treasure lies in Strahd's tomb (chapter 4, area K86) .", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/53.png")
Transmuter = Cards("Transmuter", "common_deck", "Go to a place of dizzying heights, where the stone itself is alive! ", "The treasure lies in Castle Ravenloft's north tower peak (chapter 4, area K60)", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/52.png")
Diviner = Cards("Diviner", "common_deck", "Look to the one who sees all. The treasure is hidden in her camp. ", "The treasure lies in Madam Eva's encampment (chapter 2, area G). If she is the one performing the card reading, she says, \"I think the treasure is under my very nose!\"", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/14.png")
Enchanter = Cards("Enchanter", "common_deck", "I see a kneeling woman-a rose of great beauty plucked too soon. The master of the marsh knows of whom I speak. ", "The treasure lies under Marina's monument in Berez (chapter 10, area US). \"The master of the marsh\" refers to Burgomaster Lazio Ulrich (area U2), whose ghost can point characters toward the monument. ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/18.png")
Abjurer = Cards("Abjurer", "common_deck", "I see a fallen house guarded by a great stone dragon. Look to the highest peak. ", "The treasure lies in the beacon of Argynvostholt (chapter 7, area Q53). \"Great stone dragon\" refers to the statue in area Ql. ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/1.png")
Elementalist = Cards("Elementalist", "common_deck", "The treasure is hidden in a small castle beneath a mountain, guarded by amber giants. ", "The treasure is inside a model of Castle Ravenloft in the Amber Temple (chapter 13, area X20).", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/17.png")
Evoker = Cards("Evoker", "common_deck", "Search for the crypt of a wizard ordinaire. His staff is the key. ", "The treasure is hidden in.the crypt of Gralmore Nimblenobs (chapter 4, area K84, crypt 37). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/19.png")
Illusionist = Cards("Illusionist", "common_deck", "A man is not what he seems. He comes here in a carnival wagon. Therein lies what you seek.", "The treasure lies in Rictavio's carnival wagon (chapter 5, area NS). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/26.png")
Necromancer = Cards("Necromancer", "common_deck", "A woman hangs above a roaring fire. Find her, and you will find the treasure. ", "The treasure lies in Castle Ravenloft's study (chapter 4, area K37). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/36.png")
Conjurer = Cards("Conjurer", "common_deck", "I see a dead village, drowned by a river, ruled by one who has brought great evil into the world. ", "The treasure is in Baba Lysaga's hut (chapter 10 , area U3). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/11.png")
Wizard = Cards("Wizard", "common_deck", "Look for a wizard's tower on a lake. Let the wizard's name and servant guide you to that which you seek.", "The treasure lies on the top floor of Van Richten's Tower (chapter 11, area V7). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/54.png")
Swashbuckler = Cards("Swashbuckler", "common_deck", "I see the skeleton of a deadly warrior, lying on a bed of stone flanked by gargoyles. ", "The treasure lies in the crypt of Endorovich (chapter 4, area K84, crypt 7). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/45.png")
Philanthropist = Cards("Philanthropist", "common_deck", "Look to a place where sickness and madness are bred. Where children once cried, the treasure lies still. ", "The treasure is in the nursery of the Abbey of Saint Markovia (chapter 8, area S23). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/38.png")
Trader = Cards("Trader", "common_deck", "Look to the wizard of wines! In wood and sand the treasure hides. ", "The treasure lies in the glassblower's workshop in the Wizard of the Wines winery (chapter 12, area W10)", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/50.png")
Merchant = Cards("Merchant", "common_deck", "Seek a cask that once contained the finest wine, of which not a drop remains. ", "The treasure lies in Castle Ravenloft's wine cellar (chapter 4, area K63). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/30.png")
Guild_Member = Cards("Guild_Member", "common_deck", "I see a dark room full of bottles. It is the tomb of a guild member. ", "The treasure lies in the crypt of Artank Swilovich (chapter 4, area K84, crypt 5)", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/22.png")
Beggar = Cards("Beggar", "common_deck", "A wounded elf has what you seek. He will part with the treasure to see his dark dreams fulfilled. ", "The treasure is hidden in Kasimir's hovel (chapter 5, area N9a). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/6.png")
Thief = Cards("Thief", "common_deck", "What you seek lies at the crossroads of life and death, among the buried dead. ", "The treasure is buried in the graveyard at the River Ivlis crossroads (chapter 2, area F). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/48.png")
Tax_Collector = Cards("Tax_Collector", "common_deck", "The Vistani have what you seek. A missing child holdsthe key to the treasure's release.", "The treasure is hidden in the Vistani treasure wagon (chapter 5, area N9i). \"A missing child\" refers to Arabelle (see chapter 2, area L).", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/46.png")
Miser = Cards("Miser", "common_deck", "Look for a fortress inside a fortress, in a place hidden behind fire. ", "The treasure lies in Castle Ravenloft's treasury (chapter 4, area K41). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/31.png")
Rogue = Cards("Rogue", "common_deck", "I see a nest of ravens. There you will find the prize.", "The treasure is hidden in the attic of the Blue Water Inn (chapter 5, area N2q).", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/41.png")
Monk = Cards("Monk", "common_deck", "The treasure you seek is hidden behind the sun, in the house of a saint.", "The treasure lies in the main hall of the Abbey of Saint Markovia (chapter 8, area S13). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/34.png")
Missionary = Cards("Missionary", "common_deck", "I see a garden dusted with snow, watched over by a scarecrow with a sackcloth grin. Look not to the garden but to the guardian. ", "The treasure is hidden inside one of the scarecrows in the garden of the Abbey of Saint Markovia (chapter 8, area S9). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/32.png")
Healer = Cards("Healer", "common_deck", "Look to the west. Find a pool blessed by the light of the white sun. ", "The treasure lies beneath the gazebo in the Shrine of the White Sun (chapter 8, area S4). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/23.png")
Shepherd = Cards("Shepherd", "common_deck", "Find the mother she who gave birth to evil.", "The treasure lies in the tomb of King Barov and Queen Ravenovia (chapter 4, area K88). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/43.png")
Druid = Cards("Druid", "common_deck", "An evil tree grows atop a hill of graves where the ancient dead sleep. The ravens can help you find it. Look for the treasure there. ", "The treasure lies at the base of the Gulthias free (chapter 14, area Y4). Any wereraven encountered in the wilderness can lead the characters to the location.", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/16.png")
Anarchist = Cards("Anarchist", "common_deck", "I see walls of bones, a chandelier of bones, and a table of bones-all that remains of enemies long forgotten. ", "The treasure lies in Castle Ravenloft's hill of bones (chapter 4, area K67).", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/2.png")
Charlatan = Cards("Charlatan", "common_deck", "I see a lonely mill on a precipice. The treasure lies within.", "The treasure lies in the attic of Old Bonegrinder (chapter 6, area 04). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/10.png")
Bishop = Cards("Bishop", "common_deck", "What you seek lies in a pile of treasure, beyond a set of amber doors. ", "The treasure lies in the sealed treasury of the Amber Temple (chapter 13, area X40). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/8.png")
Traitor = Cards("Traitor", "common_deck", "Look for a wealthy woman. A staunch ally of the devil, she keeps the treasure under lock and key, with the bones of an ancient enemy. ", "The treasure is hidden in the master bedroom of Wachterhaus (chapter 5, area N4o).", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/51.png")
Priest = Cards("Priest", "common_deck", "You will find what you seek in the castle, amid the ruins of a place of supplication.", "The treasure lies in Castle Ravenloft's chapel (chapter 4, area K15). ", "", "", r"E:\15. Programming/Learning-to-Code/Python/Own Projects/Tarokka_Reading/39.png")

common_deck = [Avenger, Paladin, Soldier, Mercenary, Myrmidon, Berserker, Hooded_One, Dictator, Torturer, Warrior, Transmuter, Diviner, Enchanter, 
               Abjurer, Elementalist, Evoker, Illusionist, Necromancer, Conjurer, Wizard, Swashbuckler, Philanthropist, Trader, Merchant, Guild_Member, Beggar, Thief, Tax_Collector, 
               Miser, Rogue, Monk, Missionary, Healer, Shepherd, Druid, Anarchist, Charlatan, Bishop, Traitor, Priest]

#simple function checking if the player is the dm
def dm_test():
    counter = 0        
    while counter == 0:
        dm = input("Are you the dm? y/n")
        if dm == 'y':
            dm = True
            counter += 1
        if dm == 'n':
            dm = False
            counter += 1
        else:
            continue
    return dm

dm = dm_test()
print(Charlatan)

###Code for story to be below: For starters from Codecademy course
######
# TREENODE CLASS
######
class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    self.choices.append(node)

  def traverse(self):
    story_node = self
    print(story_node.story_piece)
    while len(story_node.choices) > 0:
      choice = input("Enter 1 or 2 to continue the story: ")
      if choice not in ["1", "2"]:
        print("Invalid choice. Try again.")
      else:
        chosen_index = int(choice)
        chosen_index -= 1
        chosen_child = story_node.choices[chosen_index]
        print(chosen_child.story_piece)
        story_node = chosen_child

######
# VARIABLES FOR TREE

story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")

choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

story_root.add_child(choice_a)
story_root.add_child(choice_b)

choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.
 
YOU REMAIN LOST.
""")

choice_b_1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.
 
YOU REMAIN LOST.
""")

choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)
story_root.traverse()
######
# user_choice = input('What is your name?')
# print(user_choice)

######
# TESTING AREA
######


