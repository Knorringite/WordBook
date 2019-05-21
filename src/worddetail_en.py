class WordDetailEn():
    def __init__(self, dict_en,mainform):
        self.dict_en = dict_en
        self.mainform = mainform
        mainform.next_bt_en.clicked.connect(mainform.nextword_en)

    def update(self):
        self.mainform.word_pb_en.setValue(
            int(self.dict_en.nowcount/self.dict_en.word_total_count))
        self.mainform.detail_tb_en.setHtml(self.dict_en.nowword_detail_html)
