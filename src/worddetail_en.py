from src.UI.worddetailUI import Ui_worddetail
from PyQt5 import QtWidgets, QtCore, QtGui

class WordDetailen_form(Ui_worddetail):
    def __init__(self, dict_en,mainform):
        super().__init__()
        self.setupUi(self)
        self.dict_en = dict_en
        self.next_bt.clicked.connect(mainform.nextword_en)

    def update(self):
        self.word_pb.setValue(int(self.dict_en.nowcount/self.dict_en.word_total_count))
        self.detail_tb.setHtml(self.dict_en.nowword_detail_html)
