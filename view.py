import os
import sys
from collections.abc import Sequence, Mapping
from typing import Generic

MAX_PLAYER: int = 8

class PokerTerminalView:
    def clear_screen(self) -> None:
        """Clear the terminal."""

        cmd = 'cls' if sys.platform in {'win32', 'cygwin', 'msys'} else 'clear'
        os.system(cmd)

    def show_term_number(self, term: int):
        print(f'Term {term}\n')


    def ask_for_number_of_players(self) -> int:
        """Ask the user for number of players for the Poker game."""
        
        while True:
            if (player_count := self._ask_for_player("Select number of players", MAX_PLAYER)) is None:
                self.clear_screen()
                continue
            
            return player_count
    
    def _ask_for_player(self, msg: str, max_player: int, min_player: int = 1) -> int | None:
        """Catch errors in case user enters out of bounds / invalid input"""
        try:
            inp: int = int(self._input(f'{msg} [{min_player} - {max_player}]: '))

            if inp < min_player or inp > max_player:
                raise ValueError()
            
            return inp
        except (ValueError, IndexError):
            self._print_error(f'[INVALID CHOICE] Pick an integer between 1-{max_player}')
            return None

    def _print_error(self, msg: str) -> None:
        print(f'\nERROR: {msg}\n')
        input('Press Enter to continue...')
        self.clear_screen()

    def _input(self, msg: str) -> str:
        return input(msg).strip()