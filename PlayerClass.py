import ColorAlign as CA
from token_manager import TokenManager 

class Player:
    def __init__(self,name):
        self.name = name
        self.points = 0
        self.tokens = TokenManager({'green': 0, 'white': 0, 'blue': 0, 'white': 0, 'black': 0, 'gold': 0})
        self.card_power = {'green': 1, 'white': 0, 'blue': 1, 'white': 0, 'black': 1, 'gold': 0}


        # All coins including jokers
        self.coinsList = [0 for _ in range(6)]

        # List of the indexes of all dev cards that the user has
        self.DevelopmentCards = []

    def displayStatus(self):
        print("Player Status")
        print("Name:", self.name)
        print("Points:",self.points)
        print("Total Tokens:")
        print(self.tokens)
        print("Total Card Power:")
        print(self.card_power)
        iter = 0
        for coin in self.coinsList:
            print(CA.colorAlign(iter) + ":",coin)
            iter += 1


    def card_power_calc(self):
        # Needs to update based on the dev cards held
        self.card_power = {'green': 1, 'white': 0, 'blue': 1, 'white': 0, 'black': 1, 'gold': 0}

    # Player Actions
        
    # Picks Tokens
    def pick_up_tokens(self):
        # This method should have all of the error handling etc
        print("Now pick 2 of the same token, 3 different tokens, or the Gold Joker and a card.")
        print("Select the coins that you would like in the following format.")
        print("[Green, White, Blue, Black, Red, Gold (Joker)]")
        print("Ex. 1,1,0,1,0,0 for 1 Green, 1 White, and 1 Black")

        choice = input("Provide your input here:")
        # For now going to assume that people input this correctly. Could check the size.

        #Turning the input into a list

        choice_list = choice.split(",")

        choice_list_int = [int(x) for x in choice_list]

        print(choice_list_int)

        # Palceholder value, will connect this to the actual board later
        token_deck = [1,2,3,4,5,6]
        print(token_deck)

        #Add tokens by taking them from the board game
        #self.tokens.add_tokens()

        num_tokens = sum(choice_list_int)

        # Need to add error handling for people buying jokers with other stuff......***

        # Check whether the input is too big or too small
        if num_tokens > 3 | num_tokens <= 0:
            pass
        
        # Check if 3, that all are different
        elif num_tokens == 3:
            # Only 1 token of each, so max would be 1 
            if max(choice_list_int) == 1:
                #Draw those 3 from the pile
                pass
            else: 
                # Incorrect input, start token selection again.
                print("All 3 tokens must be the same amount.")
                print("Please pick again.")
                self.pick_up_tokens()

        elif num_tokens == 2:
            # Two of the same selected
            if max(choice_list_int) == 2:
                #Draw those 2 cards
                pass
            else:
                print("You provided something wrong.")
                print("Please pick again.")


        elif num_tokens == 1 and choice_list_int[5] == 1 :
            pass
            #Joker Token situation handling

        else:
            print("Something went wrong. Please re-enter your choice.")





#Testing
"""       
P1 = Player("Josh")
P1.displayStatus()
"""