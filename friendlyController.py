import typer 
from rich.console import Console
from rich.table import Table 
from data.dataHelpers import DataHelpers
from data.dataParsers import DataParsers


#Typer is a CLI library 
#Rich is a Terminal library to display info 
console = Console()
app = typer.Typer()


# List of prompts

PERSON_NAME_PROMPT ="Please enter the person name: "
PERSON_NAME_INVALID_PROMPT="You provided an invalid person name, please input a new value:"
FREQUENCY_PROMPT = "Please enter the frequency of contact in the format w,m,q: "
FRREQUENCY_INVALID_PROMPT = "You provided an invalid frequency, please input a new value:"
START_DATE_PROMPT = "Please enter the person startDate in the format dd/mm/yyyy: "
START_DATE_INVALID_PROMPT = "You provided an invalid frequency, please input a new value:"
INFO_TO_MODIFY_PROMPT="Do you want to modify:\n0.Cancel\n1.Frequency\n2.Name\n3.Start Date"

# needed linked classes 
DataHelper= DataHelpers()
InputParser = DataParsers()



"""
--  Commands 
"""

# create a new reminder (name,frequency,startDate)
# and add it in the data base 
@app.command()
def addReminder(name:str=None,frequency:str=None,startDate:str=None):
    infoReminder= completeMissingPersonInfo(name,frequency,startDate)
    DataHelper.addReminder(infoReminder)
   

#The function prompt the user with a given name and then asked the info
# he want to modify and then enter it 
@app.command()
def modifyPersonInfo(name:str=None):
    infoToModify = completeMissingModifyingInfo(name,False)
    DataHelper.modifyInfo(infoToModify)
    
    
@app.command()
def freezePerson(name:str=None,period:str=None):
    freezingHandler(True,name,period)

@app.command()
def UnfreezePerson(name:str=None,period:str=None):
    freezingHandler(False,name,period)   

@app.command()
def removeReminder(name:str=None):
    infoReminder = completeMissingModifyingInfo(name,True)
    DataHelper.removeReminder(infoReminder)

@app.command()
def showPersonInfo(name:str=None):
    infoReminder = completeMissingModifyingInfo(name,True)
    DataHelper.showPersonInfo(infoReminder)

@app.command()
def showAllPersonsInfo():
    DataHelper.showAllPersonInfo()

@app.command()
def showPersonsToContact():
    DataHelper.showPersonsToContact()



#Freezing or Unfreezing a given person
def freezingHandler(toFreeze,name,period):
    infoReminder= completeInfoFreezePerson(name,period)
    DataHelper.HandleFreeze(infoReminder,toFreeze)



"""
--  Helpers functions 
"""
'''
TODO:Error cases: 
1. format of name/frequency/startDate is not good
    -> loop until we have a good format 
2. StartDate is posterior to the current date: 
    -> prompt : Changing date to posterior or current date 
'''

# check if there is missing info on the personne 
def completeMissingPersonInfo(name,frequency,startDate):

    infoPerson = {"name":name,"frequency":frequency,"startDate":startDate}
    if name == None:
        infoPerson["name"]= input(PERSON_NAME_PROMPT)
        while(InputParser.parseInput.parseInput("name",infoPerson["name"])==False):
            infoPerson["name"]= input(PERSON_NAME_INVALID_PROMPT)
    
    if frequency == None:
        infoPerson["frequency"]= input(FREQUENCY_PROMPT)
        while(InputParser.parseInput("frequency",infoPerson["frequency"])==False):
            infoPerson["frequency"]= input(FRREQUENCY_INVALID_PROMPT)
    
    if startDate == None:
       infoPerson["startDate"]= input(START_DATE_PROMPT)
       while(InputParser.parseInput("startDate",infoPerson["startDate"])==False):
            infoPerson["startDate"]= input(START_DATE_INVALID_PROMPT)

    return infoPerson



#return the info to modify
def completeMissingModifyingInfo(name,onlyName):
    if name == None:
        checkedName = input(PERSON_NAME_PROMPT)
        while(InputParser.parseInput("name",checkedName)==False):
            checkedName = input(PERSON_NAME_INVALID_PROMPT)

    if not onlyName:
        infoToModify = input(INFO_TO_MODIFY_PROMPT)

    return {checkedName,infoToModify}



# stop tracking the person for a given period
def completeInfoFreezePerson(name,period):
    if name == None:
        checkedName = input(PERSON_NAME_PROMPT)
        while(InputParser.parseInput("name",checkedName)==False):
            checkedName = input(PERSON_NAME_INVALID_PROMPT)
        
    if period == None:
        checkedPeriod = input(PERSON_NAME_PROMPT)
        while(InputParser.parseInput("period",checkedPeriod)==False):
            checkedName = input(PERSON_NAME_INVALID_PROMPT)

    return {checkedName,checkedPeriod}




# Insure that the format inputed in the function is good
if __name__ =="__main__":
    app()
