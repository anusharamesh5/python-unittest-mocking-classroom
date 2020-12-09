import sqlite3
from sqlite3 import Error


class DbHelper:

    def sqlite_connection(self):
        try:
            con = sqlite3.connect("employeedatabase.db")
            return con
        except Error:
            print(Error)

    def sqlite_table(self, con):
        cursor_obj = con.cursor()
        cursor_obj.execute("PRAGMA foreign_keys=ON")
        cursor_obj.execute("DROP TABLE Employees")
        cursor_obj.execute("CREATE TABLE Employees(emp_no INT, emp_name"
                           " VARCHAR(20), salary FLOAT)")
        sql = "INSERT INTO Employees(emp_no, emp_name, salary) VALUES (?,?,?)"
        values = [(1, 'Naresh', 20000),
                  (2, 'Suresh', 40000),
                  (3, 'Uma', 10000),
                  (4, 'Savitha', 50000),
                  (5, 'Kamala', 5000),
                  (6, 'Vishal', 9000),
                  (7, 'Fathima', 30000),
                  (8, 'Arnab', 70000),
                  (9, 'Vijaya', 80000),
                  (10, 'Harini', 100000)]
        cursor_obj.executemany(sql, values)
        con.commit()
        # print(cursorObj.rowcount, "was inserted.")

    def get_maximum_salary(self, con):
        """
        Implement the logic to find and return
        maximum salary from employee table
        """
        cursorObj = con.cursor()
        cursorObj.execute("PRAGMA foreign_keys=ON")
        cursorObj.execute("SELECT MAX(salary) from Employees")
        max_sal = float(cursorObj.fetchone()[0])
        return max_sal

    def get_minimum_salary(self, con):
        """
        Implement the logic to find and return
        minimum salary from employee table
        """
        cursorObj = con.cursor()
        cursorObj.execute("PRAGMA foreign_keys=ON")
        cursorObj.execute("SELECT MIN(salary) from Employees")
        min_sal = float(cursorObj.fetchone()[0])
        return min_sal


if __name__ == "__main__":
    db_helper = DbHelper()
    conn = db_helper.sqlite_connection()
    db_helper.sqlite_table(conn)
    min_salary = db_helper.get_minimum_salary(conn)
    max_salary = db_helper.get_maximum_salary(conn)
    print(max_salary)
    print(min_salary)
