# Aethyr Poker
A poker game that is heavily inspired by Leisterez Poker from the Roblox Game [Terminal Escape Room](https://www.roblox.com/games/14026026722/Terminal-Escape-Room).

## Rationale
While the game this was inspired on was initially an escape room (that personally felt tedious to do with all the puzzles and it being targeted for solo play compared to group play), one of the rooms (or should I say subpuzzles?) involved a fictional card game that involves a different deck of cards compared to the traditional 52 cards. Laid out was *the entire mechanics of the Poker game (including ones that was not needed for the escape room)* which seemed fun to play on its own. Hence, this is the fully-fledged game on its own from my (BluNuggets) interpretation of the game 
## Mechanics
Unlike the traditional 4 suits of 13 cards, *Aethyr Poker* uses a deck ~~with one Phoenix Card and~~ 3 suits (Flames, Circuits, Puzzles) each made up of 12 cards:
- 9 **Number** Cards (1, 2, 3, 4, 5, 6, 7, 8, 9)
- 2 **Child** Cards
- 1 **President** Card

In addition, there are three copies of each suit, resulting in a total of ~~109~~ 108 cards. (To change the amount of copies or lessen the number of cards, change the `COPIES` variable in `model.py`)
### Setting Up the Game
At the beginning of the game, the user is asked to determine how many players will play the game. Afterward, three cards will be given to each player and a random President Card will be placed at the *center cards*.

### During the Game
The Gameplay consists of *Terms*, which are similar to one another. At the beginning of every term, 2 cards will be discarded into the discard pile and 2 cards will be drawn and placed to the center cards, with the exception of the *first term*. The first term discards 2 cards and only places one card from the deck into the center cards.

**Action Phase** \
Players will have an option to do the following in a Round Robin fashion:
- Discard one Card : Remove one card from the player's personal hand and draw a card from the deck.
- Inaugurate a Child Card : More details below
- Pass : Do nothing during the term

**Inauguration Phase** \
The Inauguration Phase will occur when the following conditions are met:
- The player has a Child card
- There is a President card in the center cards
- An Inauguration Phase has not yet happened during the term (ex: The first player has already Inaugurated a Child Card)

If at least one condition was not met, the Inauguration Phase will not continue and the player will be asked to select another action.
Given the conditions, the player will be able to *swap their Child card with a President card in play*.

### End of the Game (Scoring System)
WIP

## Running the Game
Simply run the code in the terminal using the command `py main.py` (Windows), `python main.py` (Windows, Mac), or`python3 main.py` (Linux). Alternatively, you can run the `main.py` file in your preferred code editor.

## Limitations
- The game was created with Python 3.12.0. Some modules (such as `StrEnum`) may not work as intended when running the game lower versions of Python.
- At the moment, the Phoenix Card has not yet been implemented.
- The outputs are currently only outputted through the terminal. Plans to update the game into one with UI Design (pygame, textual, etc.) are unforseeable in the future.

## Acknowledgements
Huge thanks to the team behind [Terminal Escape Room](https://www.roblox.com/games/14026026722/Terminal-Escape-Room) as this has started the (mostly impulsive) implementation of their room.
