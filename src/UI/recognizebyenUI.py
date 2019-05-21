# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecognizeByEN.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_recognizebyenUI(object):
    def setupUi(self, recognizebyenUI):
        recognizebyenUI.setObjectName("recognizebyenUI")
        recognizebyenUI.resize(800, 600)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(recognizebyenUI)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.html_table = QtWidgets.QTextBrowser(recognizebyenUI)
        self.html_table.setObjectName("html_table")
        self.verticalLayout_2.addWidget(self.html_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.yes_btn = QtWidgets.QPushButton(recognizebyenUI)
        self.yes_btn.setObjectName("yes_btn")
        self.horizontalLayout.addWidget(self.yes_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.no_button = QtWidgets.QPushButton(recognizebyenUI)
        self.no_button.setObjectName("no_button")
        self.horizontalLayout.addWidget(self.no_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.too_easy_button = QtWidgets.QPushButton(recognizebyenUI)
        self.too_easy_button.setObjectName("too_easy_button")
        self.verticalLayout.addWidget(self.too_easy_button)
        self.play_audio_button = QtWidgets.QPushButton(recognizebyenUI)
        self.play_audio_button.setObjectName("play_audio_button")
        self.verticalLayout.addWidget(self.play_audio_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(recognizebyenUI)
        self.yes_btn.clicked.connect(recognizebyenUI.yes)
        self.no_button.clicked.connect(recognizebyenUI.no)
        self.play_audio_button.clicked.connect(recognizebyenUI.play_audio)
        self.too_easy_button.clicked.connect(recognizebyenUI.too_ez)
        QtCore.QMetaObject.connectSlotsByName(recognizebyenUI)

    def retranslateUi(self, recognizebyenUI):
        _translate = QtCore.QCoreApplication.translate
        recognizebyenUI.setWindowTitle(_translate("recognizebyenUI", "按英文背中文"))
        self.yes_btn.setText(_translate("recognizebyenUI", "认识"))
        self.no_button.setText(_translate("recognizebyenUI", "不认识"))
        self.too_easy_button.setText(_translate("recognizebyenUI", "太简单"))
        self.play_audio_button.setText(_translate("recognizebyenUI", "读音"))

