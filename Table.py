import os
'''
This class handles the generation and management of tables in a database.
A database table will be created as a file within a directory. A database will be the directory iteself.
'''
class Table:


    def create(self, fileName, inputList):
        # append the file extension if needed
        if not fileName.endswith('.md'):
            fileName = fileName + '.md'
        
        #create the table
        try:
            f = open(fileName, "x")
            print("Table ", fileName, " created.")
        # if fails, creation not possible
        except OSError:
            print("!Failed to create table ", fileName, " because it already exists.")
        
        # if input is provided, the table is being created with parameters 
        if inputList is not None:
            f = open(fileName, "w")
            for ele in inputList:
                f.write(ele)
                f.write(',')
            f.close()
        # if input in not provided, create a blank table


    def delete(self, fileName):
        if os.path.exists(fileName):
            os.remove(fileName)
            print("Table ", fileName, " deleted.")
        else:
            print("!Failed to delete table ", fileName, " because it does not exist.")

    def update(self):
        pass
    
    def query(self):
        pass
        