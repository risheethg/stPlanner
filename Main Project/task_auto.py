# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task.ui'
#
# Created: Wed Apr 10 18:39:44 2019
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
        Dialog.resize(665, 615)
        self.tV_data = QtGui.QTableView(Dialog)
        self.tV_data.setGeometry(QtCore.QRect(30, 30, 601, 471))
        self.tV_data.setObjectName(_fromUtf8("tV_data"))
        self.pb_addrow = QtGui.QPushButton(Dialog)
        self.pb_addrow.setGeometry(QtCore.QRect(40, 550, 93, 28))
        self.pb_addrow.setObjectName(_fromUtf8("pb_addrow"))
        self.pb_save = QtGui.QPushButton(Dialog)
        self.pb_save.setGeometry(QtCore.QRect(150, 550, 93, 28))
        self.pb_save.setObjectName(_fromUtf8("pb_save"))
        self.pb_teacher = QtGui.QPushButton(Dialog)
        self.pb_teacher.setGeometry(QtCore.QRect(390, 550, 101, 28))
        self.pb_teacher.setObjectName(_fromUtf8("pb_teacher"))
        self.pb_subbject = QtGui.QPushButton(Dialog)
        self.pb_subbject.setGeometry(QtCore.QRect(270, 550, 101, 28))
        self.pb_subbject.setObjectName(_fromUtf8("pb_subbject"))
        self.pb_close = QtGui.QPushButton(Dialog)
        self.pb_close.setGeometry(QtCore.QRect(520, 550, 93, 28))
        self.pb_close.setObjectName(_fromUtf8("pb_close"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pb_close, QtCore.SIGNAL(_fromUtf8("pressed()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "tasks", None))
        self.pb_addrow.setText(_translate("Dialog", "Add Row", None))
        self.pb_save.setText(_translate("Dialog", "Save", None))
        self.pb_teacher.setText(_translate("Dialog", "Choose Teacher", None))
        self.pb_subbject.setText(_translate("Dialog", "Choose Subject", None))
        self.pb_close.setText(_translate("Dialog", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

