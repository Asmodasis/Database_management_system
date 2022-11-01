import os
import math
class Table:
    '''
    This class handles the generation and management of tables in a database.
    A database table will be created as a file within a directory. A database will be the directory iteself.
    
    Attributes
    ----------

    def create(self, tableName, inputList):
        Creates a Table

    def drop(self, tableName):
        Drops a Table

    def delete(self, tableName, constraintName=None, constraintValue=None, operationOnConstraint="equal"):
        Deletes a entity from the Table

    def alter(self, tableName, updateString, constraint=None):
        Adds a characteristic to a table

    def insert(self, tableName, inputList):
        Inserts a list of entries to a Table

    def update(self, tableName, keyToModify, valueToAssign, constraintName, constraintValue):
        Updates a tables values based on the constraint. Constraints applied like where clause.

    def query(self, tableName, selectList=None, constraintName=None, constraintValue=None, operationOnConstraint="equal"):
        Selects a tables values, either all or some.

    def __findConstraint__(self,constraintName,lines):
        Helper function to find a constraint given a list (The where clause).

    def __findSelectionLocations__(self, item, lines):
        Helper function to find the amount of locations on a partial query. 

    def __fixTableName__(self, tableName):
        Helper function to fix the name of the name for reading.

    def __del__(self):
        Helper function to print a newline after table deletion (make the terminal pretty)

    '''
   
    def create(self, tableName, inputList):

        #create the table
        try:
            f = open(self.__fixTableName__(tableName), "x")
            print("Table ", tableName, " created.", sep = '')

            # if input is provided, the table is being created with parameters 
            count = 0
            f = open(self.__fixTableName__(tableName), "a")  
            if inputList is not None:

                #f.write(inputList)

                
                for ele in inputList:
                    f.write(ele)
                    # subtract one to account for the final comma, if split on comma, it would make a false entry
                    if count < len(inputList)-1: 
                        f.write('|')
                        count = count + 1 
                
            # if input in not provided, create a blank table
            else:
                pass
            
            f.close()
            # if fails, creation not possible
        except OSError:
            print("!Failed to create table ", tableName, " because it already exists.", sep = '')
        

    def drop(self, tableName):
        # check the directory path for the file, if there then remove
        if os.path.exists(self.__fixTableName__(tableName)):
            os.remove(self.__fixTableName__(tableName))
            print("Table ", tableName, " deleted.", sep = '')
        else:
            print("!Failed to delete ", tableName, " because it does not exist.", sep = '')

    def delete(self, tableName, constraintName=None, constraintValue=None, operationOnConstraint="equal"):
            
        if not os.path.exists(self.__fixTableName__(tableName)):
            print("!Failed to delete from ", tableName, " because it does not exist.", sep = '')
        elif os.stat(self.__fixTableName__(tableName)).st_size == 0:
            print("!Failed to delete from ", tableName, " because the file is empty.", sep = '')
        else:

            f = open(self.__fixTableName__(tableName), 'r')
            # readlines returns a list of lines, each line is an item in the list
            lines = f.readlines()
            f.close()
            # if function is called, one item is being deleted
            deleteCount = 1
            # find the constraint
            constraintLocation = self.__findConstraint__(constraintName,lines)
           
            f = open(self.__fixTableName__(tableName), 'w')
            f.write(lines[0])
            for item in range(1,len(lines)-1):
                if operationOnConstraint == "equal" and item  != constraintLocation:
                        f.write(lines[item])
                elif operationOnConstraint == "not-equal":
                    # FUTURE IMPLEMENTATION 
                    pass
                elif operationOnConstraint == "greater" and (float(lines[item].split("|")[constraintLocation].strip("\n"))) < (float(constraintValue)):
                        f.write(lines[item])
                elif operationOnConstraint == "less":
                    # FUTURE IMPLEMENTATION 
                    pass
                elif operationOnConstraint == "greater-equal":
                    # FUTURE IMPLEMENTATION 
                    pass
                elif operationOnConstraint == "less-equal":
                    # FUTURE IMPLEMENTATION 
                    pass
                else:
                    # FUTURE IMPLEMENTATION 
                    deleteCount = deleteCount + 1
            print(deleteCount, " records deleted.",sep='') 
            f.close()
    def alter(self, tableName, updateString, constraint=None):
        if not os.path.exists(self.__fixTableName__(tableName)):
            print("!Failed to Alter table ", tableName, " because it does not exist.", sep = '')
        else:
            print("Table ", tableName, "modified.", sep = '')
            f = open(self.__fixTableName__(tableName), 'r')
            # readlines returns a list of lines, each line is an item in the list
            lines = f.readlines()
            f.close()

            if constraint is None and lines is not None:
                lines[0] = lines[0] + '|' + updateString
            # the constraint is the location
            else:
                # Adjusts the whole row (entity) by the constraint (position)
                # Currently requires the decoding of the position prior to call
                lines[constraint] = lines[constraint] + updateString

            #TODO: Inefficient way to handle file updating   
            f = open(self.__fixTableName__(tableName), 'w')
            for item in range(0,len(lines)):
                f.write(lines[item])
            f.close()


    def insert(self, tableName, inputList):
        if not os.path.exists(self.__fixTableName__(tableName)):
            print("!Failed to insert into ", tableName, " because it does not exist.", sep = '')
        elif os.stat(self.__fixTableName__(tableName)).st_size == 0:
            print("!Failed to insert into ", tableName, " because the file is empty.", sep = '')
        else:
            f = open(self.__fixTableName__(tableName), "r+")
    
            # if input is provided, the table is being created with parameters 
            count = 0

            if inputList is not None:
                # TODO: Why?
                # I shouldn't have to find the length of lists this way, len(list) doesn't do what it should 
                # because Python is Python
                iCount = 0
                jCount = 0
                
                for i in f.readline().split("|"):
                    iCount = iCount + 1
                for j in inputList:
                    jCount = jCount  + 1

                if iCount == jCount:
                    f.write('\n')
                    for ele in inputList:
                        f.write(ele)
                        # subtract one to account for the final comma, if split on comma, it would make a false entry
                        if count < len(inputList)-1: 
                            f.write('|')
                            count = count + 1 
                else:
                # more elements added to insert than allowed
                # have to update first
                    print("!Failed to insert into ", tableName, " because the format is incorrect.", sep = '')
                    return
            
            else:
                print("!Failed to insert into ", tableName, " a null entry.", sep = '')
                return
            print("1 new record inserted.")
            f.close()



    def update(self, tableName, keyToModify, valueToAssign, constraintName, constraintValue):
        if not os.path.exists(self.__fixTableName__(tableName)):
            print("!Failed to update table ", tableName, " because it does not exist.", sep = '')
        elif os.stat(self.__fixTableName__(tableName)).st_size == 0:
            print("!Failed to update table", tableName, " because the fdile is empty.", sep = '')
        else:

            
            modifyCount = 0
        
            f = open(self.__fixTableName__(tableName), 'r+')
            # readlines returns a list of lines, each line is an item in the list
            lines = f.readlines()
            f.close()


            # The location of the key to modify
            keyModifyLocation = 0
            constraintLocation = 0

            for cons in lines[0].split("|"):
                if constraintName not in cons:
                    constraintLocation = constraintLocation + 1
                else:
                    # Location of the constrain is found -- column
                    break

            for key in lines[0].split("|"):
                if keyToModify not in key:
                    keyModifyLocation = keyModifyLocation + 1
                else:
                    # Location of the key to modify is found -- column
                    break

            # Break apart the line into a C++ style 2d array 
            # Python is confusing
            newLineList = []
            for line in lines:
                newLineList.append(line.split("|"))

            for i in range(0,len(newLineList)):
                for _ in range(0,len(newLineList[0])-1):
                    if constraintValue in newLineList[i][constraintLocation]:

                        if keyModifyLocation == len(newLineList[0])-1:
                            newLineList[i][keyModifyLocation] = valueToAssign+"\n"
                            modifyCount = modifyCount + 1
                        else:
                            newLineList[i][keyModifyLocation] = valueToAssign
                            modifyCount = modifyCount + 1
                        
                        
            
            # Reconstruct into a python style format
            
            f = open(self.__fixTableName__(tableName), 'w')
            for i in newLineList:
                f.write("|".join(i))
            f.close()
            
            if modifyCount > 1:
                modifyCount = modifyCount - 2
            else:
                print("\n")
            print(modifyCount, " records modified.",sep='')

                    

    def query(self, tableName, selectList=None, constraintName=None, constraintValue=None, operationOnConstraint="equal"):

        if not os.path.exists(self.__fixTableName__(tableName)):
            print("!Failed to query table ", tableName, " because it does not exist.", sep = '')
        elif os.stat(self.__fixTableName__(tableName)).st_size == 0:
            print("!Failed to query table ", tableName, " because the file is empty.", sep = '')
        else:
            f = open(self.__fixTableName__(tableName), 'r')
            lines = f.readlines()
        
            # if no constraints, query the whole file
            if constraintName is None:
                for line in lines:
                    print(line, sep = '', end='')
                    #print("\n",end='')
            else:

                constraintLocation = self.__findConstraint__(constraintName,lines)

                selectionInts = []
                # Allows the selection of multiply entries

                for item in selectList:
                    selectionInts.append(self.__findSelectionLocations__(item, lines))

                for line in lines:

                    printCount = 1
                    for inte in selectionInts:

                        if operationOnConstraint == "equal" and selectList[constraintLocation] == constraintValue:
                            # FUTURE IMPLEMENTATION 
                            pass 
                        elif operationOnConstraint == "not-equal" and  line.split("|")[constraintLocation] != constraintValue:
                            
                            print(line.split("|")[inte],end='')
                            
                            if printCount < len(selectionInts):
                                print("|",end='')
                                printCount = printCount + 1
                            else:
                                printCount = 1
                        elif operationOnConstraint == "greater" and selectList[constraintLocation] > constraintValue:
                            # FUTURE IMPLEMENTATION 
                            pass
                        elif operationOnConstraint == "less" and selectList[constraintLocation] < constraintValue:
                            # FUTURE IMPLEMENTATION 
                            pass
                        elif operationOnConstraint == "greater-equal" and selectList[constraintLocation] <= constraintValue:
                            # FUTURE IMPLEMENTATION 
                            pass
                        elif operationOnConstraint == "less-equal" and constraintValue <= selectList[constraintLocation]:
                            # FUTURE IMPLEMENTATION 
                            pass
                        else:
                            # FUTURE IMPLEMENTATION 
                            pass
            print("\n")
            f.close()  

    def __findConstraint__(self,constraintName,lines):
        # find the constraint

        constraintLocation = 0  
        for constraint in lines[0].split("|"):

            if constraintName not in constraint:
                constraintLocation = constraintLocation + 1
            else:
                # Constraint name location has been found

                break

        return constraintLocation

    def __findSelectionLocations__(self, item, lines):
        count = 0
        for line in lines[0].split("|"):
            if item in line:
                return count
            else:
                count = count + 1

    def __fixTableName__(self, tableName):
        # append the file extension if needed
        if not tableName.endswith('.md'):
            tableName = tableName + '.md'
        return tableName

 