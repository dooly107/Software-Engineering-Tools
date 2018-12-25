# Import PySide classes

import sys
from PySide.QtCore import *
from PySide.QtGui import *

from ExperimentWindow import *

class Consumer(QMainWindow, Ui_mainWindow):

    def __init__(self, parent=None):
        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.btnShow.clicked.connect(self.displayNameInLabel)
        self.chkItalic.stateChanged.connect(self.makeItalic)


    def displayNameInLabel(self):

        # Get the name
        nameEntered = self.txtName.text()

        # Assign the name.
        self.lblMessage.setText(nameEntered)

    def makeItalic(self):

        isChecked = self.chkItalic.isChecked()

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setItalic(isChecked)
        font.setBold(True)
        self.lblMessage.setFont(font)


currentApp = QApplication(sys.argv)
currentForm = Consumer()

currentForm.show()
currentApp.exec_()
