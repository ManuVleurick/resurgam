from controller.books_controller import BooksController

class BooksGUI:

    def __init__(self):
        self.controller = BooksController()

    def add_book(self,book,info):
        return self.controller.add_book(book,info)
