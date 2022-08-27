from controller.books_controller import BooksController

class BooksGUI:

    def __init__(self):
        self.controller = BooksController()

    def add_book(self,book):
       books = self.controller.add_book(book)
       print(f'books na toevoeging {books}')
