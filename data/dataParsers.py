from datetime import datetime
class DataParsers:
    def __init__(self):
        pass



    def parseInput(self,elementToParse,type)->bool:
        if type =="name":
            self.validateName(elementToParse)
        elif type == "frequency":
            self.validateFrequency(elementToParse)
        elif type == "period":
            self.validatePeriod(elementToParse)
        else: # start date 
            self.validateDate(elementToParse)
        return False


   #name: most be different than empty space 
   #does not contain 
    def validateName(self,name):
        if name == "":
            return False
        return not name.isnumeric
            

    def validateFrequency(self):
        pass

    def validatePeriod(self):
        pass

    #Format yyy-mm-dd
    def validateDate(self,dateString:str)->bool:
        try:
            datetime.strptime(dateString, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    