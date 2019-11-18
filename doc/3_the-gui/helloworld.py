# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './helloworld.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(325, 223)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnOK = QtGui.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(110, 130, 90, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnOK.setFont(font)
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.lblMsg = QtGui.QLabel(self.centralwidget)
        self.lblMsg.setGeometry(QtCore.QRect(20, 30, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lblMsg.setFont(font)
        self.lblMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMsg.setObjectName(_fromUtf8("lblMsg"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnOK.setText(_translate("MainWindow", "OK", None))
        self.lblMsg.setText(_translate("MainWindow", "Hello World", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

