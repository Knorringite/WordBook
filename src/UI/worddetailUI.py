# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'worddetail.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_worddetailUI(object):
    def setupUi(self, worddetailUI):
        worddetailUI.setObjectName("worddetailUI")
        worddetailUI.resize(800, 600)
        self.detail_tb = QtWidgets.QTextBrowser(worddetailUI)
        self.detail_tb.setGeometry(QtCore.QRect(0, 0, 800, 510))
        self.detail_tb.setObjectName("detail_tb")
        self.next_bt = QtWidgets.QPushButton(worddetailUI)
        self.next_bt.setGeometry(QtCore.QRect(0, 530, 800, 70))
        self.next_bt.setObjectName("next_bt")
        self.word_pb = QtWidgets.QProgressBar(worddetailUI)
        self.word_pb.setGeometry(QtCore.QRect(0, 510, 800, 20))
        self.word_pb.setProperty("value", 24)
        self.word_pb.setObjectName("word_pb")

        self.retranslateUi(worddetailUI)
        self.next_bt.clicked.connect(worddetailUI.next_word)
        QtCore.QMetaObject.connectSlotsByName(worddetailUI)

    def retranslateUi(self, worddetailUI):
        _translate = QtCore.QCoreApplication.translate
        worddetailUI.setWindowTitle(_translate("worddetailUI", "单词详情"))
        self.next_bt.setText(_translate("worddetailUI", "下一个"))

