import numpy as np
import pickle
from DICT.stardict import StarDict
from DICT.dictutils import Treasure

class dict_en():
    def __init__(self, dbname):
        self.DICT = StarDict(dbname)
        self.treasure = Treasure()
    words = []
    wrongwords = []

    def __getsql(self,choice):
        sql = '''select * from stardict where '''
        if choice.tag:
            sql_tag ="(tag like '%[233|"
            if choice.zk:
                sql_tag += 'zk|'
            if choice.gk:
                sql_tag += 'gk|'
            if choice.cet4:
                sql_tag += 'cet4|'
            if choice.cet6:
                sql_tag += 'cet6|'
            if choice.ky:
                sql_tag += 'ky|'
            if choice.toefl:
                sql_tag += 'toefl|'
            if choice.ielts:
                sql_tag += 'ielts|'
            sql_tag += "2333]%) and "
            sql+=sql_tag
        if choice.oxford:
            sql += "oxford = 1 and "
        else:
            sql+= "oxford = 0 and "
        if choice.bnc:
            sql += "bnc >= "+str(choice.bnc_num)+" and "
        if choice.frq:
            sql += "frq >= "+str(choice.bnc_num)+" and "
        if choice.pos:
            sql_pos="pos like %[233|"
            if choice.pos_v:
                sql_pos+="v|"
            if choice.pos_n:
                sql_pos += "n|"
            if choice.pos_prep:
                sql_pos += "v|"
            if choice.pos_adj:
                sql_pos += "j|"
            if choice.pos_adv:
                sql_pos += "r|"
            sql_pos += "2333]% "
            sql += sql_pos+"and "
        if choice.collins:
            sql += "collins = " + str(choice.collins_num) + " and "
        sql += "2>1"
        return sql

    def selectword(self, choice, count, select=True):
        word_ids = self.__getwrong()
        if count > word_ids.count():
            count -= word_ids.count()
        if select:
            sql = self.__getsql(choice)
            self.words = self.DICT.query_sql(sql)
        else:
            total_count = self.DICT.count()
            if count > total_count:
                word_ids += np.random.randint(1, total_count, size=total_count)
                self.words = self.DICT.query_batch(word_ids)
            else:
                word_ids += np.random.randint(1, total_count, size=count)
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

    def getnextword(self):
        if self.words.count() > 1:
            now = self.words.pop()
            html_def = treasure.define_html(now)
            treasure.get_translation
        else:
            return None
