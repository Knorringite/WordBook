from src.UI.recognizebyenUI import Ui_recognizebyen
import pyttsx3
from PyQt5 import QtWidgets, QtCore, QtGui

class RecogbyEN_form(QtWidgets.QWidget,Ui_recognizebyen):
    def __init__(self,dict_en,mainform):
        super().__init__()
        self.setupUi(self)
        self.dict_en = dict_en
        self.error_count = 0
        self.mainform = mainform
        self.ok_btn.clicked.connect(mainform.remember_en)
        self.no_btn.clicked.connect(mainform.forget_en)
        self.playaudio_btn.clicked.connect(self.playaudio)
        self.tooeasy_btn.clicked.connect(mainform.tooeasy_en)
        self.audio_engine = pyttsx3.init()

    def playaudio(self):
        self.audio_engine.say(self.dict_en.nowword['word'])
        self.audio_engine.runAndWait()

    def update(self):
        tips_html = ''
        for i in range(self.error_count):
            tips_html+=self.html[i]+'\n'
        self.html_tb.setHtml(tips_html)

    def initform(self):
        self.error_count = 0
        self.html = self.dict_en.nowwordtips_html
