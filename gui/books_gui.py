from controller.books_controller import BooksController
from  tkinter import *
import pyinputplus as pyip
import os
from domain.book import Book

class BooksGUI:

    def __init__(self):
        self.books_con = BooksController()
        self.start_console()

    def start_console(self):
        #self.books_con.ini_mock_data()
        keuze = 0
        while not keuze==5:
            print("1. Toon alle boeken\n2. Voeg boek toe\n3. Update boek\n4. Verwijder boek\n5. Exit")
            keuze = 0
            while not keuze in [1,2,3,4,5]:
                keuze = pyip.inputInt()
            self._book_menu(keuze)
            
    def _book_menu(self,keuze):
        if keuze == 1:
            self._show_all_books()
        elif keuze == 2:
            self._add_new_book()
        elif keuze == 3:
            self._update_book()
        elif keuze == 4:
            self._delete_book()
        else:
            self.books_con.close_db()
            exit()

    def _delete_book(self):
        os.system('cls')
        books = self.books_con.get_all_books()
        teller = 1
        for book in books:
            print(f'{teller}. {book.title}-{book.author} {book.year}')
            teller+=1
        keuze = pyip.inputInt('Geef het nummer van het boek dat je wil aanpassen:',min=1,max=teller-1)
        self.books_con.delete_book(books[keuze-1])

    def _update_book(self):
        os.system('cls')
        books = self.books_con.get_all_books()
        teller = 1
        for book in books:
            print(f'{teller}. {book.title}-{book.author} {book.year}')
            teller+=1
        keuze = pyip.inputInt('Geef het nummer van het boek dat je wil aanpassen:',min=1,max=teller-1)
        arg_dict = {}
        print('Laat blank om attribuut niet aan te passen')
        title = pyip.inputStr('Title:',blank=True)
        author = pyip.inputStr('Author:',blank=True)
        year = pyip.inputStr('Year(formaat=dd/mm/yyyy):',blank=True)
        description = pyip.inputStr('Description:',blank=True)
        language = pyip.inputStr('Language:',blank=True)
        pages = pyip.inputInt('Pages:',blank=True)
        tags = pyip.inputStr('Tags(Seperate with ,):',blank=True)
        score = pyip.inputFloat('Score:',blank=True,min=0,max=10)
        date_gelezen = pyip.inputDate('Datum wanneer gelezen(formaat=mm/dd/yyyy):',blank=True)
        status = pyip.inputStr('Status:',blank=True)
        if not title=='':
            arg_dict['title']=title
        if not author=='':
            arg_dict['author']=author
        if not year=='':
            arg_dict['year']=year
        if not description=='':
            arg_dict['description']=description
        if not language=='':
            arg_dict['language']=language
        if not pages=='':
            arg_dict['pages']=pages
        if not tags=='':
            arg_dict['tags']=tags
        if not score=='':
            arg_dict['score']=score
        if not date_gelezen=='':
            arg_dict['date_gelezen']=date_gelezen
        if not status=='':
            arg_dict['status']=status

        self.books_con.update_book(books[keuze-1].book_id,arg_dict)
        

    def _add_new_book(self):
        os.system('cls')
        title = pyip.inputStr('Title:')
        author = pyip.inputStr('Author:')
        year = pyip.inputStr('Year(formaat=dd/mm/yyyy):')
        description = pyip.inputStr('Description:')
        genre = pyip.inputStr('Genre:')
        language = pyip.inputStr('Language:')
        pages = pyip.inputInt('Pages:')
        tags = pyip.inputStr('Tags(Seperate with ,)(Can leave empty):',blank=True)
        score = pyip.inputFloat('Score(Can leave empty):',blank=True,min=0,max=10)
        date_gelezen = pyip.inputStr('Datum wanneer gelezen(Can leave empty)(formaat=mm/dd/yyyy):',blank=True)
        status = pyip.inputStr('Status(Can leave empty):',blank=True)
        if tags=='':
            tags=None
        if score=='':
            score=None
        if date_gelezen=='':
            date_gelezen=None
        if status=='':
            status=None
        book = Book(title,author,year,genre,description,language,pages,tags,score=score,date_gelezen=date_gelezen,status=status)
        self.books_con.add_book(book)


    def _show_all_books(self):
        os.system('cls')
        print('BOEKEN')
        print('--'*15)
        books = self.books_con.get_all_books()
        if len(books)==0:
            print('Geen boeken in de database')
            print('--'*15)
        for book in books:
            print(book.to_string())
            print('--'*15)
        

        