class QuizController:
    
    def __init__(self):
        self.quiz_db = QuizDatabase()
        self.quiz_repo = QuizRepository()

    def close_db(self):
        self.quiz_db.close_db()

    def command(self,sql,expect_return=False):
        if expect_return:
            return self.quiz_db.console_command(sql,expect_return)
        self.quiz_db.console_command(sql)

    def ini_mock_data(self):
        pass
        

