class Score:
    _computerScore = 0
    _userScore = 0
    _drawScore = 0

    def increment_computer_score(self):
        self._computerScore += 1

    def increment_user_score(self):
        self._userScore += 1

    def increment_draw_score(self):
        self._drawScore += 1

    def get_computer_score(self):
        return self._computerScore

    def get_user_score(self):
        return self._userScore

    def get_draw_score(self):
        return self._drawScore