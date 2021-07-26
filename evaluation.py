class Evaluation:
    def __init__(self, user_choice, computer_choice, score):
        self.userChoice = user_choice
        self.computer_choice = computer_choice
        self._score = score

    def evaluate(self):
        result = {"winner": None, "choice": None}

        if self.userChoice.get_stronger_id() == self.computer_choice.get_id():
            result["winner"] = "Computer"
            result["choice"] = self.computer_choice
            self._score.increment_computer_score()
        elif self.computer_choice.get_stronger_id() == self.userChoice.get_id():
            result["winner"] = "User"
            result["choice"] = self.userChoice
            self._score.increment_user_score()
        else:
            self._score.increment_draw_score()

        return result
