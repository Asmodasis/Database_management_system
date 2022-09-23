import DBMS
import Table

def unit_test_table_create():
    t = Table()
    # create table
    t.create("test_tbl_1.md")
    # failed to create table because it already exists
    t.create("test_tbl_1.md")

def unit_test_table_delete():
    t = Table()
    t.delete("test_tbl_2.md")
    # delete table
    t.delete("test_tbl_2.md")
    # failed to delete table because it does not exist
    t.delete("test_tbl_2.md")

if __name__ == "__main__":
    unit_test_table_create()