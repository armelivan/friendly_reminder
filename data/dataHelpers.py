
import typer

# List of prompt 
REMINDER_ALREADY_IN_DB="The reminder is already in DB"

class DataHelpers:
    def __init__(self):
        pass


    def isReminderInDataBase(infoReminder) -> bool:
        return False


    #receive info, look in the DB if there and modify it 
    def modifyInfo(infoToModify):
        typer.echo(f"modifying  person info")

    def addReminder(infoReminder):
        if not isReminderInDataBase(infoReminder):
            typer.echo(f"adding a new person {name}, {frequency},{startDate}")
        else:
            typer.echo(REMINDER_ALREADY_IN_DB)