
import PlayerClass as PC

def introText():
    print("Hello and welcome to Splendor - Python Edition.")
    num_players = int(input("How many humans are playing? Please provide a number 2-4. "))

    #This section could possibly be made into a player array later, that may be more dynamic and manageable

    P1 = PC.Player(input("What is the name of player 1? "))    
    print(P1.name)

    P2 = PC.Player(input("What is the name of player 2? "))    
    print(P2.name)

    player_list = []

    player_list.append(P1)
    player_list.append(P2)
    #print(player_list)
    #player_list[1].displayStatus()

    if num_players > 2:
        P3 = PC.Player(input("What is the name of player 3? "))    
        print(P3.name)
        player_list.append(P3)

    if num_players > 3:
        P4 = PC.Player(input("What is the name of player 4? "))    
        print(P4.name)
        player_list.append(P4)

        if num_players > 4:
            print("Sorry, only 4 people at most can play at a time. Take turns and let them play next time!")

    print("This ends the setup phase. Time to start the game\n")

    return player_list


