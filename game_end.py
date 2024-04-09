def end_text():
    playagain = str(input("Would you like to play again? Type 'yes' or else the game will end. "))

    if playagain == "yes":
        #Is it right to import it like this to loop through the game again??
        import play_splendor as PS

    else:
        print("Thanks for playing, the game will now end!")


