# My Modules
from load_save import load_save
import game_start as GS
import game_loop as GL
import winner_calc as WC
import game_end as GE

def play_splendor():

    # Intro Text
    input("\nHello and welcome to Splendor - Python Edition (press enter to continue)\n")


    # Load Save?
    print("Would you like to load an existing game save?")
    load_save_ans = input('Type "yes" if you wanted to load the save, otherwise a new game will start.\n')


    # Load Save Decision
    if load_save_ans == "yes" or load_save_ans == "y":

        # Loading the Save data
        player_list, board_tokens, noble_cards, dclo, dclt, dclr = load_save("game_save.json")

    else:
        #Game Start and Player Setup
        player_list, board_tokens, noble_cards, dclo, dclt, dclr = GS.introText()


    # Playing the Game Loop
    GL.theLoop(player_list, board_tokens, noble_cards, dclo, dclt, dclr)


    # Winner Announcement
    WC.winner_calc(player_list)


    # Game Wrap Up
    GE.end_text()


if __name__ == "__main__":
    play_splendor()
