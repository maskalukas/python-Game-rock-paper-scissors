class Choice:
    def __init__(self, options):
        self._options = options
        

    def chooseOption(self):
        print(self._getInputOptionSentence())
        inputValue = input()
        isInputValid = self._checkIfInputIsNumberInRightFormat(inputValue)
        if(isInputValid):
            inputValueNumber = int(inputValue)
            return next(option for option in self._options if option.getId() == inputValueNumber)
        else:
            return False

    def _getInputOptionSentence(self):
        sentence = ""
        for idx, option in enumerate(self._options):
            sentence += option.getName() + " id: " + str(option.getId())
            if(idx != len(self._options)-1):
                sentence += ","
        return sentence

    def _checkIfInputIsNumberInRightFormat(self, inputValue):
        inputValueInt = None

        try:
            inputValueInt = int(inputValue) 
        except:
            print("The input value is not type of number.")
            return False

        isValidIdOfOption = any(option.getId() == inputValueInt for option in self._options)
        if(not isValidIdOfOption):
            print("The input value is not the right number.")
            return False
            
        return True

        
            