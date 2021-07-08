import pandas as pd
import json
import random
from urllib.request import urlopen
from urllib.error import URLError
import Movie_expert
import sys
from PySide2.QtWidgets import QApplication

try:
    with urlopen('https://opentdb.com/api.php?amount=50&category=11&difficulty=easy&type=multiple') as webpage:
        data = json.loads(webpage.read().decode())
        df = pd.DataFrame(data['results'])
        # print(df.head())
        # print(df.columns)  # creating a list of all columns

except URLError as e:
    if hasattr(e, 'reason'):
        print('Some problems with Internet connection')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('Some problems with Internet connection')
        print('Error code: ', e.code)
    app = QApplication(sys.argv)
    error = Movie_expert.NoInternet()
    sys.exit(app.exec_())

parameters = {
    'question': [],
    'answer1': [],
    'answer2': [],
    'answer3': [],
    'answer4': [],
    'correct': [],
    'score': 0,
    'index': []
}


def formatting(fraze):
    formatting_list = [
        ("#039;", "'"),
        ("&'", "'"),
        ("&quot;", '"'),
        ("&lt;", "less than SYMBOL"),
        ("&gt;", "greater than SYMBOL"),
        ("&amp;", ""),
        ("&ntilde;&aacute;", "na"),
        ("&rsquo;", "'")]
    for i in formatting_list:
        fraze = fraze.replace(i[0], i[1])
    return fraze


def formatting_wrong(wrong):
    formatting_list = [
        ("#039;", "'"),
        ("&'", "'"),
        ("&quot;", '"'),
        ("&lt;", "less than SYMBOL"),
        ("&gt;", "greater than SYMBOL"),
        ("&amp;", ""),
        ("&rsquo;", "'"),
        ("&ntilde;&aacute;", "na")]
    for i in formatting_list:
        wrong = [j.replace(i[0], i[1]) for j in wrong]
    return wrong


class QuestionAnswers:
    def __init__(self):
        self.get_index()
        self.question = formatting(df['question'][self.idx])
        self.correct = formatting(df['correct_answer'][self.idx])
        self.wrong_answers = formatting_wrong(df['incorrect_answers'][self.idx])
        self.all_answers = self.wrong_answers + [self.correct]
        random.shuffle(self.all_answers)

        print(self.question)
        print(self.correct)

        parameters['question'].append(self.question)
        parameters['correct'].append(self.correct)
        parameters['answer1'].append(self.all_answers[0])
        parameters['answer2'].append(self.all_answers[1])
        parameters['answer3'].append(self.all_answers[2])
        parameters['answer4'].append(self.all_answers[3])
        parameters['index'].append(self.idx)

    def get_index(self):
        self.idx = random.randint(0, 49)
        for _ in parameters['index']:
            if self.idx in parameters['index']:
                self.idx = random.randint(0, 49)
        else:
            return self.idx
