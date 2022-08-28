from database.books_db import BooksDatabase
from domain.book import Book

class BooksController:
    
    def __init__(self):
        self.books_db = BooksDatabase()

    def add_book(self,book):
        self.books_db.insert_book(book)
        return self.get_all_books()

    def delete_book(self,book_id):
        self.books_db.delete_book(book_id)
        return self.get_all_books()

    def update_book(self,book):
        self.books_db.update_book(book)
        return self.get_all_books()

    def get_book(self,book_id):
        data =  self.books_db.get_book(book_id)
        book = Book(book_id=data[0],title=data[1],author=data[2],year=data[3],genre=data[4],description=data[5],language=data[6],ISBN=data[7],pages=data[8],score=data[9],status=data[10],review_score=data[11],review=data[12],bib_place=data[13],tags=data[14],date_gelezen=data[15])
        return book

    def get_all_books(self):
        data = self.books_db.get_all_books()
        books = []
        for x in data:
            book = Book(book_id=x[0],title=x[1],author=x[2],year=x[3],genre=x[4],description=x[5],language=x[6],ISBN=x[7],pages=x[8],score=x[9],status=x[10],review_score=x[11],review=x[12],bib_place=x[13],tags=x[14],date_gelezen=x[15])
            books.append(book)
        
        return books

    def close_db(self):
        self.books_db.close_db()

    def command(self,sql,expect_return):
        if expect_return:
            return self.books_db.console_command(sql,expect_return)
        self.books_db.console_command(sql)

