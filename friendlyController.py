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



'''
Error cases: 
1. person already exists in the dataBase 
    -> do you want to modify the person info instead
'''

@app.command()
def addReminder(name:str=None,frequency:str=None,startDate:str=None):
    infoReminder= completeMissingPersonInfo(name,frequency,startDate)
    DataHelper.isReminderInDataBase(infoReminder)
    typer.echo(f"adding a new person {name}, {frequency},{startDate}")
    pass


@app.command()
def modifyPersonInfo():
    typer.echo(f"modifying  person info")
    pass

@app.command()
def freezePerson():
    typer.echo(f"freezing person")
    pass 

@app.command()
def removePerson():
    typer.echo(f"supprimer person")
    pass

@app.command()
def showPersonInfo():
    typer.echo(f"montrer info person")
    pass

@app.command()
def showAllPersonsInfo():
    typer.echo(f"show all persons ")
    pass

@app.command()
def showPersonsToContact():
    typer.echo(f"Show all person to contact")
    pass



'''
Error cases: 
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

if __name__ =="__main__":
    app()
