from PyQt5.QtWidgets import QDialog
from src.UI.worddetailUI import Ui_worddetailUI


class WordDetailPage(QDialog, Ui_worddetailUI):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.word_html = []
        self.remed_word_count = 0
        self.word_count = 0

    def init_ui(self):
        self.detail_tb.clear()
        self.detail_tb.append(self.word_html)
        self.word_pb.setMaximum(self.word_count)
        self.word_pb.setValue(self.remed_word_count)

    def get_word(self, content):
        self.word_html = content[0]
        self.remed_word_count, self.word_count = content[1]

    def next_word(self):
        self.close()
