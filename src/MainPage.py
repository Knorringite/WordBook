import os
import pickle
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from src.UI.MainUI import Ui_Main
from src.OptionPage import OptionPage
from src.RecognizeByChPage import RecognizeByChPage
from src.RecognizeByEnPage import RecognizeByEnPage


class WordBook(QWidget, Ui_Main):
    setting_signals = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.option_page = OptionPage()
        self.recognize_by_ch_page = RecognizeByChPage()
        self.recognize_by_en_page = RecognizeByEnPage()

        self.settings = {}

        self.update_state()

    def emit_settings(self):
        setting_content = self.settings
        self.setting_signals.emit(setting_content)

    def turn_to_option_page(self):
        self.option_page.show()
        self.option_page.setting_signals.connect(self.get_option_page_signal)
        # self.option_page.setting_signals.connect(self.recognize_by_ch_page.read_settings)

    def turn_to_remember_by_ch_page(self):
        if self.settings == {}:
            self.turn_to_option_page()
        else:
            self.recognize_by_ch_page.show()
            self.setting_signals.connect(self.recognize_by_ch_page.read_settings)
            self.emit_settings()
            self.setting_signals.disconnect(self.recognize_by_ch_page.read_settings)
            self.recognize_by_ch_page.init_words()

    def turn_to_remember_by_en_page(self):
        if self.settings == {}:
            self.turn_to_option_page()
        else:
            self.recognize_by_en_page.show()
            self.setting_signals.connect(self.recognize_by_en_page.read_settings)
            self.emit_settings()
            self.setting_signals.disconnect(self.recognize_by_en_page.read_settings)
            self.recognize_by_en_page.init_words()

    def get_option_page_signal(self, content):
        self.settings = content
        self.option_page.setting_signals.disconnect(self.get_option_page_signal)

    def update_state(self):
        right_words = []
        if os.path.exists('../DICT/right_word_record.pkl'):
            with open('../DICT/right_word_record.pkl', 'rb') as f:
                while True:
                    try:
                        right_words.append(pickle.load(f))
                    except:
                        break
        self.word_status_label.setText('您已背诵 %d 个单词' % len(right_words))
