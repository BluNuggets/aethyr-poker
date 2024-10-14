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

        while not model.is_game_over:
            view.clear_screen()
            view.show_term_number(model.term)

            #setup the initial deck and hands
            if model.term == 1:
                model.setup(model.deck)
            
            #view.show_term()
            #view.show_all_hands()
            print(model.center_cards)

            model.update_term()

#first ask for number of players
view = PokerTerminalView()
view.clear_screen()
player_count = view.ask_for_number_of_players()

model = PokerGameModel(player_count)
controller = PokerMainController(model, view)
controller.start()