import sys
from PyQt5 import QtWidgets, QtCore
from src.MainPage import WordBook

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = WordBook()
    Window.show()
    sys.exit(app.exec_())
