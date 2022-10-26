from domain.drag_drop_vraag import DragDropVraag
from domain.input_vraag import InputVraag
from domain.multiple_choice import MultipleChoiceVraag
from flask import Flask,render_template,session,url_for,redirect,request
from database.quiz_db import QuizDatabase
import random

quiz_db = QuizDatabase()
app = Flask(__name__)
app.secret_key = b'yoinkersbedoinkers'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vragen')
def vragen():
    quiz_db = QuizDatabase()
    vragen = quiz_db.get_vragen()
    return render_template('vragen.html',vragen=vragen)

@app.route('/quizzes')
def quizzes():
    quiz_db = QuizDatabase()
    quizzes = quiz_db.get_quizzes()
    return render_template('quizzes.html',quizzes=quizzes)

@app.route('/quiz/<quiz_id>/start')
def quiz_start(quiz_id):
    quiz_db = QuizDatabase()
    quiz = quiz_db.get_quiz(quiz_id)
    quizzes = quiz_db.get_quizzes()
    vragen = quiz_db.get_vragen_from_quiz(quiz_id)
    
    return render_template('quiz_start.html',quiz=quiz,vragen=vragen,quizzes=quizzes)

@app.route('/quiz/<quiz_id>/starting')
def quiz_starting(quiz_id):
    quiz_db = QuizDatabase()
    session['vraagnr'] = 0
    session['bezige_vragen'] = quiz_db.get_vragen_from_quiz(quiz_id)
    session['antwoorden'] = []
    random.shuffle(session['bezige_vragen'])

    return redirect(url_for('quiz_vraag',vraag_id=session['bezige_vragen'][session['vraagnr']]))

@app.route('/quiz/vraag/<vraag_id>')
def quiz_vraag(vraag_id):
    quiz_db = QuizDatabase()
    vraag = quiz_db.get_vraag(vraag_id)
    quiz_naam = quiz_db.get_quiz(vraag.get_quiz_id()).get_naam()

    if type(vraag)==InputVraag:
        return render_template('inputvraag.html',vraag=vraag,vraagnr=session['vraagnr']+1,quiz_naam=quiz_naam,len_vragen=len(session['bezige_vragen']))
    elif type(vraag)==MultipleChoiceVraag:
        return render_template('multiplechoice.html',vraag=vraag)
    elif type(vraag)==DragDropVraag:
        return render_template('dragndrop.html',vraag=vraag)
    
    app.logger.error('Fout met vraag op te halen')
    return render_template('error.html')

@app.route('/quiz/vraag/klaar',methods=['POST'])
def vraag_klaar():
    if session['vraagnr']==len(session['bezige_vragen']):
        session.pop('vraagnr',None)
        return render_template('quiz_klaar.html',vragen=session['bezige_vragen'],antwoorden=session['antwoorden'])
    session['vraagnr'] += 1
    session['antwoorden'].append(request.form['antwoord'])
    
    return redirect(url_for('quiz_vraag',vraag_id=session['bezige_vragen'][session['vraagnr']]))


if __name__=='__main__':
    app.run(debug=True)