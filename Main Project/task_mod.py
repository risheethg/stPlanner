import sys
import os
import sqlite3
from PyQt4 import QtSql
import chooseSubject_mod  
import chooseTeacher_mod  
from task_auto import *

class MyForm(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        dbfile = "student_planner.db"
        self.conn = sqlite3.connect(dbfile)
        
        #this is where we will bind the event handlers

        self.ui.pb_save.clicked.connect(self.save);
        self.ui.pb_addrow.clicked.connect(self.addrow);
        self.ui.pb_teacher.clicked.connect(self.cTeacher);
        self.ui.pb_subbject.clicked.connect(self.cSubject);

        if os.path.exists(dbfile):
            db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(dbfile)
            db.open()
        else:
            QtGui.QMessageBox.critical(self, "Critical Error", "Database file was not found")
            return None
        print(db.lastError().text())


        self.retrieve()
#This is where we will insert the functions (defs)
    def retrieve(self):
        self.model=QtSql.QSqlTableModel(self);
        self.model.setTable("tasks");
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit);
        self.model.select();
        self.ui.tV_data.setModel(self.model);

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Task Id");
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Task Name");
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Subject");
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Assigned By:");
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Importance No.");

    def save(self):
        self.model.submitAll()
        self.model.select()
        self.ui.tV_data.setModel(self.model)

    def addrow(self):
        self.model.insertRows(self.model.rowCount(), 1);

    def cTeacher(self):
        teacher = chooseTeacher_mod.MyForm(self);
        result = teacher.exec_();
        print(result);
        if(result == 1):
            selTeach = teacher.selected();
            li = selTeach.split();
            print(selTeach);
            index = self.ui.tV_data.currentIndex();
            self.model.setData(index, li[0]);

    def cSubject(self):
        sub = chooseSubject_mod.MyForm(self);
        result = sub.exec_();
        print(result);
        if(result == 1):
            selSub = sub.selected();
            li = selSub.split();
            print(selSub);
            index = self.ui.tV_data.currentIndex();
            self.model.setData(index, li[0]);
            

            
        
        
        
        

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())

