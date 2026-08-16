import json

def end_text():
    
    playagain = str(input("Would you like to play again? Type 'yes' or else the game will end. "))

    if playagain == "yes":
        # Delete the old save file. It'll be written over anyways, but wanted to give it a fresh start
        with open("game_save.json","w") as j_file:
            j_file.write("")
    
        # Restarts the game
        import play_splendor as PS

    else:
        print("Thanks for playing, the game will now end!")
