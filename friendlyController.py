import typer 
from rich.console import Console
from rich.table import table 

#Typer is a CLI library 
#Rich is a Terminal library to display info 
console = Console()
app = typer.Typer()


@app.command()
def addPerson(name:str=None,frequency:str=None,startDate:str=None):
    completeMissingPersonInfo(name,frequency,startDate)
    pass

@app.command()
def modifyPersonInfo():
    pass

@app.command()
def freezePerson():
    pass 

@app.command()
def removePerson():
    pass

@app.command()
def showPersonInfo():
    pass

@app.command()
def showAllPersonsInfo():
    pass

@app.command()
def showPersonsToContact():
    pass




def completeMissingPersonInfo(name,frequency,startDate):
    infoPerson = {"name":name,"frequency":frequency,"startDate":startDate}
    if name==None:
        infoPerson["name"]
    if frequency ==None:
        pass
    if startDate==None:
        pass


if __name__ =="__main__":
    app()
