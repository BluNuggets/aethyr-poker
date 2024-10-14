#Common types across Aethyr Poker components

from __future__ import annotations
from typing import NewType, Protocol
from enum import StrEnum, IntEnum

class Action(StrEnum):
    PASS = 'Pass'
    DISCARD = 'Discard'
    INAUGURATE = 'Inaugurate'

class Rank(IntEnum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    #Avoiding the Straight
    Child = 11
    President = 12
    #Avoiding the Straight Again
    Phoenix = 14
    
class Suit(IntEnum):
    NoSuit = 0
    Flames = 1
    Circuits = 2
    Puzzles = 3
    
