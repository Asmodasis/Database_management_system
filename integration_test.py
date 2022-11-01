import os 
from DBMS import DBMS

d = DBMS()

def integration_test_DBMS_create_database():
    d.createDatabase("db_integration_1")
def integration_test_DBMS_delete_database():
    d.createDatabase("db_integration_2")
    d.deleteDatabase("db_integration_2")
def integration_test_DBMS_create_table():
    d.__parseInput__("CREATE TABLE tbl_1 (a1 int, a2 varchar(20));")
def integration_test_DBMS_delete_table():
    d.__parseInput__("DROP TABLE tbl_1;")
def integration_test_DBMS_use_database():
    d.createDatabase("DB_1")
    d.createDatabase("DB_2")
    d.use("DB_1")
    d.__parseInput__("CREATE TABLE tbl_1 (a1 int, a2 varchar(20));")

def integration_test_DBMS_parse_database_create():
    d.__parseInput__("CREATE DATABASE db_1;")
def integration_test_DBMS_parse_database_delete():
    d.__parseInput__("DROP DATABASE db_1;")
def integration_test_DBMS_parse_database_use():
    d.__parseInput__("CREATE DATABASE db_use_me;")
    d.__parseInput__("USE db_use_me;")
    d.__parseInput__("CREATE TABLE tbl_1 (a1 int, a2 varchar(20));")
    d.__parseInput__("CREATE DATABASE db_use_me2;")
    d.__parseInput__("USE db_use_me2;")
    d.__parseInput__("CREATE TABLE tbl_1 (a1 int, a2 varchar(20));")

def integration_test_DBMS_parse_table_create():
    pass
def integration_test_DBMS_parse_table_delete():
    pass

def integration_test_DBMS_parse_table_alter():
    d.__parseInput__("CREATE DATABASE db_alter_1;")
    d.__parseInput__("USE db_alter_1;")
    d.__parseInput__("CREATE TABLE tbl_1 (a1 int, a2 varchar(20));")
    d.__parseInput__("ALTER TABLE tbl_1 ADD a3 float;")

def integration_test_DBMS_parse_table_select():
    pass
    d.__parseInput__("CREATE DATABASE db_select_1;")
    d.__parseInput__("USE db_select_1;")
    d.__parseInput__("CREATE TABLE tbl_1 (a1 int, a2 varchar(20));")
    d.__parseInput__("SELECT * FROM tbl_1;")

def integration_test_DBMS_part_2():
    d.__parseInput__("CREATE DATABASE CS457_PA2;")
    d.__parseInput__("USE CS457_PA2")
    d.__parseInput__("CREATE TABLE Product (pid int, name varchar(20), price float);")
    
    d.__parseInput__("insert into Product values(1, 'Gizmo', 19.99);")
    d.__parseInput__("insert into Product values(2,	'PowerGizmo', 29.99);")
    d.__parseInput__("insert into Product values(3,	'SingleTouch', 	149.99);")
    d.__parseInput__("insert into Product values(4,	'MultiTouch', 	199.99);")
    d.__parseInput__("insert into Product values(5,	'SuperGizmo', 	49.99);")
    
    d.__parseInput__("select * from Product;")

    d.__parseInput__("update Product set name = 'Gizmo' where name = 'SuperGizmo';")
    d.__parseInput__("update Product set price = 14.99 where name = 'Gizmo';")

    d.__parseInput__("select * from Product;")

    d.__parseInput__("delete from product where name = 'Gizmo';")
    d.__parseInput__("delete from product where price > 150;")

    d.__parseInput__("select * from Product;")

    d.__parseInput__("select name, price from product where pid != 2;")

if __name__ == "__main__":
    #integration_test_DBMS_create_database()
    #integration_test_DBMS_delete_database()

    #integration_test_DBMS_create_table()
    #integration_test_DBMS_create_table()

    #integration_test_DBMS_delete_table()
    #integration_test_DBMS_use_database()
    #integration_test_DBMS_parse_database_create()
    #integration_test_DBMS_parse_database_delete()
    #integration_test_DBMS_parse_database_use()
    #integration_test_DBMS_parse_table_alter()
    #integration_test_DBMS_parse_table_select()
    integration_test_DBMS_part_2()