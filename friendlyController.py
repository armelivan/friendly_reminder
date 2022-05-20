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
START_DATE_PROMPT = "Please enter the person startDate in the format yyyy-mm-dd:"
START_DATE_INVALID_PROMPT = "You provided an invalid start date, please input a new value:"
INFO_TO_MODIFY_PROMPT="Do you want to modify:\n0.Cancel\n1.Frequency\n2.Name\n3.Start Date"
INFO_TO_MODIFY_PROMPT_INVALID_PROMPT ="Please enter a proper answer :\n0.Cancel\n1.Frequency\n2.Name\n3.Start Date "
PERSON_PERIOD_START ="Please provide with a start date in the format yyyy-mm-dd:"
PERSON_PERIOD_END = "Please provide wih an end date in the format yyyy-mm-dd: "
PERSON_PERIOD_START_INVALID_PROMPT =" You provided an invalid start date, Please enter date in format yyyy-mm-dd: "
PERSON_PERIOD_END_INVALID_PROMPT =" You provided an invalid end date, Please enter date in format yyyy-mm-dd: "

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


"""
--  Helpers functions 
"""

#Freezing or Unfreezing a given person
def freezingHandler(toFreeze,name,period):
    infoReminder= completeInfoFreezePerson(name,toFreeze)
    DataHelper.HandleFreeze(infoReminder,toFreeze)

# check if there is missing info on the personne 
def completeMissingPersonInfo(name,frequency,startDate):

    infoPerson = {"name":name,"frequency":frequency,"startDate":startDate}

    if name == None:
        retrySimplePromptOnError("name",infoPerson,PERSON_NAME_PROMPT,PERSON_NAME_INVALID_PROMPT)
    if frequency == None:
        retrySimplePromptOnError("frequency",infoPerson,FREQUENCY_PROMPT,FRREQUENCY_INVALID_PROMPT)
    if startDate == None:
       retrySimplePromptOnError("startDate",infoPerson["startDate"],START_DATE_PROMPT,START_DATE_INVALID_PROMPT)

    return infoPerson

#return the info to modify
def completeMissingModifyingInfo(name,onlyName):
    infoPerson = {"name":name,"infoToModify":None}

    if name == None:
        retrySimplePromptOnError("name",infoPerson,PERSON_NAME_PROMPT,PERSON_NAME_INVALID_PROMPT)
    if not onlyName:
        retrySimplePromptOnError("infoToModify",infoPerson,INFO_TO_MODIFY_PROMPT,INFO_TO_MODIFY_PROMPT_INVALID_PROMPT)

    return infoPerson

# stop tracking the person for a given period
def completeInfoFreezePerson(name,toFreeze):
    infoPeriod = {"name":name,"checkedPeriod":None}
    if name == None:
        retrySimplePromptOnError("name",infoPeriod,PERSON_NAME_PROMPT,PERSON_NAME_INVALID_PROMPT)
 
    if toFreeze==True:
        cS = input(PERSON_PERIOD_START)
        cE = input(PERSON_PERIOD_END)
        infoPeriod["checkedPeriod"] = (cS,cE)
        while(InputParser.parseInput("period",(cS,cE))==False):
                cS = input(PERSON_PERIOD_START_INVALID_PROMPT)
                cE = input(PERSON_PERIOD_END_INVALID_PROMPT)
                infoPeriod["checkedPeriod"]=(cS,cE)

    return infoPeriod

# loop till we have the good input format
def retrySimplePromptOnError(type:str,structRef,prompt:str,retryPrompt:str):
    structRef[type]= input(prompt)
    while(not InputParser.parseInput(type,structRef[type])):
            structRef= input(retryPrompt)
    
# Insure that the format inputed in the function is good
if __name__ =="__main__":
    app()
