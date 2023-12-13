# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScheduleTasks.ui'
#
# Created: Wed Apr 10 18:39:21 2019
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
        Dialog.resize(502, 338)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 80, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 53, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.dE_startDate = QtGui.QDateEdit(Dialog)
        self.dE_startDate.setGeometry(QtCore.QRect(190, 71, 131, 41))
        self.dE_startDate.setObjectName(_fromUtf8("dE_startDate"))
        self.dE_endDate = QtGui.QDateEdit(Dialog)
        self.dE_endDate.setGeometry(QtCore.QRect(190, 120, 131, 41))
        self.dE_endDate.setObjectName(_fromUtf8("dE_endDate"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 180, 53, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lE_task = QtGui.QLineEdit(Dialog)
        self.lE_task.setGeometry(QtCore.QRect(170, 180, 171, 22))
        self.lE_task.setObjectName(_fromUtf8("lE_task"))
        self.pb_save = QtGui.QPushButton(Dialog)
        self.pb_save.setGeometry(QtCore.QRect(200, 250, 93, 28))
        self.pb_save.setObjectName(_fromUtf8("pb_save"))
        self.pb_moreSD = QtGui.QPushButton(Dialog)
        self.pb_moreSD.setGeometry(QtCore.QRect(360, 70, 61, 28))
        self.pb_moreSD.setObjectName(_fromUtf8("pb_moreSD"))
        self.pb_moreED = QtGui.QPushButton(Dialog)
        self.pb_moreED.setGeometry(QtCore.QRect(360, 120, 61, 28))
        self.pb_moreED.setObjectName(_fromUtf8("pb_moreED"))
        self.pb_moreTasks = QtGui.QPushButton(Dialog)
        self.pb_moreTasks.setGeometry(QtCore.QRect(360, 180, 61, 28))
        self.pb_moreTasks.setObjectName(_fromUtf8("pb_moreTasks"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Schedule Tasks", None))
        self.label.setText(_translate("Dialog", "Start Date", None))
        self.label_2.setText(_translate("Dialog", "End Date", None))
        self.label_3.setText(_translate("Dialog", "Task ", None))
        self.pb_save.setText(_translate("Dialog", "Save", None))
        self.pb_moreSD.setText(_translate("Dialog", "...", None))
        self.pb_moreED.setText(_translate("Dialog", "...", None))
        self.pb_moreTasks.setText(_translate("Dialog", "...", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

