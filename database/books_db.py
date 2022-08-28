import sqlite3
from sqlite3 import Error
import json
import random

PATH_DB = "./resources/books.db"


    

class BooksDatabase():
    
    def __init__(self):
        try:
            print('Start connection database...')
            self.db = sqlite3.connect(PATH_DB)
            print(f'Connection book database made!')
        except Error as e:
            print(f'Connection to book database failed!\nError: {e}')

        self.make_db()
        
    #book=dict en info=dict
    def insert_book(self,book):
        mycursor = self.db.cursor()

        data = [value for value in book.get_values()]
        mycursor.execute(f'INSERT INTO book VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',data)

        self.db.commit()
        mycursor.close()

    def delete_book(self,book_id):
        mycursor = self.db.cursor()
        mycursor.execute(f'DELETE FROM book WHERE book_id={book_id}')

        self.db.commit()
        mycursor.close()

    def update_book(self,book):
        mycursor = self.db.cursor()
        mycursor.execute(f'UPDATE book SET  WHERE book_id={book.book_id}')
        mycursor.close()

    def get_book(self,book_id):
        mycursor = self.db.cursor()
        mycursor.execute(f'SELECT * FROM book WHERE book_id={book_id}')
        data = mycursor.fetchone()
        mycursor.close()
        return data

    def console_command(self,sql_statement,expect_return=False):
        mycursor = self.db.cursor()
        mycursor.execute(f'{sql_statement}')
        if expect_return:
            data = mycursor.fetchall()
            return data
        self.db.commit()
        mycursor.close()

    def get_all_books(self):
        mycursor = self.db.cursor()
        mycursor.execute(f'SELECT * FROM book')
        data = mycursor.fetchall()
        mycursor.close()
        return data

    def close_db(self):
        self.db.close()

    def make_db(self):
        mycursor = self.db.cursor()
        #books table
        mycursor.execute("CREATE TABLE IF NOT EXISTS book (book_id TEXT PRIMARY KEY,title TEXT NOT NULL,author TEXT NOT NULL,year DATE NOT NULL,genre TEXT NOT NULL,description TEXT,language TEXT NOT NULL,ISBN TEXT,pages INT,score REAL,status TEXT,review_score REAL,review TEXT,bib_place TEXT,tags TEXT,date_gelezen DATE)")

        self.db.commit()
        mycursor.close()
