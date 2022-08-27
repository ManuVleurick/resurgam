from database.books_db import BooksDatabase

class BooksController:
    
    def __init__(self):
        self.books_db = BooksDatabase()

    def add_book(self,book):
        self.books_db.insert_book(book)
        return self.books_db.get_all_books()

    def delete_book(self,book_id):
        self.books_db.delete_book(book_id)
        return self.books_db.get_all_books()

    def update_book(self,book):
        self.books_db.update_book(book)
        return self.books_db.get_all_books()

    def get_book(self,book_id):
        return self.books_db.get_book(book_id)

    def get_all_books(self):
        return self.books_db.get_all_books()

    def command(self,sql):
        return self.books_db.console_command(sql)

