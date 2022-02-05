# questions

class Questions:
    def __init__(self,text,choices,answer):
        self.text = text 
        self.choices = choices 
        self.answer = answer

    def checkanswer(self,answer):
        return self.answer == answer
 
# Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'soru {self.questionIndex + 1}:  {question.text}')

        for q in question.choices:
            print('-'+q)

        answer = input('cevap :')
        self.guess(answer)
        self.loadQuestions()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkanswer(answer):
            self.score += 1
        self.questionIndex += 1

        
    def loadQuestions(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress
            self.displayQuestion()

    def showScore(self):
        print(f'score: {self.score}')

    def displayProgress(self):
        totalQuestions = len(self.questions)
        questionsNumber = self.questionIndex + 1

        if questionsNumber > totalQuestions:
            print('quiz bitti...')
        else:
            print(f',Question {questionsNumber} of {totalQuestions}'.center(100,'*'))

q1 = Questions('en iyi programlama dili hangisidir? ',['c#','python','java','php'],'python')
q2 = Questions('en kolay programlama dili hangisidir? ',['c#','python','java','php'],'python')
q3 = Questions('en basit programlama dili hangisidir? ',['c#','python','java','php'],'python')
questions = [q1,q2,q3]

quiz = Quiz(questions)

quiz.loadQuestions()