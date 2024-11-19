from common_types import Action, Card
from model import PokerGameModel
from view import PokerTerminalView
from controller import PokerMainController
from scoring_system import PokerScore
import pprint as p # for testing purposes

if __name__ == "__main__":
    #first ask for number of players
    view = PokerTerminalView()
    model = PokerGameModel()
    score = PokerScore()
    controller = PokerMainController(model, view, score)
    controller.start()