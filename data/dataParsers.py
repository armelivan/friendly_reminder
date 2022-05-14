class DataParsers:
    def __init__(self):
        pass



    def parseInput(self,elementToParse,type) ->bool:
        if type =="name":
            self.validateName(elementToParse)
        elif type == "frequency":
            self.validateFrequency(elementToParse)
        elif type == "period":
            validatePeriod(elementToParse)
        else: # start date 
            self.validateDate(elementToParse)


    # Objects parsing
    def validateName(self):
        pass

    def validateFrequency(self):
        pass

    def validatePeriod(self):
        pass

    def validateDate(self):
        pass
