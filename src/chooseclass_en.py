import json
import os
class ChooseClassEn():
    def __init__(self, dict_en ,mainform):
        self.choice = {}
        self.mainform = mainform
        if os.path.exists('./DICT/choice_en.pkl'):
            with open('./DICT/choice_en.pkl','r') as f:
                self.choice = json.load(f)
        else:
            self.choice['all'] = True
            self.choice['tag'] = False
            self.choice['zk'] = False
            self.choice['gk'] = False
            self.choice['cet4'] = False
            self.choice['cet6'] = False
            self.choice['ky'] = False
            self.choice['toefl'] = False
            self.choice['ielts'] = False
            self.choice['oxford'] = False
            self.choice['bnc'] = False
            self.choice['frq'] = False
            self.choice['pos'] = False
            self.choice['pos_v'] = False
            self.choice['pos_n'] = False
            self.choice['pos_prep'] = False
            self.choice['pos_adj'] = False
            self.choice['pos_adv'] = False
            self.choice['collins'] = False
            self.choice['collins_num'] = 0
            self.choice['bnc_num'] = 0
            self.choice['frq_num'] = 0
        self.haveselected = False
        self.wantnum = 100
        self.actalnum = 0
        self.mainform.bnc_slider_en.setRange(0, 100000)
        self.mainform.frq_slider_en.setRange(0, 100000)
        self.mainform.beginrecog_btn_en.clicked.connect(
            self.mainform.choose2remember_en)
        self.mainform.back_btn_en.clicked.connect(self.mainform.choose2main_en)
        self.mainform.frq_cb_en.toggled.connect(self.updatechoice)
        self.mainform.prep_cb_en.toggled.connect(self.updatechoice)
        self.mainform.adj_cb_en.toggled.connect(self.updatechoice)
        self.mainform.gk_cb_en.toggled.connect(self.updatechoice)
        self.mainform.bnc_cb_en.toggled.connect(self.updatechoice)
        self.mainform.oxford_cb_en.toggled.connect(self.updatechoice)
        self.mainform.frq_tl_en.textChanged.connect(self.updatechoice)
        self.mainform.collins3_rbtn_en.toggled.connect(self.updatechoice)
        self.mainform.bnc_tl_en.textChanged.connect(self.updatechoice)
        self.mainform.cet6_cb_en.toggled.connect(self.updatechoice)
        self.mainform.collins5_rbtn_en.toggled.connect(self.updatechoice)
        self.mainform.zk_cb_en.toggled.connect(self.updatechoice)
        self.mainform.collins2_rbtn_en.toggled.connect(self.updatechoice)
        self.mainform.wordcount_tl_en.textChanged.connect(self.updatechoice)
        self.mainform.toefl_cb_en.toggled.connect(self.updatechoice)
        self.mainform.back_btn_en.toggled.connect(self.updatechoice)
        self.mainform.ielts_cb_en.toggled.connect(self.updatechoice)
        self.mainform.all_rbtn_en.toggled.connect(self.updatechoice)
        self.mainform.bnc_slider_en.valueChanged.connect(self.updatechoice)
        self.mainform.tag_cb_en.toggled.connect(self.updatechoice)
        self.mainform.verb_cb_en.toggled.connect(self.updatechoice)
        self.mainform.cet4_cb_en.toggled.connect(self.updatechoice)
        self.mainform.adv_cb_en.toggled.connect(self.updatechoice)
        self.mainform.posothers_cb_en.toggled.connect(self.updatechoice)
        self.mainform.ky_cb_en.toggled.connect(self.updatechoice)
        self.mainform.frq_slider_en.valueChanged.connect(self.updatechoice)
        self.mainform.collins4_rbtn_en.toggled.connect(self.updatechoice)
        self.mainform.beginrecog_btn_en.clicked.connect(self.updatechoice)
        self.mainform.collins_cb_en.toggled.connect(self.updatechoice)
        self.mainform.collins1_rbtn_en.toggled.connect(self.updatechoice)
        self.mainform.pos_cb_en.toggled.connect(self.updatechoice)
        self.mainform.n_cb_en.toggled.connect(self.updatechoice)
        self.mainform.select_rbtn_en.toggled.connect(self.updatechoice)



    def updatestate(self):
        print('updatestate')

        self.mainform.all_rbtn_en.setChecked(self.choice['all'])
        self.mainform.select_rbtn_en.setChecked(not self.choice['all'])
        self.mainform.tag_cb_en.setCheckable(not self.choice['all'])
        self.mainform.bnc_cb_en.setCheckable(not self.choice['all'])
        self.mainform.frq_cb_en.setCheckable(not self.choice['all'])
        self.mainform.pos_cb_en.setCheckable(not self.choice['all'])
        self.mainform.collins_cb_en.setCheckable(not self.choice['all'])

        self.mainform.tag_cb_en.setCheckState(self.choice['tag'])
        self.mainform.zk_cb_en.setCheckState(self.choice['zk'])
        self.mainform.gk_cb_en.setCheckState(self.choice['gk'])
        self.mainform.cet4_cb_en.setCheckState(self.choice['cet4'])
        self.mainform.ielts_cb_en.setCheckState(self.choice['tag'])
        self.mainform.toefl_cb_en.setCheckState(self.choice['tag'])
        self.mainform.cet6_cb_en.setCheckState(self.choice['cet6'])
        self.mainform.ky_cb_en.setCheckState(self.choice['ky'])
        self.mainform.oxford_cb_en.setCheckState(self.choice['oxford'])

        self.mainform.zk_cb_en.setCheckable(self.choice['tag'])
        self.mainform.gk_cb_en.setCheckable(self.choice['tag'])
        self.mainform.cet4_cb_en.setCheckable(self.choice['tag'])
        self.mainform.ielts_cb_en.setCheckable(self.choice['tag'])
        self.mainform.toefl_cb_en.setCheckable(self.choice['tag'])
        self.mainform.cet6_cb_en.setCheckable(self.choice['tag'])
        self.mainform.ky_cb_en.setCheckable(self.choice['tag'])
        self.mainform.oxford_cb_en.setCheckable(self.choice['tag'])

        self.mainform.bnc_cb_en.setCheckState(self.choice['bnc'])
        self.mainform.frq_cb_en.setCheckState(self.choice['frq'])
        self.mainform.bnc_slider_en.setValue(int(self.choice['bnc_num']))
        self.mainform.frq_slider_en.setValue(int(self.choice['frq_num']))
        self.mainform.bnc_slider_en.setDisabled(self.choice['bnc'])
        self.mainform.frq_slider_en.setDisabled(self.choice['frq'])

        self.mainform.pos_cb_en.setCheckState(self.choice['pos'])
        self.mainform.prep_cb_en.setCheckState(self.choice['prep'])
        self.mainform.adv_cb_en.setCheckState(self.choice['adv'])
        self.mainform.verb_cb_en.setCheckState(self.choice['verb'])
        self.mainform.n_cb_en.setCheckState(self.choice['n'])
        self.mainform.adj_cb_en.setCheckState(self.choice['adj'])
        self.mainform.posothers_cb_en.setCheckState(self.choice['posothers'])
        self.mainform.prep_cb_en.setCheckable(self.choice['pos'])
        self.mainform.adv_cb_en.setCheckable(self.choice['pos'])
        self.mainform.verb_cb_en.setCheckable(self.choice['pos'])
        self.mainform.n_cb_en.setCheckable(self.choice['pos'])
        self.mainform.adj_cb_en.setCheckable(self.choice['pos'])
        self.mainform.posothers_cb_en.setCheckable(self.choice['pos'])

        self.mainform.collins_cb_en.setCheckState(self.choice['collins'])
        if self.choice['collins_num'] == 1:
            self.mainform.collins1_rbtn_en.setChecked(True)
        else:
            self.mainform.collins1_rbtn_en.setChecked(False)
        if self.choice['collins_num'] == 2:
            self.mainform.collins2_rbtn_en.setChecked(True)
        else:
            self.mainform.collins2_rbtn_en.setChecked(False)
        if self.choice['collins_num'] == 3:
            self.mainform.collins3_rbtn_en.setChecked(True)
        else:
            self.mainform.collins3_rbtn_en.setChecked(False)
        if self.choice['collins_num'] == 4:
            self.mainform.collins4_rbtn_en.setChecked(True)
        else:
            self.mainform.collins4_rbtn_en.setChecked(False)
        if self.choice['collins_num'] == 5:
            self.mainform.collins5_rbtn_en.setChecked(True)
        else:
            self.mainform.collins5_rbtn_en.setChecked(False)

        self.mainform.collins1_rbtn_en.setCheckable(self.choice['collins'])
        self.mainform.collins2_rbtn_en.setCheckable(self.choice['collins'])
        self.mainform.collins3_rbtn_en.setCheckable(self.choice['collins'])
        self.mainform.collins4_rbtn_en.setCheckable(self.choice['collins'])
        self.mainform.collins5_rbtn_en.setCheckable(self.choice['collins'])
        if self.haveselected:
            self.mainform.status_label_en.setText(
                '已找到'+str(self.actalnum)+'个单词')


    def updatechoice(self):

        self.choice['all'] = self.mainform.all_rbtn_en.isChecked()
        self.choice['tag'] = self.mainform.tag_cb_en.isChecked()
        self.choice['zk'] = self.mainform.zk_cb_en.isChecked()
        self.choice['gk'] = self.mainform.gk_cb_en.isChecked()
        self.choice['cet4'] = self.mainform.cet4_cb_en.isChecked()
        self.choice['cet6'] = self.mainform.cet6_cb_en.isChecked()
        self.choice['oxford'] = self.mainform.oxford_cb_en.isChecked()
        self.choice['ky'] = self.mainform.ky_cb_en.isChecked()
        self.choice['ielts'] = self.mainform.ielts_cb_en.isChecked()
        self.choice['toefl'] = self.mainform.toefl_cb_en.isChecked()

        self.choice['bnc'] = self.mainform.bnc_cb_en.isChecked()
        num = self.mainform.bnc_tl_en.text()
        if num.isdigit():
            self.choice['bnc_num'] = int(num)
        else:
            self.choice['bnc_num'] = 0

        self.choice['frq'] = self.mainform.frq_cb_en.isChecked()

        num = self.mainform.frq_tl_en.text()
        if num.isdigit():
            self.choice['frq_num'] = int(num)
        else:
            self.choice['frq_num'] = 0

        self.choice['pos'] = self.mainform.pos_cb_en.isChecked()
        self.choice['prep'] = self.mainform.prep_cb_en.isChecked()
        self.choice['adv'] = self.mainform.adv_cb_en.isChecked()
        self.choice['verb'] = self.mainform.verb_cb_en.isChecked()
        self.choice['n'] = self.mainform.n_cb_en.isChecked()
        self.choice['adj'] = self.mainform.adj_cb_en.isChecked()
        self.choice['posothers'] = self.mainform.posothers_cb_en.isChecked()

        self.choicecollins = self.mainform.collins1_rbtn_en.setChecked(self.choice['tag'])
        self.choicecollins_num = self.mainform.collins2_rbtn_en.setChecked(
            self.choice['tag'])

        num = self.mainform.wordcount_tl_en.text()
        if num.isdigit():
            self.wantnum = int(num)
        else:
            self.wantnum = 0

        self.updatestate()

    def updatebnc(self,value):
        self.mainform.bnc_tl_en.setText(str(value))
        self.updatechoice()

    def updatefrq(self,value):
        self.mainform.frq_tl_en.setText(str(value))
        self.updatechoice()
