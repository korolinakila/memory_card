from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QRadioButton, QMessageBox, QLabel, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.question = question



app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

main_win.score = 0
main_win.total = 0

q = Question('Какого народа не существует?', 'Энцы', 'Смурфы', 'Чулымцы', 'Алеуты')

question = QLabel('Какаой национальсти не существует?')

answer = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

questions_list = []
questions_list.append(Question('Какое число я загадал?', '1', '2', '3', '4'))
questions_list.append(Question('Скоько мне лет?', '14', '12', '15', '13'))
questions_list.append(Question('1000-7?', '993', '986', '979', '972'))
questions_list.append(Question('В какой стране находится Киев?', 'Россия', 'Украина', 'Беларусь', 'США'))
questions_list.append(Question('Президент России?', 'Путин', 'Владимир', 'Владимирович', 'Вова'))

RadioGroup = QButtonGroup()

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    answer.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def star_test():
    if answer.text() == ('Ответить'):
        show_result()
    else:
        show_question()



answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]





def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    Label2.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        Label1.setText('Правильно')
        main_win.score += 1
    else:
        Label1.setText('Неправильно')
    show_result()
    print('Статистика ')
    print('Всего вопросов:', main_win.total)
    print('Всего ответов:', main_win.score)
    print('Рейтинг:', main_win.score / main_win.total * 100, '%')

def next_question():
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
    main_win.total += 1


def click_OK():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()


AnswerGroupBox = QGroupBox('Результат теста')
AnswerGroupBox.hide()
Label1 = QLabel('Правильно/Неправильно')
Label2 = QLabel('Правильный ответ')

layout_answer1 = QVBoxLayout()

layout_answer1.addWidget(Label1, alignment = Qt.AlignLeft)
layout_answer1.addWidget(Label2, alignment = Qt.AlignCenter)

AnswerGroupBox.setLayout(layout_answer1)



RadioGroup = QButtonGroup()

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment = Qt.AlignCenter)
layout_main.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
layout_main.addWidget(AnswerGroupBox, alignment = Qt.AlignCenter)
layout_main.addWidget(answer, alignment = Qt.AlignCenter)

next_question()

answer.clicked.connect(click_OK)

main_win.setLayout(layout_main)
main_win.show()
app.exec_()