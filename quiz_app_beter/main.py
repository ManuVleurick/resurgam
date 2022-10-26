from flask import Flask,render_template,session,url_for,redirect,request
from database.QuizDatabase import QuizDatabase

def main():
    quiz_db = QuizDatabase()
    app = Flask(__name__)
    app.secret_key = b'yoinkersbedoinkers'
    

main()