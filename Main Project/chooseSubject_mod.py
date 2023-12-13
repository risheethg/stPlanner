import sys
import os
import sqlite3
from PyQt4 import QtSql
from chooseSubjects_auto import *

class MyForm(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        dbfile = "student_planner.db"
        self.conn = sqlite3.connect(dbfile)
        self.setWindowTitle("Choose Subjects/Sports")

        #Connect to DB
        self.conn = sqlite3.connect("student_planner.db");
        
        #Retrieve
        self.retrieve()
        
        
    #Define Functions
    def retrieve(self):
        self.ui.lw_subjects.clear()
        try:
            cursor = self.conn.cursor()
            cursor.execute("Select * from codes where code_type = 't'")
            row = cursor.fetchall()
            self.conn.commit()

            for i in row:
                code_id, code_type, code_desc = i
                string = "";
                string += str(code_id) + " " + code_desc
                self.ui.lw_subjects.addItem(string)
                
        except sqlite3.Error as e:
            w = QtGui.QWidget()
            QtGui.QMessageBox.information(w, "An Error Occured", e.args[0])
            print(e)
    
    def selected(self):
        selected = self.ui.lw_subjects.item(self.ui.lw_subjects.currentRow()).text();
        return selected;
    
        
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())
