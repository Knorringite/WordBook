from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from src.UI.OptionUI import Ui_Option


class OptionPage(QDialog, Ui_Option):
    setting_signals = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.default_signals = {'is_random': 1, 'word_number': 10, 'is_condition': 0, 'is_tag': 0, 'is_collins': 0,
                                'is_bnc': 0, 'is_frq': 0, 'is_pos': 0, 'is_zk': 0, 'is_gk': 0, 'is_cet4': 0,
                                'is_cet6': 0, 'is_ielts': 0, 'is_toefl': 0, 'is_ky': 0,
                                'is_oxford': 0, 'collins_star': 0, 'bnc_frq': 50, 'frq_frq': 50, 'pos_v': 0, 'pos_n': 0,
                                'pos_prep': 0, 'pos_adj': 0, 'pos_adv': 0, 'pos_other': 0}
        self.change_setting = {}

    def emit_settings(self):
        self.check_settings()
        setting_content = self.change_setting
        self.setting_signals.emit(setting_content)
        self.close()

    def return_main(self):
        self.setting_signals.emit(self.default_signals)
        self.close()

    def check_settings(self):
        if self.select_all_randomly_button.isChecked():
            self.change_setting['is_random'] = 1
        else:
            self.change_setting['is_random'] = 0

        self.change_setting['word_number'] = self.word_number_spin.value()

        if self.select_by_condition_button.isChecked():
            self.change_setting['is_condition'] = 1
        else:
            self.change_setting['is_condition'] = 0

        if self.tag_cb.isChecked():
            self.change_setting['is_tag'] = 1
        else:
            self.change_setting['is_tag'] = 0

        if self.collins_cb.isChecked():
            self.change_setting['is_collins'] = 1
        else:
            self.change_setting['is_collins'] = 0

        if self.bnc_cb.isChecked():
            self.change_setting['is_bnc'] = 1
        else:
            self.change_setting['is_bnc'] = 0

        if self.frq_cb.isChecked():
            self.change_setting['is_frq'] = 1
        else:
            self.change_setting['is_frq'] = 0

        if self.pos_cb.isChecked():
            self.change_setting['is_pos'] = 1
        else:
            self.change_setting['is_pos'] = 0

        if self.zk_cb.isChecked():
            self.change_setting['is_zk'] = 1
        else:
            self.change_setting['is_zk'] = 0

        if self.gk_cb.isChecked():
            self.change_setting['is_gk'] = 1
        else:
            self.change_setting['is_gk'] = 0

        if self.cet4_cb.isChecked():
            self.change_setting['is_cet4'] = 1
        else:
            self.change_setting['is_cet4'] = 0

        if self.cet6_cb.isChecked():
            self.change_setting['is_cet6'] = 1
        else:
            self.change_setting['is_cet6'] = 0

        if self.ielts_cb.isChecked():
            self.change_setting['is_ielts'] = 1
        else:
            self.change_setting['is_ielts'] = 0

        if self.toefl_cb.isChecked():
            self.change_setting['is_toefl'] = 1
        else:
            self.change_setting['is_toefl'] = 0

        if self.ky_cb.isChecked():
            self.change_setting['is_ky'] = 1
        else:
            self.change_setting['is_ky'] = 0

        if self.oxford_cb.isChecked():
            self.change_setting['is_oxford'] = 1
        else:
            self.change_setting['is_oxford'] = 0

        self.change_setting['collins_star'] = 0
        if self.collins1_cb.isChecked():
            self.change_setting['collins_star'] = 1
        if self.collins2_cb.isChecked():
            self.change_setting['collins_star'] = 2
        if self.collins3_cb.isChecked():
            self.change_setting['collins_star'] = 3
        if self.collins4_cb.isChecked():
            self.change_setting['collins_star'] = 4
        if self.collins5_cb.isChecked():
            self.change_setting['collins_star'] = 5

        self.change_setting['bnc_frq'] = self.bnc_spin.value()
        self.change_setting['frq_frq'] = self.frq_spin.value()

        if self.verb_cb.isChecked():
            self.change_setting['pos_v'] = 1
        if self.n_cn.isChecked():
            self.change_setting['pos_n'] = 1
        if self.prep_cb.isChecked():
            self.change_setting['pos_prep'] = 1
        if self.adv_cb.isChecked():
            self.change_setting['pos_adv'] = 1
        if self.adj_cb.isChecked():
            self.change_setting['pos_adj'] = 1
        if self.other_cb.isChecked():
            self.change_setting['pos_other'] = 1
