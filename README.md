Hello, here is my recreation of the board game Splendor.

This is a chance to demonstrate my python skills, practice making games, and potentially add some analysis of the game and computer players.

This project now works with the exception of being able to buy with jokers and a few things might break if you tried really hard to, but as a whole you can get from the start of the game to the end as intended.

The game is currently text based, which isn't as easy to play, but it was fun to see how to make the best of that.

Below are some of my development notes for future development and past lessons learned.

Future Development

    Could add a rules explanation at the start of the game.

    Additional minor error proofing throughout.
    
    Colored fonts to make it easier to read.

    Could display the total number of remaining cards in a level deck

    Can't use Jokers to buy yet.

    Can take tokens even if it goes negative.

    Further compliance with PEP8

    Could make the noble cards more visually appealing

    Reduce code redudnancy

    Could try to "solve" the game based on which cards held could lead to free purchase of other cards and how that stacks and then rank which to pick first because they lead to so many others. Could make a bot that does this. Each card is essentially scored based on this to determine which to pick next.


What I'm learning / Lessons Learned

    Managing many modules while maintaining the necessary access to data

    Standard Pythton data types and common loops

    Practice with Git and Github

    Some user interface and input

    Practice aligning with PEP8

    Make it less easy to break. Responds to incorrect user entry

    Using dictionaries

    Using Chat GPT to assist in some code development. Simulates working with another team member to develop code. Only about 5% of this code is copied from.

    The way you implement a solution can and does matter, but sometimes its best to just get started and change it from there. Hard to solve it all in your head.

    used several existing modules. os, copy, & random.

    cls has an error and won't delete the scrollback buffer so had to make a workaround for that.

    Don't use multiple line quotes (triple quotes) within a list. This will cause an issue...

    Making this game text based in not the ideal way to play this game, but it was fun to try to see how to make the best of that situation and see what creative fixes could be applied there. (Added line breaks, cleared the terminal, moved outputs from multiple lines into a single line.)

    Sometimes writing the comment of things to add in the future takes more time than to just fix it now.

    Sometimes you have to delete code you worked hard on if its no longer the best solution.


