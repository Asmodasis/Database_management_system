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
    t.drop("test_tbl_1.md")
    # failed to delete table because it does not exist
    t.drop("test_tbl_2.md")

def unit_test_table_alter():
    t = Table()
    # create table
    t.create("test_tbl_alter_1.md", ['a1 int', 'a2 varchar(20)'])

    t.alter("test_tbl_alter_1.md", 'a3 varchar(30)')
    
    t.create("test_tbl_alter_2.md", ['a1 int', 'a2 varchar(20)'])

    t.alter("test_tbl_alter_2.md", 'a3 varchar(30)')
    t.alter("test_tbl_alter_2.md", 'a4 int')

def unit_test_table_query():
    t = Table()
    t.create("test_tbl_alter_1.md", ['a1 int', 'a2 varchar(20)'])
    t.query("test_tbl_1.md")
    t.query("test_tbl_3.md")

def unit_test_DBMS_parse():
    d = DBMS()

def unit_test_table_insert():
    #CREATE TABLE Product (pid int, name varchar(20), price float);
    #insert into Product values(1,	'Gizmo',      	19.99);
    t = Table()
    t.create("test_tbl_insert_1.md", ['pid int', 'name varchar(20)', 'price float'])
    t.insert("test_tbl_insert_1.md", ['1','Gizmo', '19.99'])
    t.insert("test_tbl_insert_1.md",['2',	'PowerGizmo', 	'29.99'])
    t.insert("test_tbl_insert_1.md",['3'])
    t.query("test_tbl_insert_1.md")

def unit_test_table_update():
    t = Table()
    t.create("test_tbl_update_1.md", ['pid int', 'name varchar(20)', 'price float'])
    t.insert("test_tbl_update_1.md", ['1','Gizmo', '19.99'])
    t.insert("test_tbl_update_1.md", ['2',	'PowerGizmo', 	'29.99'])
    #update test_tbl_update_1 
    #set price = 14.99 
    #where name = 'Gizmo';
    #update(self, tableName, keyToModify, valueToAssign, constraint=None)
    t.update("test_tbl_update_1.md","price","14.99", "name","Gizmo")
    t.query("test_tbl_update_1.md")

def unit_test_table_delete_from():
    #delete from product 
    #where name = 'Gizmo';
    t = Table()
    t.create("test_tbl_delete_1.md", ['pid int', 'name varchar(20)', 'price float'])
    t.insert("test_tbl_delete_1.md", ['1','Gizmo', '19.99'])
    t.insert("test_tbl_delete_1.md", ['2',	'PowerGizmo', 	'29.99'])
    t.delete("test_tbl_delete_1.md", "name", "Gizmo", "equal")

def unit_test_table_query_with_constraint():
    #select name, price 
    #from product 
    #where pid != 2;
    t = Table()
    t.create("test_tbl_query_with_constraint_1.md", ['pid int', 'name varchar(20)', 'price float'])
    t.insert("test_tbl_query_with_constraint_1.md", ['1',   'Gizmo',        '19.99'])
    t.insert("test_tbl_query_with_constraint_1.md", ['2',	'PowerGizmo', 	'29.99'])
    t.insert("test_tbl_query_with_constraint_1.md", ['3',	'SingleTouch', 	'149.99'])
    t.insert("test_tbl_query_with_constraint_1.md", ['4',	'Multitouch', 	'199.99'])
    t.insert("test_tbl_query_with_constraint_1.md", ['5',	'SuperGizmo', 	'49.99'])
    t.query("test_tbl_query_with_constraint_1.md", ["name", "price"],"pid", "2","not-equal")

def unit_test_table_delete_with_constraint():
    #delete from product 
    #where price > 150;
    t = Table()
    t.create("test_tbl_delete_with_constraint_1.md", ['pid int', 'name varchar(20)', 'price float'])
    t.insert("test_tbl_delete_with_constraint_1.md", ['1',   'Gizmo',        '19.99'])
    t.insert("test_tbl_delete_with_constraint_1.md", ['2',	'PowerGizmo', 	'29.99'])
    t.insert("test_tbl_delete_with_constraint_1.md", ['3',	'SingleTouch', 	'149.99'])
    t.insert("test_tbl_delete_with_constraint_1.md", ['4',	'Multitouch', 	'199.99'])
    t.insert("test_tbl_delete_with_constraint_1.md", ['5',	'SuperGizmo', 	'49.99'])
    t.delete("test_tbl_delete_with_constraint_1.md","price", 150 ,"greater")

if __name__ == "__main__":
    #unit_test_table_create()
    #unit_test_table_alter()
    #unit_test_table_delete()
    #unit_test_table_query()
    unit_test_table_insert()
    #unit_test_table_update()
    #unit_test_table_delete_from()
    #unit_test_table_query_with_constraint()
    #unit_test_table_delete_with_constraint()