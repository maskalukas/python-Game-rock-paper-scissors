class Option:
    # string
    _name = None

    # int
    _id = None

    _stronger_id = None

    # @returnType: string
    def get_name(self):
        return self._name

    # @returnType: string
    def get_id(self):
        return self._id

    def set_stronger_id(self, option_id):
        self._stronger_id = option_id

    def get_stronger_id(self):
        return self._stronger_id


class Rock(Option):
    def __init__(self):
        self._id = 1
        self._name = "Rock"
        self.set_stronger_id(3)  # paper


class Paper(Option):
    def __init__(self):
        self._id = 3
        self._name = "Paper"
        self.set_stronger_id(2)  # scissors


class Scissors(Option):
    def __init__(self):
        self._id = 2
        self._name = "Scissors"
        self.set_stronger_id(1)  # rock
