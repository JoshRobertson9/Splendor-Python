
# [CardColor, [costColorArray], PointsWorth, CardLevel]

# [Green, White, Blue, Black, Red, Gold]

DevelopmentCards = [

["E", [0, 1, 1, 2, 1], 0, 1 ],
["D", [4, 0, 0, 0, 0], 1, 1 ],
["R", [0, 3, 0, 0, 0], 0, 1 ],


]

#Returns the appropriate description string based on which token type is being referenced.

def colorAlign(i):
    match i:
        case 0 | "E":
            return "Emerald (Green)"
        case 1 | "D":
            return "Diamond (White)"
        case 2:
            return "Sapphire (Blue)"
        case 3:
            return "Onyx (Black)"
        case 4:
            return "Ruby (Red)"
        case 5:
            return "Gold (Yellow)"


#print(DevelopmentCards[0])

def PrintCard(index):

    #The Card's Color
    print("The Color:")
    print(colorAlign(DevelopmentCards[index][0]))
    print()

    #The Card's Cost
    print("The Cost:")
    iter = 0
    for cost in DevelopmentCards[index][1]:

        #Switch this back to 0 instead of -1 if you want to exclude the 0's
        if cost > -1:
            print(colorAlign(iter), ":", cost)

        iter += 1

    #The Card's Points
    print()
    print("Points Worth:")
    print(DevelopmentCards[index][2])

    #The Card's Level
    print()
    print("The Card's Level:")
    print(DevelopmentCards[index][3])


#Test Case
PrintCard(1)

#for card in DevelopmentCards:
#    PrintCard()
