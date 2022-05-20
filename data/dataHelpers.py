
import typer
from data.database import databaseHandler;
DB_PATH = "data/datase.py";

# List of prompt 
REMINDER_ALREADY_IN_DB="The reminder is already in DB"

class DataHelpers:
    def __init__(self):
        pass


    #receive info, look in the DB if there and modify it 
    def modifyInfo(infoToModify):
        typer.echo(f"modifying  person info")

    def HandleFreeze(infoReminder,toFreeze):
        pass

    def addReminder(self,infoReminder):
        if not self.isReminderInDataBase(infoReminder):
            typer.echo(f"adding a new person {infoReminder.name}, {infoReminder.frequency},{infoReminder.startDate}")
        else:
            typer.echo(REMINDER_ALREADY_IN_DB)
    
    def removeReminder(self,infoReminder):
        pass

    def showPersonInfo(self,infoReminder):
        pass

    def showAllPersonInfo(self):
        pass

    def showPersonsToContact(self):
        pass