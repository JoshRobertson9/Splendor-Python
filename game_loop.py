# Existing Modules
import os
import random

# My Modules
import development_cards as DC
import player_class as PC
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
            player_list[n].display_status()

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

            # Points update for that player - resets to 0 and re-calculates it.
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
    print("Option 2 - Buy a Development Card")
    print("Option 3 - Select Development Card & Joker to Reserve")
    print("Option 4 - Purchase a held Development Card")
    print("Option 5 - Display all user's details")

    # Need to add error handling for non-int's
    try:
        choice = int(input("What will it be?: "))
    except ValueError:
        choice = 0

    match choice:
        case 1:
            # Pick Tokens
            player.pick_up_tokens(board_tokens)
            # Display Tokens

        case 2:
            # Buy card
            try:
                card_num = int(input("Please provide the number of the card that you would like. "))
            except ValueError:
                card_num = 0

            match card_num:
                case 1 | 2 | 3 | 4 :

                    sel_card = DC.dev_cards_lvl_one_copy[card_num - 1]
                    sel_card_dict = sel_card[2]

                    # Chat gpt helped me write the below line a little bit.
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
                        selected_card = DC.dev_cards_lvl_one_copy.pop(card_num-1)
                        player.card_list.append(selected_card)

                    else:
                        print("Sorry, but you cannot afford this one. Try again.")
                        PlayerAction(player,board_tokens,player_list)

                case 5 | 6 | 7 | 8:
                    
                    sel_card = DC.dev_cards_lvl_two_copy[card_num - 1 - 4]
                    sel_card_dict = sel_card[2]

                    # Chat gpt helped me write the below line a little bit.
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
                        selected_card = DC.dev_cards_lvl_two_copy.pop(card_num-1-4)
                        player.card_list.append(selected_card)

                    else:
                        print("Sorry, but you cannot afford this one. Try again.")
                        PlayerAction(player,board_tokens,player_list)


                case 9 | 10 | 11 | 12:

                    sel_card = DC.dev_cards_lvl_three_copy[card_num - 1 - 8]
                    sel_card_dict = sel_card[2]

                    # Chat gpt helped me write the below line a little bit.
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
                        selected_card = DC.dev_cards_lvl_three_copy.pop(card_num-1-8)
                        player.card_list.append(selected_card)

                    else:
                        print("Sorry, but you cannot afford this one. Try again.")
                        PlayerAction(player,board_tokens,player_list)


                case _:
                    print("Incorrect input, please try again.")
                    PlayerAction(player,board_tokens,player_list)

        # Select Dev Card
        case 3:

            if board_tokens['gold'] <= 0:
                print("Sorry no Joker more tokens to select. Please choose something else.")
                PlayerAction(player,board_tokens,player_list)

            else:
                # Assumes people put in a correct number.    
                card_num = int(input("Please provide the number of the card that you would like (1-12). "))

                #if card_num < 1 | card_num > 12:

                match card_num:
                    case 1 | 2 | 3 | 4 :
                        selected_card = DC.dev_cards_lvl_one_copy.pop(card_num-1)
                        player.card_hold.append(selected_card)

                    case 5 | 6 | 7 | 8 :
                        selected_card = DC.dev_cards_lvl_two_copy.pop(card_num-1-4)
                        player.card_hold.append(selected_card)

                    case 9 | 10 | 11 | 12 :
                        selected_card = DC.dev_cards_lvl_three_copy.pop(card_num-1-8)
                        player.card_hold.append(selected_card)

                board_tokens['gold'] -= 1
                player.tokens['gold'] += 1
                print("The Card has been reserved.")


        # Buying a Dev Card
        case 4:
            if player.card_hold == []:
                print("You don't have any card's held to buy.")
                print("Please make a different selection")
                PlayerAction(player,board_tokens,player_list)

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
                    PlayerAction(player,board_tokens,player_list)

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
                    PlayerAction(player,board_tokens,player_list)

        # Display Scores
        case 5:
            # Display other user's scores
            print("\nHere are the details of all the players")
            for index, player in enumerate(player_list):
                player.display_status()
                print()
            print("____________________________\n")
            PlayerAction(player,board_tokens,player_list)

        # Anything else.
        case _ :
            # Re-loops through the action questions
            print("Incorrect input, please try again.")
            PlayerAction(player,board_tokens,player_list)

