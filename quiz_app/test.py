from database.quiz_db import QuizDatabase

db = QuizDatabase()
#quiz = Quiz('QuizNaam','Beschrijving van quiz',['liter','europ'])
#db.add_quiz(quiz)
# quiz_id = 'RWwUFX5zAV'
# multiplechoice = MultipleChoiceVraag('een vraag wie is boke aller tijden?',['literatuuur','intelectuel'],'Een beschijfdiqglkqjmdgqdfmqjdlddskjdfmg:sf',quiz_id,'Duned',['Sheesh','jesuss'])
# dragndrop = DragDropVraag('Vraagnaam',['horror','litera'],'brschrijving',quiz_id,['antwoord1','antw2'],['choice 1','choi2'])
# inputv = InputVraag('Vraaginunaam',['onderw','onderwer2'],'description over input',quiz_id,'antwoord')
# db.add_vraag(inputv)
#v = db.get_vragen()
#print('vragen')
#print(v)

vraag_id = 'lLridaxgV1'
data = db.get_vraag(vraag_id)
print(data)
print(type(data))


# print(db.get_quizzes())
# quiz = Quiz('Geschiedenis tijdens Napoleon','Napoleon lorem ipsum...',['geschiedenis','literatuur'])
# quiz = db.add_quiz(quiz)
# quiz_id = quiz.quiz_id
# multiplechoice = MultipleChoiceVraag('een vraag wie is boke aller tijden?',['literatuuur','intelectuel'],'Een beschijfdiqglkqjmdgqdfmqjdlddskjdfmg:sf',quiz_id,'Duned',['Sheesh','jesuss'])
# dragndrop = DragDropVraag('Vraagnaam',['horror','litera'],'brschrijving',quiz_id,['antwoord1','antw2'],['choice 1','choi2'])
# inputv = InputVraag('Vraaginunaam',['onderw','onderwer2'],'description over input',quiz_id,'antwoord')
# db.add_vraag(inputv)
# db.add_vraag(multiplechoice)
# quizzes = db.get_quizzes()
# for quiz in quizzes:
#     print(f'Quiz: {quiz}')
#     vragen = db.get_vraag_from_quiz(quiz.quiz_id)
#     print(f'Vragen van {quiz.naam}')
#     print(vragen)