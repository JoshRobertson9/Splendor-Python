#Standard Imports
import copy
import random

#My Imports
import ColorAlign as CA

# Old Card Format
# [CardColor, [costColorList], PointsWorth, CardLevel]

# New Card Format
# [CardColor, PointValue, CardCostDict]
# [Green, White, Blue, Black, Red, Gold]


dev_cards_lvl_one = [

["green", 0, {'green': 1, 'white': 0, 'blue': 1, 'black': 1, 'red': 0, 'gold': 0}],
["white", 1, {'green': 4, 'white': 0, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}],
["red", 0, {'green': 0, 'white': 3, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}],
["blue", 0, {'green': 1, 'white': 1, 'blue': 0, 'black': 1, 'red': 1, 'gold': 0}],
["blue", 0, {'green': 3, 'white': 0, 'blue': 1, 'black': 0, 'red': 1, 'gold': 0}],
["blue", 0, {'green': 0, 'white': 1, 'blue': 0, 'black': 2, 'red': 0, 'gold': 0}],
["white", 0, {'green': 0, 'white': 0, 'blue': 3, 'black': 0, 'red': 0, 'gold': 0}],

["red", 0, {'green': 1, 'white': 2, 'blue': 0, 'black': 2, 'red': 0, 'gold': 0}],
["red", 0, {'green': 0, 'white': 1, 'blue': 0, 'black': 3, 'red': 1, 'gold': 0}],
["green", 0, {'green': 0, 'white': 0, 'blue': 1, 'black': 2, 'red': 2, 'gold': 0}],
["red", 0, {'green': 1, 'white': 2, 'blue': 1, 'black': 1, 'red': 0, 'gold': 0}],
["green", 0, {'green': 0, 'white': 0, 'blue': 2, 'black': 0, 'red': 2, 'gold': 0}],
["blue", 0, {'green': 2, 'white': 0, 'blue': 0, 'black': 2, 'red': 0, 'gold': 0}],
["blue", 0, {'green': 1, 'white': 1, 'blue': 0, 'black': 1, 'red': 2, 'gold': 0}],
["black", 0, {'green': 0, 'white': 2, 'blue': 2, 'black': 0, 'red': 1, 'gold': 0}],
["green", 1, {'green': 0, 'white': 0, 'blue': 0, 'black': 4, 'red': 0, 'gold': 0}],
["green", 0, {'green': 0, 'white': 1, 'blue': 1, 'black': 1, 'red': 1, 'gold': 0}],
["red", 0, {'green': 1, 'white': 1, 'blue': 1, 'black': 1, 'red': 0, 'gold': 0}],
["red", 1, {'green': 0, 'white': 4, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}],

["red", 0, {'green': 0, 'white': 2, 'blue': 0, 'black': 0, 'red': 2, 'gold': 0}],
["white", 0, {'green': 2, 'white': 0, 'blue': 1, 'black': 1, 'red': 1, 'gold': 0}],
["white", 0, {'green': 0, 'white': 0, 'blue': 2, 'black': 2, 'red': 0, 'gold': 0}],
["white", 0, {'green': 0, 'white': 3, 'blue': 1, 'black': 1, 'red': 0, 'gold': 0}],
["blue", 0, {'green': 2, 'white': 1, 'blue': 0, 'black': 0, 'red': 2, 'gold': 0}],
["blue", 1, {'green': 0, 'white': 0, 'blue': 0, 'black': 0, 'red': 4, 'gold': 0}],
["black", 0, {'green': 1, 'white': 1, 'blue': 1, 'black': 0, 'red': 1, 'gold': 0}],
["black", 0, {'green': 3, 'white': 0, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}],
["red", 0, {'green': 1, 'white': 0, 'blue': 2, 'black': 0, 'red': 0, 'gold': 0}],
["white", 0, {'green': 0, 'white': 0, 'blue': 0, 'black': 1, 'red': 2, 'gold': 0}],
["green", 0, {'green': 0, 'white': 2, 'blue': 1, 'black': 0, 'red': 0, 'gold': 0}],
["black", 0, {'green': 1, 'white': 1, 'blue': 2, 'black': 0, 'red': 1, 'gold': 0}],
["green", 0, {'green': 1, 'white': 1, 'blue': 3, 'black': 0, 'red': 0, 'gold': 0}],
["white", 0, {'green': 2, 'white': 0, 'blue': 2, 'black': 1, 'red': 0, 'gold': 0}],
["white", 0, {'green': 1, 'white': 0, 'blue': 1, 'black': 1, 'red': 1, 'gold': 0}],
["black", 1, {'green': 0, 'white': 0, 'blue': 4, 'black': 0, 'red': 0, 'gold': 0}],
["green", 0, {'green': 0, 'white': 0, 'blue': 0, 'black': 0, 'red': 3, 'gold': 0}],
["black", 0, {'green': 2, 'white': 2, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}],
["black", 0, {'green': 2, 'white': 0, 'blue': 0, 'black': 0, 'red': 1, 'gold': 0}],
["black", 0, {'green': 1, 'white': 0, 'blue': 0, 'black': 1, 'red': 3, 'gold': 0}],
["blue", 0, {'green': 0, 'white': 0, 'blue': 0, 'black': 3, 'red': 0, 'gold': 0}]

]

