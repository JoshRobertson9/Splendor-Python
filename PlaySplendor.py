
#Imports
import GameStart as GS
import GameLoop as GL
import GameEnd as GE
import PlayerClass as PC


#Game Start and Player Setup

P1,P2,P3,P4,num_Players = GS.introText()

# print(P1.name)
# P1.displayStatus()

# Playing the Game Loop
GL.theLoop(P1)


# Game Wrap Up

GE.endText()



