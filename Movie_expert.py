# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QMainWindow, QFrame
from PySide2.QtWidgets import QGraphicsDropShadowEffect  # for the splash screen
from PySide2.QtGui import QColor  # for the splash screen
from PySide2.QtGui import QPixmap, QIcon
from PySide2 import QtCore
from PySide2.QtGui import QCursor
import sys
import Data_file
from splashscreen import Ui_SplashScreen


class MainFrame(QMainWindow):
    """Window with logo and button PLAY"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Who want to be a MOVIE EXPERT')
        self.setMinimumSize(1000, 600)
        self.setStyleSheet('background: #282a36;')
        #
        self.ico = QIcon()
        self.ico.addFile('ico.ico')
        self.setWindowIcon(self.ico)
        #
        self.image = QPixmap('logo1.png')
        self.logo = QLabel()
        self.logo.setPixmap(self.image)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)

        self.button_play = QPushButton('PLAY')
        self.button_play.setStyleSheet(
            '*{border: 4px solid "#bd93f9";'
            'border-radius: 45px;'
            'font-family: Arial;'
            'font-size: 35px;'
            'color: "#8be9fd";'
            'padding: 25px 0;'  # space inside the button
            'margin: 50px 200px;'  # space outside the button
            '}'
            '*:hover{background: "#6272a4";}')
        self.button_play.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_play.clicked.connect(lambda x: self.click_on_play())

        self.grid = QGridLayout()
        self.grid.addWidget(self.logo, 0, 0)
        self.grid.addWidget(self.button_play, 1, 0)

        self.container = QFrame()
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)

        self.show()

    def click_on_play(self):
        """Open window with question and answers by clicking on button PLAY"""
        GameFrame()
        self.close()


class GameFrame(QMainWindow):
    """Window with question and answers"""
    def __init__(self):
        super().__init__()
        Data_file.QuestionAnswers()
        self.setWindowTitle('Who want to be a MOVIE EXPERT')
        self.setMinimumSize(800, 400)
        self.setStyleSheet('background: #282a36;')

        self.ico = QIcon()
        self.ico.addFile('ico.ico')
        self.setWindowIcon(self.ico)

        self.image = QPixmap('logo1.png')
        self.logo = QLabel()
        self.logo.setPixmap(self.image)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.setMinimumSize(1000, 600)

        self.question = QLabel(Data_file.parameters['question'][-1])
        self.question.setMinimumHeight(220)
        self.question.setWordWrap(True)
        self.question.setAlignment(QtCore.Qt.AlignCenter)
        self.question.setStyleSheet(
            'font-family: Arial;'
            'font-size: 25px;'
            'color: "#8be9fd";'
            'padding: 75px;')

        self.score = QLabel(str(Data_file.parameters['score']))
        self.score.setAlignment(QtCore.Qt.AlignCenter)
        self.score.setFixedSize(70, 70)
        self.score.setStyleSheet(
            'font-size: 35px;'
            'color: "#282a36";'
            'background: "#50fa7b";'
            'border: 1px solid "#64A314";'
            'border-radius: 35px;')

        self.your_score = QLabel("Your <strong>score</strong>:")
        self.your_score.setAlignment(QtCore.Qt.AlignRight)
        self.your_score.setStyleSheet(
            "font-family: 'Arial'; "
            "font-size: 35px; "
            "color: '#50fa7b'; "
            "margin: 50px 0px;")

        self.btn1 = self.create_button(Data_file.parameters['answer1'][-1], 85, 15)
        self.btn2 = self.create_button(Data_file.parameters['answer2'][-1], 15, 85)
        self.btn3 = self.create_button(Data_file.parameters['answer3'][-1], 85, 15)
        self.btn4 = self.create_button(Data_file.parameters['answer4'][-1], 15, 85)
        self.click_on_btn()

        self.image = QPixmap('logo2.png')
        self.logo = QLabel()
        self.logo.setPixmap(self.image)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setStyleSheet('margin-top: 50px; margin-bottom: 30px;')

        self.grid = QGridLayout()
        self.grid.addWidget(self.your_score, 0, 0)
        self.grid.addWidget(self.score, 0, 1)
        self.grid.addWidget(self.question, 1, 0, 1, 2)
        self.grid.addWidget(self.btn1, 2, 0)
        self.grid.addWidget(self.btn2, 2, 1)
        self.grid.addWidget(self.btn3, 3, 0)
        self.grid.addWidget(self.btn4, 3, 1)
        self.grid.addWidget(self.logo, 4, 0, 1, 2)

        self.container = QFrame()
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)
        self.show()

    def create_button(self, answer, l_margin, r_margin):
        """Method create buttons with answers"""
        self.btn = QPushButton(answer)
        self.btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btn.setFixedWidth(500)
        self.btn.setStyleSheet(
            '*{border: 4px solid "#bd93f9";'
            'margin-left: ' + str(l_margin) + 'px;'
            'margin-right: ' + str(r_margin) + 'px;'
            'border-radius: 25px;'
            'font-size: 16px;'
            'color: "#8be9fd";'
            'padding: 15px 0;'
            'margin-top: 20px;'
            '}'
            '*:hover{background: "#6272a4";}')
        return self.btn

    def click_on_btn(self):
        """Button click event with response"""
        self.btn1.clicked.connect(lambda x: self.click(self.btn1.text()))
        self.btn2.clicked.connect(lambda x: self.click(self.btn2.text()))
        self.btn3.clicked.connect(lambda x: self.click(self.btn3.text()))
        self.btn4.clicked.connect(lambda x: self.click(self.btn4.text()))

    def click(self, text):
        """The method checks whether the answer is correct or not and open Victory window or Lose window"""
        if text == Data_file.parameters['correct'][-1]:
            Data_file.parameters['score'] += 10
            if Data_file.parameters['score'] == 100:
                WinFrame().show()
                self.close()
            self.score.setText(str(Data_file.parameters['score']))
            Data_file.QuestionAnswers()
            self.question.setText(Data_file.parameters['question'][-1])
            self.btn1.setText(Data_file.parameters['answer1'][-1])
            self.btn2.setText(Data_file.parameters['answer2'][-1])
            self.btn3.setText(Data_file.parameters['answer3'][-1])
            self.btn4.setText(Data_file.parameters['answer4'][-1])

        else:
            LoseFrame().show()
            self.close()


class WinFrame(QMainWindow):
    """Victory window with congratulations"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Who want to be a MOVIE EXPERT')
        self.setMinimumSize(1000, 600)
        self.setStyleSheet('background: #282a36;')

        self.ico = QIcon()
        self.ico.addFile('ico.ico')
        self.setWindowIcon(self.ico)

        self.grid = QGridLayout()
        self.container = QFrame()
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)

        self.win_message = QLabel('Congratulations!\nYou are a TRUE MOVIE EXPERT!\n\nYour score is:')
        self.win_message.setAlignment(QtCore.Qt.AlignRight)
        self.win_message.setStyleSheet("font-family: 'Arial'; font-size: 25px; color: '#50fa7b'; margin: 50px 0px;")

        self.image = QPixmap('logo2.png')
        self.logo = QLabel()
        self.logo.setPixmap(self.image)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)

        self.score = QLabel('100')
        self.score.setAlignment(QtCore.Qt.AlignLeft)
        self.score.setStyleSheet("font-family: 'Arial'; font-size: 100px; color: #f1fa8c; margin: 50px 75px 0px 75px;")

        self.message = QLabel("OK, now go back to WORK \n\n OR")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setStyleSheet("font-family: 'Arial'; font-size: 30px; color: '#8be9fd'; ")

        self.btn_try_again = QPushButton('TRY AGAIN')
        self.btn_try_again.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_try_again.setStyleSheet(
            '*{border: 4px solid "#bd93f9";'
            'border-radius: 45px;'
            'font-family: Arial;'
            'font-size: 35px;'
            'color: "#8be9fd";'
            'padding: 25px 0;'  # space inside the button
            'margin: 50px 200px;'  # space outside the button
            '}'
            '*:hover{background: "#6272a4";}')
        self.btn_try_again.clicked.connect(lambda x: self.click_try_again())

        self.grid.addWidget(self.win_message, 1, 0)
        self.grid.addWidget(self.score, 1, 1)
        self.grid.addWidget(self.message, 2, 0, 1, 2)
        self.grid.addWidget(self.btn_try_again, 3, 0, 1, 2)
        self.grid.addWidget(self.logo, 4, 0, 1, 2)

    def click_try_again(self):
        Data_file.parameters = {
            'question': [],
            'answer1': [],
            'answer2': [],
            'answer3': [],
            'answer4': [],
            'correct': [],
            'score': 0,
            'index': []
        }
        MainFrame()
        self.close()


