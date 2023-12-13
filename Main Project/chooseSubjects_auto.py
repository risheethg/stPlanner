# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseSubjects.ui'
#
# Created: Wed Apr  3 18:29:38 2019
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
        Dialog.resize(413, 601)
        self.lw_subjects = QtGui.QListWidget(Dialog)
        self.lw_subjects.setGeometry(QtCore.QRect(40, 30, 331, 481))
        self.lw_subjects.setObjectName(_fromUtf8("lw_subjects"))
        self.pb_select = QtGui.QPushButton(Dialog)
        self.pb_select.setGeometry(QtCore.QRect(60, 540, 93, 28))
        self.pb_select.setObjectName(_fromUtf8("pb_select"))
        self.pb_close = QtGui.QPushButton(Dialog)
        self.pb_close.setGeometry(QtCore.QRect(260, 540, 93, 28))
        self.pb_close.setObjectName(_fromUtf8("pb_close"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pb_select, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.pb_close, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Choose ", None))
        self.pb_select.setText(_translate("Dialog", "Select", None))
        self.pb_close.setText(_translate("Dialog", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

