
#Imports
import GameStart as GS
import GameLoop as GL
import GameEnd as GE


#Game Start and Player Setup

a,b = GS.introText()

print(a.name)


# Playing the Game Loop

GL.theLoop()


# Game Wrap Up

GE.endText()



