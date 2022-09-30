from genericpath import isfile
import os
from Table import Table

class DBMS:
    # creates the database management system, this will form the link with the terminal to accept input
    def __init__(self):
        self.table = Table()
        # retrieve and store the original directory
        self.originalDirectory = os.getcwd()

    def run(self):

        x = ''
        while('.EXIT' not in x):
            x = input()
            #print(x)
            self.__parseInput__(x)

    def __parseInput__(self, inputLine):
        #input Line will contain an entire line of sql code
        #splitData = inputLine.replace(';','').replace('\r','').split(" ")
        #TODO: Why does .replace keep the size of the string?
        splitData = inputLine.split(" ")
        newString = ""

        if splitData[0] == "USE":
            self.use(splitData[1].split(";")[0])
            
        elif splitData[0] == "CREATE":
            #loop through the string to find the '('
            if splitData[1] == "DATABASE":
                #split of semicolon, take the first half (it lacks the semicolon)
                self.createDatabase(splitData[2].split(";")[0])
            else:
                for i in range(0, len(inputLine)):
                    if inputLine[i] == "(":
                        # collect the string from the '(' to the ')'
                        for j in range(i+1, len(inputLine)):
                            newString = newString + inputLine[j]

                            # minus 2 for the last parathesis, the semicolon AND the end character \r
                            if j == len(inputLine)-3:
                                # string ended
                                break
                    # string finished
                        break
                self.table.create(splitData[2], [newString])
        elif splitData[0] == "DROP":
            if splitData[1] == "DATABASE":
                #split of semicolon, take the first half (it lacks the semicolon)
                self.deleteDatabase(splitData[2].split(";")[0])
            else:
                self.table.delete(splitData[2])

        elif splitData[0] == "ALTER":
            # if we are adding a specification to the entity
            if splitData[3] == "ADD":
                # loop from the add
                for i in range(4,len(splitData)):
                    newString = newString + " " + (splitData[i].split(';')[0])
            self.table.update(splitData[2],newString, None)
            
        elif splitData[0] == "SELECT":
            # select all
            if splitData[1] == "*":
                self.table.query(splitData[3].split(';')[0], None)
            # select something where constraint
            else:
                pass
        elif splitData[0] == ".EXIT":
            print("All done.")
            return 0
        
    
    def use(self, location):
        # Not currently using a table
        os.chdir(self.originalDirectory)
        
        if not os.path.exists(location):
            print("!Failed to use database because it does not exist.")
        else:
            os.chdir(location)
        '''     
            if os.getcwd().endswith("Database_management_system"):
                os.chdir(location)
            # currently using a table, have to go back a file location to use another
            else:
                os.chdir(self.originalDirectory + location)
            print("Using database ", location)
        '''
    def createDatabase(self, dataBase):

        os.chdir(self.originalDirectory)

        if not os.path.exists(dataBase):
            os.makedirs(dataBase)
            print("Database ", dataBase, " created.")
        else:
            print("!Failed to create database ", dataBase, " because it already exists.")
    
    def deleteDatabase(self, dataBase):

        os.chdir(self.originalDirectory)

        if os.path.exists(dataBase):
            os.rmdir(dataBase)
            print("Database ", dataBase, " deleted.")
        else:
            print("!Failed to delete database ", dataBase, " because it does not exist.")
    

if __name__ == "__main__":
    d = DBMS()
    d.run()