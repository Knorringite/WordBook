from src.UI.chooseclassUI import Ui_ChooseClass
import pickle


class ChooseClassEn_form(QtWidgets.QWidget, Ui_ChooseClass):
    def __init__(self, dict_en ,mainform):
        super().__init__()
        self.setupUi(self)
        self.choice = pickle.load('./DICT/choice_en.pkl')
        if self.choice is None:
            self.choice.all = True
            self.choice.tag = False
            self.choice.zk = False
            self.choice.gk = False
            self.choice.cet4 = False
            self.choice.cet6 = False
            self.choice.ky = False
            self.choice.toefl = False
            self.choice.ielts = False
            self.choice.oxford = False
            self.choice.bnc = False
            self.choice.frq = False
            self.choice.pos = False
            self.choice.pos_v = False
            self.choice.pos_n = False
            self.choice.pos_prep = False
            self.choice.pos_adj = False
            self.choice.pos_adv = False
            self.choice.collins = False
            self.choice.collins_num = 0
            self.choice.bnc_num = 0
            self.choice.frq_num = 0
        self.haveselected = False
        self.wantnum = 100
        self.actalnum = 0
        self.bnc_slider.setRange(0, 100000)
        self.frq_slider.setRange(0, 100000)
        self.ok_btn.clicked.connect(mainform.choose2remember_en)
        self.back_btn.clicked.connect(mainform.choose2main_en)

    def updatestate(self):
        self.all_rbtn.setChecked(self.choice.all)
        self.select_rbtn.setChecked(not self.choice.all)
        self.tag_cb.setCheckable(not self.choice.all)
        self.bnc_cb.setCheckable(not self.choice.all)
        self.frq_cb.setCheckable(not self.choice.all)
        self.pos_cb.setCheckable(not self.choice.all)
        self.collins_cb.setCheckable(not self.choice.all)

        self.tag_cb.setCheckState(self.choice.tag)
        self.zk_cb.setCheckState(self.choice.zk)
        self.gk_cb.setCheckState(self.choice.gk)
        self.cet4_cb.setCheckState(self.choice.cet4)
        self.ielts_cb.setCheckState(self.choice.tag)
        self.toefl_cb.setCheckState(self.choice.tag)
        self.cet6_cb.setCheckState(self.choice.cet6)
        self.ky_cb.setCheckState(self.choice.ky)
        self.oxford_cb.setCheckState(self.choice.oxford)

        self.zk_cb.setCheckable(self.choice.tag)
        self.gk_cb.setCheckable(self.choice.tag)
        self.cet4_cb.setCheckable(self.choice.tag)
        self.ielts_cb.setCheckable(self.choice.tag)
        self.toefl_cb.setCheckable(self.choice.tag)
        self.cet6_cb.setCheckable(self.choice.tag)
        self.ky_cb.setCheckable(self.choice.tag)
        self.oxford_cb.setCheckable(self.choice.tag)

        self.bnc_cb.setCheckState(self.choice.bnc)
        self.frq_cb.setCheckState(self.choice.frq)
        self.bnc_slider.setValue(self.choice.bnc_num)
        self.frq_slider.setValue(self.choice.frq_num)
        self.bnc_slider.setDisabled(self.choice.bnc)
        self.frq_slider.setDisabled(self.choice.frq)

        self.pos_cb.setCheckState(self.choice.pos)
        self.prep_cb.setCheckState(self.choice.prep)
        self.adv_cb.setCheckState(self.choice.adv)
        self.verb_cb.setCheckState(self.choice.verb)
        self.n_cb.setCheckState(self.choice.n)
        self.adj_cb.setCheckState(self.choice.adj)
        self.posothers_cb.setCheckState(self.choice.posothers)
        self.prep_cb.setCheckable(self.choice.pos)
        self.adv_cb.setCheckable(self.choice.pos)
        self.verb_cb.setCheckable(self.choice.pos)
        self.n_cb.setCheckable(self.choice.pos)
        self.adj_cb.setCheckable(self.choice.pos)
        self.posothers_cb.setCheckable(self.choice.pos)

        self.collins_cb.setCheckState(self.choice.collins)
        if self.choice.collins_num == 1:
            self.collins1_rbtn.setCheckState(True)
        else:
            self.collins1_rbtn.setCheckState(False)
        if self.choice.collins_num == 2:
            self.collins2_rbtn.setCheckState(True)
        else:
            self.collins2_rbtn.setCheckState(False)
        if self.choice.collins_num == 3:
            self.collins3_rbtn.setCheckState(True)
        else:
            self.collins3_rbtn.setCheckState(False)
        if self.choice.collins_num == 4:
            self.collins4_rbtn.setCheckState(True)
        else:
            self.collins4_rbtn.setCheckState(False)
        if self.choice.collins_num == 5:
            self.collins5_rbtn.setCheckState(True)
        else:
            self.collins5_rbtn.setCheckState(False)

        self.collins1_rbtn.setCheckable(self.choice.collins)
        self.collins2_rbtn.setCheckable(self.choice.collins)
        self.collins3_rbtn.setCheckable(self.choice.collins)
        self.collins4_rbtn.setCheckable(self.choice.collins)
        self.collins5_rbtn.setCheckable(self.choice.collins)
        if self.haveselected:
            self.status_label.setText('已找到'+str(self.actalnum)+'个单词')


    def updatechoice(self):
        self.choice.all = self.all_rbtn().isChecked()
        self.choice.tag = self.tag_cb.isChecked()
        self.choice.zk = self.zk_cb.isChecked()
        self.choice.gk = self.gk_cb.isChecked()
        self.choice.cet4 = self.cet4_cb.isChecked()
        self.choice.cet6 = self.cet6_cb.isChecked()
        self.choice.oxford = self.oxford_cb.isChecked()
        self.choice.ky = self.ky_cb.isChecked()
        self.choice.ielts = self.ielts_cb.isChecked()
        self.choice.toefl = self.toefl_cb.isChecked()

        self.choice.bnc = self.bnc_cb.isChecked()
        self.choice.bnc_num = self.bnc_tl.text()

        self.choice.frq = self.frq_cb.isChecked()
        self.choice.frq_num = self.frq_tl.text()

        self.choice.pos = self.pos_cb.isChecked()
        self.choice.prep = self.prep_cb.isChecked()
        self.choice.adv = self.adv_cb.isChecked()
        self.choice.verb = self.verb_cb.isChecked()
        self.choice.n = self.n_cb.isChecked()
        self.choice.adj = self.adj_cb.isChecked()
        self.choice.posothers = self.posothers_cb.isChecked()

        self.choice.collins = self.collins1_rbtn.setCheckState(self.choice.tag)
        self.choice.collins_num = self.collins2_rbtn.setCheckState(self.choice.tag)

        self.wantnum = self.wordcount_tl.text()

        self.updatestate()

    def updatebnc(self,value):
        self.bnc_tl.setText(str(value))
        self.updatechoice()

    def updatefrq(self,value):
        self.frq_tl.setText(str(value))
        self.updatechoice()
