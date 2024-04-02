
import PlayerClass as PC

def introText():
    print("Hello and welcome to Splendor - Python Edition.")
    numPlayers = int(input("How many humans are playing? Please provide a number 2-4. "))

    P1 = PC.Player(input("What is the name of player 1? "))    
    print(P1.name)

    P2 = PC.Player(input("What is the name of player 2? "))    
    print(P2.name)

    if numPlayers > 2:
        P3 = PC.Player(input("What is the name of player 3? "))    
        print(P3.name)

    if numPlayers > 3:
        P4 = PC.Player(input("What is the name of player 4? "))    
        print(P4.name)

    print("The ends the setup phase. Time to start the same")

    return P1, P2

    # Add picking or assigning player order randomly later

#introText()


