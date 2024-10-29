from common_types import Card
from itertools import combinations, groupby
import pprint as p # for testing purposes

class PokerScore:
    def score_hand(self, players: int, all_hands: dict[int, list[Card]], center: list[Card]) -> int:
        high: int = 0
        output: dict[int, int] = {(i+1): 0 for i in range(players)}
        card_list: list[tuple[Card, ...]]

        for player in all_hands:
            card_list: list[tuple[Card, ...]] = list(combinations(all_hands[player] + center, 6))
            #p.pp(all_hands)
            #print(len(card_list))
            
            for comb in card_list:
                high_cur: int = self._check_matches(list(comb))
                if high_cur > high:
                    high = high_cur
                
                #self._check_runs(list(comb))
                #self._check_president(list(comb))
                #self._check_child(list(comb))
                #self._check_lineage(list(comb))
        
        #print(output)
        return high
    
    def _check_matches(self, cl: list[Card]) -> int:
        high: int = 0
        cl.sort()

        i = groupby(cl, lambda x: x.rank)

        for key, group in i:
            if len(list(group)) == 3:
                high = high + (50 + key*3)
            elif len(list(group)) == 2:
                high = high + (50 + key*2)
            else: #solo
                high = high
        return high
    
    def _check_runs(self, cl: list[Card]) -> int:
        high: int = 0
        return high

    def _check_president(self, cl: list[Card]) -> int:
        high: int = 0
        return high

    def _check_child(self, cl: list[Card]) -> int:
        high: int = 0
        return high

    def _check_lineage(self, cl: list[Card]) -> int:
        high: int = 0
        return high
    