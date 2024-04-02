


def endText():
    playagain = str(input("Would you like to play again? Type 'yes' or else the game will end. "))

    if playagain == "yes":
        pass
        #Is it right to import it like this to loop through the game again??
        import PlaySplendor as PS

    else:
        print("Thanks for playing, the game will now end!")


