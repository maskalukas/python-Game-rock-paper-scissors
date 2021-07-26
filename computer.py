import random


class Computer:

    def __init__(self, options_list):
        self.options_list = options_list

    def choose_random_option(self):
        random_num = random.randint(1, 3)
        return self.options_list.get_option_by_id(random_num)
