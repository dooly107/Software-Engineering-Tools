import sys

from PySide.QtGui import *
from BasicUI import *
from xml.etree.ElementTree import Element, SubElement
import xml.etree.ElementTree as ET


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.inputText = [self.txtStudentName, self.txtStudentID]
        self.componentName = [self.txtComponentName_1,self.txtComponentName_2,self.txtComponentName_3,self.txtComponentName_4,self.txtComponentName_5,self.txtComponentName_6,self.txtComponentName_7,self.txtComponentName_8,self.txtComponentName_9,self.txtComponentName_10,self.txtComponentName_11,self.txtComponentName_12,self.txtComponentName_13,self.txtComponentName_14,self.txtComponentName_15,self.txtComponentName_16,self.txtComponentName_17,self.txtComponentName_18,self.txtComponentName_19,self.txtComponentName_20]
        self.componentCount = [self.txtComponentCount_1,self.txtComponentCount_2,self.txtComponentCount_3,self.txtComponentCount_4,self.txtComponentCount_5,self.txtComponentCount_6,self.txtComponentCount_7,self.txtComponentCount_8,self.txtComponentCount_9,self.txtComponentCount_10,self.txtComponentCount_11,self.txtComponentCount_12,self.txtComponentCount_13,self.txtComponentCount_14,self.txtComponentCount_15,self.txtComponentCount_16,self.txtComponentCount_17,self.txtComponentCount_18,self.txtComponentCount_19,self.txtComponentCount_20]
        self.btnSave.setEnabled(False)

        #SaveButton Enable & Disable Connection
        self.txtStudentName.textChanged.connect(self.saveloadButtonEnable)
        self.txtStudentID.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_1.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_2.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_3.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_4.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_5.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_6.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_7.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_8.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_9.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_10.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_11.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_12.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_13.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_14.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_15.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_16.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_17.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_18.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_19.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_20.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentName_20.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_1.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_2.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_3.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_4.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_5.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_6.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_7.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_8.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_9.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_10.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_11.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_12.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_13.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_14.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_15.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_16.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_17.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_18.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_19.textChanged.connect(self.saveloadButtonEnable)
        self.txtComponentCount_20.textChanged.connect(self.saveloadButtonEnable)
        self.cboCollege.currentIndexChanged.connect(self.saveloadButtonEnable)
        self.chkGraduate.stateChanged.connect(self.saveloadButtonEnable)


        #Actions for buttons
        self.btnClear.clicked.connect(self.clearState)
        self.btnLoad.clicked.connect(self.loadData)
        self.btnSave.clicked.connect(self.SaveData)

    def loadDataFromFile(self, filePath):
        tree = ET.parse(filePath)
        content = tree.getroot()
        for child in content:
            if child.tag == "StudentName":
                name = child.text
                self.txtStudentName.setText(name)
                if child.attrib.get('graduate') == 'true':
                    self.chkGraduate.setChecked(True)
                else:
                    self.chkGraduate.setChecked(False)
            elif child.tag == "StudentID":
                ID = child.text
                self.txtStudentID.setText(ID)
            elif child.tag == "College":
                college = child.text
                index = self.cboCollege.findText(college)
                self.cboCollege.setCurrentIndex(index)
            elif child.tag == "Components":
                compnames = []
                numcounts = []
                for components in child:
                    compnames.append(components.attrib.get('name'))
                for counts in child:
                    numcounts.append(counts.attrib.get('count'))
                length_compnames = len(compnames)
                if length_compnames > 20:
                    for i in range(20):
                        self.componentName[i].setText(compnames[i])
                        self.componentCount[i].setText(numcounts[i])
                else:
                    for i in range(length_compnames):
                        self.componentName[i].setText(compnames[i])
                        self.componentCount[i].setText(numcounts[i])


    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return
        self.loadDataFromFile(filePath)


    def SaveData(self):
        if self.chkGraduate.isChecked() == True:
            graduate = '"true"'
        else:
            graduate = '"false"'
        studentName = self.txtStudentName.text()
        studentID = self.txtStudentID.text()
        College = self.cboCollege.itemText(self.cboCollege.currentIndex())
        numnames = []
        numcounts = []
        for names in self.componentName:
            if names.text() == "":
                pass
            else:
                numnames.append(names.text())
        for counts in self.componentCount:
            if counts.text() == "":
                pass
            else:
                numcounts.append(counts.text())
        with open("target.xml", 'w') as myFile:
            myFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            myFile.write('<Content>\n')
            myFile.write('    <StudentName graduate='+graduate+'>'+studentName+'</StudentName>\n')
            myFile.write('    <StudentID>'+studentID+'</StudentID>\n')
            myFile.write('    <College>'+College+'</College>\n')
            myFile.write('    <Components>\n')
            for i in range(len(numnames)):
                myFile.write('        <Component name="'+numnames[i]+'" count="'+numcounts[i]+'" />\n')
            myFile.write('    </Components>\n')
            myFile.write('</Content>')



    def saveloadButtonEnable(self):
        if len(self.txtStudentName.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtStudentID.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_1.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_2.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_3.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_4.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_5.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_6.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_7.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_8.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_9.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_10.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_11.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_12.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_13.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_14.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_15.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_16.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_17.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_18.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_19.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentName_20.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_1.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_2.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_3.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_4.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_5.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_6.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_7.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_8.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_9.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_10.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_11.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_12.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_13.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_14.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_15.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_16.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_17.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_18.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_19.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif len(self.txtComponentCount_20.text()) > 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif self.cboCollege.currentIndex() != 0:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        elif self.chkGraduate.isChecked() == True:
            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)
        else:
            self.btnSave.setEnabled(False)
            self.btnLoad.setEnabled(True)


    def clearState(self):
        for texts in self.inputText:
            texts.clear()
        self.cboCollege.setCurrentIndex(0)
        self.chkGraduate.setChecked(False)
        for names in self.componentName:
            names.clear()
        for counts in self.componentCount:
            counts.clear()
        self.btnSave.setEnabled(False)



if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
