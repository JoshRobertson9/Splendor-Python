# My Modules
import game_start as GS
import game_loop as GL
import game_end as GE
import player_class as PC
import winner_calc as WC

#Game Start and Player Setup
player_list = GS.introText()

# Playing the Game Loop
GL.theLoop(player_list)

# Winner Announcement
WC.winner_calc(player_list)

# Game Wrap Up
GE.end_text()