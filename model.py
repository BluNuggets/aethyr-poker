from typing import NewType
from common_types import Rank, Suit
import random
import pprint as p # for testing purposes

# --- class for card (singular)
# pylance does not like dunder methods, hence the many type ignores :/
class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank.name} of {self.suit.name}" if self.suit != Suit.NoSuit \
            else f"{self.rank.name} Card"

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
    def __init__(self, players: int):
        self._players: int = players
        self._term_number: int = 1
        self._current_player: int = 1

        self._deck: list[Card] = self._create_deck()
        self._all_hands: dict[int, list[Card]]

        self._center_cards: list[Card] = []
        self._discards: list[Card] = []

        self._is_game_over: bool = False

    @property
    def players(self) -> int:
        return self._players
    
    @property
    def term(self) -> int:
        return self._term_number

    @property
    def cur_player(self) -> int:
        return self._current_player
    
    @property
    def deck(self) -> list[Card]:
        return self._deck
    
    @property
    def center_cards(self) -> list[Card]:
        return self._center_cards
    
    @property
    def discards(self) -> list[Card]:
        return self._discards
    
    @property
    def all_hands(self) -> dict[int, list[Card]]:
        return self._all_hands
    
    @property
    def is_game_over(self) -> bool:
        return self._is_game_over
    
    def _create_deck(self) -> list[Card]:
        '''Create a deck of 109 Cards for Aethyr Poker'''
        
        card_list: list[Card] = []

        for j in Rank:
            for k in Suit:
                if j == 14 or k == 0:
                    #continue if Phoenix Rank or NoSuit Suit
                    continue
                else:
                    for _ in range(3):
                        if j == 11:
                            #add one more child for each suit
                            card_list.append(Card(j,k))
                        
                        card_list.append(Card(j,k))
        
        #add Phoenix suit at the end
        return card_list + [Card(Rank.Phoenix, Suit.NoSuit)]
    
    def setup(self, deck: list[Card]) -> None:
        president_cards: list[int] = [i for i, card in enumerate(deck) if card.rank == 12]
        p.pp(president_cards)

        random.shuffle(president_cards)
        picked_pres: int = president_cards[0]
        
        self._center_cards.append(self._deck.pop(picked_pres))
        random.shuffle(self._deck)

        self._all_hands = self._distribute_hands()
        p.pp(self._all_hands)
        return
    
    def update_term(self) -> None:
        self._term_number += 1

        if self._term_number > 3:
            self._is_game_over = True
        
        return
    
    def _distribute_hands(self) -> dict[int, list[Card]]:
        # distribute cards one by one to each player
        all_hands: dict[int, list[Card]] = {}

        # (popping the first 3 cards for each player could work, but it seems funnier to do it this way)
        for i in range(3):
            for j in range(self.players):
                if i == 0:
                    all_hands[j+1] = []

                all_hands[j+1].append(self._deck.pop(0))

        return all_hands