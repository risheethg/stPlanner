import sys
import os
import sqlite3
from PyQt4 import QtSql
from code_maintenance_auto import *

class MyForm(QtGui.QDialog):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self);
        dbfile = "student_planner.db"
        self.conn = sqlite3.connect("student_planner.db")

        self.ui.pb_retrieve.clicked.connect(self.openRetrieve)
        self.ui.pb_save.clicked.connect(self.save)
        self.ui.pb_add.clicked.connect(self.add);
        


        if os.path.exists(dbfile):
            db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName(dbfile)
            db.open();

        else:
            QtGui.QMessageBox.critical(self, "Critical Error", "Database file was not located.")
            return None;

        self.openRetrieve();
   
     
    

    def openRetrieve(self):
        self.model = QtSql.QSqlTableModel(self);
        self.model.setTable("codes");
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select();
        self.ui.tb_data.setModel(self.model);
        
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Description");
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Type");
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Code ID");

    def save(self):
        print("Hello")
        self.model.submitAll()
        self.model.select()
        self.ui.tb_data.setModel(self.model);

    def add(self):
        self.model.insertRows(self.model.rowCount(), 1)
        

if __name__=="__main__":
 app=QtGui.QApplication(sys.argv)
 myapp=MyForm()
 myapp.show()
 sys.exit(app.exec_())
