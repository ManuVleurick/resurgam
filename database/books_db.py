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
        print(f'Data: {data}')
        #array not supported in sqlite so convert to string
        data[14] = " ".join(data[14])
        print(f'tags: {data[14]}')
        mycursor.execute(f'INSERT INTO book VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',data)

        #self.db.commit()
        mycursor.close()

    def delete_book(self,book_id):
        pass

    #dict met alle attributen
    def update_book(self,book,info):
        pass

    def get_book(self,book_id):
        pass

    def console_command(self,sql_statement):
        pass

    #array with tuples with Book en info
    def get_all_books(self):
        pass

    def close_db(self):
        self.db.close()

    def make_db(self):
        mycursor = self.db.cursor()
        #books table
        mycursor.execute("CREATE TABLE IF NOT EXISTS book (book_id INT PRIMARY KEY,title TEXT NOT NULL,author TEXT NOT NULL,year DATE NOT NULL,genre TEXT NOT NULL,description TEXT,language TEXT NOT NULL,ISBN TEXT,pages INT,score REAL,status TEXT,review_score REAL,review TEXT,bib_place TEXT,tags TEXT,date_gelezen DATE)")

        self.db.commit()
        mycursor.close()
        print(f'Database book build!')