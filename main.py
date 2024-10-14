from common_types import Action
from model import PokerGameModel
from view import PokerTerminalView
import pprint as p # for testing purposes

class PokerMainController:
    def __init__(self, model: PokerGameModel, view: PokerTerminalView):
        self._model = model
        self._view = view

    def start(self):
        model = self._model
        view = self._view

        is_new_game = True

        while not model.is_game_over:
            view.clear_screen()

            if is_new_game:
                model.setup(model.deck)
                is_new_game = False

            if model.term == 1:
                model.pull_card(True)
            else:
                # does this twice when 2nd/3rd term
                model.pull_card(False)
                model.pull_card(False)

            print('new\n')

            for _ in range(1,model.players+1):
                view.clear_screen()
                view.show_term_number(model.term)

                #setup the initial deck and hands
                view.show_center_cards(model.center_cards)
                view.show_personal_hand(model.all_hands, model.cur_player)

                action: Action = view.ask_for_action()

                if action == Action.DISCARD:
                    print(action)
                elif action == Action.INAUGURATE:
                    print(action)
                #else continue to next player/new term
                
                #print(model.center_cards)
                print(model.discards)

                model.update_player()

#first ask for number of players
view = PokerTerminalView()
view.clear_screen()
player_count = view.ask_for_number_of_players()

model = PokerGameModel(player_count)
controller = PokerMainController(model, view)
controller.start()