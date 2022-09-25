import os
from Table import Table

class DBMS:
    # creates the database management system, this will form the link with the terminal to accept input
    def __init__(self):
        pass

    def __readFromFile__(self):
        pass

    def __readFromTerminal__(self):
        pass

    def __parseInput__(self):
        pass
    
    def use(self, location):
        # Not currently using a table
        if os.getcwd().endswith("Database_management_system"):
            os.chdir("./"+location)
        # currently using a table, have to go back a file location to use another
        else:
            os.chdir("../"+location)


    def createDatabase(self, dataBase):
        if not os.path.exists(dataBase):
            os.makedirs(dataBase)
            print("Database ", dataBase, " created.")
        else:
            print("!Failed to create database ", dataBase, " because it already exists.")
    
    def deleteDatabase(self, dataBase):
        if os.path.exists(dataBase):
            os.rmdir(dataBase)
            print("Database ", dataBase, " deleted.")
        else:
            print("!Failed to delete database ", dataBase, " because it does not exist.")
    