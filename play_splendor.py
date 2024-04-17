# My Modules
import game_start as GS
import game_loop as GL
import game_end as GE
import player_class as PC
import winner_calc as WC


print("\nHello and welcome to Splendor - Python Edition.\n")

print("Would you like to load an existing game save?")
load_save_ans = input('Type "yes" if you wanted to load the save, otherwise a new game will start.')

if load_save_ans == "yes" or load_save_ans == "y": 
    print("Thanks for trying to load a save. This feature doesnt't quite work yet and will start the usual way for now.\n")
    player_list = GS.introText()

else:
    #Game Start and Player Setup
    player_list = GS.introText()



# Playing the Game Loop
GL.theLoop(player_list)

# Winner Announcement
WC.winner_calc(player_list)

# Game Wrap Up
GE.end_text()