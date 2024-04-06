import ColorAlign as CA
from token_manager import TokenManager 

class Player:
    def __init__(self,name):
        self.name = name
        self.points = 0
        #self.tokens = TokenManager({'green': 2, 'white': 2, 'blue': 2, 'black': 2, 'red': 2, 'gold': 0})
        self.tokens = {'green': 2, 'white': 2, 'blue': 2, 'black': 2, 'red': 2, 'gold': 0}
        self.card_power = {'green': 2, 'white': 2, 'blue': 2, 'black': 2, 'red': 2, 'gold': 0}
        self.card_list = []
        self.card_hold = []
        self.noble_count = 0

        # All coins including jokers
        self.coinsList = [0 for _ in range(6)]

        # List of the indexes of all dev cards that the user has
        self.DevelopmentCards = []

    def displayStatus(self):
        print("Player Status")
        print("Name:", self.name)
        print("Total Points:",self.points)
        print("Total Tokens:    ", self.tokens)
        print("Total Card Power:", self.card_power)
        #iter = 0
        #for coin in self.coinsList:
        #    print(CA.colorAlign(iter) + ":",coin)
        #    iter += 1


    def card_power_calc(self):
        # Updates based on the dev cards held

        # Resets to 0 and then recounts it all from there.
        self.card_power = {'green': 0, 'white': 0, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}

        #print(self.card_list)

        for card in self.card_list:
            key = card[0]
            self.card_power[key] += 1

            """
            card_dict = card[2]
            #print("CARD", card)
            for key in card_dict:
                #print("KEY", key)
                #print(card[key])
                self.card_power[key] += card_dict[key]
            """

    def points_update(self):

        card_points = 0

        for card in self.card_list:
            card_points += card[1]

        # Each noble is worth 3 points, so you just need to retain the count of them you have.
        self.points = card_points + (self.noble_count)*3

    def check_nobles(self,noble_deck):
        #print(noble_deck)
        match_list = []
        iter = 0

        players_power = self.dict_to_list()

        for noble in noble_deck:

            comparison_result = []
            # Looks through each noble to see 
            for i in range(len(noble)):
                #print("This noble: ", noble)
                #print("This players_power: ", players_power)

                comparison_result.append(players_power[i] >= noble[i])

            #print("Comp Res:",comparison_result)
            # After getting the comparison result, it checks if all are true and if so it adds to match list
            if all(comparison_result):
                match_list.append(iter)

            iter += 1

        #print("This is the match list: ",match_list)

        if match_list:
            print()
            # If the list isn't empty it will remove the first match in the list of matches and update the score
            if len(match_list) > 1:
                print("You could actually get more than 1 of the noble cards, but can only 1 per turn.")
            #print(noble_deck)
            noble_deck.pop(match_list[0])
            self.noble_count += 1
            print("You just earned a noble card! Your points will increase by 3.")
            print("Current Noble Count:", self.noble_count)
            #print("Here are the remaining noble cards.")
            #print(noble_deck)


    def dict_to_list(self):
        power_list = []
        # Could update this later to iterate through a list of these strings
        power_list.append(self.card_power['green'])
        power_list.append(self.card_power['white'])
        power_list.append(self.card_power['blue'])
        power_list.append(self.card_power['black'])
        power_list.append(self.card_power['red'])
        power_list.append(self.card_power['gold'])
        #print("This is my power list for the player ",power_list)
        return power_list        


    # Player Actions
        
    # Picks Tokens
    def pick_up_tokens(self,board_tokens):
        # This method should have all of the error handling etc
        print("\nNow pick 2 of the same token, 3 different tokens, or the Gold Joker and a card.")
        print("Select the tokens that you would like in the following format.")
        print("  [Green, White, Blue, Black, Red, Gold (Joker)]")
        print("Ex. 1,      1,    0,     1,    0,   0 but with no spaces for 1 Green, 1 White, and 1 Black")
        # Could make this a lot more user friendly. Could just ask each color at a time.
        choice = input("Provide your input here: ")
        # For now going to assume that people input this correctly. Could check the size.

        #Turning the input into a list

        choice_list = choice.split(",")
        choice_list_int = [int(x) for x in choice_list]
        print(choice_list_int)

        #Turn choices into a dictionary
        choice_dict = {'green': 0, 'white': 0, 'blue': 0, 'black': 0, 'red': 0, 'gold': 0}

        choice_dict['green'] = choice_list_int[0]
        choice_dict['white'] = choice_list_int[1]
        choice_dict['blue'] = choice_list_int[2]
        choice_dict['black'] = choice_list_int[3]
        choice_dict['red'] = choice_list_int[4]
        choice_dict['gold'] = choice_list_int[5]

        print("Choice Dict: ",choice_dict)

        # The Tokens
        #board_tokens - is a dict
        #token_deck = [1,2,3,4,5,6]
        """
        token_deck = [
            board_tokens['green'],
            board_tokens['white'],            
            board_tokens['blue'],
            board_tokens['black'],
            board_tokens['red'],
            board_tokens['gold']
        ]
        print(token_deck)
        """

        #Add tokens by taking them from the board game
        #self.tokens.add_tokens()

        num_tokens = sum(choice_list_int)

        # Need to add error handling for people buying jokers with other stuff......***

        # Check whether the input is too big or too small
        if num_tokens > 3 | num_tokens <= 0:
            pass
            print("You picked too many tokens, too little, or a negative amount. Nothing will happen.")
            self.pick_up_tokens(board_tokens)

        # Check if 3, that all are different
        elif num_tokens == 3:
            # Only 1 token of each, so max would be 1 
            if max(choice_list_int) == 1:
                #Draw those 3 from the pile
                for key in choice_dict:
                    # increase player count by _ amount
                    self.tokens[key] += choice_dict[key]
                    # decrease token count by _ amount
                    board_tokens[key] -= choice_dict[key]

            else: 
                # Incorrect input, start token selection again.
                print("All 3 tokens must be the same amount.")
                print("Please pick again.")
                self.pick_up_tokens(board_tokens)

        # Checks if 2 of the same were picked
        elif num_tokens == 2:
            # Two of the same selected
            if max(choice_list_int) == 2:
                #Draw those 2 cards
                for key in choice_dict:
                    # increase player count by _ amount
                    self.tokens[key] += choice_dict[key]
                    # decrease token count by _ amount
                    board_tokens[key] -= choice_dict[key]

            else:
                print("You provided something wrong.")
                print("Please pick again.")
                self.pick_up_tokens(board_tokens)

        elif num_tokens == 1 and choice_list_int[5] == 1 :
            #Joker Token situation handling

            # increase joker count by _ amount
            self.tokens['gold'] += choice_dict['gold']
            # decrease token count by _ amount
            board_tokens['gold'] -= choice_dict['gold']

            # Add the card to the player's hand.
            print("Still need to add the card to the player's hand too...")
            #self.card_hold.append()

        else:
            print("Something went wrong. Please re-enter your choice.")
            self.pick_up_tokens(board_tokens)

    def buy_card(self,card_list):
        pass
        self.card_list.append()


#Testing
"""       
P1 = Player("Josh")
P1.displayStatus()
"""