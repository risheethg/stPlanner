import sys
from PyQt4 import QtCore, QtGui, uic

from mainmenu_auto import *
import task_mod
import code_maintenance_mod
import ScheduleTasks_mod
import pendingtasks_mod
import comptasks_mod

class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
     def __init__(self, parent=None):
         QtGui.QMainWindow.__init__(self, parent)
         self.setupUi(self)

         #this is where we will bind the event handlers
         self.connect(self.actionCode_Maintenance, QtCore.SIGNAL('triggered()'), self.openCodeM);
         self.connect(self.actionTasks, QtCore.SIGNAL('triggered()'), self.openTasks);
         self.connect(self.actionScheduling, QtCore.SIGNAL('triggered()'), self.openSchedTasks);
         self.connect(self.actionPending_Tasks, QtCore.SIGNAL('triggered()'), self.openPendTasks);
         self.connect(self.actionCompleted_Tasks, QtCore.SIGNAL('triggered()'), self.openCompletedTasks);

    #This is where we will insert the functions (defs)
         
     def openCodeM(self):
          codeM = code_maintenance_mod.MyForm()
          codeM.exec_();
          
     def openTasks(self):
          taskWind = task_mod.MyForm();
          taskWind.exec_();

     def openSchedTasks(self):
          windo = ScheduleTasks_mod.MyForm(self);
          windo.exec_();

     def openPendTasks(self):
          windo = pendingtasks_mod.MyForm(self);
          windo.exec_();

     def openCompletedTasks(self):
          windo = comptasks_mod.MyForm(self);
          windo.exec_();
          
        
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
