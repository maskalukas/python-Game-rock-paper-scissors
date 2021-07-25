class Option:
    # string
    _name = None

    # int
    _id = None

    # @returnType: string
    def getName(self):
        return self._name

    # @returnType: string
    def getId(self):
        return self._id




class Rock(Option):
    def __init__(self):
        self._id = 1
        self._name = "Rock"




class Paper(Option):
    def __init__(self):
        self._id = 2
        self._name = "Paper"



class Scissors(Option):
    def __init__(self):
        self._id = 3
        self._name = "Scissors"

