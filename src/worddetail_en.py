from PyQt5 import QtWidgets, QtCore, QtGui
from src.UI.worddetailUI import Ui_worddetailUI


class worddetail_form(Ui_worddetailUI):
    def __init__(self,dict_en):
        self.setupUi(self)
        self.dict_en = dict_en
        self.nowword = dict_en.getnextword()

    def update(self):
        self.word_pb.setValue(int(self.dict_en.nowcount/self.dict_en.word_total_count))
        self.detail_tb.setHtml(self.dict_en.nowword_detail_html)
