import sys
import os
import sqlite3
from PyQt4 import QtSql
from comptasks_auto import *

class MyForm(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        dbfile = "student_planner.db"
        self.conn = sqlite3.connect(dbfile)

        #connect to DB
        self.conn = sqlite3.connect("student_planner.db");

        if os.path.exists("student_planner.db"):
            db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName("student_planner.db")
            db.open()
        else:
            QtGui.QMessageBox.critical(self, "Critical Error", "Database file was not found")
            return None
        print(db.lastError().text())

        self.retrieve()


    def retrieve(self):
        self.model = QtSql.QSqlTableModel(self)
        query = QtSql.QSqlQuery("select task_id, start_date, end_date, cmpltchck from schedule where cmpltchck == 'C'")
        self.model = QtSql.QSqlTableModel(self);
        select = self.model.setQuery(query);
        self.model.select()
        self.ui.tV_data.setModel(self.model);
        
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Task Id");
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Start Date");
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "End Date");
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Status");

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())
