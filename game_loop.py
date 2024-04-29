# Existing Modules
import os
import random
import json

# My Modules
import development_cards as DC
import player_class as PC
#import noble_cards as NC

def theLoop(player_list,board_tokens,noble_cards, dclo, dclt, dclr):

    #round_num = 1

    # Start of the game loop
    GameState = True

    while GameState == True:

        # All players will take a turn. 
        for player in player_list:

            # Display the board
            display_board(player, noble_cards, board_tokens, dclo, dclt, dclr)

            # The Player's turn
            player_action(player, board_tokens, player_list, dclo, dclt, dclr)

            # Post-turn Player updates
            player_update(player,noble_cards)
            
            # If Player's points >= 15 then Gamestate = False
            if player.points >= 15:
                print("Someone just got 15 or more points. The game ends after this round.")
                GameState = False

            # End of Player turn text
            filler = input("Your turn has ended. Press enter to move to the next player.")

            # "Clears" the terminal after each peron's turn
            print("\n" * 50)

        # Option to save the Game
        #save_q = input(f"That ends round {round_num}. Would you like to save the game? (yes) ")
        save_q = input(f"The current round has now ended. Would you like to save the game? If so, type 'yes'. ")
        #round_num += 1
        #save_q = "yes"

        if save_q == "yes":

            # Display other user's scores
            #print("Right now this just saves the player data.")
            #player.display_status()
            #players_json_string = json.dumps(player,indent=4)
            #players_json_string = player.toJSON()

            file_path = "game_save.json"


            with open(file_path,"w") as j_file:
                j_file.write("[\n")
                
                # Writing the board tokens to the JSON
                #j_file.write("\n")
                json.dump(board_tokens,j_file, indent=4)
                j_file.write(",\n")


                # Writing the noble card deck to the JSON
                #j_file.write("\n")
                json.dump(noble_cards,j_file, indent=4)
                j_file.write(",\n")

                # Writing the Development card decks to the JSON
                #json.dump(dev_cards_lvl_one_copy,j_file, indent=4)
                #j_file.write(",\n")
                dev_card_decks_dict = {"Deck1": dclo,"Deck2": dclt, "Deck3" : dclr}
                json.dump(dev_card_decks_dict,j_file, indent=4)
                j_file.write(",\n")

                # Writing the Player List to the JSON
                j_file.write("[\n")
                # j_file.write(players_json_string)
                
                for pl in player_list:
                    j_file.write(pl.toJSON())
                    if pl is not player_list[-1]:
                        j_file.write(",")

                j_file.write("\n]")
                j_file.write("\n]")

            print("The player data has been saved!")
            lll = input("Press enter to continue the game and your turn.")
        
        print("\n" * 50)


def display_board(player, noble_cards, board_tokens, dclo, dclt, dclr):
    
    # Display user's status
    player.display_status()
    print("___________________________________\n")

    # Display noble cards
    print("Noble Cards:", noble_cards)
    print("___________________________________\n")

    # Display available cards
    DC.three_levels_display(dclo, dclt, dclr)
    print("___________________________________\n")

    # Display available tokens
    print("These are the available tokens to draw from.")
    print(board_tokens)
    print("___________________________________\n")


