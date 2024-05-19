import sqlite3

conn = sqlite3.connect('univ.db')  # creates or/and connects to db. - connection

cur = conn.cursor()                 # cursor to execute the query.

# cur.execute('CREATE TABLE Dept(deptno integer primary key, name text)')
# cur.execute('CREATE TABLE Students(roll integer primary key, name text, city text, deptno integer, foreign key(deptno) references Dept(deptno))')

# query = "INSERT INTO Dept VALUES (30,'EEE'),(40,'ECE')"
# query = "INSERT INTO Students VALUES (6,'Mehul','Mumbai',10),(4,'Suraj','Bangalore',20),(5,'Sneha','Surat',30)"
query = "select * from students"

rows = cur.execute(query)
print(rows.fetchone())
print(rows.fetchmany(2))
print(rows.fetchall())

# conn.commit()

cur.close()

conn.close()

