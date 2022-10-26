import random
from config.glob_vars import LEN_ID

class Vraag:

    def __init__(self,vraag,onderwerpen,description,quiz_id):
        self.set_vraag_id()
        self.set_vraag(vraag)
        self.set_onderwerpen(onderwerpen)
        self.set_aantal_correct()
        self.set_aantal()
        self.set_description(description)
        self.set_quiz_id(quiz_id)

    def generate_id(self):
        chars = list('0123456789azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN')
        id = ''
        for x in range(LEN_ID):
            id += random.choice(chars)
        return id
        #return random.randint(100000000,999999999)

    def get_vraag_id(self):
        return self.vraag_id

    def set_vraag_id(self,vraag_id=''):
        if vraag_id=='':
            self.vraag_id = self.generate_id()
        else:
            self.vraag_id = vraag_id

    def set_vraag(self,vraag):
        if type(vraag) == str:
            self.vraag = vraag
        else:
            raise Exception(f'vraag has the wrong type must be str but is {type(vraag)}')

    def get_vraag(self):
        return self.vraag

    def set_onderwerpen(self,onderwerpen):
        if type(onderwerpen) == list:
            self.onderwerpen = onderwerpen
        else:
            raise Exception(f'onderwerpen has the wrong type must be array but is {type(onderwerpen)}')

    def get_onderwerpen(self):
        return self.onderwerpen

    def set_aantal_correct(self,aantal_correct=0):
        if type(aantal_correct) == int:
            self.aantal_correct = aantal_correct
        else:
            raise Exception(f'aantal_correct has the wrong type must be array but is {type(aantal_correct)}')

    def get_aantal_correct(self):
        return self.aantal_correct

    def set_aantal(self,aantal=0):
        if type(aantal) == int:
            self.aantal = aantal
        else:
            raise Exception(f'aantal has the wrong type must be array but is {type(aantal)}')

    def get_aantal(self):
        return self.aantal

    def set_description(self,description):
        if type(description) == str:
            self.description = description
        else:
            raise Exception(f'description has the wrong type must be str but is {type(description)}')

    def get_description(self):
        return self.description

    def set_quiz_id(self,quiz_id):
        if type(quiz_id) == str:
            self.quiz_id = quiz_id
        else:
            raise Exception(f'quiz_id has the wrong type must be str but is {type(quiz_id)}')

    def get_quiz_id(self):
        return self.quiz_id

    def to_string(self):
        string = ''
        string += f'Vraag ID: {self.get_vraag_id()}\n'
        string += f'Quiz ID: {self.get_quiz_id()}\n'
        string += f'Vraag: {self.get_vraag()}\n'
        string += f'Onderwerpen: {self.get_onderwerpen()}\n'
        string += f'Aantal keer beantwoord: {self.get_aantal()}\n'
        string += f'Aantal keer correct beantwoord: {self.get_aantal_correct()}\n'
        string += f'Description: {self.get_description()}'
        return string
