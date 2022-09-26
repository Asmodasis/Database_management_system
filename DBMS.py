from genericpath import isfile
import os
import sys
from Table import Table

class DBMS:
    # creates the database management system, this will form the link with the terminal to accept input
    def __init__(self):

        if len(sys.argv) > 1:
            # There is more than one argument, we have file mode

            #invalid input
            if sys.argv[1] is not '<':
                print("Invalid terminal input: Please try again.")
            else:
                self.__readFromFile__(sys.argv[2])

            
            
        else: 
            self.__readFromTerminal__()
            

    def __readFromFile__(self, fileName):

        if not os.path.isfile(fileName):
            print("Invalid file: Please try again.")
        else:
            f = open(fileName, 'r')
            lines = f.readlines()
            for line in lines:
                self.__parseInput__(line)
            f.close()

    def __readFromTerminal__(self):
        pass

    def __parseInput__(self, inputLine):
        #input Line will contain an entire line of sql code
        splitData = inputLine.split(" ")
        size = len(splitData)

        if splitData[0] == "USE":
            self.use(str(splitData[1]))
            
        elif splitData[0] == "CREATE":
            print("Test create")

        elif splitData[0] == "DROP":
            print("Test drop")
        elif splitData[0] == "ALTER":
            print("Test alter")
        elif splitData[0] == ".EXIT":
            return 0
        
    
    def use(self, location):
        # Not currently using a table
        if os.getcwd().endswith("Database_management_system"):
            os.chdir("./"+location)
        # currently using a table, have to go back a file location to use another
        else:
            os.chdir("../"+location)
        print("Using database ", location)

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
    