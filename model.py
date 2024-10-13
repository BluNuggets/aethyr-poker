from typing import NewType
from common_types import Rank, Suit

PlayerId = NewType('PlayerId', int)

# --- class for card (singular)
# pylance does not like dunder methods, hence the many type ignores :/
class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank.name} of {self.suit.name}"

    # comparisons for rank
    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"
    
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

    
class PokerGameModel:
    def __init__(self):
        self._current_player: PlayerId = 1
        self._deck: list[Card]
        self._all_hands: dict[PlayerId, list[Card]]
        self._is_game_over: bool = False