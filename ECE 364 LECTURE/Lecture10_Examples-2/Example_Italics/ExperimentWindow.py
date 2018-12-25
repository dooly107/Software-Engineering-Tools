# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\UserApps\Google Drive\Purdue\ECE 364 2015-1 Spring\Examples\Python Qt\Example2\ExperimentWindow.ui'
#
# Created: Mon Mar 23 11:03:01 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtName = QtGui.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(130, 20, 191, 20))
        self.txtName.setObjectName("txtName")
        self.txtLabel = QtGui.QLabel(self.centralwidget)
        self.txtLabel.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.txtLabel.setObjectName("txtLabel")
        self.lblMessage = QtGui.QLabel(self.centralwidget)
        self.lblMessage.setGeometry(QtCore.QRect(20, 170, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.lblMessage.setFont(font)
        self.lblMessage.setText("")
        self.lblMessage.setObjectName("lblMessage")
        self.btnShow = QtGui.QPushButton(self.centralwidget)
        self.btnShow.setGeometry(QtCore.QRect(20, 70, 111, 23))
        self.btnShow.setObjectName("btnShow")
        self.chkItalic = QtGui.QCheckBox(self.centralwidget)
        self.chkItalic.setGeometry(QtCore.QRect(160, 70, 70, 17))
        self.chkItalic.setChecked(True)
        self.chkItalic.setObjectName("chkItalic")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.txtLabel.setText(QtGui.QApplication.translate("mainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.btnShow.setText(QtGui.QApplication.translate("mainWindow", "Show Name ", None, QtGui.QApplication.UnicodeUTF8))
        self.chkItalic.setText(QtGui.QApplication.translate("mainWindow", "Italic", None, QtGui.QApplication.UnicodeUTF8))

