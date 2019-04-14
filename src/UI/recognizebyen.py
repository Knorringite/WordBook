# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_designer\recognizebyen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_recognizebyen_form(object):
    def setupUi(self, recognizebyen_form):
        recognizebyen_form.setObjectName("recognizebyen_form")
        recognizebyen_form.resize(800, 600)
        self.word_label = QtWidgets.QLabel(recognizebyen_form)
        self.word_label.setGeometry(QtCore.QRect(100, 50, 600, 70))
        self.word_label.setText("")
        self.word_label.setObjectName("word_label")
        self.ok_btn = QtWidgets.QPushButton(recognizebyen_form)
        self.ok_btn.setGeometry(QtCore.QRect(100, 460, 301, 91))
        self.ok_btn.setObjectName("ok_btn")
        self.no_btn = QtWidgets.QPushButton(recognizebyen_form)
        self.no_btn.setGeometry(QtCore.QRect(400, 460, 301, 91))
        self.no_btn.setObjectName("no_btn")
        self.tooeasy_btn = QtWidgets.QPushButton(recognizebyen_form)
        self.tooeasy_btn.setGeometry(QtCore.QRect(710, 70, 75, 23))
        self.tooeasy_btn.setObjectName("tooeasy_btn")
        self.tips_tb = QtWidgets.QTextBrowser(recognizebyen_form)
        self.tips_tb.setGeometry(QtCore.QRect(100, 120, 600, 341))
        self.tips_tb.setObjectName("tips_tb")
        self.playaudio_btn = QtWidgets.QPushButton(recognizebyen_form)
        self.playaudio_btn.setGeometry(QtCore.QRect(710, 120, 75, 171))
        self.playaudio_btn.setObjectName("playaudio_btn")

        self.retranslateUi(recognizebyen_form)
        QtCore.QMetaObject.connectSlotsByName(recognizebyen_form)

    def retranslateUi(self, recognizebyen_form):
        _translate = QtCore.QCoreApplication.translate
        recognizebyen_form.setWindowTitle(_translate("recognizebyen_form", "按英文背中文"))
        self.ok_btn.setText(_translate("recognizebyen_form", "认识"))
        self.no_btn.setText(_translate("recognizebyen_form", "不认识"))
        self.tooeasy_btn.setText(_translate("recognizebyen_form", "太简单"))
        self.playaudio_btn.setText(_translate("recognizebyen_form", "读音"))

