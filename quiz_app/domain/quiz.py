import random
from config.glob_vars import LEN_ID

class Quiz:

    def __init__(self,naam,description,onderwerpen,aantal_keer_gedaan=0,gemid_score=0):
        self.set_quiz_id()
        self.set_naam(naam)
        self.set_description(description)
        self.set_onderwerpen(onderwerpen)
        self.set_aantal_keer_gedaan(aantal_keer_gedaan)
        self.set_gemid_score(gemid_score)

    def generate_id(self):
        chars = list('0123456789azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN')
        id = ''
        for x in range(LEN_ID):
            id += random.choice(chars)
        return id
        #return random.randint(100000000,999999999)

    def get_quiz_id(self):
        return self.quiz_id

    def set_quiz_id(self,quiz_id=''):
        if quiz_id=='':
            self.quiz_id = self.generate_id()
        else:
            self.quiz_id = quiz_id

    def set_naam(self,naam):
        if type(naam) == str:
            self.naam = naam
        else:
            raise Exception(f'naam has the wrong type must be str but is {type(naam)}')

    def get_naam(self):
        return self.naam

    def set_description(self,description):
        if type(description) == str:
            self.description = description
        else:
            raise Exception(f'description has the wrong type must be str but is {type(description)}')

    def get_description(self):
        return self.description

    def set_onderwerpen(self,onderwerpen):
        if type(onderwerpen) == list:
            self.onderwerpen = onderwerpen
        else:
            raise Exception(f'onderwerpen has the wrong type must be list but is {type(onderwerpen)}')

    def get_onderwerpen(self):
        return self.onderwerpen    

    def set_aantal_keer_gedaan(self,aantal_keer_gedaan):
        if type(aantal_keer_gedaan) == int:
            self.aantal_keer_gedaan = aantal_keer_gedaan
        else:
            raise Exception(f'aantal_keer_gedaan has the wrong type must be int but is {type(aantal_keer_gedaan)}')

    def get_aantal_keer_gedaan(self):
        return self.aantal_keer_gedaan 

    def set_gemid_score(self,gemid_score):
        if (type(gemid_score) == int) and ((gemid_score>=0) and (gemid_score<=100)):
            self.gemid_score = gemid_score
        else:
            raise Exception(f'gemid_score has the wrong type must be int and between 0 and 100 but is {type(gemid_score)} and value={gemid_score}')

    def get_gemid_score(self):
        return self.gemid_score 

    def to_string(self):
        string = ''
        string += f'Quiz ID: {self.get_quiz_id()}\n'
        string += f'Naam: {self.get_naam()}\n'
        string += f'Description: {self.get_description()}\n'
        string += f'Onderwerpen: {self.get_onderwerpen()}\n'
        string += f'Aantal keer gedaan: {self.get_aantal_keer_gedaan()}\n'
        string += f'Gemiddelde score: {self.get_gemid_score()}\n'
        return string