# Development Card Deck Level 2 - not updated yet
dev_cards_lvl_two = [

["red", 2, {'green': 0, 'white': 0, 'blue': 0, 'black': 5, 'red': 0, 'gold': 0}],
["white", 2, {'green': 0, 'white': 0, 'blue': 0, 'black': 3, 'red': 5, 'gold': 0}],
["black", 3, {'green': 0, 'white': 0, 'blue': 0, 'black': 6, 'red': 0, 'gold': 0}],
["green", 1, {'green': 2, 'white': 3, 'blue': 0, 'black': 0, 'red': 3, 'gold': 0}],
["red", 1, {'green': 0, 'white': 2, 'blue': 0, 'black': 3, 'red': 2, 'gold': 0}],
["green", 2, {'green': 0, 'white': 4, 'blue': 2, 'black': 1, 'red': 0, 'gold': 0}],
["white", 1, {'green': 0, 'white': 2, 'blue': 3, 'black': 0, 'red': 3, 'gold': 0}],
["blue", 1, {'green': 2, 'white': 0, 'blue': 2, 'black': 0, 'red': 3, 'gold': 0}],
["blue", 2, {'green': 0, 'white': 5, 'blue': 3, 'black': 0, 'red': 0, 'gold': 0}],
["black", 1, {'green': 2, 'white': 3, 'blue': 2, 'black': 0, 'red': 0, 'gold': 0}],
["black", 2, {'green': 0, 'white': 5, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}],
["green", 2, {'green': 3, 'white': 0, 'blue': 5, 'black': 0, 'red': 0, 'gold': 0}],
["white", 1, {'green': 3, 'white': 0, 'blue': 0, 'black': 2, 'red': 2, 'gold': 0}],
["blue", 2, {'green': 0, 'white': 2, 'blue': 0, 'black': 4, 'red': 1, 'gold': 0}],
["red", 2, {'green': 2, 'white': 1, 'blue': 4, 'black': 0, 'red': 0, 'gold': 0}],
["red", 2, {'green': 0, 'white': 3, 'blue': 0, 'black': 5, 'red': 0, 'gold': 0}],
["blue", 1, {'green': 3, 'white': 0, 'blue': 2, 'black': 3, 'red': 0, 'gold': 0}],
["white", 2, {'green': 1, 'white': 0, 'blue': 0, 'black': 2, 'red': 4, 'gold': 0}],

["white", 2, {'green': 0, 'white': 0, 'blue': 0, 'black': 0, 'red': 5, 'gold': 0}],
["red", 1, {'green': 0, 'white': 0, 'blue': 3, 'black': 3, 'red': 2, 'gold': 0}],
["green", 2, {'green': 5, 'white': 0, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}],
["green", 1, {'green': 0, 'white': 2, 'blue': 3, 'black': 2, 'red': 0, 'gold': 0}],
["green", 3, {'green': 6, 'white': 0, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}],
["red", 3, {'green': 0, 'white': 0, 'blue': 0, 'black': 0, 'red': 6, 'gold': 0}],
["black", 2, {'green': 5, 'white': 0, 'blue': 0, 'black': 0, 'red': 3, 'gold': 0}],
["blue", 3, {'green': 0, 'white': 0, 'blue': 6, 'black': 0, 'red': 0, 'gold': 0}],
["white", 3, {'green': 0, 'white': 6, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}],
["blue", 2, {'green': 0, 'white': 0, 'blue': 5, 'black': 0, 'red': 0, 'gold': 0}],
["black", 1, {'green': 3, 'white': 3, 'blue': 0, 'black': 2, 'red': 0, 'gold': 0}],
["black", 2, {'green': 4, 'white': 0, 'blue': 1, 'black': 0, 'red': 2, 'gold': 0}]

]

