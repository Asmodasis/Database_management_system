import os
'''
This class handles the generation and management of tables in a database.
A database table will be created as a file within a directory. A database will be the directory iteself.
'''
class Table:

    '''
    function: create

    '''
    def create(self, fileName, inputList):
        
        #create the table
        try:
            f = open(self.__fixFileName__(fileName), "x")
            print("Table ", fileName, " created.")

            # if input is provided, the table is being created with parameters 
            count = 0
            f = open(self.__fixFileName__(fileName), "a")  
            if inputList is not None:

                #f.write(inputList)

                
                for ele in inputList:
                    f.write(ele)
                    # subtract one to account for the final comma, if split on comma, it would make a false entry
                    if count < len(inputList)-1: 
                        f.write(',')
                        count = count + 1 
                
            # if input in not provided, create a blank table
            else:
                pass
            
            f.close()
            # if fails, creation not possible
        except OSError:
            print("!Failed to create table ", fileName, " because it already exists.")
        
      

        


    def delete(self, fileName):
        # check the directory path for the file, if there then remove
        if os.path.exists(self.__fixFileName__(fileName)):
            os.remove(self.__fixFileName__(fileName))
            print("Table ", fileName, " deleted.")
        else:
            print("!Failed to delete ", fileName, " because it does not exist.")


    def update(self, fileName, updateString, constraint=None):
        if not os.path.exists(self.__fixFileName__(fileName)):
            print("!Failed to update table ", fileName, " because it does not exist.")
        else:
            print("Table ", fileName, "modified.")
            f = open(self.__fixFileName__(fileName), 'r')
                # readlines returns a list of lines, each line is an item in the list
            lines = f.readlines()
            f.close()

            if constraint is None and lines is not None:
                lines[0] = lines[0] + ',' + updateString
            # the constraint is the location
            else:
                # Adjusts the whole row (entity) by the constraint (position)
                # Currently requires the decoding of the position prior to call
                lines[constraint] = lines[constraint] + updateString

            #TODO: Inefficient way to handle file updating   
            f = open(self.__fixFileName__(fileName), 'w')
            for item in range(0,len(lines)):
                f.write(lines[item])
            f.close()

    def query(self, fileName, constraint=None):
        if not os.path.exists(self.__fixFileName__(fileName)):
            print("!Failed to query table ", fileName, " because it does not exist.")
        else:
            f = open(self.__fixFileName__(fileName), 'r')

            # if no constraints, query the whole file
            if constraint is None:
                lines = f.readlines()
                for line in lines:
                    print(line.replace(",", " | "))
            else:
                pass

            f.close()
        
    def __fixFileName__(self, fileName):
        # append the file extension if needed
        if not fileName.endswith('.md'):
            fileName = fileName + '.md'
        return fileName