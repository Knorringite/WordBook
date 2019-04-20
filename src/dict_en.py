import numpy as np
import pickle
from DICT.stardict import StarDict
from DICT.dictutils import Treasure

class dict_en():
    def __init__(self, dbname):
        self.DICT = StarDict(dbname)
        self.dbname = dbname
        self.treasure = Treasure()
    words = []
    wrongwords = []
    nowword = None
    nowword_html = ''
    nowword_detail_html = ''
    word_total_count = 0
    nowcount = 0

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
        DICT = StarDict(self.dbname)
        word_ids = self.__getwrong()
        if count > word_ids.count():
            count -= word_ids.count()
        if select:
            sql = self.__getsql(choice)
            self.words = DICT.query_sql(sql)
        else:
            total_count =DICT.count()
            if count > total_count:
                word_ids += np.random.randint(1, total_count, size=total_count)
                self.words = DICT.query_batch(word_ids)
                self.word_total_count = total_count
            else:
                word_ids += np.random.randint(1, total_count, size=count)
                self.words = DICT.query_batch(word_ids)
                self.word_total_count = count


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
        if self.words.count() >= 1:
            now = self.words.pop()
            self.nowcount += 1
            self.nowwordtips_html = self.__gettipshtml(now)
            self.nowword = now
        else:
            self.nowword = None


    def __gettipshtml(self, data):

        html = None
        html_return = []

        html.first = []
        text = "<div style='text-align:center'><h1>%s</h1></div>"
        html.first.append(text % self.treasure.text2html(data['word']))
        html.first.append("<div style='text-align:center; font-size:85%;'>")
        text = "<span style='font-family: Arial; color:blue;'>%s</span>"
        html.first.append(text % self.treasure.get_phonetic(data))
        text = "<span style='font-family: Arial; color:gray;'>%s</span>"
        html.first.append(text % self.treasure.get_level(data))
        html.first.append('</div>')
        html_return.append('\n'.join(html.first))


        html.second = []
        html.second.append('<div>')

        hr = "height:1px;border:none;border-top:1px dashed #0066CC;"
        hr = hr + "background-color:#ffffff;"
        hr = '<hr style="%s">' % hr

        memo = self.treasure.get_memo(data)
        if memo:
            html.second.append(
                '<div style="text-align:left;color:#895b8a;font-size:14px;">')
            html.second.append(memo)
            html.second.append('</div>')
            html.second.append(hr)

        explain = self.treasure.get_explain(data)
        if explain:
            html.second.append('<div style="text-align:left;font-size:14px;">')
            html.second.append(explain)
            html.second.append('</div>')

        extra = self.treasure.get_extra(data)
        if extra:
            html.second.append(hr)
            html.second.append('<div style="color:gray;font-size:14px;text-align:left">')
            html.second.append(extra)
            html.second.append('</div>')
        html.second.append('<br></div>')
        if html.second.count() > 2:
            html_return.append('\n'.join(html.second))


        html.third = []
        text = "<div style='color:BlueViolet;text-align:center;font-size:16px;'>%s</div>"
        html.third.append(text % self.treasure.get_definition(data))
        html.third.append('<br>')
        html_return.append('\n'.join(html.third))

        html.fourth = []
        text = "<div style='color:BlueViolet;text-align:center;font-size:16px;'>%s</div>"
        html.fourth.append(text % self.treasure.get_translation(data))
        html.fourth.append('<br>')
        html_return.append('\n'.join(html.fourth))

        return html_return

    def __getdetailhtml(self, data):
        pass
