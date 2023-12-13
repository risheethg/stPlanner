import sys
import os
import sqlite3
from PyQt4 import QtSql
from calendar_auto import *


class MyForm(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    
    def getDate(self):
        date = self.ui.calendarWidget.selectedDate();
        print(date);
        return date;


if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())
