from common_types import Card
from itertools import combinations
import pprint as p # for testing purposes

class PokerScore:
    def score_hand(self, players: int, all_hands: dict[int, list[Card]], center: list[Card]) -> dict[int, int]:
        output: dict[int, int] = {(i+1): 0 for i in range(players)}
        card_list: list[tuple[Card, ...]]

        for player in all_hands:
            card_list: list[tuple[Card, ...]] = list(combinations(all_hands[player] + center, 6))
            p.pp(all_hands)

            p.pp(card_list)
            print(len(card_list))
            
            self._check_matches(card_list)
            self._check_runs(card_list)
            self._check_president(card_list)
            self._check_child(card_list)
            self._check_lineage(card_list)
        
        #print(output)
        return output
    
    def _check_matches(self, card_list: list[tuple[Card, ...]]) -> int:
        high: int = 0
        return high
    
    def _check_runs(self, card_list: list[tuple[Card, ...]]) -> int:
        high: int = 0
        return high

    def _check_president(self, card_list: list[tuple[Card, ...]]) -> int:
        high: int = 0
        return high

    def _check_child(self, card_list: list[tuple[Card, ...]]) -> int:
        high: int = 0
        return high

    def _check_lineage(self, card_list: list[tuple[Card, ...]]) -> int:
        high: int = 0
        return high
    