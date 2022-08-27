from database.books_db import BooksDatabase

class BooksRepo:

    def __init__(self):
        self.books_db = BooksDatabase()
        #array of books
        #self.books = self.books_db.get_all_books()
        self.books = {}

    def add_book(self,book):
        self.books_db.insert_book(book)
        print(f'book_id={book.get_book_id()}')
        print(f'{book.to_string()}')
        self.books[book.get_book_id()]=book
        return self.books

    def delete_book(self,book_id):
        self.books_db.delete_book(book_id)
        self.books.pop(book_id)
        return self.books

    def update_book(self,book=None,info=None):
        self.books_db.update_book(book,info)
        if book:
            self.books[book.book_id][0] = book
        if info:
            self.books[info.book_id][1] = info
        return self.books

    def get_book(self,book_id):
        return self.books[book_id]

    def command(self,sql):
        return self.books_db.console_command(sql)

    def get_books(self):
        return self.books