# Development Card Deck Level 3 - not updated yet
dev_cards_lvl_three = [

["white", 3, {'green': 3, 'white': 0, 'blue': 3, 'black': 3, 'red': 5, 'gold': 0}],
["black", 4, {'green': 3, 'white': 0, 'blue': 0, 'black': 3, 'red': 6, 'gold': 0}],
["blue", 4, {'green': 0, 'white': 7, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}],
["blue", 4, {'green': 0, 'white': 6, 'blue': 3, 'black': 3, 'red': 0, 'gold': 0}],
["green", 4, {'green': 3, 'white': 3, 'blue': 6, 'black': 0, 'red': 0, 'gold': 0}],
["green", 3, {'green': 0, 'white': 5, 'blue': 3, 'black': 3, 'red': 3, 'gold': 0}],
["blue", 3, {'green': 3, 'white': 3, 'blue': 0, 'black': 5, 'red': 3, 'gold': 0}],
["red", 3, {'green': 3, 'white': 3, 'blue': 5, 'black': 3, 'red': 0, 'gold': 0}],
["blue", 5, {'green': 0, 'white': 7, 'blue': 3, 'black': 0, 'red': 0, 'gold': 0}],
["white", 4, {'green': 0, 'white': 0, 'blue': 0, 'black': 7, 'red': 0, 'gold': 0}],
["red", 4, {'green': 6, 'white': 0, 'blue': 3, 'black': 0, 'red': 3, 'gold': 0}],
["black", 3, {'green': 5, 'white': 3, 'blue': 3, 'black': 0, 'red': 3, 'gold': 0}],
["black", 4, {'green': 0, 'white': 0, 'blue': 0, 'black': 0, 'red': 7, 'gold': 0}],
["white", 5, {'green': 0, 'white': 3, 'blue': 0, 'black': 7, 'red': 0, 'gold': 0}],
["white", 4, {'green': 0, 'white': 3, 'blue': 0, 'black': 6, 'red': 3, 'gold': 0}],
["red", 5, {'green': 7, 'white': 0, 'blue': 0, 'black': 0, 'red': 3, 'gold': 0}],
["red", 4, {'green': 7, 'white': 0, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}],
["green", 4, {'green': 0, 'white': 0, 'blue': 7, 'black': 0, 'red': 0, 'gold': 0}],
["black", 5, {'green': 0, 'white': 0, 'blue': 0, 'black': 3, 'red': 7, 'gold': 0}],
["green", 5, {'green': 3, 'white': 0, 'blue': 7, 'black': 0, 'red': 0, 'gold': 0}]

]


# Inputs are list of cards and which index of that list to show.
def PrintCard(card_list,index):

    # Color and Point Value
    print("Color | Point Value | Cost: ", card_list[index][0] , "|", str(card_list[index][1]), "|", card_list[index][2])

    #The Card's Color
    #print("The Color:   " + card_list[index][0])
    #print("The Color       :", CA.colorAlign(card_list[index][0]))

    #The Card's Points
    #print("Points Worth: " + str(card_list[index][1]))
    #print("Points Worth    :" , card_list[index][2])

    #The Card's Cost
    #print("Card Cost:  ", card_list[index][2])
    """
    print("The Cost:")
    iter = 0
    for cost in card_list[index][1]:

        #Switch this back to 0 instead of -1 if you want to exclude the 0's
        if cost > -1:
            print(CA.colorAlign(iter), ":", cost)

        iter += 1
    print()
    """

#Test Case
"""
PrintCard(dev_cards_lvl_one,1)

PrintCard(dev_cards_lvl_one,2)

for num in range(0,4):
    PrintCard(dev_cards_lvl_one,num)
"""

#Card Deck Copies
dev_cards_lvl_one_copy = copy.deepcopy(dev_cards_lvl_one)
dev_cards_lvl_two_copy = copy.deepcopy(dev_cards_lvl_two)
dev_cards_lvl_three_copy = copy.deepcopy(dev_cards_lvl_three)


#Shuffle Cards
random.shuffle(dev_cards_lvl_one_copy)
random.shuffle(dev_cards_lvl_two_copy)
random.shuffle(dev_cards_lvl_three_copy)


#PrintCard(dev_cards_lvl_three_copy,0)

#Display the top 4 cards of a deck
def display_top_four(card_list):
    
    lvl_len = len(card_list)
    #print(lvl_len)

    if lvl_len >=4:
        for n in range(4):
            #print("Number:",n+1)
            PrintCard(card_list,n)
            print()

    elif lvl_len >= 1:
        for n in range(lvl_len):
            #print("Number:",n+1)
            PrintCard(card_list,n)
            print()

    elif lvl_len == 0:
        print("This deck is empty.")
        print()

    else:
        print("Something is wrong with the card deck.")


#Example:
#display_top_four(dev_cards_lvl_three_copy)


#Display the three levels

def three_levels_display():

    print("Level 1 (cards 1-4):")
    display_top_four(dev_cards_lvl_one_copy)

    print("____\n")

    print("Level 2 (cards 5-8):")
    display_top_four(dev_cards_lvl_two_copy)

    print("____\n")

    print("Level 3 (cards 9-12):")
    display_top_four(dev_cards_lvl_three_copy)

    #print("____\n")

#three_levels_display()
# Removing Card from list and returning it
# The player will be able to add to their deck or reserve pile

def removecard(card_list,index):
    card = card_list.pop(index)
    return card


#removecard(dev_cards_lvl_three_copy,0)
#three_levels_display()



