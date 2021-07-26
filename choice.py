class Choice:
    def __init__(self, options):
        self._options = options

    def choose_option(self):
        print(self._get_input_option_sentence())
        input_value = input()
        if self._check_if_input_is_number_in_right_format(input_value):
            input_value_number = int(input_value)
            return next(option for option in self._options if option.get_id() == input_value_number)
        else:
            return False

    def _get_input_option_sentence(self):
        sentence = ""
        for idx, option in enumerate(self._options):
            sentence += option.get_name() + " id: " + str(option.get_id())
            if idx != len(self._options) - 1:
                sentence += ","
        return sentence

    def _check_if_input_is_number_in_right_format(self, input_value):
        input_value_int = None

        try:
            input_value_int = int(input_value)
        except:
            print("The input value is not type of number.")
            return False

        is_valid_id_of_option = any(option.get_id() == input_value_int for option in self._options)
        if not is_valid_id_of_option:
            print("The input value is not the right number.")
            return False

        return True
