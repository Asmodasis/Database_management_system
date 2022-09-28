import os 
from DBMS import DBMS

def integration_test_DBMS_create_database():
    pass
def integration_test_DBMS_delete_database():
    pass
def integration_test_DBMS_create_table():
    pass
def integration_test_DBMS_delete_table():
    pass
def integration_test_DBMS_use_database():
    pass

def integration_test_DBMS_parse_database_create():
    pass
def integration_test_DBMS_parse_database_delete():
    pass
def integration_test_DBMS_parse_database_use():
    pass

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
    integration_test_DBMS_create_database()