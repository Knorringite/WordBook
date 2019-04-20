# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_designer\recognizebyen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_recognizebyenUI(object):
    def setupUi(self, recognizebyenUI):
        recognizebyenUI.setObjectName("recognizebyenUI")
        recognizebyenUI.resize(800, 600)
        self.ok_btn = QtWidgets.QPushButton(recognizebyenUI)
        self.ok_btn.setGeometry(QtCore.QRect(30, 480, 330, 90))
        self.ok_btn.setObjectName("ok_btn")
        self.no_btn = QtWidgets.QPushButton(recognizebyenUI)
        self.no_btn.setGeometry(QtCore.QRect(370, 480, 330, 90))
        self.no_btn.setObjectName("no_btn")
        self.tooeasy_btn = QtWidgets.QPushButton(recognizebyenUI)
        self.tooeasy_btn.setGeometry(QtCore.QRect(710, 20, 75, 61))
        self.tooeasy_btn.setObjectName("tooeasy_btn")
        self.html_tb = QtWidgets.QTextBrowser(recognizebyenUI)
        self.html_tb.setGeometry(QtCore.QRect(30, 20, 670, 460))
        self.html_tb.setObjectName("html_tb")
        self.playaudio_btn = QtWidgets.QPushButton(recognizebyenUI)
        self.playaudio_btn.setGeometry(QtCore.QRect(710, 120, 75, 171))
        self.playaudio_btn.setObjectName("playaudio_btn")

        self.retranslateUi(recognizebyenUI)
        QtCore.QMetaObject.connectSlotsByName(recognizebyenUI)

    def retranslateUi(self, recognizebyenUI):
        _translate = QtCore.QCoreApplication.translate
        recognizebyenUI.setWindowTitle(_translate("recognizebyenUI", "按英文背中文"))
        self.ok_btn.setText(_translate("recognizebyenUI", "认识"))
        self.no_btn.setText(_translate("recognizebyenUI", "不认识"))
        self.tooeasy_btn.setText(_translate("recognizebyenUI", "太简单"))
        self.playaudio_btn.setText(_translate("recognizebyenUI", "读音"))

