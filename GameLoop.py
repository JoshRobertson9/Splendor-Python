# Existing Imports
import os
import random

# My Imports
import DevelopmentCards as DC
import PlayerClass as PC
import noble_cards as NC



def theLoop(player_list):
    
    num_players = len(player_list)

    board_tokens = {'green': 4, 'white': 4, 'blue': 4, 'black': 4, 'red': 4, 'gold': 5}

    # Prep Tokens
    match num_players:
        case 2:
            board_tokens = {'green': 4, 'white': 4, 'blue': 4, 'black': 4, 'red': 4, 'gold': 5}
        case 3:
            board_tokens = {'green': 5, 'white': 5, 'blue': 5, 'black': 5, 'red': 5, 'gold': 5}
        case 4:
            board_tokens = {'green': 7, 'white': 7, 'blue': 7, 'black': 7, 'red': 7, 'gold': 5}
        case _ :
            print("Error: Invalid Number of players listed.")

    # Prep Nobles
    NC.prep_nobles(num_players)


    # Start of the game loop
    GameState = True

    while GameState == True:

        # All players will take a turn. 
        for n in range(num_players):


            #Display user's status
            player_list[n].displayStatus()

            print("___________________________________\n")

            #Display noble cards
            print("Noble Cards:", NC.noble_card_deck)

            print("___________________________________\n")

            # Display available cards
            DC.three_levels_display()

            print("___________________________________\n")

            # Display available tokens
                # Create token display
            print("These are the available tokens to draw from.")
            #print("Pick 3 different tokens or 2 of the same, or the Joker (Gold) and 1 card to hold.")
            print(board_tokens)

            print("___________________________________\n")

            #The person's turn
            PlayerAction(player_list[n],board_tokens,player_list)

            # Post-turn follow up actions

            # Update player's card power
            player_list[n].card_power_calc()

            # Checks if they qualified for a noble card and gives one if so
                # may just pick for now if the qualify for two and later update to let the player decide
            player_list[n].check_nobles(NC.noble_card_deck)



            # Points update for that player
            player_list[n].points_update()

            # If someone's points > = 15 -> Gamestate = False
            if player_list[n].points >= 15:
                print("Someone just got 15 or more points. The game ends after this round.")
                GameState = False

            # turn end text
            filler = input("Your turn has ended. Press enter to move to the next player.")

            # Clears the terminal after each peron's turn
            # Fake clear because it doesn't clear the scroll buffer
            print("\n" * 50)

            #os.system('cls' if os.name == 'nt' else 'clear')


def PlayerAction(player,board_tokens,player_list):
    print()
    print("What will you do? Type the corresponding number and then press enter.")
    print("Option 1 - Pick Tokens")
    print("Option 2 - Buy a Card")
    print("Option 3 - Display all user's details")

    choice = int(input("What will it be?: "))

    match choice:
        case 1:
            # Pick Tokens
            player.pick_up_tokens(board_tokens)
            # Display Tokens
            pass
        case 2:
            # Buy card
            pass
            card_num = int(input("Please provide the number of the card that you would like. "))

            match card_num:
                case 1 | 2 | 3 | 4 :
                    selected_card = DC.dev_cards_lvl_one_copy.pop(card_num-1)
                    player.card_list.append(selected_card)
                case 5 | 6 | 7 | 8:
                    selected_card = DC.dev_cards_lvl_two_copy.pop(card_num-1-4)
                    player.card_list.append(selected_card)
                case 9 | 10 | 11 | 12:
                    selected_card = DC.dev_cards_lvl_three_copy.pop(card_num-1-8)
                    player.card_list.append(selected_card)
                case _:
                    print("Incorrect input, please try again.")
                    PlayerAction(player,board_tokens,player_list)

        case 3:
            # Display other user's scores
            print("\nHere are the details of all the players")
            for n in range(len(player_list)):
                player_list[n].displayStatus()
                print()
            print("____________________________\n")
            PlayerAction(player,board_tokens,player_list)

        case _ :
            # Re-loops through the action questions
            print("Incorrect input, please try again.")
            PlayerAction(player,board_tokens,player_list)