class LoseFrame(WinFrame):
    """Lose window"""
    def __init__(self):
        super().__init__()
        self.lose_message = QLabel("Sorry, this answer was wrong!\n\n Your score is:")
        self.lose_message.setAlignment(QtCore.Qt.AlignRight)
        self.lose_message.setStyleSheet("font-family: 'Arial'; font-size: 25px; color: '#50fa7b'; margin: 100px 0px;")

        self.lose_score = QLabel(str(Data_file.parameters['score']))
        self.lose_score.setAlignment(QtCore.Qt.AlignLeft)
        self.lose_score.setStyleSheet("font-size: 100px; color: #ff5555; margin: 80px 75px 0px 75px;")

        self.grid = QGridLayout()
        self.grid.addWidget(self.lose_message, 1, 0)
        self.grid.addWidget(self.lose_score, 1, 1)
        self.grid.addWidget(self.btn_try_again, 3, 0, 1, 2)
        self.grid.addWidget(self.logo, 4, 0, 1, 2)

        self.container = QFrame()
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)


class NoInternet(QMainWindow):
    """Window when there is no internet"""
    def __init__(self):
        super().__init__()

        self.setMinimumSize(500, 300)
        self.setWindowTitle('Who want to be a MOVIE EXPERT')
        self.setStyleSheet('background: #282a36;')

        self.ico = QIcon()
        self.ico.addFile('ico.ico')
        self.setWindowIcon(self.ico)

        self.message = QLabel('Some problems with Internet connection\n\nTry later')
        self.message.setMinimumHeight(220)
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setStyleSheet(
            'font-family: Arial;'
            'font-size: 25px;'
            'color: "#ff5555";'
        )

        self.image = QPixmap('logo2.png')
        self.logo = QLabel()
        self.logo.setPixmap(self.image)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)

        self.grid = QGridLayout()
        self.grid.addWidget(self.message)
        self.grid.addWidget(self.logo)

        self.container = QFrame()
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)

        self.show()


class SplashScreen(QMainWindow, Ui_SplashScreen):
    """Startup splash screen with loading process"""
    def __init__(self):
        super().__init__()
        self.ico = QIcon()
        self.ico.addFile('ico.ico')
        self.setWindowIcon(self.ico)
        self.setupUi(self)
        self.setWindowTitle('Who want to be a MOVIE EXPERT')

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        # Q TIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(20)  # time in ms after which the counter changes in def progress

        # CHANGE DESCRIPTION
        QtCore.QTimer.singleShot(0, lambda: self.label_description.setText('<strong>LOADING</strong> DATABASE'))
        QtCore.QTimer.singleShot(2000, lambda: self.label_description.setText('<strong>LOADING</strong> '
                                                                              'USER INTERFACE'))
        self.show()

    def progress(self):
        global counter
        # SET VALUE TO progressBar
        self.progressBar.setValue(counter)
        # CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 100:
            # STOP Timer
            self.timer.stop()
            # SHOW MainFrame
            MainFrame()
            # CLOSE SPLASH SCREEN
            self.close()
        # INCREASE COUNTER
        counter += 1


counter = 0  # counter for SplashScreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = SplashScreen()
    sys.exit(app.exec_())
