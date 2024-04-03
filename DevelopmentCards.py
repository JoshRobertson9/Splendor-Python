#Standard Imports
import copy
import random

#My Imports
import ColorAlign as CA



# [CardColor, [costColorArray], PointsWorth, CardLevel]

# [Green, White, Blue, Black, Red, Gold]

dev_cards_lvl_one = [

["E", [0, 1, 1, 2, 1], 0, 1 ],
["D", [4, 0, 0, 0, 0], 1, 1 ],
["R", [0, 3, 0, 0, 0], 0, 1 ],
["S", [1, 1, 0, 1, 1], 0, 1 ],
["S", [3, 0, 1, 0, 1], 0, 1 ],
["S", [0, 1, 0, 2, 0], 0, 1 ],
["D", [0, 0, 3, 0, 0], 0, 1 ],

]

# Development Card Deck Level 2 - not updated yet
dev_cards_lvl_two = [

["E", [0, 1, 1, 2, 1], 0, 1 ],
["D", [4, 0, 0, 0, 0], 1, 1 ],
["R", [0, 3, 0, 0, 0], 0, 1 ],
["S", [1, 1, 0, 1, 1], 0, 1 ],
["S", [3, 0, 1, 0, 1], 0, 1 ],
["S", [0, 1, 0, 2, 0], 0, 1 ],
["D", [0, 0, 3, 0, 0], 0, 1 ],

]

# Development Card Deck Level 3 - not updated yet
dev_cards_lvl_three = [

["E", [0, 1, 1, 2, 1], 0, 1 ],
["D", [4, 0, 0, 0, 0], 1, 1 ],
["S", [1, 1, 0, 1, 1], 0, 1 ]

]


"""
["R", [0, 3, 0, 0, 0], 0, 1 ],
["S", [3, 0, 1, 0, 1], 0, 1 ],
["S", [0, 1, 0, 2, 0], 0, 1 ],
["D", [0, 0, 3, 0, 0], 0, 1 ],
"""




# Inputs are list of cards and which index of that list to show.
def PrintCard(card_list,index):

    #The Card's Color
    print("The Color       :", CA.colorAlign(card_list[index][0]))

    #The Card's Points
    print("Points Worth    :" , card_list[index][2])

    #The Card's Level
    #print("The Card's Level: " , card_list[index][3])

    #The Card's Cost
    print("The Cost:")
    iter = 0
    for cost in card_list[index][1]:

        #Switch this back to 0 instead of -1 if you want to exclude the 0's
        if cost > -1:
            print(CA.colorAlign(iter), ":", cost)

        iter += 1
    print()


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

    elif lvl_len >= 1:
        for n in range(lvl_len):
            #print("Number:",n+1)
            PrintCard(card_list,n)

    elif lvl_len == 0:
        print("This deck is empty.")

    else:
        print("Something is wrong with the card deck")


#Example:
#display_top_four(dev_cards_lvl_three_copy)


#Display the three levels

def three_levels_display():

    print("Level 1 cards (1-4):")

    display_top_four(dev_cards_lvl_one_copy)

    print("Level 2 cards (5-8):")

    display_top_four(dev_cards_lvl_two_copy)

    print("Level 3 cards (9-12):")

    display_top_four(dev_cards_lvl_three_copy)



three_levels_display()








