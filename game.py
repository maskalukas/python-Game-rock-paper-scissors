from choice import Choice
import time
from evaluation import Evaluation
from options_list import Options_list
from computer import Computer
from score import Score


class Game:
    _optionsList = Options_list()
    _score = Score()

    def play(self):
        while True:
            for option in self._optionsList.get_list():
                print(option.get_name())
                time.sleep(0.3)

            choice = Choice(self._optionsList.get_list())
            user_choice = choice.choose_option()

            computer = Computer(self._optionsList)
            computer_choice = computer.choose_random_option()

            evaluation = Evaluation(user_choice, computer_choice, self._score)
            result = evaluation.evaluate()

            if result["winner"] is None:
                print("Draw!!")
            else:
                print("Winner is: " + result["winner"] + " s hodnotou: " + result["choice"].get_name())

            print("-------------------------------------------------------------------------")
            print("State: computer: " + str(self._score.get_computer_score()) + " | user: " + str(self._score.get_user_score()) + " | draw: " + str(self._score.get_draw_score()))
            print("-------------------------------------------------------------------------")
