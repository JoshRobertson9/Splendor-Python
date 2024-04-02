import ColorAlign as CA


class Player:
    def __init__(self,name):
        self.name = name
        self.points = 0

        # All coins including jokers
        self.coinsList = [0 for _ in range(6)]


        # List of the indexes of all dev cards that the user has
        self.DevelopmentCards = []

    def displayStatus(self):
        print("Player Status")
        print("Name:", self.name)
        print("Points:",self.points)
        print("Total Coins:")
        iter = 0
        for coin in self.coinsList:
            print(CA.colorAlign(iter) + ":",coin)
            iter += 1

#Testing
        
#P1 = Player("Josh")
#P1.displayStatus()

