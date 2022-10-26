import shutil
import sqlite3
from sqlite3 import Error
from config.glob_vars import PATH_DB_QUIZ, PATH_DB_QUIZ_BACK
from config.loggers import logger_db
from domain.multiple_choice import MultipleChoiceVraag
from domain.input_vraag import InputVraag
from domain.drag_drop_vraag import DragDropVraag
from domain.quiz import Quiz

class QuizDatabase():
    
    def __init__(self):
        try:
            #logger_db.info('Start connection quiz database...')
            self.db = sqlite3.connect(PATH_DB_QUIZ)
            print('db connectie!')
            #logger_db.info(f'Connection quiz database made!')
        except Error as e:
            #logger_db.setLevel(logging.error)
            #logger_db.error(f'Connection to quiz database failed!\nError: {e}')
            print('error quiz_db')

        self.make_db()

    def get_vragen(self):
        vragen = []
        mycursor = self.db.cursor()
        mycursor.execute(f'SELECT * FROM Vraag')
        data = mycursor.fetchall()
        for data_vraag in data:
            vraag_id = data_vraag[0]
            typ = data_vraag[6]
            if typ=='multiplechoice':
                mycursor.execute(f'SELECT * FROM MultipleChoice WHERE vraag_id="{vraag_id}"')
                data_typ = mycursor.fetchall()[0]
            elif typ=='dragndrop':
                mycursor.execute(f'SELECT * FROM DragnDrop WHERE vraag_id="{vraag_id}"')
                data_typ = mycursor.fetchall()[0]
            elif typ=='inputvraag':
                mycursor.execute(f'SELECT * FROM InputVraag WHERE vraag_id="{vraag_id}"')
                data_typ = mycursor.fetchall()[0]

            data = data_vraag + data_typ[1:]
            vraag = self.transform_to_vraag(data)
            vragen.append(vraag)
        mycursor.close()
        return data

    def get_quizzes(self):
        quizzes = []
        mycursor = self.db.cursor()
        mycursor.execute(f'SELECT * FROM Quiz')
        data = mycursor.fetchall()
        for data_quiz in data:
            quizzes.append(self.transform_to_quiz(data_quiz))
        mycursor.close()
        return quizzes

    def get_vragen_from_quiz(self,quiz_id):
        vragen = []
        mycursor = self.db.cursor()
        mycursor.execute(f'SELECT * FROM Vraag WHERE quiz_id="{quiz_id}"')
        data = mycursor.fetchall()
        for data_vraag in data:
            vraag_id = data_vraag[0]
            typ = data_vraag[6]
            if typ=='multiplechoice':
                mycursor.execute(f'SELECT * FROM MultipleChoice WHERE vraag_id="{vraag_id}"')
                data_typ = mycursor.fetchall()[0]
            elif typ=='dragndrop':
                mycursor.execute(f'SELECT * FROM DragnDrop WHERE vraag_id="{vraag_id}"')
                data_typ = mycursor.fetchall()[0]
            elif typ=='inputvraag':
                mycursor.execute(f'SELECT * FROM InputVraag WHERE vraag_id="{vraag_id}"')
                data_typ = mycursor.fetchall()[0]

            data = data_vraag + data_typ[1:]
            vraag = self.transform_to_vraag(data)
            vragen.append(vraag)
        mycursor.close()
        return vragen

    def get_vraag(self,vraag_id):
        mycursor = self.db.cursor()
        mycursor.execute(f'SELECT * FROM Vraag WHERE vraag_id="{vraag_id}"')
        data_vraag = mycursor.fetchall()[0]
        typ = data_vraag[6]
        if typ=='multiplechoice':
            mycursor.execute(f'SELECT * FROM MultipleChoice WHERE vraag_id="{vraag_id}"')
            data_typ = mycursor.fetchall()[0]
        elif typ=='dragndrop':
            mycursor.execute(f'SELECT * FROM DragnDrop WHERE vraag_id="{vraag_id}"')
            data_typ = mycursor.fetchall()[0]
        elif typ=='inputvraag':
            mycursor.execute(f'SELECT * FROM InputVraag WHERE vraag_id="{vraag_id}"')
            data_typ = mycursor.fetchall()[0]

        data = data_vraag + data_typ[1:]
        vraag = self.transform_to_vraag(data)
        mycursor.close()
        return vraag

    def transform_to_quiz(self,data):
        quiz = Quiz(data[1],data[2],data[3].split("|"),data[4],data[5])
        quiz.set_quiz_id(data[0])
        return quiz

    def transform_to_vraag(self,data):
        typ = data[6]
        if typ=='multiplechoice':
            vraag = MultipleChoiceVraag(data[1],data[2].split("|"),data[5],data[7],data[8],data[9].split("|"))
            vraag.set_vraag_id(data[0])
            vraag.set_aantal_correct(data[3])
            vraag.set_aantal(data[4])
        elif typ=='dragndrop':
            vraag = DragDropVraag(data[1],data[2].split("|"),data[5],data[7],data[8].split("|"),data[9].split("|"))
            vraag.set_vraag_id(data[0])
            vraag.set_aantal_correct(data[3])
            vraag.set_aantal(data[4])
        elif typ=='inputvraag':
            vraag = InputVraag(data[1],data[2].split("|"),data[5],data[7],data[8])
            vraag.set_vraag_id(data[0])
            vraag.set_aantal_correct(data[3])
            vraag.set_aantal(data[4])

        return vraag

    def get_quiz(self,quiz_id):
        mycursor = self.db.cursor()
        mycursor.execute(f'SELECT * FROM Quiz WHERE quiz_id="{quiz_id}"')
        data = mycursor.fetchall()[0]
        mycursor.close()
        quiz = self.transform_to_quiz(data)
        return quiz

    def add_quiz(self,quiz):
        mycursor = self.db.cursor()
        values = (quiz.get_quiz_id(),quiz.get_naam(),quiz.get_description(),'|'.join(quiz.get_onderwerpen()),quiz.get_aantal_keer_gedaan(),quiz.get_gemid_score())
        mycursor.execute(f'INSERT INTO Quiz VALUES (?,?,?,?,?,?)',values)
        self.db.commit()
        mycursor.close()
        id = quiz.get_quiz_id()
        return self.get_quiz(id)

    def add_vraag(self,vraag):
        mycursor = self.db.cursor()
        if(type(vraag)==MultipleChoiceVraag):
            typ = 'multiplechoice'
            values_vraag = (vraag.get_vraag_id(),vraag.get_vraag(),"|".join(vraag.get_onderwerpen()),vraag.get_aantal_correct(),vraag.get_aantal(),vraag.get_description(),typ,vraag.get_quiz_id())
            values = (vraag.get_vraag_id(),vraag.get_antwoord(),"|".join(vraag.get_choices()))
            mycursor.execute(f'INSERT INTO Vraag VALUES (?,?,?,?,?,?,?,?)',values_vraag)
            mycursor.execute(f'INSERT INTO MultipleChoice VALUES (?,?,?)',values)
        elif(type(vraag)==DragDropVraag):
            typ = 'dragndrop'
            values_vraag = (vraag.get_vraag_id(),vraag.get_vraag(),"|".join(vraag.get_onderwerpen()),vraag.get_aantal_correct(),vraag.get_aantal(),vraag.get_description(),typ,vraag.get_quiz_id())
            values = (vraag.get_vraag_id(),"|".join(vraag.get_antwoorden()),"|".join(vraag.get_choices()))
            mycursor.execute(f'INSERT INTO Vraag VALUES (?,?,?,?,?,?,?,?)',values_vraag)
            mycursor.execute(f'INSERT INTO DragnDrop VALUES (?,?,?)',values)
        elif(type(vraag)==InputVraag):
            typ = 'inputvraag'
            values_vraag = (vraag.get_vraag_id(),vraag.get_vraag(),"|".join(vraag.get_onderwerpen()),vraag.get_aantal_correct(),vraag.get_aantal(),vraag.get_description(),typ,vraag.get_quiz_id())
            values = (vraag.get_vraag_id(),vraag.get_antwoord())
            mycursor.execute(f'INSERT INTO Vraag VALUES (?,?,?,?,?,?,?,?)',values_vraag)
            mycursor.execute(f'INSERT INTO InputVraag VALUES (?,?)',values)

        self.db.commit()
        mycursor.close()
        return self.get_vraag(vraag.get_vraag_id())

    def update_vraag(self,arg_dict):
        mycursor = self.db.cursor()
        items = ''
        for item in arg_dict.items():
            items += f'{item[0]} = {item[1]},'

        items=items[:-1]
        mycursor.execute(f'UPDATE Vraag SET {items} WHERE vraag_id = "{arg_dict["vraag_id"]}"')
        if arg_dict["type"]=='multiplechoice':
            mycursor.execute(f'UPDATE MultipleChoice SET {items} WHERE vraag_id = "{arg_dict["vraag_id"]}"')
        elif arg_dict["type"]=='dragndrop':
            mycursor.execute(f'UPDATE DragnDrop SET {items} WHERE vraag_id = "{arg_dict["vraag_id"]}"')
        elif arg_dict["type"]=='inputvraag':
            mycursor.execute(f'UPDATE InputVraag SET {items} WHERE vraag_id = "{arg_dict["vraag_id"]}"')

        mycursor.close()

    def update_quiz(self,arg_dict):
        mycursor = self.db.cursor()
        items = ''
        for item in arg_dict.items():
            items += f'{item[0]} = {item[1]},'

        items=items[:-1]
        mycursor.execute(f'UPDATE Quiz SET {items} WHERE quiz_id = "{arg_dict["quiz_id"]}"')
        mycursor.close()

    def delete_vraag(self,vraag_id,type):
        mycursor = self.db.cursor()
        mycursor.execute(f'DELETE FROM Vraag WHERE vraag_id = "{vraag_id}"')
        if type=='multiplechoice':
            mycursor.execute(f'DELETE FROM MultipleChoice WHERE vraag_id = "{vraag_id}"')
        elif type=='dragndrop':
            mycursor.execute(f'DELETE FROM DragnDrop WHERE vraag_id = "{vraag_id}"')
        elif type=='inputvraag':
            mycursor.execute(f'DELETE FROM InputVraag WHERE vraag_id = "{vraag_id}"')

        mycursor.close()

    def delete_quiz(self,quiz_id):
        mycursor = self.db.cursor()
        mycursor.execute(f'DELETE FROM Quiz WHERE quiz_id = "{quiz_id}"')
        mycursor.close()
        
    def console_command(self,sql_statement,expect_return=False):
        mycursor = self.db.cursor()
        mycursor.execute(f'{sql_statement}')
        if expect_return:
            data = mycursor.fetchall() 
            return data
        self.db.commit()
        mycursor.close()

    def close_db(self):
        shutil.copyfile(PATH_DB_QUIZ,PATH_DB_QUIZ_BACK)
        self.db.close()
        logger_db.warning('Database quiz closed')

    def make_db(self):
        mycursor = self.db.cursor()
        #quiz table
        mycursor.execute("CREATE TABLE IF NOT EXISTS Quiz (quiz_id TEXT PRIMARY KEY,naam TEXT NOT NULL,description TEXT NOT NULL,onderwerpen TEXT NOT NULL,aantal_keer_gedaan INT NOT NULL, gemid_score INT NOT NULL)")
        #vraag super table
        mycursor.execute("CREATE TABLE IF NOT EXISTS Vraag (vraag_id TEXT PRIMARY KEY,vraag TEXT NOT NULL,onderwerpen TEXT NOT NULL,aantalCorrect INT NOT NULL,aantal INT NOT NULL,description TEXT NOT NULL,vraag_type TEXT NOT NULL,quiz_id TEXT, FOREIGN KEY (quiz_id) REFERENCES Quiz(quiz_id))")
        #multiple choice vraag table
        mycursor.execute("CREATE TABLE IF NOT EXISTS MultipleChoice (vraag_id TEXT PRIMARY KEY,antwoord TEXT NOT NULL,choices TEXT NOT NULL, FOREIGN KEY (vraag_id) REFERENCES Vraag(vraag_id))")
        #input vraag table
        mycursor.execute("CREATE TABLE IF NOT EXISTS InputVraag (vraag_id TEXT PRIMARY KEY, antwoord TEXT NOT NULL, FOREIGN KEY (vraag_id) REFERENCES Vraag(vraag_id))")
        #DragnDrop vraag table
        mycursor.execute("CREATE TABLE IF NOT EXISTS DragnDrop (vraag_id TEXT PRIMARY KEY, antwoord TEXT NOT NULL,choices TEXT NOT NULL, FOREIGN KEY (vraag_id) REFERENCES Vraag(vraag_id))")

        self.db.commit()
        mycursor.close()
