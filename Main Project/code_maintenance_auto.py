# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'code_maintenance.ui'
#
# Created: Wed Mar 20 18:53:47 2019
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
        Dialog.resize(661, 614)
        self.pb_add = QtGui.QPushButton(Dialog)
        self.pb_add.setGeometry(QtCore.QRect(50, 510, 93, 71))
        self.pb_add.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pb_add.setObjectName(_fromUtf8("pb_add"))
        self.pb_retrieve = QtGui.QPushButton(Dialog)
        self.pb_retrieve.setGeometry(QtCore.QRect(200, 510, 93, 71))
        self.pb_retrieve.setObjectName(_fromUtf8("pb_retrieve"))
        self.pb_save = QtGui.QPushButton(Dialog)
        self.pb_save.setGeometry(QtCore.QRect(360, 510, 93, 71))
        self.pb_save.setObjectName(_fromUtf8("pb_save"))
        self.pb_close = QtGui.QPushButton(Dialog)
        self.pb_close.setGeometry(QtCore.QRect(520, 510, 93, 71))
        self.pb_close.setObjectName(_fromUtf8("pb_close"))
        self.tb_data = QtGui.QTableView(Dialog)
        self.tb_data.setGeometry(QtCore.QRect(40, 50, 581, 441))
        self.tb_data.setObjectName(_fromUtf8("tb_data"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pb_close, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pb_add.setText(_translate("Dialog", "Add", None))
        self.pb_retrieve.setText(_translate("Dialog", "Retrieve", None))
        self.pb_save.setText(_translate("Dialog", "Save", None))
        self.pb_close.setText(_translate("Dialog", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

