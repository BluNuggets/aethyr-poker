from common_types import Action, Card
from model import PokerGameModel
from view import PokerTerminalView
from scoring_system import PokerScore
import pprint as p # for testing purposes

class PokerMainController:
    def __init__(self, model: PokerGameModel, view: PokerTerminalView, score: PokerScore):
        self._model = model
        self._view = view
        self._score = score

    def start(self):
        model = self._model
        view = self._view
        score = self._score

        is_new_game: bool = True
        is_error: bool = False
        term_check = 0

        while not model.is_game_over:
            if is_new_game:
                # setup the initial deck and hands
                model.setup(model.deck)
                is_new_game = False

            if not is_error and model.term != term_check:
                if model.term == 1:
                    # once only for first term (betting WIP)
                    model.pull_card(True)
                else:
                    # does this twice when 2nd/3rd term
                    model.pull_card(False)
                    model.pull_card(False)
                term_check += 1

            # Main Game
            view.clear_screen()
            
            view.show_term_number(model.term)
            view.show_center_cards(model.center_cards)
            view.show_personal_hand(model.all_hands, model.cur_player)
            action: Action = view.ask_for_action(model.term, model.center_cards, model.all_hands, model.cur_player)

            if action == Action.DISCARD:
                discarded_card: int = view.ask_for_discards(model.all_hands, model.cur_player, model.center_cards)
                model.action_discard(discarded_card)
            elif action == Action.INAUGURATE:
                inaugurate_output: tuple[Card | None, Card | None, bool] = view.ask_for_inaugurate(model.all_hands, model.cur_player, model.center_cards)

                if not inaugurate_output[2]:
                    is_error = True
                    continue

                model.action_inau(inaugurate_output[0], inaugurate_output[1])
            #else continue to next player/new term
            
            #print(model.center_cards)
            #print(model.discards)
            is_error = False
            model.update_player()
        
        nye: int = score.score_hand(model.players, model.all_hands, model.center_cards)
        print(nye)

        
#first ask for number of players
view = PokerTerminalView()
view.clear_screen()
player_count = view.ask_for_number_of_players()

model = PokerGameModel(player_count)
score = PokerScore()
controller = PokerMainController(model, view, score)
controller.start()