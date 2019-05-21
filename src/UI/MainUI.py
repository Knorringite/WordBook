# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 600)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Main)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(50, 5, 50, 5)
        self.verticalLayout_3.setSpacing(50)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.setting_button = QtWidgets.QPushButton(Main)
        self.setting_button.setObjectName("setting_button")
        self.horizontalLayout_2.addWidget(self.setting_button)
        spacerItem = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(50)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.word_status_label = QtWidgets.QLabel(Main)
        self.word_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.word_status_label.setObjectName("word_status_label")
        self.verticalLayout_2.addWidget(self.word_status_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.remember_by_ch_button = QtWidgets.QPushButton(Main)
        self.remember_by_ch_button.setObjectName("remember_by_ch_button")
        self.horizontalLayout.addWidget(self.remember_by_ch_button)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.remember_by_en_button = QtWidgets.QPushButton(Main)
        self.remember_by_en_button.setObjectName("remember_by_en_button")
        self.horizontalLayout.addWidget(self.remember_by_en_button)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.update_state_button = QtWidgets.QPushButton(Main)
        self.update_state_button.setObjectName("update_state_button")
        self.horizontalLayout_4.addWidget(self.update_state_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.version_label = QtWidgets.QLabel(Main)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.version_label.setFont(font)
        self.version_label.setObjectName("version_label")
        self.horizontalLayout_3.addWidget(self.version_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 30)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.retranslateUi(Main)
        self.remember_by_ch_button.clicked.connect(Main.turn_to_remember_by_en_page)
        self.remember_by_en_button.clicked.connect(Main.turn_to_remember_by_ch_page)
        self.setting_button.clicked.connect(Main.turn_to_option_page)
        self.update_state_button.clicked.connect(Main.update_state)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "WordBook"))
        self.setting_button.setText(_translate("Main", "设置"))
        self.word_status_label.setText(_translate("Main", "#单词掌握情况"))
        self.remember_by_ch_button.setText(_translate("Main", "看英文背中文"))
        self.remember_by_en_button.setText(_translate("Main", "看中文背英文"))
        self.update_state_button.setText(_translate("Main", "刷新背单词情况"))
        self.version_label.setText(_translate("Main", "test version"))
