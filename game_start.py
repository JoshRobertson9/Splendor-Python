# Existing Modules
import os
import random

# My Modules
import player_class as PC
import noble_cards as NC
import development_cards as DC

def introText():

    # Player Initialization
    try:
        num_players = int(input("How many people are playing? No computer players are available at this time.\nPlease provide a number 2-4. "))
    except ValueError:
        print("Invalid input for the number of players. Number of players is now set to 2.\n")
        num_players = 2

    if num_players < 2:
        print("The number of players it too low. It has been rounded up to the minimum required amount of 2.")
        num_players = 2
    
    if num_players > 4:
        print("Sorry, only 4 people at most can play at a time. Take turns and let them play next time!")
        num_players = 4

    player_list = []

    for i in range(1,num_players+1):
        player_list.append(PC.Player(input(f"What is the name of player {i}? ")))

    # Shuffling the player order
    random.shuffle(player_list)
    print("\nThe player order has been randomly shuffled.")

    # Board Token initialization
    match len(player_list):
        case 2:
            board_tokens = {'green': 4, 'white': 4, 'blue': 4, 'black': 4, 'red': 4, 'gold': 5}
        case 3:
            board_tokens = {'green': 5, 'white': 5, 'blue': 5, 'black': 5, 'red': 5, 'gold': 5}
        case 4:
            board_tokens = {'green': 7, 'white': 7, 'blue': 7, 'black': 7, 'red': 7, 'gold': 5}
        case _ :
            # This shouldn't happen because it should be constrained to 2, 3, or 4 from earlier, but kept just in case
            print("Error: Invalid Number of players listed.")

    # Preparing Noble Cards
    noble_cards = NC.prep_nobles(len(player_list))

    # Preparing the Development Cards
    dclo, dclt, dclr = DC.create_card_decks()

    # The end of the game setup
    print("This ends the setup phase. Time to start the game.")
    input("Press enter to start the game.")
    os.system('cls' if os.name == 'nt' else 'clear')

    return player_list, board_tokens, noble_cards, dclo, dclt, dclr

if __name__ == "__main__":
    player_list, board_tokens, noble_cards, dclo, dclt, dclr = introText()
    