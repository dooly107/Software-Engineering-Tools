# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\UserApps\Google Drive\Purdue\ECE 364 2015-1 Spring\Examples\Python Qt\Last\UI_Relations.ui'
#
# Created: Mon Mar 30 09:03:30 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 370)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grp1 = QtGui.QGroupBox(self.centralwidget)
        self.grp1.setGeometry(QtCore.QRect(20, 20, 301, 301))
        self.grp1.setTitle("")
        self.grp1.setObjectName("grp1")
        self.btnSubtract = QtGui.QPushButton(self.grp1)
        self.btnSubtract.setGeometry(QtCore.QRect(250, 140, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnSubtract.setFont(font)
        self.btnSubtract.setObjectName("btnSubtract")
        self.btnAdd = QtGui.QPushButton(self.grp1)
        self.btnAdd.setGeometry(QtCore.QRect(10, 140, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.layoutWidget = QtGui.QWidget(self.grp1)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 20, 135, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt1 = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt1.setFont(font)
        self.txt1.setAlignment(QtCore.Qt.AlignCenter)
        self.txt1.setObjectName("txt1")
        self.verticalLayout.addWidget(self.txt1)
        self.txt2 = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt2.setFont(font)
        self.txt2.setAlignment(QtCore.Qt.AlignCenter)
        self.txt2.setObjectName("txt2")
        self.verticalLayout.addWidget(self.txt2)
        self.txt3 = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt3.setFont(font)
        self.txt3.setAlignment(QtCore.Qt.AlignCenter)
        self.txt3.setObjectName("txt3")
        self.verticalLayout.addWidget(self.txt3)
        self.txt4 = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt4.setFont(font)
        self.txt4.setAlignment(QtCore.Qt.AlignCenter)
        self.txt4.setObjectName("txt4")
        self.verticalLayout.addWidget(self.txt4)
        self.txt5 = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt5.setFont(font)
        self.txt5.setAlignment(QtCore.Qt.AlignCenter)
        self.txt5.setObjectName("txt5")
        self.verticalLayout.addWidget(self.txt5)
        self.grp2 = QtGui.QGroupBox(self.centralwidget)
        self.grp2.setGeometry(QtCore.QRect(330, 20, 421, 301))
        self.grp2.setTitle("")
        self.grp2.setObjectName("grp2")
        self.lblToday = QtGui.QLabel(self.grp2)
        self.lblToday.setGeometry(QtCore.QRect(10, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblToday.setFont(font)
        self.lblToday.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblToday.setObjectName("lblToday")
        self.txtDay = QtGui.QLineEdit(self.grp2)
        self.txtDay.setGeometry(QtCore.QRect(270, 140, 133, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtDay.setFont(font)
        self.txtDay.setText("")
        self.txtDay.setAlignment(QtCore.Qt.AlignCenter)
        self.txtDay.setObjectName("txtDay")
        self.layoutWidget1 = QtGui.QWidget(self.grp2)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 20, 111, 271))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnMon = QtGui.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.btnMon.setFont(font)
        self.btnMon.setObjectName("btnMon")
        self.verticalLayout_2.addWidget(self.btnMon)
        self.btnTue = QtGui.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnTue.setFont(font)
        self.btnTue.setObjectName("btnTue")
        self.verticalLayout_2.addWidget(self.btnTue)
        self.btnWed = QtGui.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnWed.setFont(font)
        self.btnWed.setObjectName("btnWed")
        self.verticalLayout_2.addWidget(self.btnWed)
        self.btnThu = QtGui.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnThu.setFont(font)
        self.btnThu.setObjectName("btnThu")
        self.verticalLayout_2.addWidget(self.btnThu)
        self.btnFri = QtGui.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnFri.setFont(font)
        self.btnFri.setObjectName("btnFri")
        self.verticalLayout_2.addWidget(self.btnFri)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSubtract.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.txt1.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.txt2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.txt3.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.txt4.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.txt5.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.lblToday.setText(QtGui.QApplication.translate("MainWindow", "Today is:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMon.setText(QtGui.QApplication.translate("MainWindow", "Monday", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTue.setText(QtGui.QApplication.translate("MainWindow", "Tuesday", None, QtGui.QApplication.UnicodeUTF8))
        self.btnWed.setText(QtGui.QApplication.translate("MainWindow", "Wednesday", None, QtGui.QApplication.UnicodeUTF8))
        self.btnThu.setText(QtGui.QApplication.translate("MainWindow", "Thursday", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFri.setText(QtGui.QApplication.translate("MainWindow", "Friday", None, QtGui.QApplication.UnicodeUTF8))
