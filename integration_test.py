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
    d.__parseInput__("USE db_use_me2;")
    d.__parseInput__("CREATE TABLE tbl_1 (a1 int, a2 varchar(20));")
def integration_test_DBMS_parse_table_create():
    pass
def integration_test_DBMS_parse_table_delete():
    pass
def integration_test_DBMS_parse_table_alter():
    pass
def integration_test_DBMS_parse_table_select():
    pass
    #t.__parseInput__("USE tb1")
    #t.__parseInput__("CREATE TABLE tbl_1 (a1 int, a2 varchar(20))")
    #t.__parseInput__("SELECT * FROM tbl_1;")
    #t.__parseInput__("DROP TABLE tbl_1;")
    #t.__parseInput__("ALTER TABLE tbl_1 ADD a3 float;")

if __name__ == "__main__":
    #integration_test_DBMS_create_database()
    #integration_test_DBMS_delete_database()
    #integration_test_DBMS_create_table()
    #integration_test_DBMS_delete_table()
    #integration_test_DBMS_use_database()
    #integration_test_DBMS_parse_database_create()
    #integration_test_DBMS_parse_database_delete()
    integration_test_DBMS_parse_database_use()