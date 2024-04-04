
#Imports
import GameStart as GS
import GameLoop as GL
import GameEnd as GE
import PlayerClass as PC
import winner_calc as WC

#Game Start and Player Setup
player_list = GS.introText()



# Playing the Game Loop
GL.theLoop(player_list)


# Winner Announcement
WC.winner_calc(player_list)


# Game Wrap Up

GE.endText()



