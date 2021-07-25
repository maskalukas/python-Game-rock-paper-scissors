from options import Rock, Scissors, Paper
from choice import Choice
import time

class Game:
    _options = [Rock(), Scissors(), Paper()]

    def play(self):
        for option in self._options:
            print(option.getName())
            time.sleep(0.3)
        choice = Choice(self._options)
        result = choice.chooseOption()

    
