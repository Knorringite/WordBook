import numpy as np
import pickle
from DICT.stardict import StarDict


class dict_en():
    def __init__(self, dbname):
        self.DICT = StarDict(dbname)
    words = []
    wrongwords = []

    def selectword(self, choice, count, select=True):
        word_ids = self.__getwrong()
        if count > word_ids.count():
            count -= word_ids.count()
        if select:
            sql = '''select id,word,phonetic'''

        else:
            total_count = self.DICT.count()
            if count > total_count:
                word_ids = np.random.randint(1, total_count, size=total_count)
                self.words = self.DICT.query_batch(word_ids)
            else:
                word_ids = np.random.randint(1, total_count, size=count)
                self.words = self.DICT.query_batch(word_ids)

    def __getwrong(self):
        wrongwords = pickle.load('./DICT/wrongEN.pkl')
        if wrongwords is None:
            return []
        else:
            return wrongwords

    def addwrong(self, wordid):
        self.wrongwords = self.__getwrong()
        if wordid not in self.wrongwords:
            self.wrongwords.append(wordid)
            pickle.dump(self.wrongwords, './DICT/wrongEN.pkl')

    def delwrong(self, wordid):
        self.wrongwords = self.__getwrong()
        if wordid in self.wrongwords:
            self.wrongwords.remove(wordid)
            pickle.dump(self.wrongwords, './DICT/wrongEN.pkl')
