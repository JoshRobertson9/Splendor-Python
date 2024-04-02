
def theLoop():
    pass
    GameState = True

    while GameState == True:
        


        
        
        GameState = False



def PlayerAction():
    
    print("What will you do? Type the corresponding number.")
    print("Option 1: ")


    u = input("")

    match u:
        case 1:
            pass
        case 2:
            return "Diamond (White)"
        case 2 | "S":
            return "Sapphire (Blue)"
        case 3 | "O":
            return "Onyx (Black)   "
        case _ :
            print("Error: Invalid Input.")


