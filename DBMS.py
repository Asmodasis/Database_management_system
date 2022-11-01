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

    def __init__(self):
        Create the DBMS

    def run(self):
        Run the DBMS

    def __parseInput__(self, inputLine):
        This function parses the input provided to the database management system.
        After parsing it will call the appropriate table function to be operated on.
                        
    def use(self, location):
        Uses a database.
    def createDatabase(self, dataBase):
        Creates a database.

    def deleteDatabase(self, dataBase):
        Delets a database.
        
    '''
   
    # creates the database management system, this will form the link with the terminal to accept input
    def __init__(self):
        self.table = Table()
        # retrieve and store the original directory
        self.originalDirectory = os.getcwd()

    def run(self):

        
        try:
            x = ''
            while(True):
                # retrieve all the SQL commands
                x = input()
                self.__parseInput__(x) 
        except EOFError:        
            print("All Done.")

    def __parseInput__(self, inputLine):
        
        #input Line will contain an entire line of sql code
        if inputLine == '':
            return 0
        splitData = inputLine.split(" ")
        newString = ""
        passSign = ""

        for i in range(0, len(splitData)):
            splitData[i] = splitData[i].replace(';', '').replace('\r', '')


        if splitData[0] == "USE" or splitData[0] == "use" :
            self.use(splitData[1])
            
        elif splitData[0] == "CREATE" or splitData[0] == "create" :

            #loop through the string to find the '('
            if splitData[1] == "DATABASE" or splitData[1] == "database" :

                self.createDatabase(splitData[2])
            else: # ELSE CREATE TABLE
                for i in range(3,len(splitData),+2):

                    if not splitData[i].__contains__("),"):
                        # does not contains a varchar
                        splitData[i].replace('(','').replace(')','') 

                for i in range(0, len(inputLine)):
                    if inputLine[i] == "(":
                        # collect the string from the '(' to the ')'
                        for j in range(i+1, len(inputLine)):
                        
                            if (inputLine[j] == ")" and inputLine[j+1] == ";"):
                                # string ended
                                break
                            else:
                                newString = newString + inputLine[j].replace('\r', '').replace('\t','')

                    # string finished
                        break
                
                returnList = newString.split(",")

                self.table.create(splitData[2], returnList)

        elif splitData[0] == "DROP" or splitData[0] == "drop" :
            if splitData[1] == "DATABASE" or splitData[1] == "database" :
                #split of semicolon, take the first half (it lacks the semicolon)
                self.deleteDatabase(splitData[2])
            else:
                self.table.drop(splitData[2])

        elif splitData[0] == "ALTER" or splitData[0] == "alter" :
            # if we are adding a specification to the entity
            if splitData[3] == "ADD" or splitData[3] == "add" :
                # loop from the add
                for i in range(4,len(splitData)):
                    newString = newString + " " + (splitData[i])
            self.table.alter(splitData[2],newString, None)
            
        elif splitData[0] == "SELECT" or splitData[0] == "select" :
            # select all
            if splitData[1] == "*":
                self.table.query(splitData[3], None,None,None,None)
            # select something where constraint
            else:
                
                selectList = []
                
                for j in range(1,  len(splitData)):
                    
                    if splitData[j] == "FROM" or splitData[j] == "from":
                        break
                    selectList.append(splitData[j].strip(","))
                if splitData[7] == "=":
                    passSign = "equal"
                elif splitData[7] == "!=":
                    passSign = "not-equal"
                elif splitData[7] == ">":
                    passSign = "greater"
                elif splitData[7] == "<":
                    passSign = "less"
                elif splitData[7] == ">=":
                    passSign = "greater-equal"
                elif splitData[7] == "<=":
                    passSign = "less-equal"
                
                self.table.query(splitData[4], selectList,splitData[6],splitData[8],passSign)

        elif splitData[0] == "INSERT" or splitData[0] == "insert" :

            if splitData[1] == "INTO" or splitData[1] == "into" :
                for i in range(3,len(splitData),+2):

                    if not splitData[i].__contains__("),"):
                        # does not contains a varchar
                        splitData[i].replace('(','').replace(')','') 

                for i in range(0, len(inputLine)):
                    if inputLine[i] == "(":
                        # collect the string from the '(' to the ')'
                        for j in range(i+1, len(inputLine)):
                        
                            if (inputLine[j] == ")" and inputLine[j+1] == ";"):
                                # string ended
                                break
                            else:
                                newString = newString + inputLine[j].replace('\r', '').replace('\t','')

                    # string finished
                        break
                
                returnList = newString.split(",")

                self.table.insert(splitData[2], returnList)
            # select something where constraint
            else:
                pass
        elif splitData[0] == "DELETE" or splitData[0] == "delete" :

            #TODO: This implementation can only delete from a table with ONE constraint
            if splitData[1] == "FROM" or splitData[1] == "from" :
                if splitData[3] == "WHERE" or splitData[3] == "where" :
                    if splitData[5] == "=":
                        passSign = "equal"
                    elif splitData[5] == "!=":
                        passSign = "not-equal"
                    elif splitData[5] == ">":
                        passSign = "greater"
                    elif splitData[5] == "<":
                        passSign = "less"
                    elif splitData[5] == ">=":
                        passSign = "greater-equal"
                    elif splitData[5] == "<=":
                        passSign = "less-equal"
                    self.table.delete(splitData[2],splitData[4],splitData[6],passSign)
            else:
                # FUTURE IMPLEMENTATION
                pass
        elif splitData[0] == "UPDATE" or splitData[0] == "update":
        
            if splitData[2] == "SET" or splitData[2] == "set" :
                  #TODO: This implementation can only delete from a table with ONE constraint
           
                    if splitData[8] == "=":
                        self.table.update(splitData[1],splitData[3],splitData[5],splitData[7],splitData[9])
                    elif splitData[8] == "!=":
                        # FUTURE IMPLEMENTATION
                        pass
                    elif splitData[8] == ">":
                        # FUTURE IMPLEMENTATION
                        pass
                    elif splitData[8] == "<":
                        # FUTURE IMPLEMENTATION
                        pass
                    elif splitData[8] == ">=":
                        # FUTURE IMPLEMENTATION
                        pass
                    elif splitData[8] == "<=":
                        # FUTURE IMPLEMENTATION
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
            print("Database ", dataBase, " deleted.", sep = '')
        else:
            print("!Failed to delete database ", dataBase, " because it does not exist.", sep = '')
    def __del__(self):
        # on table end, print a new line to make terminal read more
        
        print("\n")

if __name__ == "__main__":
    d = DBMS()
    d.run()