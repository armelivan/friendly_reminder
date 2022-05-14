import typer 
from rich.console import Console
from rich.table import Table 
from data.dataHelpers import DataHelpers


#Typer is a CLI library 
#Rich is a Terminal library to display info 
console = Console()
app = typer.Typer()


# List of prompts
PERSON_NAME_PROMPT ="Please enter the person name: "
FREQUENCY_PROMPT = "Please enter the frequency of contact in the format d,w,m,q: "
START_DATE_PROMPT = "Please enter the person startDate in the format dd/mm/yyyy: "


# needed linked classes 
DataHelper= DataHelpers()




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
    infoToModify = completeMissingModifyingInfo(name)
    DataHelper.modifyInfo(infoToModify)
    
    
@app.command()
def freezePerson(name:str=None,period:str=None):
    freezingHandler(True,name,period)

@app.command()
def UnfreezePerson(name:str=None,period:str=None):
    freezingHandler(False,name,period)   

@app.command()
def removeReminder(name:str=None):
    infoReminder = completeMissingModifyingInfo(name)
    DataHelper.removeReminder(infoReminder)

@app.command()
def showPersonInfo(name:str=None):
    infoReminder = completeMissingModifyingInfo(name)
    DataHelper.showPersonInfo(infoReminder)

@app.command()
def showAllPersonsInfo():
    DataHelper.showAllPersonInfo()

@app.command()
def showPersonsToContact():
    DataHelper.showPersonsToContact()



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
    if name==None:
        infoPerson["name"]= input(PERSON_NAME_PROMPT)
    if frequency ==None:
        infoPerson["frequency"]= input(FREQUENCY_PROMPT)
    
    if startDate==None:
       infoPerson["startDate"]= input(START_DATE_PROMPT)
    return infoPerson


#return the info to modify
def completeMissingModifyingInfo(name):
    pass

# stop tracking the person for a given period
def CompleteInfoFreezePerson(name,period):
    pass

#Freezing or Unfreezing a given person
def freezingHandler(toFreeze,name,period):
    infoReminder= CompleteInfoFreezePerson(name,period)
    DataHelper.HandleFreeze(infoReminder,toFreeze)

if __name__ =="__main__":
    app()
