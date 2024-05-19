import pyodbc as pyo
import mysql.connector as pyo
import psycopg2 as pyo
import cx_Oracle as pyo
import sqlite3 as pyo
from database_config import sqlserver_connectionString,mysql_config,postgres_config,oracle_config
from tkinter import messagebox


class BookDB:
    def __init__(self) -> None:
        self.con = pyo.connect("mybooks.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, ISBN INTEGER)")
        self.con.commit()
        print('You are connected to the database')
        print(self.con)

    def view(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return rows
    
    def insert(self,title,author,isbn):
        # query = "INSERT INTO books(Title,Author,ISBN) VALUES(?,?,?)"
        query = "INSERT INTO books(Title,Author,ISBN) VALUES(?, ?, ?)"
        params = [title,author,isbn]
        self.cursor.execute(query,params)
        self.con.commit()
        messagebox.showinfo(title='Book Database',message='New book added to database')

    def update(self,id,title,author,isbn):
        query = "UPDATE books SET Title=?,Author=?,ISBN=? WHERE id=?"
        params = [title,author,isbn,id]
        self.cursor.execute(query,params)
        self.con.commit()
        messagebox.showinfo(title='Book Database',message='Book Updated')

    def delete(self,id):
        query = "DELETE FROM books WHERE id=?"
        params = [id]
        self.cursor.execute(query,params)
        self.con.commit()
        messagebox.showinfo(title='Book Database',message='Book Deleted')

    def __del__(self):
        self.cursor.close()
        self.con.close()

