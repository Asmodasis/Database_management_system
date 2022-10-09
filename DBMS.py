from genericpath import isfile
import os
import shutil # recursive remove
from Table import Table

class DBMS:

    '''
    This class is a database management system. Of which handles the creation and management of databases.
    
    Attributes
    ----------
    originalDirectory
        The original directory for the database management system, used to cd back and forth

    table
        The class that handles table operatios like create, delete etc

    Methods
    ----------
    run()
        Run the database management system

    __parseInput__(inputLine)
        Parse the input into sql commands

    use(location)
        Use a database

    createDatabase(dataBase)
        Create a database

    deleteDatabase(dataBase)
        Delete a database
        
    '''
   
    # creates the database management system, this will form the link with the terminal to accept input
    def __init__(self):
        self.table = Table()
        # retrieve and store the original directory
        self.originalDirectory = os.getcwd()

    def run(self):

        x = ''
        while(True):
            # retrieve all the SQL commands
            x = input()

            if x.__contains__('.EXIT'):
                print("All done.", sep = '')
                return 0
            else:
                self.__parseInput__(x)
        

    def __parseInput__(self, inputLine):

        #input Line will contain an entire line of sql code
        if inputLine == '':
            return 0
        splitData = inputLine.split(" ")
        newString = ""

        for i in range(0, len(splitData)):

            splitData[i] = splitData[i].replace(';', '').replace('\r', '')

        if splitData[0] == "USE":
            self.use(splitData[1])
            
        elif splitData[0] == "CREATE":

            #loop through the string to find the '('
            if splitData[1] == "DATABASE":

                self.createDatabase(splitData[2])
            else:
                for i in range(0, len(inputLine)):
                    if inputLine[i] == "(":
                        # collect the string from the '(' to the ')'
                        for j in range(i+1, len(inputLine)):
                            newString = newString + inputLine[j]

                            if inputLine[j] == ")" and inputLine[j+1] == ")":
                                # string ended
                                break
                    # string finished
                        break
                self.table.create(splitData[2], [newString])

        elif splitData[0] == "DROP":
            if splitData[1] == "DATABASE":
                #split of semicolon, take the first half (it lacks the semicolon)
                self.deleteDatabase(splitData[2])
            else:
                self.table.delete(splitData[2])

        elif splitData[0] == "ALTER":
            # if we are adding a specification to the entity
            if splitData[3] == "ADD":
                # loop from the add
                for i in range(4,len(splitData)):
                    newString = newString + " " + (splitData[i])
            self.table.update(splitData[2],newString, None)
            
        elif splitData[0] == "SELECT":
            # select all
            if splitData[1] == "*":
                self.table.query(splitData[3], None)
            # select something where constraint
            else:
                pass
    
    
    def use(self, location):
        # Not currently using a table

        os.chdir(self.originalDirectory)
        
        if not os.path.exists(location):
            print("!Failed to use database because it does not exist.", sep = '')
        else:
            print("Using database ", location, ".", sep = '')
            os.chdir(location)

    def createDatabase(self, dataBase):
 
        os.chdir(self.originalDirectory)

        try:
            os.makedirs(dataBase,exist_ok=False)
            print("Database ", dataBase, " created.", sep = '')
        except FileExistsError:
            print("!Failed to create database ", dataBase," because it already exists.", sep = '')

    def deleteDatabase(self, dataBase):

        os.chdir(self.originalDirectory)

        if os.path.exists(dataBase):
            shutil.rmtree(dataBase)
            #os.rmdir(dataBase)
            print("Database ", dataBase, " deleted.", sep = '')
        else:
            print("!Failed to delete database ", dataBase, " because it does not exist.", sep = '')
    

if __name__ == "__main__":
    d = DBMS()
    d.run()