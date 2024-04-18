# Existing Modules
import json
import os

# My Modules
import game_start as GS
import game_loop as GL
import game_end as GE
import player_class as PC
import winner_calc as WC

# Intro Text
freeze = input("\nHello and welcome to Splendor - Python Edition.\n")


# Load Save?
print("Would you like to load an existing game save?")
load_save_ans = input('Type "yes" if you wanted to load the save, otherwise a new game will start.\n')


# Load Save Decision
if load_save_ans == "yes" or load_save_ans == "y": 
    #print("Thanks for trying to load a save. This feature doesnt't quite work yet and will start the usual way for now.\n")
    #player_list, board_tokens, noble_cards, dclo, dclt, dclr = GS.introText()
    # Loading the Save data
    with open("game_save.json") as file:
        data = json.load(file)

    # Extracting Variables
    board_tokens = data[0]
    noble_cards = data[1]
    dclo = data[2]['Deck1']
    dclt = data[2]['Deck2']
    dclr = data[2]['Deck3']

    player_list = []
    for player_data in data[3]:
        player = PC.Player(player_data['name'])
        player.points = player_data['points']
        player.tokens = player_data['tokens']
        player.card_power = player_data['card_power']
        player.card_list = player_data['card_list']
        player.card_hold = player_data['card_hold']
        player.noble_count = player_data['noble_count']
        player.coinsList = player_data['coinsList']
        player.DevelopmentCards = player_data['DevelopmentCards']
        player_list.append(player)

    print("Success! The save data has been loaded.")
    input("Press enter to start the game.")
    os.system('cls' if os.name == 'nt' else 'clear')

else:
    #Game Start and Player Setup
    player_list, board_tokens, noble_cards, dclo, dclt, dclr = GS.introText()


# Playing the Game Loop
GL.theLoop(player_list, board_tokens, noble_cards, dclo, dclt, dclr)


# Winner Announcement
WC.winner_calc(player_list)


# Game Wrap Up
GE.end_text()