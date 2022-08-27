import sqlite3
from sqlite3 import Error
import json
import random

PATH_DB = "./resources/books.db"
NAME_DB = 'book'

def generate_id():
    return random.randint(100000000,999999999)
    

class BooksDatabase():
    
    def __init__(self):
        try:
            print('Start connection database...')
            self.db = sqlite3.connect(PATH_DB)
            print(f'Connection {NAME_DB} database made!')
        except Error as e:
            print(f'Connection to {NAME_DB} database failed!\nError: {e}')

        self.make_db()
        
    #book=dict en info=dict
    def insert_book(self,book,info):
        mycursor = self.db.cursor()
        
        data = [value for value in book.values()]
        id = generate_id()
        data.insert(0,id)
        print(f'Data: {data}')
        print(f'type: {type(data)}')
        mycursor.executemany(f'INSERT INTO book VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',data)

        self.db.commit()
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
        mycursor.execute("CREATE TABLE IF NOT EXISTS book (book_id INT PRIMARY KEY,title TEXT NOT NULL,author TEXT NOT NULL,year DATE NOT NULL,genre TEXT NOT NULL,description TEXT,language TEXT NOT NULL,ISBN TEXT,pages INT,score REAL,status TEXT DEFAULT 'Plan To Read')")
        #info table
        mycursor.execute("CREATE TABLE IF NOT EXISTS info (book_id INT PRIMARY KEY,review_score REAL,review TEXT,bib_place TEXT,tags TEXT,date_gelezen DATE,FOREIGN KEY (book_id) REFERENCES book (book_id))")

        self.db.commit()
        mycursor.close()
        print(f'Database {NAME_DB} build!')

    def fill_db_mock(self):
        with open('./testing/mock_data_books.json') as file:
            obj = json.load(file)
            file.close()

            mycursor = self.db.cursor()

            for book in obj['books']:
                if 'status' in book:
                    data = [
                        (book["book_id"],book["title"],book["author"],book["year"],book["genre"],book["description"],book["language"],book["ISBN"],book["pages"],book["score"],book["status"]),
                    ]
                    mycursor.executemany(f'INSERT INTO book VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',data)
                else:
                    data = [
                        (book["book_id"],book["title"],book["author"],book["year"],book["genre"],book["description"],book["language"],book["ISBN"],book["pages"],book["score"],None),
                    ]
                    mycursor.executemany(f'INSERT INTO book VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',data)

            
            #self.db.commit()

            mycursor.execute('SELECT * from book')
            iets = mycursor.fetchall()

            print(iets)

            mycursor.close()