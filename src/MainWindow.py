import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from src.chooseclass_en import ChooseClassEn_form
from src.UI.mainformUI import Ui_WordBook_mainform
from src.dict_en import dict_en
from src.worddetail_en import WordDetailen_form
from src.recog_en import RecogbyEN_form
class WordBook(QtWidgets.QWidget,Ui_WordBook_mainform):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dbname = './DICT/ecdict.db'
        self.dict_en = dict_en(self.dbname)
        self.formstack = QtWidgets.QStackedWidget(self)
        self.form_chooseEn = ChooseClassEn_form(self.dict_en, self)
        self.form_worddetailEn = WordDetailen_form(self.dict_en, self)
        self.form_recogEn = RecogbyEN_form(self.dict_en, self)
        self.form_chooseZh = None
        self.form_worddetailZh = None
        self.form_recogZh = None
        self.form_addword = None
        self.formstack.addWidget(self.form_addword)
        self.formstack.addWidget(self.form_chooseEn)
        self.formstack.addWidget(self.form_worddetailEn)
        self.formstack.addWidget(self.form_recogEn)
        self.formstack.addWidget(self.form_chooseZh)
        self.formstack.addWidget(self.form_worddetailZh)
        self.formstack.addWidget(self.form_recogZh)
        self.RemEn_btn.clicked.connect(self.main2choose_en)

    def nextword_en(self):
        self.dict_en.getnextword()
        self.formstack.setCurrentIndex(3)
        self.form_recogEn.initform()
        self.form_recogEn.update()

    def choose2remember_en(self):
        self.dict_en.selectword(
            self.form_chooseEn.choice, self.form_chooseEn.wantnum, select=not self.form_chooseEn.choice.all)
        self.formstack.setCurrentIndex(3)
        self.form_recogEn.initform()
        self.form_recogEn.update()

    def choose2main_en(self):
        pass

    def remember_en(self):
        self.formstack.setCurrentIndex(2)
        self.dict_en.getnextword()
        self.form_worddetailEn.update()

    def forget_en(self):
        self.form_recogEn.error_count += 1
        self.dict_en.wrongwords.append(self.dict_en.nowword)
        if self.form_recogEn.error_count > self.form_recogEn.html.count():
            self.self.formstack.setCurrentIndex(2)

    def tooeasy_en(self):
        self.dict_en.getnextword()
        self.form_recogEn.initform()
        self.form_recogEn.update()

    def main2choose_en(self):
        self.formstack.setCurrentIndex(1)
