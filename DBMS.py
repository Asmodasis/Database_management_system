import os

class DBMS:
    # creates the database management system, this will form the link with the terminal to accept input
    def __init__(self):
        pass

    def setDirectoryLocation(self, location):
        self.directory = location

    def createDatabase(self, dataBase):
        if not os.path.exists(dataBase):
            os.makedirs(dataBase)
        else:
            print("!Failed to create database ", dataBase, " because it already exists.")
    
    def deleteDatabase(self, dataBase):
        if os.path.exists(dataBase):
            os.rmdir(dataBase)
        else:
            print("!Failed to delete database ", dataBase, " because it does not exist.")

    