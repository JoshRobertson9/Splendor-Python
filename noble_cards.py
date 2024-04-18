# Existing Modules
import random

noble_card_deck = [
[4,0,4,0,0,0],
[0,0,0,4,4,0],
[3,3,3,0,0,0],
[0,3,0,3,3,0],
[0,4,0,4,0,0],
[4,0,0,0,4,0],
[0,4,4,0,0,0],
[3,0,3,0,3,0],
[3,0,0,3,3,0],
[0,3,3,3,0,0]
]

# Preps the nobles deck for gameplay
def prep_nobles(num_players):
    # Randomly sort
    random.shuffle(noble_card_deck)

    # Remove all but the needed cards (n players + 1)
    del noble_card_deck[-(10-num_players-1):]    
    return noble_card_deck
"""
print(noble_card_deck)
prep_nobles(4)
print(noble_card_deck)
"""