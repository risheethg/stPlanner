import sys
import os
import sqlite3
from PyQt4 import QtSql
from ScheduleTasks_auto import *
import calendar_mod
import taskhelp_mod

class MyForm(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        dbfile = "student_planner.db"
        self.conn = sqlite3.connect(dbfile)

        #connect to DB
        self.conn = sqlite3.connect("student_planner.db");
        
        #Button Bindings
        self.ui.pb_moreSD.clicked.connect(self.calender);
        self.ui.pb_moreED.clicked.connect(self.calender2);
        self.ui.pb_moreTasks.clicked.connect(self.openTask);
        self.ui.pb_save.clicked.connect(self.save);
        
        
    def calender(self):
        windo = calendar_mod.MyForm(self);
        result = windo.exec_();
        if(result == 1):
            date = windo.getDate();
            self.ui.dE_startDate.setDisplayFormat("MMM d yyyy");
            self.ui.dE_startDate.setDate(date);

    def calender2(self):
        windo = calendar_mod.MyForm();
        result = windo.exec_();
        if(result == 1):
            date = windo.getDate();
            self.ui.dE_endDate.setDisplayFormat("MMM d yyyy");
            self.ui.dE_endDate.setDate(date);

    def openTask(self):
        windo = taskhelp_mod.MyForm(self);
        result = windo.exec_();
        if(result == 1):
            taskID = windo.getTaskId();
            self.ui.lE_task.setText(str(taskID))

    def save(self):
        try:
            cursor = self.conn.cursor();
            cursor.execute("INSERT into schedule(task_id, start_date, end_date, cmpltchck) VALUES(?, ?, ?, ?) ", (self.ui.lE_task.text(), self.ui.dE_startDate.text(), \
                                                                                                                   self.ui.dE_endDate.text(), "N"))
            self.conn.commit();

            w = QtGui.QWidget()
            QtGui.QMessageBox.information(w, "Saved Successfuly!", "Saved Successfuly!");
            print("Saved!")
           
        except sqlite3.Error as e:
            w = QtGui.QWidget();
            QtGui.QMessageBox.information(w, "An Error Occured!:", e.args[0]);
        
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())
