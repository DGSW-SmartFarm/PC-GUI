# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\nareusya_2_2\gui\gui_learning\test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color : white;\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, -20, 1960, 120))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/north_bar.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.credit = QtWidgets.QPushButton(self.centralwidget)
        self.credit.setGeometry(QtCore.QRect(1790, 20, 40, 40))
        self.credit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit.setStyleSheet("QPushButton{image:url(./image/credit.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/credit2.png); border:0px;}\n"
"\n"
"\n"
"")
        self.credit.setText("")
        self.credit.setObjectName("credit")
        self.set = QtWidgets.QPushButton(self.centralwidget)
        self.set.setGeometry(QtCore.QRect(1850, 20, 40, 40))
        self.set.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set.setStyleSheet("QPushButton{image:url(./image/set.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/set2.png); border:0px;}\n"
"\n"
"\n"
"")
        self.set.setText("")
        self.set.setObjectName("set")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 100, 1921, 321))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(50, 5, 50, 0)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.credit_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_4.sizePolicy().hasHeightForWidth())
        self.credit_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.credit_4.setFont(font)
        self.credit_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit_4.setStyleSheet("QPushButton{image:url(./image/chk_temp.png); border:0px;color : rgb(255,113,113);}\n"
"QPushButton:hover{image:url(./image/chk_temp2.png); border:0px;color : rgb(255,113,113);}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.credit_4.setObjectName("credit_4")
        self.horizontalLayout.addWidget(self.credit_4)
        self.credit_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_3.sizePolicy().hasHeightForWidth())
        self.credit_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.credit_3.setFont(font)
        self.credit_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit_3.setStyleSheet("QPushButton{image:url(./image/chk_hum.png); border:0px;color:rgb(0,185,250);}\n"
"QPushButton:hover{image:url(./image/chk_hum2.png); border:0px;color:rgb(0,185,250);}\n"
"\n"
"\n"
"")
        self.credit_3.setObjectName("credit_3")
        self.horizontalLayout.addWidget(self.credit_3)
        self.credit_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_5.sizePolicy().hasHeightForWidth())
        self.credit_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.credit_5.setFont(font)
        self.credit_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit_5.setStyleSheet("QPushButton{image:url(./image/chk_co2.png); border:0px;color:rgb(146,208,80);}\n"
"QPushButton:hover{image:url(./image/chk_co22.png); border:0px;color:rgb(146,208,80);}\n"
"\n"
"\n"
"")
        self.credit_5.setObjectName("credit_5")
        self.horizontalLayout.addWidget(self.credit_5)
        self.credit_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_6.sizePolicy().hasHeightForWidth())
        self.credit_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.credit_6.setFont(font)
        self.credit_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit_6.setStyleSheet("QPushButton{image:url(./image/chk_ph.png); border:0px;color:rgb(38,137,242);}\n"
"QPushButton:hover{image:url(./image/chk_ph2.png); border:0px;color:rgb(38,137,242);}\n"
"\n"
"\n"
"")
        self.credit_6.setObjectName("credit_6")
        self.horizontalLayout.addWidget(self.credit_6)
        self.credit_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_7.sizePolicy().hasHeightForWidth())
        self.credit_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.credit_7.setFont(font)
        self.credit_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit_7.setStyleSheet("QPushButton{image:url(./image/chk_tds.png); border:0px;color:rgb(147,62,197);}\n"
"QPushButton:hover{image:url(./image/chk_tds2.png); border:0px;color:rgb(147,62,197);}\n"
"\n"
"\n"
"")
        self.credit_7.setObjectName("credit_7")
        self.horizontalLayout.addWidget(self.credit_7)
        self.credit_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_2.sizePolicy().hasHeightForWidth())
        self.credit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.credit_2.setFont(font)
        self.credit_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit_2.setStyleSheet("QPushButton{image:url(./image/chk_light.png); border:0px;color:rgb(222,217,0);}\n"
"QPushButton:hover{image:url(./image/chk_light2.png); border:0px;color:rgb(222,217,0);}\n"
"\n"
"\n"
"")
        self.credit_2.setObjectName("credit_2")
        self.horizontalLayout.addWidget(self.credit_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.credit_4.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"69°"))
        self.credit_3.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"74%"))
        self.credit_5.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"58"))
        self.credit_6.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"82"))
        self.credit_7.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"45"))
        self.credit_2.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"19"))

