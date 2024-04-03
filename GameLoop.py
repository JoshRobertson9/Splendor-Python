from DevelopmentCards import three_levels_display
import PlayerClass as PC

def theLoop(player):
    pass
    GameState = True

    while GameState == True:
        
        #Display user's status
        player.displayStatus()

        # Display available cards
        three_levels_display

        # Display available tokens
            # Create coin display
        

        #The person's turn

        PlayerAction(player)


        # If someone's points > = 15 -> Gamestate = False

        GameState = False





def PlayerAction(player):
    print()
    print("What will you do? Type the corresponding number.")
    print("Option 1 - Pick Tokens")
    print("Option 2 - Buy Cards")
    print("Option 3 - Display Nobile Tiles")
    print("Option 4 - Display other user's scores")

    choice = int(input("What will it be?: "))

    match choice:
        case 1:
            # Pick Tokens
            player.pick_up_tokens()
            #Display Tokens
            pass
        case 2:
            # Buy cards
            pass
        case 3:
            # 
            pass
        case 4:
            # Display other user's scores
            pass
        case _ :
            #Re-loops through the action questions
            print("Incorrect input, please try again.")
            PlayerAction()



