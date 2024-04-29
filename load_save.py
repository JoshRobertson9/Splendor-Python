# Existing Modules
import json
import os

# My Modules
import player_class as PC

# Function to load the save data from the json save file.
def load_save(file_name):

    with open(file_name) as file:
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


    return player_list, board_tokens, noble_cards, dclo, dclt, dclr