def player_action(player, board_tokens, player_list, dclo, dclt, dclr):
    print("\nWhat will you do? Type the corresponding number and then press enter.")
    print("Option 1 - Pick Tokens")
    print("Option 2 - Buy a Development Card")
    print("Option 3 - Select Development Card & Joker to Reserve")
    print("Option 4 - Purchase a held Development Card")
    print("Option 5 - Display all user's details")
    #print("Option 6 - Save the game and exit")
    #print("Player Name:", player.return_name())

    # Need to add error handling for non-int's
    try:
        choice = int(input("What will it be?: "))
    except ValueError:
        choice = 0

    match choice:
        # Pick Tokens
        case 1:
            player.pick_up_tokens(board_tokens)

        # Buy card
        case 2:
            
            try:
                card_num = int(input("Please provide the number of the card that you would like. "))
            except ValueError:
                card_num = 0

            match card_num:
                case 1 | 2 | 3 | 4 :

                    sel_card = dclo[card_num - 1]
                    sel_card_dict = sel_card[2]

                    # Chat gpt helped me write the below line a little bit.
                    if all(value <= (player.tokens[key] + player.card_power.get(key,0))  for key, value in sel_card_dict.items()):
                        
                        buy_card(player, dclo, sel_card_dict, board_tokens, card_num, 0)

                    else:
                        print("Sorry, but you cannot afford this one. Try again.")
                        player_action(player, board_tokens, player_list, dclo, dclt, dclr)

                case 5 | 6 | 7 | 8:
                    
                    sel_card = dclt[card_num - 1 - 4]
                    sel_card_dict = sel_card[2]

                    # Chat gpt helped me write the below line a little bit.
                    if all(value <= (player.tokens[key] + player.card_power.get(key,0))  for key, value in sel_card_dict.items()):
                        buy_card(player, dclt, sel_card_dict, board_tokens, card_num, 4)

                    else:
                        print("Sorry, but you cannot afford this one. Try again.")
                        player_action(player, board_tokens, player_list, dclo, dclt, dclr)

                case 9 | 10 | 11 | 12:

                    sel_card = dclr[card_num - 1 - 8]
                    sel_card_dict = sel_card[2]

                    # Chat gpt helped me write the below line a little bit.
                    if all(value <= (player.tokens[key] + player.card_power.get(key,0))  for key, value in sel_card_dict.items()):
                        buy_card(player, dclr, sel_card_dict, board_tokens, card_num, 8)
                        
                    else:
                        print("Sorry, but you cannot afford this one. Try again.")
                        player_action(player, board_tokens, player_list, dclo, dclt, dclr)

                case _:
                    print("Incorrect input, please try again.")
                    player_action(player, board_tokens, player_list, dclo, dclt, dclr)

        # Select Dev Card
        case 3:

            if board_tokens['gold'] <= 0:
                print("Sorry no Joker more tokens to select. Please choose something else.")
                player_action(player, board_tokens, player_list, dclo, dclt, dclr)

            else:
                # Assumes people put in a correct number.    
                card_num = int(input("Please provide the number of the card that you would like (1-12). "))
                # Doesn't error handle for a number outside of that range

                match card_num:
                    case 1 | 2 | 3 | 4 :
                        selected_card = dclo.pop(card_num-1)
                        player.card_hold.append(selected_card)

                    case 5 | 6 | 7 | 8 :
                        selected_card = dclt.pop(card_num-1-4)
                        player.card_hold.append(selected_card)

                    case 9 | 10 | 11 | 12 :
                        selected_card = dclr.pop(card_num-1-8)
                        player.card_hold.append(selected_card)

                board_tokens['gold'] -= 1
                player.tokens['gold'] += 1
                print("The Card has been reserved.")

        # Buying a Dev Card
        case 4:
            if player.card_hold == []:
                print("You don't have any card's held to buy.")
                print("Please make a different selection")
                player_action(player, board_tokens, player_list, dclo, dclt, dclr)

            else :
                print("Here are the cards you can choose from")
                for card in player.card_hold:
                    print("Color | Point Value | Cost: ", card[0] , "|", str(card[1]), "|", card[2])

                try:
                    selection = int(input("Type the number of the card you want to buy: ")) - 1
                except ValueError:
                    selection = -1

                if selection < 0 | selection > len(player.card_hold):
                    print("You have selected an invalid option. Please try again.")
                    player_action(player, board_tokens, player_list, dclo, dclt, dclr)

                # We now know the list is not empty and the user has selected a real option

                selected_card = player.card_hold[selection]
                sel_card_dict = selected_card[2]

                # The following code is coped from case two with only slight modifications.
                # Would be nice to clean this up and create re-usable functions for this at some point.
                if all(value <= (player.tokens[key] + player.card_power.get(key,0))  for key, value in sel_card_dict.items()):
                    #print("You can afford this card!")

                    # Remove tokens and put back into the pile
                    rem_card_cost = {'green': 0, 'white': 0, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}

                    for key in rem_card_cost:
                        if sel_card_dict[key] - player.card_power[key] > 0:
                            rem_card_cost[key] = sel_card_dict[key] - player.card_power[key]
                        elif sel_card_dict[key] - player.card_power[key] <= 0:
                            rem_card_cost[key] = 0

                        player.tokens[key] -= rem_card_cost[key]
                        board_tokens[key] += rem_card_cost[key]

                    print("The development card has been successfully purchased.")

                    # Adding the card to the player's list
                    selected_card = player.card_hold.pop(selection)
                    player.card_list.append(selected_card)

                else:
                    print("Sorry, but you cannot afford this one. Try again.")
                    player_action(player, board_tokens, player_list, dclo, dclt, dclr)

        # Display All Player's Scores
        case 5:
            # Display other user's scores
            print("\nHere are the details of all the players")
            for index, player in enumerate(player_list):
                player.display_status()
                print()
            print("____________________________\n")
            player_action(player, board_tokens, player_list, dclo, dclt, dclr)

        # Save (and Exit) Game
        case 11:
            print("You skipped your turn with the secret code.")

        # Anything else
        case _ :
            # Re-loops through the action questions
            print("Incorrect input, please try again.")
            player_action(player, board_tokens, player_list, dclo, dclt, dclr)


def player_update(player,noble_cards):

    # Update player's card power
    player.card_power_calc()

    # Checks if they qualified for a noble card and gives one if so
    player.check_nobles(noble_cards)

    # Points update for that player - resets to 0 and re-calculates it.
    player.points_update()


# Buying the card if is allowed
def buy_card(player, deck, sel_card_dict, board_tokens, card_num, offset):

    # Remove tokens and put back into the pile
    rem_card_cost = {'green': 0, 'white': 0, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}

    for key in rem_card_cost:
        if sel_card_dict[key] - player.card_power[key] > 0:
            rem_card_cost[key] = sel_card_dict[key] - player.card_power[key]
        elif sel_card_dict[key] - player.card_power[key] <= 0:
            rem_card_cost[key] = 0

        player.tokens[key] -= rem_card_cost[key]
        board_tokens[key] += rem_card_cost[key]

    print("The development card has been successfully purchased.")

    # Adding the card to the player's list
    selected_card = deck.pop(card_num - 1 - offset)
    player.card_list.append(selected_card)

