# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecognizeByCH.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_recognizebychUI(object):
    def setupUi(self, recognizebychUI):
        recognizebychUI.setObjectName("recognizebychUI")
        recognizebychUI.resize(800, 600)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(recognizebychUI)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.html_table = QtWidgets.QTextBrowser(recognizebychUI)
        self.html_table.setObjectName("html_table")
        self.verticalLayout_2.addWidget(self.html_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.yes_btn = QtWidgets.QPushButton(recognizebychUI)
        self.yes_btn.setObjectName("yes_btn")
        self.horizontalLayout.addWidget(self.yes_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.no_button = QtWidgets.QPushButton(recognizebychUI)
        self.no_button.setObjectName("no_button")
        self.horizontalLayout.addWidget(self.no_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.too_easy_button = QtWidgets.QPushButton(recognizebychUI)
        self.too_easy_button.setObjectName("too_easy_button")
        self.verticalLayout.addWidget(self.too_easy_button)
        self.play_audio_button = QtWidgets.QPushButton(recognizebychUI)
        self.play_audio_button.setObjectName("play_audio_button")
        self.verticalLayout.addWidget(self.play_audio_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(recognizebychUI)
        self.yes_btn.clicked.connect(recognizebychUI.yes)
        self.no_button.clicked.connect(recognizebychUI.no)
        self.play_audio_button.clicked.connect(recognizebychUI.play_audio)
        self.too_easy_button.clicked.connect(recognizebychUI.too_ez)
        QtCore.QMetaObject.connectSlotsByName(recognizebychUI)

    def retranslateUi(self, recognizebychUI):
        _translate = QtCore.QCoreApplication.translate
        recognizebychUI.setWindowTitle(_translate("recognizebychUI", "按中文背英文"))
        self.yes_btn.setText(_translate("recognizebychUI", "认识"))
        self.no_button.setText(_translate("recognizebychUI", "不认识"))
        self.too_easy_button.setText(_translate("recognizebychUI", "太简单"))
        self.play_audio_button.setText(_translate("recognizebychUI", "读音"))

