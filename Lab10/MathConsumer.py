# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *

from calculator import *

class MathConsumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MathConsumer, self).__init__(parent)
        self.setupUi(self)

        self.btnCalculate.clicked.connect(self.performOperation)

    def performOperation(self):
        try:
            num1 = float(self.edtNumber1.text())
            num2 = float(self.edtNumber2.text())
        except:
            self.edtResult.setText("E")
        else:
            calc = self.cboOperation.itemText(self.cboOperation.currentIndex())
            if calc == "+":
                result = str(num1 + num2)
                self.edtResult.setText(result)
            elif calc == "-":
                result = str(num1 - num2)
                self.edtResult.setText(result)
            elif calc == "*":
                result = str(num1 * num2)
                self.edtResult.setText(result)
            elif calc == "/":
                if num2 == 0:
                    self.edtResult.setText("E")
                else:
                    result = str(num1 / num2)
                    self.edtResult.setText(result)


currentApp = QApplication(sys.argv)
currentForm = MathConsumer()

currentForm.show()
currentApp.exec_()
