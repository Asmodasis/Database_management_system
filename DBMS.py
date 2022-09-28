from genericpath import isfile
import os
from Table import Table

class DBMS:
    # creates the database management system, this will form the link with the terminal to accept input
    def __init__(self):
        self.table = Table()
    def run(self):
        '''
        
        if len(sys.argv) > 1:
            # There is more than one argument, we have file mode
            print("{TEST} file mode")
            #invalid input
            if sys.argv[1] is not '<':
                print("Invalid terminal input: Please try again.")
            else:
                self.__readFromFile__(sys.argv[2])

            
            
        else: 
            print("{TEST} terminal mode")
            self.__readFromTerminal__()
            
        '''
        x = ''
        while('.EXIT' not in x):
            x = input()
            #print(x)
            self.__parseInput__(x)
    '''    
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
    '''
    def __parseInput__(self, inputLine):
        #input Line will contain an entire line of sql code
        #splitData = inputLine.replace(';','').replace('\r','').split(" ")
        #TODO: Why does .replace keep the size of the string?
        splitData = inputLine.split(" ")
        newString = ""

        if splitData[0] == "USE":
            self.use(splitData[1].split(";")[0])
            
        elif splitData[0] == "CREATE":
            print("Test create")
            #loop through the string to find the '('
            if splitData[1] == "DATABASE":
                #split of semicolon, take the first half (it lacks the semicolon)
                self.createDatabase(splitData[2].split(";")[0])
            else:
                print("Test create else")
                for i in range(0, len(inputLine)):
                    print("FOR FOR")
                    if inputLine[i] == "(":
                        # collect the string from the '(' to the ')'
                        for j in range(i+1, len(inputLine)):
                            print("Test create else FOR LOOP")
                            newString = newString + inputLine[j]

                            # minus 2 for the last parathesis, the semicolon AND the end character \r
                            if j == len(inputLine)-3:
                                # string ended
                                break
                    # string finished
                        break
                print("{TEST} Newstring: ", newString) 
                self.table.create(splitData[2], newString)
        elif splitData[0] == "DROP":
            print("Test drop")
            if splitData[1] == "DATABASE":
                #split of semicolon, take the first half (it lacks the semicolon)
                self.deleteDatabase(splitData[2].split(";")[0])
            else:
                self.table.delete(splitData[2])

        elif splitData[0] == "ALTER":
            for i in range(3,len(splitData)):
                newString = newString + (splitData[i])
            print("Test alter")
            self.table.update(splitData[2],newString, None)
            
        elif splitData[0] == "SELECT":
            # select all
            if splitData[1] == "*":
                self.table.query(splitData[3], None)
            # select something where constraint
            else:
                pass
        elif splitData[0] == ".EXIT":
            print("Test exit")
            return 0
        
    
    def use(self, location):
        # Not currently using a table
        if not os.path.exists(location):
            print("!Failed to use database because it does not exist.")
        else:     
            if os.getcwd().endswith("Database_management_system"):
                os.chdir(location)
            # currently using a table, have to go back a file location to use another
            else:
                os.chdir(str("../"+location))
            print("Using database ", location)

    def createDatabase(self, dataBase):
        print("{TEST} createDatabase Called") ##### REMOVE
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
    

if __name__ == "__main__":
    d = DBMS()
    d.run()