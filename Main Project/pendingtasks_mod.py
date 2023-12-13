import sys
import os
import sqlite3
from PyQt4 import QtSql
from pendingtasks_auto import *

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
        
        #event handler
        self.ui.pb_comptask.clicked.connect(self.compTask);

        self.retrieve()

##        #opening message
##        w = QtGui.QWidget()
##        QtGui.QMessageBox.information(w, "", "Choose The Task ID");

    def retrieve(self):
        self.model = QtSql.QSqlTableModel(self)
        query = QtSql.QSqlQuery("select task_id, start_date, end_date, cmpltchck from schedule where cmpltchck == 'N'")
        self.model = QtSql.QSqlTableModel(self);
        select = self.model.setQuery(query);
        self.model.select()
        self.ui.tV_data.setModel(self.model);
        
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Task Id");
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Start Date");
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "End Date");
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Status");

    def compTask(self):
        try:
            cursor = self.conn.cursor();
            tID = self.ui.tV_data.currentIndex();
            ide = self.ui.tV_data.model().data(tID);
            if(str(ide).isdigit() == True):
                cursor.execute("UPDATE schedule set cmpltchck = 'C' where task_id == " + str(ide));
                w = QtGui.QWidget()
                QtGui.QMessageBox.information(w, "Task Completed!", "Task Completed!");
                print("Task Completed!")
            else:
                w = QtGui.QWidget()
                QtGui.QMessageBox.information(w, "Error!", "Choose The Task ID");
                
        except sqlite3.Error as e:
            w = QtGui.QWidget();
            QtGui.QMessageBox.information(w, "An Error Occured!:", e.args[0]);    
        self.conn.commit()
        self.retrieve();
        
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())
