from gui.books_gui import BooksGUI
import pyinputplus as pyip
import os

def main():
    keuze = pyip.inputInt('1. Quiz\n2. BoekDB',min=1,max=2)
    os.system('cls')
    menu_keuze(keuze)

def menu_keuze(keuze):
    if keuze==1:
        gui = QuizGUI()
    elif keuze==2:
        gui = BooksGUI()

main()