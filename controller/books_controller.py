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
        return self.books_db.get_all_books()

    def update_book(self,book):
        self.books_db.update_book(book)
        return self.books_db.get_all_books()

    def get_book(self,book_id):
        return self.books_db.get_book(book_id)

    def get_all_books(self):
        data = self.books_db.get_all_books()
        books = []
        for x in data:
            book_args = x[1:]
            book = Book(title=book_args[0],author=book_args[1],year=book_args[2],genre=book_args[3],description=book_args[4],language=book_args[5],ISBN=book_args[6],pages=book_args[7],score=book_args[8],status=book_args[9],review_score=book_args[10],review=book_args[11],bib_place=book_args[12],tags=book_args[13],date_gelezen=book_args[14])
            books.append(book)
        
        return books

    def command(self,sql):
        return self.books_db.console_command(sql)

