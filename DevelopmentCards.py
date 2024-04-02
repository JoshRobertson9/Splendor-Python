import ColorAlign as CA


# [CardColor, [costColorArray], PointsWorth, CardLevel]

# [Green, White, Blue, Black, Red, Gold]

DevelopmentCards = [

["E", [0, 1, 1, 2, 1], 0, 1 ],
["D", [4, 0, 0, 0, 0], 1, 1 ],
["R", [0, 3, 0, 0, 0], 0, 1 ],
["S", [1, 1, 0, 1, 1], 0, 1 ],
["S", [3, 0, 1, 0, 1], 0, 1 ],
["S", [0, 1, 0, 2, 0], 0, 1 ],
["D", [0, 0, 3, 0, 0], 0, 1 ],




]



#print(DevelopmentCards[0])

def PrintCard(index):

    #The Card's Color
    print("The Color       :", CA.colorAlign(DevelopmentCards[index][0]))

    #The Card's Points

    print("Points Worth    : " , DevelopmentCards[index][2])

    #The Card's Level

    print("The Card's Level: " , DevelopmentCards[index][3])

    #The Card's Cost
    print("The Cost:")
    iter = 0
    for cost in DevelopmentCards[index][1]:

        #Switch this back to 0 instead of -1 if you want to exclude the 0's
        if cost > -1:
            print(CA.colorAlign(iter), ":", cost)

        iter += 1
    print()


#Test Case
PrintCard(1)

PrintCard(2)

for num in range(0,11):
    PrintCard(num)
