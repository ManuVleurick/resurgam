import sqlite3
from sqlite3 import Error
from config.loggers import logger_db
from config.glob_vars import PATH_DB

class BooksDatabase():
    
    def __init__(self):
        try:
            logger_db.info('Start connection database...')
            self.db = sqlite3.connect(PATH_DB)
            logger_db.info(f'Connection book database made!')
        except Error as e:
            logger_db.error(f'Connection to book database failed!\nError: {e}')

        self.make_db()
        
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

    def update_book(self,book_id,dict_args):
        mycursor = self.db.cursor()
        set_sql = ''
        for arg,val in dict_args.items():
            if type(val) == str:
                set_sql += f"{arg} = \'{val}\',"
            else:
                set_sql += f"{arg} = {val},"
        set_sql = set_sql[:-1]
        mycursor.execute(f'UPDATE book SET {set_sql} WHERE book_id={book_id}')
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
        logger_db.warning('Database book closed')

    def make_db(self):
        mycursor = self.db.cursor()
        #books table
        mycursor.execute("CREATE TABLE IF NOT EXISTS book (book_id TEXT PRIMARY KEY,title TEXT NOT NULL,author TEXT NOT NULL,year DATE NOT NULL,genre TEXT NOT NULL,description TEXT,language TEXT NOT NULL,ISBN TEXT,pages INT,score REAL,status TEXT,review_score REAL,review TEXT,bib_place TEXT,tags TEXT,date_gelezen DATE)")

        self.db.commit()
        mycursor.close()
