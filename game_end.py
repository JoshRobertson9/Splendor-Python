def end_text():
    playagain = str(input("Would you like to play again? Type 'yes' or else the game will end. "))

    if playagain == "yes":
        import play_splendor as PS

    else:
        print("Thanks for playing, the game will now end!")
