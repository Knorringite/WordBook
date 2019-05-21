# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from src.UI import recognizebychUI
from src.UI import recognizebyenUI

class Ui_WordBook_mainform(object):
    def setupUi(self, WordBook_mainform):
        WordBook_mainform.setObjectName("WordBook_mainform")
        WordBook_mainform.resize(800, 600)
        self.AddWord_btn = QtWidgets.QPushButton(WordBook_mainform)
        self.AddWord_btn.setGeometry(QtCore.QRect(80, 470, 640, 60))
        self.AddWord_btn.setObjectName("AddWord_btn")
        self.RemEn_btn = QtWidgets.QPushButton(WordBook_mainform)
        self.RemEn_btn.setGeometry(QtCore.QRect(80, 240, 300, 200))
        self.RemEn_btn.setObjectName("RemEn_btn")
        self.RemZh_btn = QtWidgets.QPushButton(WordBook_mainform)
        self.RemZh_btn.setGeometry(QtCore.QRect(420, 240, 300, 200))
        self.RemZh_btn.setObjectName("RemZh_btn")
        self.Version_label = QtWidgets.QLabel(WordBook_mainform)
        self.Version_label.setGeometry(QtCore.QRect(730, 580, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Version_label.setFont(font)
        self.Version_label.setObjectName("Version_label")
        self.WordStatus_label = QtWidgets.QLabel(WordBook_mainform)
        self.WordStatus_label.setGeometry(QtCore.QRect(80, 110, 641, 61))
        self.WordStatus_label.setObjectName("WordStatus_label")
        self.Setting_btn = QtWidgets.QPushButton(WordBook_mainform)
        self.Setting_btn.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.Setting_btn.setObjectName("Setting_btn")

        self.retranslateUi(WordBook_mainform)
        self.RemEn_btn.clicked.connect(WordBook_mainform.showRecognitionbychUI)
        QtCore.QMetaObject.connectSlotsByName(WordBook_mainform)

    def retranslateUi(self, WordBook_mainform):
        _translate = QtCore.QCoreApplication.translate
        WordBook_mainform.setWindowTitle(_translate("WordBook_mainform", "WordBook"))
        self.AddWord_btn.setText(_translate("WordBook_mainform", "添加单词"))
        self.RemEn_btn.setText(_translate("WordBook_mainform", "中文背英文"))
        self.RemZh_btn.setText(_translate("WordBook_mainform", "英文背中文"))
        self.Version_label.setText(_translate("WordBook_mainform", "test version"))
        self.WordStatus_label.setText(_translate("WordBook_mainform", "#单词掌握情况"))
        self.Setting_btn.setText(_translate("WordBook_mainform", "设置"))

