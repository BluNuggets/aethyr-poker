from model import PokerGameModel
from view import PokerTerminalView

class PokerMainController:
    def __init__(self, model: PokerGameModel, view: PokerTerminalView):
        self._model = model
        self._view = view

    def start(self):
        model = self._model
        view = self._view

        view.clear_screen()

print("Hello World")

model = PokerGameModel()
view = PokerTerminalView()
controller = PokerMainController(model, view)
controller.start()