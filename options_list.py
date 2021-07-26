from options import Rock, Scissors, Paper

class Options_list:
    _list = [Rock(), Scissors(), Paper()]

    def get_option_by_id(self, option_id):
        return next(option for option in self._list if option.get_id() == option_id)

    def get_list(self):
        return self._list
