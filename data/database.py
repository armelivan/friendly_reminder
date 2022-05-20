from socket import create_connection
import sqlite3
from sqlite3 import Error
from models.reminder import Reminder

REMINDER_TABLE_CREATE_PROMPT = """CREATE TABLE IF NOT EXISTS reminder(
                             personName text,
                             reminderNumber int,
                             frequency text,
                             startDate text,
                             onFreeze int,
                             frozenPeriod text;
                             )"""
class databaseHandler:

    def __init__(self,dbPath):
        self.dbPath = dbPath
        self.c = create_connection().cursor()

    def createConnectionPath(self):
        con = None;
        try:
            conn = sqlite3.connect(self.dbPath)
        except Error as e:
            print("Error:{e} ,\nwhen trying to connect")
        return conn
    
    # create a given type of table
    def createTable(self,tableQuerry):
        self.c.execute(tableQuerry)

    def insert_reminder(reminder:Reminder):
        pass

    def remove_reminder(reminder:Reminder):
        pass

    def isReminderInDB():
        pass
    


    


