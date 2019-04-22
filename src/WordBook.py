import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from src.dict_en import dict_en
from src.UI.main import Ui_WordBook
from src.recog_en import RecogbyEn
from src.chooseclass_en import ChooseClassEn
from src.worddetail_en import WordDetailEn


class WordBook(QtWidgets.QStackedWidget, Ui_WordBook):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dict_en = dict_en('./DICT/ecdict.db')
        self.recog_en = RecogbyEn(self.dict_en, self)
        self.choose_en = ChooseClassEn(self.dict_en, self)
        self.detail_en = WordDetailEn(self.dict_en, self)
        self.setCurrentIndex(0)
        self.RemEn_btn.clicked.connect(self.main2choose_en)
    '''
        0:main
        1:choose_en
        2:recog_en
        3:detail_en
        4:choose_zh
        5:recog_zh
        6:detail_zh
        7:addword
        8:setting
        9:success
        10:about
    '''
    def nextword_en(self):
        self.dict_en.getnextword()
        self.setCurrentIndex(2)
        self.recog_en.initform()
        self.recog_en.update()

    def choose2remember_en(self):
        self.dict_en.selectword(
            self.choose_en.choice, self.choose_en.wantnum, select= not self.choose_en.choice['all'])
        self.dict_en.getnextword()
        self.setCurrentIndex(2)
        self.recog_en.initform()
        self.recog_en.update()

    def choose2main_en(self):
        self.setCurrentIndex(0)

    def remember_en(self):
        self.setCurrentIndex(3)
        self.dict_en.getnextword()
        self.detail_en.update()

    def forget_en(self):
        self.recog_en.error_count += 1
        self.recog_en.update()
        self.dict_en.wrongwords.append(self.dict_en.nowword)
        if self.recog_en.error_count > len(self.dict_en.nowword_tips_html):
            self.self.setCurrentIndex(2)

    def tooeasy_en(self):
        self.dict_en.getnextword()
        self.recog_en.initform()
        self.recog_en.update()

    def main2choose_en(self):
        print('into choose')
        self.setCurrentIndex(1)
