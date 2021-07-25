from options import Rock, Scissors, Paper

class Options_list:
    _list = [Rock(), Scissors(), Paper()]

    def getOptionById(optionId):
        return next(option for option in self._options if option.getId() == inputValueNumber)


