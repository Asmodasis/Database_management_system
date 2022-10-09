import os
from DBMS import DBMS
from Table import Table

def unit_test_table_create():
    t = Table()
    # create table
    t.create("test_tbl_1.md", None)
    # failed to create table because it already exists
    t.create("test_tbl_1.md", None)

    t.create("test_tbl_3", ['a1 int', 'a2 varchar(20)'])
    # failed to create table because it already exists
    t.create("test_tbl_3.md", ['a1 int', 'a2 varchar(20)'])

def unit_test_table_delete():
    t = Table()
    t.delete("test_tbl_1.md")
    # failed to delete table because it does not exist
    t.delete("test_tbl_2.md")

def unit_test_table_update():
    t = Table()
    # create table
    t.create("test_tbl_update_1.md", ['a1 int', 'a2 varchar(20)'])

    t.update("test_tbl_update_1.md", 'a3 varchar(30)')
    
    t.create("test_tbl_update_2.md", ['a1 int', 'a2 varchar(20)'])

    t.update("test_tbl_update_2.md", 'a3 varchar(30)')
    t.update("test_tbl_update_2.md", 'a4 int')

def unit_test_table_query():
    t = Table()
    t.create("test_tbl_update_1.md", ['a1 int', 'a2 varchar(20)'])
    t.query("test_tbl_1.md")
    t.query("test_tbl_3.md")

def unit_test_DBMS_parse():
    d = DBMS()

if __name__ == "__main__":
    unit_test_table_create()
    unit_test_table_create()
    unit_test_table_delete()
    unit_test_table_query()