# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_designer\worddetail.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_worddetail(object):
    def setupUi(self, worddetail):
        worddetail.setObjectName("worddetail")
        worddetail.resize(800, 600)
        self.detail_tb = QtWidgets.QTextBrowser(worddetail)
        self.detail_tb.setGeometry(QtCore.QRect(0, 0, 800, 510))
        self.detail_tb.setObjectName("detail_tb")
        self.next_bt = QtWidgets.QPushButton(worddetail)
        self.next_bt.setGeometry(QtCore.QRect(0, 530, 800, 70))
        self.next_bt.setObjectName("next_bt")
        self.word_pb = QtWidgets.QProgressBar(worddetail)
        self.word_pb.setGeometry(QtCore.QRect(0, 510, 800, 20))
        self.word_pb.setProperty("value", 24)
        self.word_pb.setObjectName("word_pb")

        self.retranslateUi(worddetail)
        QtCore.QMetaObject.connectSlotsByName(worddetail)

    def retranslateUi(self, worddetail):
        _translate = QtCore.QCoreApplication.translate
        worddetail.setWindowTitle(_translate("worddetail", "单词详情"))
        self.next_bt.setText(_translate("worddetail", "下一个"))

