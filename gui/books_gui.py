from msilib.schema import SelfReg
from controller.books_controller import BooksController
from domain.book import Book

class BooksGUI:

    def __init__(self):
        self.books_con = BooksController()
        self.start()

    def start(self):


        