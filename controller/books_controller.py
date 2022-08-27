from repository.books_repo import BooksRepo

class BooksController:
    
    def __init__(self):
        self.books_repo = BooksRepo()

    def add_book(self,book):
        return self.books_repo.add_book(book)

    def delete_book(self,book_id):
        return self.books_repo.delete_book(book_id)

    def update_book(self,book=None,info=None):
        return self.books_repo.update_book(book,info)

    def get_book(self,book_id):
        return self.books_repo.get_book(book_id)

    def command(self,sql):
        return self.books_repo.console_command(sql)

