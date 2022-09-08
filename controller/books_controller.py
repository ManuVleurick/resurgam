from database.books_db import BooksDatabase
from domain.book import Book
from repository.books_repo import BooksRepository
class BooksController:
    
    def __init__(self):
        self.books_db = BooksDatabase()
        self.books_repo = BooksRepository()

    def add_book(self,book):
        self.books_db.insert_book(book)
        return self.get_book(book.book_id)

    def delete_book(self,book_id):
        self.books_db.delete_book(book_id)

    def update_book(self,book_id,dict_args):
        self.books_db.update_book(book_id,dict_args)
        return self.get_book(book_id)

    def get_book(self,book_id):
        book = self.books_db.get_book(book_id)
        return book

    def get_all_books(self):
        books = self.books_db.get_all_books()
        return books

    def close_db(self):
        self.books_db.close_db()

    def command(self,sql,expect_return=False):
        if expect_return:
            return self.books_db.console_command(sql,expect_return)
        self.books_db.console_command(sql)

    def ini_mock_data(self):
        book1 = Book('Dune','Mr. Down','2001-10-26','Horor','Een lange dinges yes hah kak','Nederlands',308,'Damn,Oof')
        book_id1 = self.books_db.insert_book(book1)
        book2 = Book('Frankenstein','Mary Halley','2021-09-19','Drama','Een lange dinges yes hah kak','English',214,'Poezie,Horror',score=8.5,status='Read')
        book_id2 = self.books_db.insert_book(book2)
        

