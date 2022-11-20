import os
import shutil # recursive remove
from Table import Table
import sys

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
            
    def innerJoin(self, source, target, sourceElement, targetElement, operation):
        Inner join between two tables
    def outerJoin(self, source, target, pivot, sourceElement, targetElement, operation):
        Outer join between two tables
    def __fixTableName__(self, tableName):
        fixes a table name
    def __findConstraint__(self,constraintName,lines):
        Finds the constraints for the join
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
                if ';' in x:
                    self.__parseInput__(x)  
                else:
                    pass
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
            #for i in splitData:
                #print("splitdata == ", i) ## REMOVE
            #loop through the string to find the '('
            if splitData[1] == "DATABASE" or splitData[1] == "database" :

                self.createDatabase(splitData[2])
            else: # ELSE CREATE TABLE
                s = inputLine.split('(',1)
                # To account for the lack of a space on the command
                '''
                print("length of S == ",len(s))
                print("s0 == ",s[0].split(' ',)[2])
                print("s1 == ",s[1].replace(');','') )
                for i in range(3,len(splitData),+2):

                    if not splitData[i].__contains__("),"):
                        # does not contains a varchar
                        splitData[i].replace('(','').replace(')','') 


                '''
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

                self.table.create(s[0].split(' ',)[2], returnList)

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

                #self.table.query(splitData[3], None,None,None,None)
                # Inner
                if ('inner join' in inputLine or 'INNER JOIN' in inputLine):
                    #select * from Employee E inner join Sales S on E.id = S.employeeID;
                    if splitData[11] == "=":
                        passSign = "equal"
                    elif splitData[11] == "!=":
                        passSign = "not-equal"
                    elif splitData[11] == ">":
                        passSign = "greater"
                    elif splitData[11] == "<":
                        passSign = "less"
                    elif splitData[11] == ">=":
                        passSign = "greater-equal"
                    elif splitData[11] == "<=":
                        passSign = "less-equal"
                    self.innerJoin(splitData[3], splitData[7], splitData[10], splitData[12], passSign)
                elif ('where' in inputLine or 'WHERE' in inputLine and 'join' not in inputLine):
                    #select * from Employee E, Sales S where E.id = S.employeeID;
                    if splitData[9] == "=":
                        passSign = "equal"
                    elif splitData[9] == "!=":
                        passSign = "not-equal"
                    elif splitData[9] == ">":
                        passSign = "greater"
                    elif splitData[9] == "<":
                        passSign = "less"
                    elif splitData[9] == ">=":
                        passSign = "greater-equal"
                    elif splitData[9] == "<=":
                        passSign = "less-equal"
                    self.innerJoin(splitData[3], splitData[5], splitData[8], splitData[10], passSign)
                elif 'left outer join' in inputLine or 'LEFT OUTER JOIN' in inputLine: 
                    #print("{TEST} parse left outer join")
                    #select * from Employee E left outer join Sales S on E.id = S.employeeID;
                    if splitData[12] == "=":
                        passSign = "equal"
                    elif splitData[12] == "!=":
                        passSign = "not-equal"
                    elif splitData[12] == ">":
                        passSign = "greater"
                    elif splitData[12] == "<":
                        passSign = "less"
                    elif splitData[12] == ">=":
                        passSign = "greater-equal"
                    elif splitData[12] == "<=":
                        passSign = "less-equal"
                    self.outerJoin(splitData[3], splitData[8], 'left', splitData[11], splitData[13], passSign)
            else:
                pass
                    # FUTURE IMPLEMENTATION
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
    
    # Not the best method to handle joins, this method requires the creation of separate tables for the join operation
    def innerJoin(self, source, target, sourceElement, targetElement, operation):

        sourceFile = open(self.__fixTableName__(source), 'r')
        targetFile = open(self.__fixTableName__(target), 'r')
        sourceLines = sourceFile.readlines()
        targetLines = targetFile.readlines()
        sourceFile.close()
        targetFile.close()
        sourceConstraint = self.__findConstraint__(sourceElement, sourceLines)
        targetConstraint = self.__findConstraint__(targetElement, targetLines)

        print(sourceLines[0].replace('\n','') +"|"+ targetLines[0].replace('\n',''))
        if operation == "equal":
            for i in range(1,len(sourceLines)):
                for j in range(1,len(targetLines)):
                    if sourceLines[i][sourceConstraint] == targetLines[j][targetConstraint]:
                        #print("{TEST} in for")
                        print(sourceLines[i].replace('\n','') +"|"+ targetLines[j].replace('\n',''))
            #print('\n')
        elif operation == "not-equal":
            # FUTURE IMPLEMENTATION 
            pass
        elif operation == "greater":
            # FUTURE IMPLEMENTATION 
            pass
        elif operation == "less":
            # FUTURE IMPLEMENTATION 
            pass
        elif operation == "greater-equal":
            # FUTURE IMPLEMENTATION 
            pass
        elif operation == "less-equal":
            # FUTURE IMPLEMENTATION 
            pass
        else:
            # FUTURE IMPLEMENTATION 
            pass
        
    # Might be better suited in a single function
    # Future implementation    
    def outerJoin(self, source, target, pivot, sourceElement, targetElement, operation):

        sourceFile = open(self.__fixTableName__(source), 'r')
        targetFile = open(self.__fixTableName__(target), 'r')
        sourceLines = sourceFile.readlines()
        targetLines = targetFile.readlines()
        sourceFile.close()
        targetFile.close()
        sourceConstraint = self.__findConstraint__(sourceElement, sourceLines)
        targetConstraint = self.__findConstraint__(targetElement, targetLines)

        # left outer join
        if pivot == 'left':

            print(sourceLines[0].replace('\n','') +"|"+ targetLines[0].replace('\n',''))
            for i in range(1,len(sourceLines)):
                for j in range(1,len(targetLines)):
                    if sourceLines[i][sourceConstraint] == targetLines[j][targetConstraint]:
                        print(sourceLines[i].replace('\n','') +"|"+ targetLines[j].replace('\n',''))
            
            # Find all the targets
            targetList = []
            for h in range(1,len(targetLines)):
                targetList.append(targetLines[h][targetConstraint])

            #Check if the source is in the targets, if not print it. This is the definition of a left outer join
            for k in range(1,len(sourceLines)):
                if sourceLines[k][sourceConstraint] not in targetList:
                    print(sourceLines[k].replace('\n',''),end='')
                    for _ in range(0, len(targetList[:])-1):
                        print('|',end='')
                    print('\n',end='')

            if operation == "equal":
                # FUTURE IMPLEMENTATION 
                pass 
            elif operation == "not-equal":
                # FUTURE IMPLEMENTATION 
                pass
            elif operation == "greater":
                # FUTURE IMPLEMENTATION 
                pass
            elif operation == "less":
                # FUTURE IMPLEMENTATION 
                pass
            elif operation == "greater-equal":
                # FUTURE IMPLEMENTATION 
                pass
            elif operation == "less-equal":
                # FUTURE IMPLEMENTATION 
                pass
            else:
                # FUTURE IMPLEMENTATION 
                pass
        else: # right outer join
            print("right outer join")
   
    def __fixTableName__(self, tableName):
        # append the file extension if needed
        if not tableName.endswith('.md'):
            tableName = tableName + '.md'
        return tableName
    
    def __findConstraint__(self,constraintName,lines):
        # find the constraint
        
        constraintLocation = 0  
        for constraint in lines[0].split("|"):

            if constraintName.split('.')[1] not in constraint:
                constraintLocation = constraintLocation + 1
            else:
                # Constraint name location has been found

                break

        return constraintLocation

    def __del__(self):
        # on table end, print a new line to make terminal read more
        
        print("\n")

if __name__ == "__main__":
    d = DBMS()
    d.run()