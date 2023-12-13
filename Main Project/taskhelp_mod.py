import sys
import os
import sqlite3
from PyQt4 import QtSql
from taskhelp_auto import *


class MyForm(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #connect to DB
        dbfile = "student_planner.db"
        self.conn = sqlite3.connect(dbfile)

        if os.path.exists(dbfile):
            db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(dbfile)
            db.open()
        else:
            QtGui.QMessageBox.critical(self, "Critical Error", "Database file was not found")
            return None
        print(db.lastError().text())

        self.retrieve()

    def retrieve(self):
        self.model = QtSql.QSqlTableModel(self)
        query = QtSql.QSqlQuery("select task_id, task_name, code_desc from tasks, codes where subject_id = code_id")
        self.model = QtSql.QSqlTableModel(self);
        select = self.model.setQuery(query);
        self.model.select()
        self.ui.tV_data.setModel(self.model);
        
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Task Id");
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Task Name");
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Subject");

    def getTaskId(self):
        index = self.ui.tV_data.currentIndex();
        ide  = self.ui.tV_data.model().data(index);
        print(index, ide);
        if str(ide).isdigit():
            print(str(ide))
            return ide;
      
if __name__   == "__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())
