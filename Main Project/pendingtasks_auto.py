# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pendingtasks.ui'
#
# Created: Wed Apr 24 18:57:33 2019
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(520, 588)
        self.tV_data = QtGui.QTableView(Dialog)
        self.tV_data.setGeometry(QtCore.QRect(20, 20, 481, 451))
        self.tV_data.setObjectName(_fromUtf8("tV_data"))
        self.pb_comptask = QtGui.QPushButton(Dialog)
        self.pb_comptask.setGeometry(QtCore.QRect(80, 490, 93, 71))
        self.pb_comptask.setObjectName(_fromUtf8("pb_comptask"))
        self.pb_OK_2 = QtGui.QPushButton(Dialog)
        self.pb_OK_2.setGeometry(QtCore.QRect(340, 490, 93, 71))
        self.pb_OK_2.setObjectName(_fromUtf8("pb_OK_2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pb_OK_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Pending Tasks", None))
        self.pb_comptask.setText(_translate("Dialog", "Complete Task", None))
        self.pb_OK_2.setText(_translate("Dialog", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

