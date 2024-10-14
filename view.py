import os
import sys
import time
from common_types import Card, Action
from collections.abc import Sequence, Mapping
from typing import Generic

MAX_PLAYER: int = 8
MAX_CENTER_CARDS: int = 6

class PokerTerminalView:
    def clear_screen(self) -> None:
        """Clear the terminal."""

        cmd = 'cls' if sys.platform in {'win32', 'cygwin', 'msys'} else 'clear'
        os.system(cmd)

    def show_term_number(self, term: int):
        """Show term number."""
        print(f'------------ Term {term} ------------\n')

    def show_center_cards(self, cards: list[Card]) -> None:
        """Show Center Cards."""
        print(f'Center Cards: \n')

        for i in range(MAX_CENTER_CARDS):
            try:
                print(f'[{i+1}] {cards[i]}')
            except (IndexError):
                print(f'[{i+1}] _')

        print()

    def show_personal_hand(self, all_hands: dict[int, list[Card]], current_player: int) -> None:
        """Show the *PERSONAL* hand of the current player. Other player cards are hidden."""
        for hand in all_hands:
            print(f'Player {hand} (current)') if hand == current_player \
                else print(f'Player {hand}')
            
            for i, card in enumerate(all_hands[hand]):
                print(f'[{i+1}] {card}') if hand == current_player \
                    else print(f'[{i+1}] ...')
            
            print()
        return
    
    def show_personal_hand_only(self, current_hand: list[Card], current_player: int) -> None:
        """Show the hand of the current player. For discard purposes"""
        print(f'Player {current_player}')
            
        for i, card in enumerate(current_hand):
            print(f'[{i+1}] {card}')
        
        print()
        return
    
    def show_active_president_cards(self, current_hand: list[Card]) -> None:
        """Show the hand of the president cards. For inaugurate purposes"""
        print(f'Active President Cards')
            
        for i, card in enumerate(current_hand):
            print(f'[{i+1}] {card}')
        
        print()
        return

    def ask_for_action(self, term: int, center: list[Card], all: dict[int, list[Card]], cur: int) -> Action:
        """Ask the user for actions."""
        actions: list[Action] = list(Action)
        self._show_all_actions()
        
        while True:
            if (action_int := self._ask_for_choice("Select action", len(Action))) is None:
                self.clear_screen()
                self.show_term_number(term)
                self.show_center_cards(center)
                self.show_personal_hand(all, cur)
                self._show_all_actions()
                continue
            
            return actions[action_int - 1]


    def ask_for_number_of_players(self) -> int:
        """Ask the user for number of players for the Poker game."""
        
        while True:
            if (player_count := self._ask_for_choice("Select number of players", MAX_PLAYER)) is None:
                self.clear_screen()
                continue
            
            return player_count
        
    def ask_for_discards(self, all_hands: dict[int, list[Card]], current_player: int, center: list[Card]) -> int:
        """Ask the user for which Card to discard."""
        self.clear_screen()
        print(f'------------ DISCARD PHASE ------------')
        self.show_center_cards(center)
        self.show_personal_hand_only(all_hands[current_player], current_player)

        personal_hand: list[Card] = all_hands[current_player]

        while True:
            if (dis := self._ask_for_choice("Select the card to discard", len(personal_hand))) is None:
                self.clear_screen()
                print(f'------------ DISCARD PHASE ------------')
                self.show_center_cards(center)
                self.show_personal_hand_only(all_hands[current_player], current_player)
                continue
            
            return dis-1

    def ask_for_inaugurate(self, all_hands: dict[int, list[Card]], current_player: int, center: list[Card]) -> tuple[Card | None, Card | None, bool]:
        """Ask the user for which Card to inaugurate (given that there is a child).

        Returns two things:
            the index of the child card
            the index of the president card to be swapped
            if the card comes from the center (else from another player)"""
        child_to_pick: list[Card] = [i for i in all_hands[current_player] if i.rank == 11]
        president_to_pick: list[Card] = [i for i in center if i.rank == 12]

        self._show_inaugurate_details(center, child_to_pick, president_to_pick, current_player)

        if len(child_to_pick) == 0:
            self._print_error(f'[INVALID ACTION] No child cards to inaugurate.')
            return (None, None, False)
        
        # now that i think about it, this should not be possible because there will always be one president active, but sure
        elif len(president_to_pick) == 0:
            self._print_error(f'[INVALID ACTION] No president cards to swap with.')
            return (None, None, False)

        while True:
            if (child_index := self._ask_for_choice("Select the child card to inaugurate", len(child_to_pick))) is None:
                self._show_inaugurate_details(center, child_to_pick, president_to_pick, current_player)
                continue

            if (president_index := self._ask_for_choice("Select the president card to swap with", len(president_to_pick))) is None:
                self._show_inaugurate_details(center, child_to_pick, president_to_pick, current_player)
                continue
            
            return (child_to_pick[child_index-1], president_to_pick[president_index-1], True)
    
    def _show_inaugurate_details(self, center: list[Card], child: list[Card], parent: list[Card], cur: int):
        self.clear_screen()
        print(f'------------ INAUGURATE PHASE ------------')
        self.show_center_cards(center)
        self.show_personal_hand_only(child, cur)
        self.show_active_president_cards(parent)

    def _show_all_actions(self) -> None:
        """Show all possible actions for a term."""
        print(f'Actions: ')
        for i, action in enumerate(Action):
            print(f'[{i+1}] {action}')

    def _ask_for_choice(self, msg: str, u_bound: int, l_bound: int = 1) -> int | None:
        """Catch errors in case user enters out of bounds / invalid input"""

        try:
            inp: int = int(self._input(f'{msg} [{l_bound} - {u_bound}]: ') if u_bound > 1 \
                           else self._input(f'{msg} [{u_bound}]: ') )

            if inp < l_bound or inp > u_bound:
                raise ValueError()
            
            return inp

        except (ValueError, IndexError):
            self._print_error(f'[INVALID CHOICE] Pick an integer between {l_bound}-{u_bound}')
            return None

    def _print_error(self, msg: str) -> None:
        print(f'\nERROR: {msg}\n')
        input('Press Enter to continue...')
        self.clear_screen()

    def _input(self, msg: str) -> str:
        return input(msg).strip()