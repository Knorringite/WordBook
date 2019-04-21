# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_designer\recognizebyen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_recognizebyen(object):
    def setupUi(self, recognizebyen):
        recognizebyen.setObjectName("recognizebyen")
        recognizebyen.resize(800, 600)
        self.ok_btn = QtWidgets.QPushButton(recognizebyen)
        self.ok_btn.setGeometry(QtCore.QRect(30, 480, 330, 90))
        self.ok_btn.setObjectName("ok_btn")
        self.no_btn = QtWidgets.QPushButton(recognizebyen)
        self.no_btn.setGeometry(QtCore.QRect(370, 480, 330, 90))
        self.no_btn.setObjectName("no_btn")
        self.tooeasy_btn = QtWidgets.QPushButton(recognizebyen)
        self.tooeasy_btn.setGeometry(QtCore.QRect(710, 20, 75, 61))
        self.tooeasy_btn.setObjectName("tooeasy_btn")
        self.html_tb = QtWidgets.QTextBrowser(recognizebyen)
        self.html_tb.setGeometry(QtCore.QRect(30, 20, 670, 460))
        self.html_tb.setObjectName("html_tb")
        self.playaudio_btn = QtWidgets.QPushButton(recognizebyen)
        self.playaudio_btn.setGeometry(QtCore.QRect(710, 120, 75, 171))
        self.playaudio_btn.setObjectName("playaudio_btn")

        self.retranslateUi(recognizebyen)
        QtCore.QMetaObject.connectSlotsByName(recognizebyen)

    def retranslateUi(self, recognizebyen):
        _translate = QtCore.QCoreApplication.translate
        recognizebyen.setWindowTitle(_translate("recognizebyen", "按英文背中文"))
        self.ok_btn.setText(_translate("recognizebyen", "认识"))
        self.no_btn.setText(_translate("recognizebyen", "不认识"))
        self.tooeasy_btn.setText(_translate("recognizebyen", "太简单"))
        self.playaudio_btn.setText(_translate("recognizebyen", "读音"))

