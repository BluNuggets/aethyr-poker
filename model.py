from common_types import Rank, Suit, Card
import random
import pprint as p # for testing purposes
    
class PokerGameModel:
    def __init__(self, players: int):
        self._players: int = players
        self._term_number: int = 1
        self._current_player: int = 1

        self._deck: list[Card] = self._create_deck()
        self._all_hands: dict[int, list[Card]]

        self._center_cards: list[Card] = []
        self._discards: list[Card] = []

        self._did_inauguration_happen = False
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
    def did_inauguration_happen(self) -> bool:
        return self._did_inauguration_happen
    
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
        '''Setup the hands for the players and first term'''
        president_cards: list[int] = [i for i, card in enumerate(deck) if card.rank == 12]

        random.shuffle(president_cards)
        picked_pres: int = president_cards[0]
        
        self._center_cards.append(self._deck.pop(picked_pres))
        random.shuffle(self._deck)

        self._all_hands = self._distribute_hands()
        return
    
    def update_player(self) -> None:
        if self._current_player == self._players:
            self._current_player = 1
            self.update_term()
        else:
            self._current_player += 1
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
    
    def pull_card(self, is_first_term: bool) -> None:
        if is_first_term:
            for _ in range(3):
                self._discards.append(self._deck.pop(0))
        else:
            self._discards.append(self._deck.pop(0))
        
        self._center_cards.append(self._deck.pop(0))
        return

    def action_discard(self, discarded_index: int) -> None:
        new_card: Card = self._deck.pop(0)
        discarded_card: Card = self._all_hands[self._current_player][discarded_index]
        
        #append discarded to discard pile
        self._discards.append(discarded_card)

        #switch discard card to new card in player handi
        self._all_hands[self._current_player][discarded_index] = new_card
        return
    
    def action_inau(self, child: Card, pres: Card) -> None: #to appease pylance
        #find child in current hand and swap to pres
        for i, card in enumerate(self._all_hands[self._current_player]):
            if child == card:
                self._all_hands[self._current_player].pop(i)
                self._all_hands[self._current_player].append(pres)
                break
        
        #find parent in center (or other) hand and swap to child
        for i, card in enumerate(self._center_cards):
            if pres == card:
                self._center_cards.pop(i)
                self._center_cards.append(child)
                break

        return