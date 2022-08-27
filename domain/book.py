from datetime import date

class Book:

    def __init__(self,title,author,year,genre,description,language,ISBN=,pages,score=,review_score=,review=,bib_place=,tags,date_gelezen=,status='Plan To Read'):
        self.set_title(title)
        self.set_author(author)
        self.set_year(year)
        self.set_genre(genre)
        self.set_description(description)
        self.set_language(language)
        self.set_ISBN(ISBN)
        self.set_pages(pages)
        self.set_score(score)
        self.set_status(status)
        self.set_review_score(review_score)
        self.set_review(review)
        self.set_bib_place(bib_place)
        self.set_tags(tags)
        self.set_date_gelezen(date_gelezen)

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
        if (type(year) == int) & (year<=date.today().year & year>= 0):
            self.year = year
        else:
            raise Exception(f'year has the wrong type or wrong year must be int but is {type(year)}')

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
            raise Exception(f'language has the wrong type must be str but is {type(language)}')

    def get_language(self):
        return self.language

    def set_ISBN(self,ISBN):
        if type(ISBN) == str:
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
        if ((type(score) == float) & (score>=0 & (score<=10))):
            self.score = score
        else:
            raise Exception(f'score has the wrong type or is not between 0 and 10')

    def get_score(self):
        return self.score

    def set_status(self,status):
        if type(status) == str:
            self.status = status
        else:
            raise Exception(f'status has the wrong type must be str but is {type(status)}')

    def get_status(self):
        return self.status

    def set_review_score(self,review_score):
        if type(review_score) == float:
            self.review_score = review_score
        else:
            raise Exception(f'review_score has the wrong type must be float but is {type(review_score)}')

    def get_review_score(self):
        return self.review_score

    def set_review(self,review):
        if type(review) == str:
            self.review = review
        else:
            raise Exception(f'review has the wrong type must be str but is {type(review)}')

    def get_review(self):
        return self.review

    def set_bib_place(self,bib_place):
        if type(bib_place) == str:
            self.bib_place = bib_place
        else:
            raise Exception(f'bib_place has the wrong type must be str but is {type(bib_place)}')

    def get_bib_place(self):
        return self.bib_place

    def set_tags(self,tags):
        if type(tags) == list:
            self.tags = tags
        else:
            raise Exception(f'tags has the wrong type must be array but is {type(tags)}')

    def get_tags(self):
        return self.tags

    def set_date_gelezen(self,date_gelezen):
        if type(date_gelezen) == str:
            self.date_gelezen = date_gelezen
        else:
            raise Exception(f'date_gelezen has the wrong type must be str but is {type(date_gelezen)}')

    def get_date_gelezen(self):
        return self.date_gelezen

    def values(self):
        data = [self.get_title(),self.get_author(),self.get_year(),self.get_genre(),self.get_description(),self.get_language(),self.get_ISBN(),self.get_pages(),self.get_score(),self.get_status()]
        return data