from msilib.schema import SelfReg
from controller.books_controller import BooksController
from domain.book import Book
from  tkinter import *
from tkinter import messagebox

class BooksGUI:

    def __init__(self):
        self.books_con = BooksController()
        self.start()

    def start(self):
        ws = Tk()
        def about():
            messagebox.showinfo('PythonGuides', 'Python Guides aims at providing best practical tutorials')

        menubar = Menu(root,background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
        file = Menu(menubar, tearoff=1, background='#ffcc99', foreground='black')
        file.add_command(label="New")  
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as")    
        file.add_separator()  
        file.add_command(label="Exit", command=ws.quit)  
        menubar.add_cascade(label="File", menu=file)  

        edit = Menu(menubar, tearoff=0)  
        edit.add_command(label="Undo")  
        edit.add_separator()     
        edit.add_command(label="Cut")  
        edit.add_command(label="Copy")  
        edit.add_command(label="Paste")  
        menubar.add_cascade(label="Edit", menu=edit)  

        help = Menu(menubar, tearoff=0)  
        help.add_command(label="About", command=about)  
        menubar.add_cascade(label="Help", menu=help)  

        ws.config(menu=menubar)

        ws.mainloop()

        