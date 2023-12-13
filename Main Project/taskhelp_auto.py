# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskhelp.ui'
#
# Created: Wed Apr 10 19:07:20 2019
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
        Dialog.resize(757, 543)
        self.tV_data = QtGui.QTableView(Dialog)
        self.tV_data.setGeometry(QtCore.QRect(50, 30, 651, 401))
        self.tV_data.setObjectName(_fromUtf8("tV_data"))
        self.pb_ok = QtGui.QPushButton(Dialog)
        self.pb_ok.setGeometry(QtCore.QRect(158, 450, 211, 71))
        self.pb_ok.setObjectName(_fromUtf8("pb_ok"))
        self.pb_cancel = QtGui.QPushButton(Dialog)
        self.pb_cancel.setGeometry(QtCore.QRect(390, 450, 211, 71))
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pb_ok, QtCore.SIGNAL(_fromUtf8("pressed()")), Dialog.accept)
        QtCore.QObject.connect(self.pb_cancel, QtCore.SIGNAL(_fromUtf8("pressed()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Task Help", None))
        self.pb_ok.setText(_translate("Dialog", "Ok", None))
        self.pb_cancel.setText(_translate("Dialog", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

