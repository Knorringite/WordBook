import numpy as np
import os
import pickle
import urllib.request
from playsound import playsound
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from src.UI.RecognizeByCHUI import Ui_recognizebychUI
from src.WordDetailPage import WordDetailPage
from DICT.stardict import StarDict
from DICT.dictutils import Treasure


class RecognizeByChPage(QDialog, Ui_recognizebychUI):
    word_signals = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = {'is_random': 1, 'word_number': 10, 'is_condition': 0, 'is_tag': 0, 'is_collins': 0,
                         'is_bnc': 0, 'is_frq': 0, 'is_pos': 0, 'is_zk': 0, 'is_gk': 0, 'is_cet4': 0,
                         'is_cet6': 0, 'is_ielts': 0, 'is_toelf': 0, 'is_ky': 0,
                         'is_oxford': 0, 'collins_star': 0, 'bnc_frq': 50, 'frq_frq': 50, 'pos_v': 0, 'pos_n': 0,
                         'pos_prep': 0, 'pos_adj': 0, 'pos_adv': 0, 'pos_other': 0}
        self.DICT = StarDict('../DICT/ecdict.db')
        self.word_detail_page = WordDetailPage()
        self.treasure = Treasure()
        self.words = []
        self.wrong_words = []
        self.now_word = None
        self.now_word_tips_html = ''
        self.now_word_detail_html = ''
        self.word_total_count = 0
        self.now_count = 0
        self.no_count = 0
        self.remed_word_count = 0
        self.rem_done = False

    def read_settings(self, content):
        self.settings = content

    def __get_sql(self):
        sql = 'select * from stardict where '
        querys = []
        keys = []
        if self.settings['is_random']:
            querys.append('id like ?')
            keys.append('%')
        else:
            if self.settings['is_tag']:
                if self.settings['is_zk']:
                    querys.append('tag like ?')
                    keys.append('%zk%')
                if self.settings['is_gk']:
                    querys.append('tag like ?')
                    keys.append('%gk%')
                if self.settings['is_cet4']:
                    querys.append('tag like ?')
                    keys.append('%cet4%')
                if self.settings['is_cet6']:
                    querys.append('tag like ?')
                    keys.append('%cet6%')
                if self.settings['is_ky']:
                    querys.append('tag like ?')
                    keys.append('%ky%')
                if self.settings['is_toefl']:
                    querys.append('tag like ?')
                    keys.append('%toefl%')
                if self.settings['is_ielts']:
                    querys.append('tag like ?')
                    keys.append('%ielts%')
            if self.settings['is_oxford']:
                querys.append('oxford = ?')
                keys.append('1')
            if self.settings['is_bnc']:
                querys.append('bnc <= ?')
                keys.append(int(self.settings['bnc_frq']))
            if self.settings['is_frq']:
                querys.append('frq <= ?')
                keys.append(int(self.settings['frq_frq']))
            if self.settings['is_collins']:
                querys.append('collins = ?')
                keys.append(int(self.settings['collins_star']))
        sql = sql + ' or '.join(querys) + ';'
        if sql == 'select * from stardict where ;':
            sql = 'select * from stardict where id like ?'
        return sql, keys

    def select_word(self, count, select=True):  # return word list
        word_ids = []
        if select:
            sql, keys = self.__get_sql()
            self.words = list(self.DICT.query_sql(sql, keys))
            self.words = np.random.choice(self.words, size=count, replace=False).tolist()
        else:
            total_count = self.DICT.count()
            if count > total_count:
                word_ids += np.random.randint(1, high=total_count, size=total_count).tolist()
                self.words = list(self.DICT.query_batch(word_ids))
                self.word_total_count = total_count
            else:
                word_ids += np.random.randint(1, high=total_count, size=count).tolist()
                self.words = list(self.DICT.query_batch(word_ids))
                self.word_total_count = count
        while None in self.words:
            self.words.remove(None)

    def __get_right(self):
        self.right_words = []
        if os.path.exists('../DICT/right_word_record.pkl.pkl'):
            with open('../DICT/right_word_record.pkl', 'rb') as f:
                while True:
                    try:
                        self.right_words.append(pickle.load(f))
                    except:
                        break
        return self.right_words

    def add_right(self, word):
        right_words = self.__get_right()
        if word not in right_words:
            with open('../DICT/right_word_record.pkl', 'ab+') as f:
                pickle.dump(word, f)

    def __get_wrong(self):
        self.wrong_words = []
        if os.path.exists('../DICT/wrong_word_record.pkl'):
            with open('../DICT/wrong_word_record.pkl', 'rb') as f:
                while True:
                    try:
                        self.wrong_words.append(pickle.load(f))
                    except:
                        break
        return self.wrong_words

    def add_wrong(self, word):
        self.wrong_words.append(word)
        wrong_words = self.__get_wrong()
        if word not in wrong_words:
            with open('../DICT/wrong_word_record.pkl', 'ab+') as f:
                pickle.dump(word, f)

    def del_wrong(self, word):
        while word in self.wrong_words:
            self.wrong_words.remove(word)

    def add_ez(self, word):
        ez_words = []
        if os.path.exists('../DICT/right_word_record.pkl'):
            with open('../DICT/right_word_record.pkl', 'rb') as f:
                while True:
                    try:
                        ez_words.append(pickle.load(f))
                    except:
                        break
        if word not in ez_words:
            with open('../DICT/right_word_record.pkl', 'ab+') as f:
                pickle.dump(word, f)

    def get_next_word(self):
        if not len(self.wrong_words):
            if len(self.words) >= 1:
                now = self.words.pop()
                self.remed_word_count += 1
                self.now_count += 1
                self.now_word_tips_html = self.__get_tips_html(now)
                self.now_word = now
                self.now_word_detail_html = self.__get_detail_html(now)
                return True
            else:
                return False
        else:
            ran = np.random.randint(0, 100, 1)
            if ran < 50:
                now = self.wrong_words.pop()
                self.now_count += 1
                self.now_word_tips_html = self.__get_tips_html(now)
                self.now_word = now
                self.now_word_detail_html = self.__get_detail_html(now)
                return True
            else:
                if len(self.words) >= 1:
                    now = self.words.pop()
                    self.remed_word_count += 1
                    self.now_count += 1
                    self.now_word_tips_html = self.__get_tips_html(now)
                    self.now_word = now
                    self.now_word_detail_html = self.__get_detail_html(now)
                    return True
                else:
                    return False

    def __get_tips_html(self, data):

        html = {}
        html_return = []

        html['first'] = []
        text = "<div style='text-align:center'><h1>%s</h1></div>"
        html['first'].append(text % self.treasure.get_translation(data))
        html['first'].append("<div style='text-align:center; font-size:85%;'>")
        text = "<span style='font-family: Arial; color:gray;'>%s</span>"
        html['first'].append(text % self.treasure.get_level(data))
        html['first'].append('</div>')
        html_return.append('\n'.join(html['first']))

        html['second'] = []
        html['second'].append('<div>')

        hr = "height:1px;border:none;border-top:1px dashed #0066CC;"
        hr = hr + "background-color:#ffffff;"
        hr = '<hr style="%s">' % hr

        memo = self.treasure.get_memo(data)
        if memo:
            html['second'].append(
                '<div style="text-align:center;color:#895b8a;font-size:14px;">')
            html['second'].append(memo)
            html['second'].append('</div>')
            html['second'].append(hr)

        explain = self.treasure.get_explain(data)
        if explain:
            html['second'].append('<div style="text-align:center;font-size:14px;">')
            html['second'].append(explain)
            html['second'].append('</div>')

        extra = self.treasure.get_extra(data)
        if extra:
            html['second'].append(hr)
            html['second'].append('<div style="color:gray;font-size:14px;text-align:center">')
            html['second'].append(extra)
            html['second'].append('</div>')
        html['second'].append('<br></div>')
        if len(html['second']) > 2:
            html_return.append('\n'.join(html['second']))

        html['third'] = []
        text = "<div style='color:BlueViolet;font-size:16px;'>%s</div>"
        html['third'].append(text % self.treasure.get_definition(data))
        text = "<span style='font-family: Arial; color:blue;'>%s</span>"
        html['third'].append(text % self.treasure.get_phonetic(data))
        html['third'].append('<br>')
        html_return.append('\n'.join(html['third']))

        html['fourth'] = []
        text = "<div style='color:Black;font-size:22px;'>%s</div>"
        html['fourth'].append(text % self.treasure.text2html(data['word']))
        html['fourth'].append('<br>')
        html_return.append('\n'.join(html['fourth']))

        return html_return

    def __get_detail_html(self, data):
        html = []
        text = "<div style='text-align:center'><h1>%s</h1></div>"
        html.append(text % self.treasure.text2html(data['word']))
        html.append("<div style='text-align:center; font-size:85%;'>")
        text = "<span style='font-family: Arial; color:blue;'>%s</span>"
        html.append(text % self.treasure.get_phonetic(data))
        text = "<span style='font-family: Arial; color:gray;'>%s</span>"
        html.append(text % self.treasure.get_level(data))
        html.append('</div>')
        html.append('<div>')
        hr = "height:1px;border:none;border-top:1px dashed #0066CC;"
        hr = hr + "background-color:#ffffff;"
        hr = '<hr style="%s">' % hr
        text = "<div style='color:BlueViolet;text-align:center;font-size:16px;'>%s</div>"
        html.append(text % self.treasure.get_translation(data))
        html.append('<br>')
        exchange = self.treasure.get_exchange(data)
        if exchange:
            text = "<div style='font-size:12px;color:gray;text-align:center'>%s<br></div>"
            html.append(text % exchange)
        proportion = self.treasure.get_proportion(data)
        if proportion:
            text = u"<div style='font-size:12px;color:gray;text-align:center'>分布：%s<br></div>"
            html.append(text % proportion)
        html.append(hr)
        memo = self.treasure.get_memo(data)
        if memo:
            html.append('<div style="text-align:left;color:#895b8a;font-size:14px;">')
            html.append(memo)
            html.append('<br></div>')
            html.append(hr)
        explain = self.treasure.get_explain(data)
        if explain:
            html.append('<div style="text-align:left;font-size:14px;">')
            html.append(explain)
            html.append('<br></div>')
        extra = self.treasure.get_extra(data)
        if extra:
            html.append(hr)
            html.append('<div style="color:gray;font-size:14px;text-align:left">')
            html.append(extra)
            html.append('<br></div>')
        html.append('<br></div>')
        return '\n'.join(html)

    def init_words(self):
        self.rem_done = False
        self.remed_word_count = 0
        self.select_word(self.settings['word_number'])
        self.get_next_word()
        self.html_table.clear()
        self.html_table.append(self.now_word_tips_html[0])

    def finish_text(self):
        text = "<div style='text-align:center'><h1>Finished!</h1></div>"
        self.html_table.clear()
        self.html_table.append(text)

    def show_next_word(self):
        if self.get_next_word():
            self.html_table.clear()
            self.html_table.append(self.now_word_tips_html[0])
        else:
            self.finish_text()
            self.rem_done = True

    def emit_word(self):
        content = [self.now_word_detail_html, [self.remed_word_count, self.settings['word_number']]]
        self.word_signals.emit(content)

    def turn_to_word_detail_page(self):
        self.word_detail_page.show()
        self.word_signals.connect(self.word_detail_page.get_word)
        self.emit_word()
        self.word_signals.disconnect(self.word_detail_page.get_word)
        self.word_detail_page.init_ui()

    def yes(self):
        if self.rem_done:
            return
        self.add_right(self.now_word)
        self.no_count = 0
        self.turn_to_word_detail_page()
        self.show_next_word()

    def no(self):
        if self.rem_done:
            return
        self.add_wrong(self.now_word)
        if self.no_count < 2:
            self.no_count += 1
            self.html_table.append(self.now_word_tips_html[self.no_count])
        else:
            self.turn_to_word_detail_page()
            self.show_next_word()

    def play_audio(self):
        filepath = '../Audio/' + self.now_word['word'] + '.mp3'
        if not os.path.exists(filepath):
            url = 'http://dict.youdao.com/dictvoice?type=0&audio=' + self.now_word['word']
            try:
                urllib.request.urlretrieve(url, filename=filepath)
            except:
                return
        playsound(filepath, block=False)

    def too_ez(self):
        self.add_ez(self.now_word)
        self.no_count = 0
        self.del_wrong(self.now_word)
        self.turn_to_word_detail_page()
        self.show_next_word()
