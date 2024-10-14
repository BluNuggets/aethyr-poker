#Common types across Aethyr Poker components

from __future__ import annotations
from typing import NewType, Protocol
from enum import StrEnum, IntEnum

class Action(StrEnum):
    DISCARD = 'Discard'
    INAUGURATE = 'Inaugurate'
    PASS = 'Pass'

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
    
# --- class for card (singular)
# pylance does not like dunder methods, hence the many type ignores :/
class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def suit(self) -> Suit:
        return self._suit

    def __repr__(self):
        return f"{self._rank.name} of {self._suit.name}" if self._suit != Suit.NoSuit \
            else f"{self._rank.name} Card"

    # comparisons for rank
    def __str__(self):
        return f"{self.rank.name} of {self._suit.name}" if self._suit != Suit.NoSuit \
            else f"{self._rank.name} Card"
    
    def __lt__(self, other: object) -> bool:
        return self.rank < other.rank
    
    def __le__(self, other: object) -> bool:
        return self.rank <= other.rank
    
    def __gt__(self, other: object) -> bool:
        return self.rank > other.rank
    
    def __ge__(self, other: object) -> bool:
        return self.rank >= other.rank
    
    def rank_eq(self, other: object) -> bool:
        return self.rank == other.rank

    def suit_eq(self, other: object) -> bool:
        return self.suit == other.suit