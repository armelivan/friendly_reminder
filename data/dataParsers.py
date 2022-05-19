from datetime import datetime,date 
class DataParsers:
    
    def __init__(self):
        self.DATEFORMAT = '%Y-%m-%d'

            

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
            

    def validateFrequency(self,freq:str):
        return freq.lower()  in ("q","w","m")

    #Format start date, end date (yyy-mm-dd,yyy-mm-dd)
    def validatePeriod(self,period):
        try:
            if len(period)!=2:
                return False
            if len(period[0])!=10 or len(period[1])!=10:
                return False

            if (self.validateDate(period[0]) and self.validateDate(period[1]))==False:
                return False 
            startDate = datetime.strptime(period[0], self.DATEFORMAT )
            endDate = datetime.strptime(period[1], self.DATEFORMAT )
            todayString = datetime.today().strftime(self.DATEFORMAT )
            todayDate = datetime.strptime(todayString,self.DATEFORMAT )

            if startDate>=endDate:

                return False
            return startDate >= todayDate
        except:
            return False


    #Format yyy-mm-dd
    def validateDate(self,dateString:str)->bool:
        try:
            datetime.strptime(dateString, self.DATEFORMAT)
            return True
        except ValueError:
            return False

