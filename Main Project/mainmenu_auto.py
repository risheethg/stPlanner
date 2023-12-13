# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created: Wed Apr 10 19:55:43 2019
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 160, 481, 141))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuTransactions = QtGui.QMenu(self.menubar)
        self.menuTransactions.setObjectName(_fromUtf8("menuTransactions"))
        self.menuReport = QtGui.QMenu(self.menubar)
        self.menuReport.setObjectName(_fromUtf8("menuReport"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionCode_Maintenance = QtGui.QAction(MainWindow)
        self.actionCode_Maintenance.setObjectName(_fromUtf8("actionCode_Maintenance"))
        self.actionTasks = QtGui.QAction(MainWindow)
        self.actionTasks.setObjectName(_fromUtf8("actionTasks"))
        self.actionPending_Tasks = QtGui.QAction(MainWindow)
        self.actionPending_Tasks.setObjectName(_fromUtf8("actionPending_Tasks"))
        self.actionScheduling = QtGui.QAction(MainWindow)
        self.actionScheduling.setObjectName(_fromUtf8("actionScheduling"))
        self.actionCompleted_Tasks = QtGui.QAction(MainWindow)
        self.actionCompleted_Tasks.setObjectName(_fromUtf8("actionCompleted_Tasks"))
        self.menuFile.addAction(self.actionCode_Maintenance)
        self.menuFile.addAction(self.actionTasks)
        self.menuTransactions.addAction(self.actionPending_Tasks)
        self.menuTransactions.addAction(self.actionScheduling)
        self.menuReport.addAction(self.actionCompleted_Tasks)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTransactions.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Student Planner", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuTransactions.setTitle(_translate("MainWindow", "Transactions", None))
        self.menuReport.setTitle(_translate("MainWindow", "Report", None))
        self.actionCode_Maintenance.setText(_translate("MainWindow", "Code Maintenance", None))
        self.actionTasks.setText(_translate("MainWindow", "Tasks", None))
        self.actionPending_Tasks.setText(_translate("MainWindow", "Pending Tasks", None))
        self.actionScheduling.setText(_translate("MainWindow", "Scheduling", None))
        self.actionCompleted_Tasks.setText(_translate("MainWindow", "Completed Tasks", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

