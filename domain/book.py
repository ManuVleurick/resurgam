import random
from config.glob_vars import LEN_ID

class Book:

    def __init__(self,title,author,year,genre,description,language,pages,tags=None,book_id=None,score=None,date_gelezen=None,status='Plan To Read'):
        self.set_book_id(book_id)
        self.set_title(title)
        self.set_author(author)
        self.set_year(year)
        self.set_genre(genre)
        self.set_description(description)
        self.set_language(language)
        self.set_pages(pages)
        self.set_score(score)
        self.set_status(status)
        self.set_tags(tags)
        self.set_date_gelezen(date_gelezen)

    def generate_id(self):
        chars = list('0123456789azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN')
        id = ''
        for x in range(LEN_ID):
            id += random.choice(chars)
        return id
        #return random.randint(100000000,999999999)

    def get_book_id(self):
        return self.book_id

    def set_book_id(self,book_id):
        if book_id == None:
            self.book_id = self.generate_id()
        else:
            self.book_id = book_id

    def set_title(self,title):
        if type(title) == str:
            self.title = title
        else:
            raise Exception(f'title has the wrong type must be str but is {type(title)}')

    def get_title(self):
        return self.title

    def set_author(self,author):
        if type(author) == str:
            self.author = author
        else:
            raise Exception(f'author has the wrong type must be str but is {type(author)}')

    def get_author(self):
        return self.author

    def set_year(self,year):
        if (type(year) == str):
            self.year = year
        else:
            raise Exception(f'year has the wrong type or wrong year must be str but is {type(year)}')

    def get_year(self):
        return self.year

    def set_genre(self,genre):
        if type(genre) == str:
            self.genre = genre
        else:
            raise Exception(f'genre has the wrong type must be str but is {type(genre)}')

    def get_genre(self):
        return self.genre

    def set_description(self,description):
        if type(description) == str:
            self.description = description
        else:
            raise Exception(f'description has the wrong type must be str but is {type(description)}')

    def get_description(self):
        return self.description

    def set_language(self,language):
        if type(language) == str:
            self.language = language
        else:
            raise Exception(f'language has the wrong type must be str but is {type(language)}:{language}')

    def get_language(self):
        return self.language

    def set_ISBN(self,ISBN):
        if (type(ISBN) == str) or (ISBN == None):
            self.ISBN = ISBN
        else:
            raise Exception(f'ISBN has the wrong type must be str but is {type(ISBN)}')

    def get_ISBN(self):
        return self.ISBN

    def set_pages(self,pages):
        if (type(pages) == int) & pages>=0:
            self.pages = pages
        else:
            raise Exception(f'pages has the wrong type or is not positive')

    def get_pages(self):
        return self.pages

    def set_score(self,score):
        if (score==None) or (((type(score) == float) or (type(score)==int)) & (score>=0 & (score<=10))):
            self.score = score
        else:
            raise Exception(f'score has the wrong type: or is not between 0 and 10')

    def get_score(self):
        return self.score

    def set_status(self,status):
        if (type(status) == str) | (status == None):
            self.status = status
        else:
            raise Exception(f'status has the wrong type must be str but is {type(status)}')

    def get_status(self):
        return self.status

    #tags seperated with ,
    def set_tags(self,tags):
        if type(tags) == str:
            self.tags = tags
        else:
            raise Exception(f'tags has the wrong type must be str but is {type(tags)}')

    def get_tags(self):
        return self.tags

    def set_date_gelezen(self,date_gelezen):
        if (date_gelezen==None) or (type(date_gelezen) == str):
            self.date_gelezen = date_gelezen
        else:
            raise Exception(f'date_gelezen has the wrong type must be str but is {type(date_gelezen)}')

    def get_date_gelezen(self):
        return self.date_gelezen

    def to_string(self):
        string = ''
        string += f'Book ID: {self.get_book_id() if not self.get_book_id()==None else "Geen boek ID gegeven"}\n'
        string += f'Title: {self.get_title()}\n'
        string += f'Author: {self.get_author()}\n'
        string += f'Year: {self.get_year()}\n'
        string += f'Genre: {self.get_genre()}\n'
        string += f'Description: {self.get_description()}\n'
        string += f'Language: {self.get_language()}\n'
        string += f'Pages: {self.get_pages()}\n'
        string += f'Score: {self.get_score() if not self.get_score()==None else "Geen score gegeven"}\n'
        string += f'Status: {self.get_status()}\n'
        string += f'Tags: {self.get_tags() if not self.get_tags()==None else "Geen tags gegeven"}\n'
        string += f'Date gelezen: {self.get_date_gelezen() if not self.get_date_gelezen()==None else "Geen datum gelezen gegeven"}\n'
        return string

    def get_values(self):
        data = [self.get_book_id(),self.get_title(),self.get_author(),self.get_year(),self.get_genre(),self.get_description(),self.get_language(),self.get_pages(),self.get_score(),self.get_status()]
        data.append(self.get_tags())
        data.append(self.get_date_gelezen())
        return data
