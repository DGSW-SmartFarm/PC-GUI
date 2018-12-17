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
        MainWindow.resize(1916, 1077)
        MainWindow.setStyleSheet("background-color : white;\n"
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
        self.credit.setCheckable(True)
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
        self.set.setCheckable(True)
        self.set.setObjectName("set")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, 479, 511, 601))
        self.widget.setStyleSheet("border:0px")
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 511, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 7, 1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.credit_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_3.sizePolicy().hasHeightForWidth())
        self.credit_3.setSizePolicy(sizePolicy)
        self.credit_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit_3.setStyleSheet("QPushButton{image:url(./image/mon_graph.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/mon_graph2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/mon_graph2.png); border:0px;}\n"
"")
        self.credit_3.setText("")
        self.credit_3.setCheckable(True)
        self.credit_3.setChecked(True)
        self.credit_3.setFlat(False)
        self.credit_3.setObjectName("credit_3")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.credit_3)
        self.verticalLayout.addWidget(self.credit_3)
        self.credit_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_7.sizePolicy().hasHeightForWidth())
        self.credit_7.setSizePolicy(sizePolicy)
        self.credit_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit_7.setStyleSheet("QPushButton{image:url(./image/mon_pen.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/mon_pen2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/mon_pen2.png); border:0px;}\n"
"\n"
"")
        self.credit_7.setText("")
        self.credit_7.setCheckable(True)
        self.credit_7.setObjectName("credit_7")
        self.buttonGroup.addButton(self.credit_7)
        self.verticalLayout.addWidget(self.credit_7)
        self.credit_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_6.sizePolicy().hasHeightForWidth())
        self.credit_6.setSizePolicy(sizePolicy)
        self.credit_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit_6.setStyleSheet("QPushButton{image:url(./image/mon_light.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/mon_light2.png); border:0px;}\n"
"\n"
"\n"
"QPushButton:checked{image:url(./image/mon_light2.png); border:0px;}")
        self.credit_6.setText("")
        self.credit_6.setCheckable(True)
        self.credit_6.setObjectName("credit_6")
        self.buttonGroup.addButton(self.credit_6)
        self.verticalLayout.addWidget(self.credit_6)
        self.credit_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_4.sizePolicy().hasHeightForWidth())
        self.credit_4.setSizePolicy(sizePolicy)
        self.credit_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit_4.setStyleSheet("QPushButton{image:url(./image/mon_temp.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/mon_temp2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/mon_temp2.png); border:0px;}\n"
"\n"
"")
        self.credit_4.setText("")
        self.credit_4.setCheckable(True)
        self.credit_4.setObjectName("credit_4")
        self.buttonGroup.addButton(self.credit_4)
        self.verticalLayout.addWidget(self.credit_4)
        self.credit_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_5.sizePolicy().hasHeightForWidth())
        self.credit_5.setSizePolicy(sizePolicy)
        self.credit_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit_5.setStyleSheet("QPushButton{image:url(./image/mon_co2.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/mon_co22.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/mon_co22.png); border:0px;}\n"
"\n"
"")
        self.credit_5.setText("")
        self.credit_5.setCheckable(True)
        self.credit_5.setObjectName("credit_5")
        self.buttonGroup.addButton(self.credit_5)
        self.verticalLayout.addWidget(self.credit_5)
        self.credit_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.credit_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit_2.sizePolicy().hasHeightForWidth())
        self.credit_2.setSizePolicy(sizePolicy)
        self.credit_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit_2.setStyleSheet("QPushButton{image:url(./image/mon_nutri.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/mon_nutri2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/mon_nutri2.png); border:0px;}\n"
"\n"
"")
        self.credit_2.setText("")
        self.credit_2.setCheckable(True)
        self.credit_2.setObjectName("credit_2")
        self.buttonGroup.addButton(self.credit_2)
        self.verticalLayout.addWidget(self.credit_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 450, 1921, 36))
        self.label_2.setStyleSheet("border-bottom: 2px solid rgb(217,217,217) ;")
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setLineWidth(2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 110, 1920, 321))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1921, 321))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.chk_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.chk_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.chk_layout.setContentsMargins(50, 5, 50, 0)
        self.chk_layout.setSpacing(40)
        self.chk_layout.setObjectName("chk_layout")
        self.chk_temp = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_temp.sizePolicy().hasHeightForWidth())
        self.chk_temp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.chk_temp.setFont(font)
        self.chk_temp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_temp.setStyleSheet("QPushButton{image:url(./image/chk_temp.png); border:0px;color : rgb(255,113,113);}\n"
"QPushButton:hover{image:url(./image/chk_temp2.png); border:0px;color : rgb(255,113,113);}\n"
"QPushButton:checked{image:url(./image/chk_temp2.png); border:0px;color : rgb(255,113,113);}\n"
"\n"
"\n"
"\n"
"")
        self.chk_temp.setCheckable(True)
        self.chk_temp.setObjectName("chk_temp")
        self.buttonGroup.addButton(self.chk_temp)
        self.chk_layout.addWidget(self.chk_temp)
        self.chk_hum = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_hum.sizePolicy().hasHeightForWidth())
        self.chk_hum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.chk_hum.setFont(font)
        self.chk_hum.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_hum.setStyleSheet("QPushButton{image:url(./image/chk_hum.png); border:0px;color:rgb(0,185,250);}\n"
"QPushButton:hover{image:url(./image/chk_hum2.png); border:0px;color:rgb(0,185,250);}\n"
"QPushButton:checked{image:url(./image/chk_hum2.png); border:0px;color:rgb(0,185,250);}\n"
"\n"
"")
        self.chk_hum.setCheckable(True)
        self.chk_hum.setObjectName("chk_hum")
        self.buttonGroup.addButton(self.chk_hum)
        self.chk_layout.addWidget(self.chk_hum)
        self.chk_co2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_co2.sizePolicy().hasHeightForWidth())
        self.chk_co2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.chk_co2.setFont(font)
        self.chk_co2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_co2.setStyleSheet("QPushButton{image:url(./image/chk_co2.png); border:0px;color:rgb(146,208,80);}\n"
"QPushButton:hover{image:url(./image/chk_co22.png); border:0px;color:rgb(146,208,80);}\n"
"QPushButton:checked{image:url(./image/chk_co22.png); border:0px;color:rgb(146,208,80);}\n"
"\n"
"")
        self.chk_co2.setCheckable(True)
        self.chk_co2.setObjectName("chk_co2")
        self.buttonGroup.addButton(self.chk_co2)
        self.chk_layout.addWidget(self.chk_co2)
        self.chk_ph2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_ph2.sizePolicy().hasHeightForWidth())
        self.chk_ph2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.chk_ph2.setFont(font)
        self.chk_ph2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_ph2.setStyleSheet("QPushButton{image:url(./image/chk_ph.png); border:0px;color:rgb(38,137,242);}\n"
"QPushButton:hover{image:url(./image/chk_ph2.png); border:0px;color:rgb(38,137,242);}\n"
"\n"
"QPushButton:checked{image:url(./image/chk_ph2.png); border:0px;color:rgb(38,137,242);}\n"
"")
        self.chk_ph2.setCheckable(True)
        self.chk_ph2.setObjectName("chk_ph2")
        self.buttonGroup.addButton(self.chk_ph2)
        self.chk_layout.addWidget(self.chk_ph2)
        self.chk_tds = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_tds.sizePolicy().hasHeightForWidth())
        self.chk_tds.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.chk_tds.setFont(font)
        self.chk_tds.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_tds.setStyleSheet("QPushButton{image:url(./image/chk_tds.png); border:0px;color:rgb(147,62,197);}\n"
"QPushButton:hover{image:url(./image/chk_tds2.png); border:0px;color:rgb(147,62,197);}\n"
"QPushButton:checked{image:url(./image/chk_tds2.png); border:0px;color:rgb(147,62,197);}\n"
"\n"
"")
        self.chk_tds.setCheckable(True)
        self.chk_tds.setObjectName("chk_tds")
        self.buttonGroup.addButton(self.chk_tds)
        self.chk_layout.addWidget(self.chk_tds)
        self.chk_light = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_light.sizePolicy().hasHeightForWidth())
        self.chk_light.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.chk_light.setFont(font)
        self.chk_light.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_light.setStyleSheet("QPushButton{image:url(./image/chk_light.png); border:0px;color:rgb(222,217,0);}\n"
"QPushButton:hover{image:url(./image/chk_light2.png); border:0px;color:rgb(222,217,0);}\n"
"QPushButton:checked{image:url(./image/chk_light2.png); border:0px;color:rgb(222,217,0);}\n"
"\n"
"")
        self.chk_light.setCheckable(True)
        self.chk_light.setObjectName("chk_light")
        self.buttonGroup.addButton(self.chk_light)
        self.chk_layout.addWidget(self.chk_light)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(507, 485, 1411, 595))
        self.stackedWidget.setStyleSheet("border-left : 2px solid rgb(217,217,217);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.grape = QtWidgets.QWidget()
        self.grape.setObjectName("grape")
        self.stackedWidget.addWidget(self.grape)
        self.song = QtWidgets.QWidget()
        self.song.setObjectName("song")
        self.line = QtWidgets.QFrame(self.song)
        self.line.setGeometry(QtCore.QRect(0, 430, 1411, 2))
        self.line.setStyleSheet("background-color : rgb(217,217,217);")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalSlider_5 = QtWidgets.QSlider(self.song)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(150, 450, 1071, 121))
        self.horizontalSlider_5.setStyleSheet("\n"
"QSlider::groove:horizontal {\n"
"    height:12px;\n"
"    background: rgb(217,217,217);\n"
"\n"
"\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(./image/green_slide.png);\n"
"    width: 32px;\n"
"    height: 97px;\n"
"\n"
"    margin-top: -42px;\n"
"    margin-bottom: -43px;\n"
"\n"
"\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-image: url(./image/green_slide2.png);\n"
"    width: 32px;\n"
"    height: 97px;\n"
"\n"
"    margin-top: -42px;\n"
"    margin-bottom: -43px;\n"
"\n"
"\n"
"}\n"
"QSlider{\n"
"    border : 0px;\n"
"\n"
"}")
        self.horizontalSlider_5.setMaximum(100)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.label_12 = QtWidgets.QLabel(self.song)
        self.label_12.setGeometry(QtCore.QRect(1250, 480, 131, 61))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border : 0px;\n"
"color : rgb(0,112,192);")
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.pushButton_9 = QtWidgets.QPushButton(self.song)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 450, 131, 111))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton{image:url(./image/off_big_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_big_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_big_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_big_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_9.setText("")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setChecked(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.song)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 10, 1291, 411))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(45, 10, 45, 10)
        self.gridLayout_2.setHorizontalSpacing(45)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.w1_2 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.w1_2.setEnabled(True)
        self.w1_2.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_2.setObjectName("w1_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.w1_2)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_3.setMaxLength(30)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.w1_2)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 0, 251, 181))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.w1_2)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_4.setMaxLength(30)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_11 = QtWidgets.QPushButton(self.w1_2)
        self.pushButton_11.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_11.setText("")
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setChecked(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_13 = QtWidgets.QLabel(self.w1_2)
        self.label_13.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_13.setObjectName("label_13")
        self.pushButton_12 = QtWidgets.QPushButton(self.w1_2)
        self.pushButton_12.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_12.setText("")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.w1_2)
        self.pushButton_13.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_13.setText("")
        self.pushButton_13.setCheckable(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_31 = QtWidgets.QLabel(self.w1_2)
        self.label_31.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.label_31.raise_()
        self.label_13.raise_()
        self.pushButton_10.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.gridLayout_2.addWidget(self.w1_2, 0, 0, 1, 1)
        self.w1_6 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.w1_6.setEnabled(True)
        self.w1_6.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_6.setObjectName("w1_6")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.w1_6)
        self.lineEdit_13.setEnabled(False)
        self.lineEdit_13.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_13.setMaxLength(30)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pushButton_32 = QtWidgets.QPushButton(self.w1_6)
        self.pushButton_32.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_32.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_32.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.w1_6)
        self.lineEdit_14.setEnabled(False)
        self.lineEdit_14.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_14.setMaxLength(30)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_33 = QtWidgets.QPushButton(self.w1_6)
        self.pushButton_33.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_33.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_33.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_33.setText("")
        self.pushButton_33.setCheckable(True)
        self.pushButton_33.setChecked(False)
        self.pushButton_33.setObjectName("pushButton_33")
        self.label_18 = QtWidgets.QLabel(self.w1_6)
        self.label_18.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_18.setObjectName("label_18")
        self.pushButton_34 = QtWidgets.QPushButton(self.w1_6)
        self.pushButton_34.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_34.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_34.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_34.setText("")
        self.pushButton_34.setCheckable(True)
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.w1_6)
        self.pushButton_35.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_35.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_35.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_35.setText("")
        self.pushButton_35.setCheckable(False)
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout_2.addWidget(self.w1_6, 0, 2, 1, 1)
        self.w1_5 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.w1_5.setEnabled(True)
        self.w1_5.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_5.setObjectName("w1_5")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.w1_5)
        self.lineEdit_11.setEnabled(False)
        self.lineEdit_11.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_11.setMaxLength(30)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_28 = QtWidgets.QPushButton(self.w1_5)
        self.pushButton_28.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_28.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_28.setText("")
        self.pushButton_28.setObjectName("pushButton_28")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.w1_5)
        self.lineEdit_12.setEnabled(False)
        self.lineEdit_12.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_12.setMaxLength(30)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_29 = QtWidgets.QPushButton(self.w1_5)
        self.pushButton_29.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_29.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_29.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_29.setText("")
        self.pushButton_29.setCheckable(True)
        self.pushButton_29.setChecked(False)
        self.pushButton_29.setObjectName("pushButton_29")
        self.label_17 = QtWidgets.QLabel(self.w1_5)
        self.label_17.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_17.setObjectName("label_17")
        self.pushButton_30 = QtWidgets.QPushButton(self.w1_5)
        self.pushButton_30.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_30.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_30.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_30.setText("")
        self.pushButton_30.setCheckable(True)
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.w1_5)
        self.pushButton_31.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_31.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_31.setText("")
        self.pushButton_31.setCheckable(False)
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_2.addWidget(self.w1_5, 1, 0, 1, 1)
        self.w1_4 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.w1_4.setEnabled(True)
        self.w1_4.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_4.setObjectName("w1_4")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.w1_4)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_9.setMaxLength(30)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_24 = QtWidgets.QPushButton(self.w1_4)
        self.pushButton_24.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_24.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.w1_4)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_10.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_10.setMaxLength(30)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_25 = QtWidgets.QPushButton(self.w1_4)
        self.pushButton_25.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_25.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_25.setText("")
        self.pushButton_25.setCheckable(True)
        self.pushButton_25.setChecked(False)
        self.pushButton_25.setObjectName("pushButton_25")
        self.label_16 = QtWidgets.QLabel(self.w1_4)
        self.label_16.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_16.setObjectName("label_16")
        self.pushButton_26 = QtWidgets.QPushButton(self.w1_4)
        self.pushButton_26.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_26.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_26.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_26.setText("")
        self.pushButton_26.setCheckable(True)
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.w1_4)
        self.pushButton_27.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_27.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_27.setText("")
        self.pushButton_27.setCheckable(False)
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_2.addWidget(self.w1_4, 1, 1, 1, 1)
        self.w1_7 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.w1_7.setEnabled(True)
        self.w1_7.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_7.setObjectName("w1_7")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.w1_7)
        self.lineEdit_15.setEnabled(False)
        self.lineEdit_15.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_15.setMaxLength(30)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_36 = QtWidgets.QPushButton(self.w1_7)
        self.pushButton_36.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_36.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_36.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_36.setText("")
        self.pushButton_36.setObjectName("pushButton_36")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.w1_7)
        self.lineEdit_16.setEnabled(False)
        self.lineEdit_16.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_16.setMaxLength(30)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pushButton_37 = QtWidgets.QPushButton(self.w1_7)
        self.pushButton_37.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_37.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_37.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_37.setText("")
        self.pushButton_37.setCheckable(True)
        self.pushButton_37.setChecked(False)
        self.pushButton_37.setObjectName("pushButton_37")
        self.label_19 = QtWidgets.QLabel(self.w1_7)
        self.label_19.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_19.setObjectName("label_19")
        self.pushButton_38 = QtWidgets.QPushButton(self.w1_7)
        self.pushButton_38.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_38.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_38.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_38.setText("")
        self.pushButton_38.setCheckable(True)
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.w1_7)
        self.pushButton_39.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_39.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_39.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_39.setText("")
        self.pushButton_39.setCheckable(False)
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout_2.addWidget(self.w1_7, 1, 2, 1, 1)
        self.w1_8 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.w1_8.setEnabled(True)
        self.w1_8.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_8.setObjectName("w1_8")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.w1_8)
        self.lineEdit_17.setEnabled(False)
        self.lineEdit_17.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_17.setMaxLength(30)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.pushButton_40 = QtWidgets.QPushButton(self.w1_8)
        self.pushButton_40.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_40.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_40.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_40.setText("")
        self.pushButton_40.setObjectName("pushButton_40")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.w1_8)
        self.lineEdit_18.setEnabled(False)
        self.lineEdit_18.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_18.setMaxLength(30)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.pushButton_41 = QtWidgets.QPushButton(self.w1_8)
        self.pushButton_41.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_41.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_41.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_41.setText("")
        self.pushButton_41.setCheckable(True)
        self.pushButton_41.setChecked(False)
        self.pushButton_41.setObjectName("pushButton_41")
        self.label_20 = QtWidgets.QLabel(self.w1_8)
        self.label_20.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_20.setObjectName("label_20")
        self.pushButton_42 = QtWidgets.QPushButton(self.w1_8)
        self.pushButton_42.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_42.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_42.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_42.setText("")
        self.pushButton_42.setCheckable(True)
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.w1_8)
        self.pushButton_43.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_43.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_43.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_43.setText("")
        self.pushButton_43.setCheckable(False)
        self.pushButton_43.setObjectName("pushButton_43")
        self.gridLayout_2.addWidget(self.w1_8, 0, 3, 1, 1)
        self.w1_16 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.w1_16.setEnabled(True)
        self.w1_16.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_16.setObjectName("w1_16")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.w1_16)
        self.lineEdit_33.setEnabled(False)
        self.lineEdit_33.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_33.setFont(font)
        self.lineEdit_33.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_33.setMaxLength(30)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.pushButton_72 = QtWidgets.QPushButton(self.w1_16)
        self.pushButton_72.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_72.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_72.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_72.setText("")
        self.pushButton_72.setObjectName("pushButton_72")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.w1_16)
        self.lineEdit_34.setEnabled(False)
        self.lineEdit_34.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_34.setFont(font)
        self.lineEdit_34.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_34.setMaxLength(30)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.pushButton_73 = QtWidgets.QPushButton(self.w1_16)
        self.pushButton_73.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_73.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_73.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_73.setText("")
        self.pushButton_73.setCheckable(True)
        self.pushButton_73.setChecked(False)
        self.pushButton_73.setObjectName("pushButton_73")
        self.label_28 = QtWidgets.QLabel(self.w1_16)
        self.label_28.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_28.setObjectName("label_28")
        self.pushButton_74 = QtWidgets.QPushButton(self.w1_16)
        self.pushButton_74.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_74.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_74.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_74.setText("")
        self.pushButton_74.setCheckable(True)
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_75 = QtWidgets.QPushButton(self.w1_16)
        self.pushButton_75.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_75.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_75.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_75.setText("")
        self.pushButton_75.setCheckable(False)
        self.pushButton_75.setObjectName("pushButton_75")
        self.gridLayout_2.addWidget(self.w1_16, 1, 3, 1, 1)
        self.w1_3 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.w1_3.setEnabled(True)
        self.w1_3.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_3.setObjectName("w1_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.w1_3)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_7.setMaxLength(30)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_20 = QtWidgets.QPushButton(self.w1_3)
        self.pushButton_20.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_20.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.w1_3)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_8.setMaxLength(30)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_21 = QtWidgets.QPushButton(self.w1_3)
        self.pushButton_21.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_21.setText("")
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setChecked(False)
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_15 = QtWidgets.QLabel(self.w1_3)
        self.label_15.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_15.setObjectName("label_15")
        self.pushButton_22 = QtWidgets.QPushButton(self.w1_3)
        self.pushButton_22.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_22.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_22.setText("")
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.w1_3)
        self.pushButton_23.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_23.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_23.setText("")
        self.pushButton_23.setCheckable(False)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_2.addWidget(self.w1_3, 0, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.song)
        self.label_30.setGeometry(QtCore.QRect(30, 0, 41, 421))
        self.label_30.setStyleSheet("border : 0px;")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.pushButton_76 = QtWidgets.QPushButton(self.song)
        self.pushButton_76.setGeometry(QtCore.QRect(1360, 180, 31, 61))
        self.pushButton_76.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_76.setStyleSheet("QPushButton{image:url(./image/right_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/right_2.png); border:0px;}\n"
"")
        self.pushButton_76.setText("")
        self.pushButton_76.setCheckable(False)
        self.pushButton_76.setObjectName("pushButton_76")
        self.pushButton_77 = QtWidgets.QPushButton(self.song)
        self.pushButton_77.setGeometry(QtCore.QRect(20, 180, 31, 61))
        self.pushButton_77.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_77.setStyleSheet("QPushButton{image:url(./image/left_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/left_2.png); border:0px;}\n"
"")
        self.pushButton_77.setText("")
        self.pushButton_77.setCheckable(False)
        self.pushButton_77.setObjectName("pushButton_77")
        self.stackedWidget.addWidget(self.song)
        self.balgi = QtWidgets.QWidget()
        self.balgi.setObjectName("balgi")
        self.gridLayoutWidget = QtWidgets.QWidget(self.balgi)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(79, 9, 1251, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(25, 12, 25, 12)
        self.gridLayout.setHorizontalSpacing(45)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.bal_wi_1 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.bal_wi_1.setEnabled(True)
        self.bal_wi_1.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.bal_wi_1.setObjectName("bal_wi_1")
        self.bal_text_1 = QtWidgets.QLineEdit(self.bal_wi_1)
        self.bal_text_1.setEnabled(False)
        self.bal_text_1.setGeometry(QtCore.QRect(15, 12, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.bal_text_1.setFont(font)
        self.bal_text_1.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_text_1.setMaxLength(30)
        self.bal_text_1.setObjectName("bal_text_1")
        self.bal_btn_1 = QtWidgets.QPushButton(self.bal_wi_1)
        self.bal_btn_1.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.bal_btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_btn_1.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.bal_btn_1.setText("")
        self.bal_btn_1.setObjectName("bal_btn_1")
        self.bal_label_1 = QtWidgets.QLineEdit(self.bal_wi_1)
        self.bal_label_1.setEnabled(False)
        self.bal_label_1.setGeometry(QtCore.QRect(15, 45, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.bal_label_1.setFont(font)
        self.bal_label_1.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_label_1.setMaxLength(30)
        self.bal_label_1.setObjectName("bal_label_1")
        self.bal_onoff_1 = QtWidgets.QPushButton(self.bal_wi_1)
        self.bal_onoff_1.setGeometry(QtCore.QRect(160, 40, 91, 81))
        self.bal_onoff_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_onoff_1.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.bal_onoff_1.setText("")
        self.bal_onoff_1.setCheckable(True)
        self.bal_onoff_1.setChecked(False)
        self.bal_onoff_1.setObjectName("bal_onoff_1")
        self.bal_r_1 = QtWidgets.QLabel(self.bal_wi_1)
        self.bal_r_1.setGeometry(QtCore.QRect(55, 88, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_r_1.setFont(font)
        self.bal_r_1.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_r_1.setObjectName("bal_r_1")
        self.bal_b_1 = QtWidgets.QLabel(self.bal_wi_1)
        self.bal_b_1.setGeometry(QtCore.QRect(55, 129, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_b_1.setFont(font)
        self.bal_b_1.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_b_1.setObjectName("bal_b_1")
        self.bal_w_1 = QtWidgets.QLabel(self.bal_wi_1)
        self.bal_w_1.setGeometry(QtCore.QRect(55, 170, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_w_1.setFont(font)
        self.bal_w_1.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_w_1.setObjectName("bal_w_1")
        self.bal_su_1 = QtWidgets.QPushButton(self.bal_wi_1)
        self.bal_su_1.setGeometry(QtCore.QRect(185, 170, 31, 31))
        self.bal_su_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_su_1.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.bal_su_1.setText("")
        self.bal_su_1.setCheckable(True)
        self.bal_su_1.setObjectName("bal_su_1")
        self.bal_clo_1 = QtWidgets.QPushButton(self.bal_wi_1)
        self.bal_clo_1.setGeometry(QtCore.QRect(220, 170, 31, 31))
        self.bal_clo_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_clo_1.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.bal_clo_1.setText("")
        self.bal_clo_1.setCheckable(False)
        self.bal_clo_1.setObjectName("bal_clo_1")
        self.bal_r_1.raise_()
        self.bal_b_1.raise_()
        self.bal_w_1.raise_()
        self.bal_btn_1.raise_()
        self.bal_text_1.raise_()
        self.bal_label_1.raise_()
        self.bal_onoff_1.raise_()
        self.bal_su_1.raise_()
        self.bal_clo_1.raise_()
        self.gridLayout.addWidget(self.bal_wi_1, 0, 0, 1, 1)
        self.bal_wi_2 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.bal_wi_2.setEnabled(True)
        self.bal_wi_2.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.bal_wi_2.setObjectName("bal_wi_2")
        self.bal_text_2 = QtWidgets.QLineEdit(self.bal_wi_2)
        self.bal_text_2.setEnabled(False)
        self.bal_text_2.setGeometry(QtCore.QRect(15, 12, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.bal_text_2.setFont(font)
        self.bal_text_2.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_text_2.setMaxLength(30)
        self.bal_text_2.setObjectName("bal_text_2")
        self.bal_btn_2 = QtWidgets.QPushButton(self.bal_wi_2)
        self.bal_btn_2.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.bal_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_btn_2.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.bal_btn_2.setText("")
        self.bal_btn_2.setObjectName("bal_btn_2")
        self.bal_label_2 = QtWidgets.QLineEdit(self.bal_wi_2)
        self.bal_label_2.setEnabled(False)
        self.bal_label_2.setGeometry(QtCore.QRect(15, 45, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.bal_label_2.setFont(font)
        self.bal_label_2.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_label_2.setMaxLength(30)
        self.bal_label_2.setObjectName("bal_label_2")
        self.bal_onoff_2 = QtWidgets.QPushButton(self.bal_wi_2)
        self.bal_onoff_2.setGeometry(QtCore.QRect(160, 40, 91, 81))
        self.bal_onoff_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_onoff_2.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.bal_onoff_2.setText("")
        self.bal_onoff_2.setCheckable(True)
        self.bal_onoff_2.setChecked(False)
        self.bal_onoff_2.setObjectName("bal_onoff_2")
        self.bal_r_2 = QtWidgets.QLabel(self.bal_wi_2)
        self.bal_r_2.setGeometry(QtCore.QRect(55, 88, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_r_2.setFont(font)
        self.bal_r_2.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_r_2.setObjectName("bal_r_2")
        self.bal_b_2 = QtWidgets.QLabel(self.bal_wi_2)
        self.bal_b_2.setGeometry(QtCore.QRect(55, 129, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_b_2.setFont(font)
        self.bal_b_2.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_b_2.setObjectName("bal_b_2")
        self.bal_w_2 = QtWidgets.QLabel(self.bal_wi_2)
        self.bal_w_2.setGeometry(QtCore.QRect(55, 170, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_w_2.setFont(font)
        self.bal_w_2.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_w_2.setObjectName("bal_w_2")
        self.bal_su_2 = QtWidgets.QPushButton(self.bal_wi_2)
        self.bal_su_2.setGeometry(QtCore.QRect(185, 170, 31, 31))
        self.bal_su_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_su_2.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.bal_su_2.setText("")
        self.bal_su_2.setCheckable(True)
        self.bal_su_2.setObjectName("bal_su_2")
        self.bal_clo_2 = QtWidgets.QPushButton(self.bal_wi_2)
        self.bal_clo_2.setGeometry(QtCore.QRect(220, 170, 31, 31))
        self.bal_clo_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_clo_2.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.bal_clo_2.setText("")
        self.bal_clo_2.setCheckable(False)
        self.bal_clo_2.setObjectName("bal_clo_2")
        self.bal_w_2.raise_()
        self.bal_b_2.raise_()
        self.bal_r_2.raise_()
        self.bal_btn_2.raise_()
        self.bal_text_2.raise_()
        self.bal_label_2.raise_()
        self.bal_onoff_2.raise_()
        self.bal_su_2.raise_()
        self.bal_clo_2.raise_()
        self.gridLayout.addWidget(self.bal_wi_2, 0, 1, 1, 1)
        self.bal_wi_3 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.bal_wi_3.setEnabled(True)
        self.bal_wi_3.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.bal_wi_3.setObjectName("bal_wi_3")
        self.bal_text_3 = QtWidgets.QLineEdit(self.bal_wi_3)
        self.bal_text_3.setEnabled(False)
        self.bal_text_3.setGeometry(QtCore.QRect(15, 12, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.bal_text_3.setFont(font)
        self.bal_text_3.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_text_3.setMaxLength(30)
        self.bal_text_3.setObjectName("bal_text_3")
        self.bal_btn_3 = QtWidgets.QPushButton(self.bal_wi_3)
        self.bal_btn_3.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.bal_btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_btn_3.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.bal_btn_3.setText("")
        self.bal_btn_3.setObjectName("bal_btn_3")
        self.bal_label_3 = QtWidgets.QLineEdit(self.bal_wi_3)
        self.bal_label_3.setEnabled(False)
        self.bal_label_3.setGeometry(QtCore.QRect(15, 45, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.bal_label_3.setFont(font)
        self.bal_label_3.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_label_3.setMaxLength(30)
        self.bal_label_3.setObjectName("bal_label_3")
        self.bal_onoff_3 = QtWidgets.QPushButton(self.bal_wi_3)
        self.bal_onoff_3.setGeometry(QtCore.QRect(160, 40, 91, 81))
        self.bal_onoff_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_onoff_3.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.bal_onoff_3.setText("")
        self.bal_onoff_3.setCheckable(True)
        self.bal_onoff_3.setChecked(False)
        self.bal_onoff_3.setObjectName("bal_onoff_3")
        self.bal_r_3 = QtWidgets.QLabel(self.bal_wi_3)
        self.bal_r_3.setGeometry(QtCore.QRect(55, 88, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_r_3.setFont(font)
        self.bal_r_3.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_r_3.setObjectName("bal_r_3")
        self.bal_b_3 = QtWidgets.QLabel(self.bal_wi_3)
        self.bal_b_3.setGeometry(QtCore.QRect(55, 129, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_b_3.setFont(font)
        self.bal_b_3.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_b_3.setObjectName("bal_b_3")
        self.bal_w_3 = QtWidgets.QLabel(self.bal_wi_3)
        self.bal_w_3.setGeometry(QtCore.QRect(55, 170, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_w_3.setFont(font)
        self.bal_w_3.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_w_3.setObjectName("bal_w_3")
        self.bal_su_3 = QtWidgets.QPushButton(self.bal_wi_3)
        self.bal_su_3.setGeometry(QtCore.QRect(185, 170, 31, 31))
        self.bal_su_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_su_3.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.bal_su_3.setText("")
        self.bal_su_3.setCheckable(True)
        self.bal_su_3.setObjectName("bal_su_3")
        self.bal_clo_3 = QtWidgets.QPushButton(self.bal_wi_3)
        self.bal_clo_3.setGeometry(QtCore.QRect(220, 170, 31, 31))
        self.bal_clo_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_clo_3.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.bal_clo_3.setText("")
        self.bal_clo_3.setCheckable(False)
        self.bal_clo_3.setObjectName("bal_clo_3")
        self.bal_r_3.raise_()
        self.bal_b_3.raise_()
        self.bal_w_3.raise_()
        self.bal_btn_3.raise_()
        self.bal_text_3.raise_()
        self.bal_label_3.raise_()
        self.bal_onoff_3.raise_()
        self.bal_su_3.raise_()
        self.bal_clo_3.raise_()
        self.gridLayout.addWidget(self.bal_wi_3, 0, 2, 1, 1)
        self.bal_wi_4 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.bal_wi_4.setEnabled(True)
        self.bal_wi_4.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.bal_wi_4.setObjectName("bal_wi_4")
        self.bal_text_4 = QtWidgets.QLineEdit(self.bal_wi_4)
        self.bal_text_4.setEnabled(False)
        self.bal_text_4.setGeometry(QtCore.QRect(15, 12, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.bal_text_4.setFont(font)
        self.bal_text_4.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_text_4.setMaxLength(30)
        self.bal_text_4.setObjectName("bal_text_4")
        self.bal_btn_4 = QtWidgets.QPushButton(self.bal_wi_4)
        self.bal_btn_4.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.bal_btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_btn_4.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.bal_btn_4.setText("")
        self.bal_btn_4.setObjectName("bal_btn_4")
        self.bal_label_4 = QtWidgets.QLineEdit(self.bal_wi_4)
        self.bal_label_4.setEnabled(False)
        self.bal_label_4.setGeometry(QtCore.QRect(15, 45, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.bal_label_4.setFont(font)
        self.bal_label_4.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_label_4.setMaxLength(30)
        self.bal_label_4.setObjectName("bal_label_4")
        self.bal_onoff_4 = QtWidgets.QPushButton(self.bal_wi_4)
        self.bal_onoff_4.setGeometry(QtCore.QRect(160, 40, 91, 81))
        self.bal_onoff_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_onoff_4.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.bal_onoff_4.setText("")
        self.bal_onoff_4.setCheckable(True)
        self.bal_onoff_4.setChecked(False)
        self.bal_onoff_4.setObjectName("bal_onoff_4")
        self.bal_r_4 = QtWidgets.QLabel(self.bal_wi_4)
        self.bal_r_4.setGeometry(QtCore.QRect(55, 88, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_r_4.setFont(font)
        self.bal_r_4.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_r_4.setObjectName("bal_r_4")
        self.bal_b_4 = QtWidgets.QLabel(self.bal_wi_4)
        self.bal_b_4.setGeometry(QtCore.QRect(55, 129, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_b_4.setFont(font)
        self.bal_b_4.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_b_4.setObjectName("bal_b_4")
        self.bal_w_4 = QtWidgets.QLabel(self.bal_wi_4)
        self.bal_w_4.setGeometry(QtCore.QRect(55, 170, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_w_4.setFont(font)
        self.bal_w_4.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_w_4.setObjectName("bal_w_4")
        self.bal_su_4 = QtWidgets.QPushButton(self.bal_wi_4)
        self.bal_su_4.setGeometry(QtCore.QRect(185, 170, 31, 31))
        self.bal_su_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_su_4.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.bal_su_4.setText("")
        self.bal_su_4.setCheckable(True)
        self.bal_su_4.setObjectName("bal_su_4")
        self.bal_clo_4 = QtWidgets.QPushButton(self.bal_wi_4)
        self.bal_clo_4.setGeometry(QtCore.QRect(220, 170, 31, 31))
        self.bal_clo_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_clo_4.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.bal_clo_4.setText("")
        self.bal_clo_4.setCheckable(False)
        self.bal_clo_4.setObjectName("bal_clo_4")
        self.bal_b_4.raise_()
        self.bal_r_4.raise_()
        self.bal_w_4.raise_()
        self.bal_btn_4.raise_()
        self.bal_text_4.raise_()
        self.bal_label_4.raise_()
        self.bal_onoff_4.raise_()
        self.bal_su_4.raise_()
        self.bal_clo_4.raise_()
        self.gridLayout.addWidget(self.bal_wi_4, 0, 3, 1, 1)
        self.bal_wi_5 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.bal_wi_5.setEnabled(True)
        self.bal_wi_5.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.bal_wi_5.setObjectName("bal_wi_5")
        self.bal_text_5 = QtWidgets.QLineEdit(self.bal_wi_5)
        self.bal_text_5.setEnabled(False)
        self.bal_text_5.setGeometry(QtCore.QRect(15, 12, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.bal_text_5.setFont(font)
        self.bal_text_5.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_text_5.setMaxLength(30)
        self.bal_text_5.setObjectName("bal_text_5")
        self.bal_btn_5 = QtWidgets.QPushButton(self.bal_wi_5)
        self.bal_btn_5.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.bal_btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_btn_5.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.bal_btn_5.setText("")
        self.bal_btn_5.setObjectName("bal_btn_5")
        self.bal_label_5 = QtWidgets.QLineEdit(self.bal_wi_5)
        self.bal_label_5.setEnabled(False)
        self.bal_label_5.setGeometry(QtCore.QRect(15, 45, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.bal_label_5.setFont(font)
        self.bal_label_5.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_label_5.setMaxLength(30)
        self.bal_label_5.setObjectName("bal_label_5")
        self.bal_onoff_5 = QtWidgets.QPushButton(self.bal_wi_5)
        self.bal_onoff_5.setGeometry(QtCore.QRect(160, 40, 91, 81))
        self.bal_onoff_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_onoff_5.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.bal_onoff_5.setText("")
        self.bal_onoff_5.setCheckable(True)
        self.bal_onoff_5.setChecked(False)
        self.bal_onoff_5.setObjectName("bal_onoff_5")
        self.bal_r_5 = QtWidgets.QLabel(self.bal_wi_5)
        self.bal_r_5.setGeometry(QtCore.QRect(55, 88, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_r_5.setFont(font)
        self.bal_r_5.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_r_5.setObjectName("bal_r_5")
        self.bal_b_5 = QtWidgets.QLabel(self.bal_wi_5)
        self.bal_b_5.setGeometry(QtCore.QRect(55, 129, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_b_5.setFont(font)
        self.bal_b_5.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_b_5.setObjectName("bal_b_5")
        self.bal_w_5 = QtWidgets.QLabel(self.bal_wi_5)
        self.bal_w_5.setGeometry(QtCore.QRect(55, 170, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_w_5.setFont(font)
        self.bal_w_5.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_w_5.setObjectName("bal_w_5")
        self.bal_su_5 = QtWidgets.QPushButton(self.bal_wi_5)
        self.bal_su_5.setGeometry(QtCore.QRect(185, 170, 31, 31))
        self.bal_su_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_su_5.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.bal_su_5.setText("")
        self.bal_su_5.setCheckable(True)
        self.bal_su_5.setObjectName("bal_su_5")
        self.bal_clo_5 = QtWidgets.QPushButton(self.bal_wi_5)
        self.bal_clo_5.setGeometry(QtCore.QRect(220, 170, 31, 31))
        self.bal_clo_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_clo_5.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.bal_clo_5.setText("")
        self.bal_clo_5.setCheckable(False)
        self.bal_clo_5.setObjectName("bal_clo_5")
        self.bal_w_5.raise_()
        self.bal_b_5.raise_()
        self.bal_r_5.raise_()
        self.bal_btn_5.raise_()
        self.bal_text_5.raise_()
        self.bal_label_5.raise_()
        self.bal_onoff_5.raise_()
        self.bal_su_5.raise_()
        self.bal_clo_5.raise_()
        self.gridLayout.addWidget(self.bal_wi_5, 1, 0, 1, 1)
        self.bal_wi_6 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.bal_wi_6.setEnabled(True)
        self.bal_wi_6.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.bal_wi_6.setObjectName("bal_wi_6")
        self.bal_text_6 = QtWidgets.QLineEdit(self.bal_wi_6)
        self.bal_text_6.setEnabled(False)
        self.bal_text_6.setGeometry(QtCore.QRect(15, 12, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.bal_text_6.setFont(font)
        self.bal_text_6.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_text_6.setMaxLength(30)
        self.bal_text_6.setObjectName("bal_text_6")
        self.bal_btn_6 = QtWidgets.QPushButton(self.bal_wi_6)
        self.bal_btn_6.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.bal_btn_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_btn_6.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.bal_btn_6.setText("")
        self.bal_btn_6.setObjectName("bal_btn_6")
        self.bal_label_6 = QtWidgets.QLineEdit(self.bal_wi_6)
        self.bal_label_6.setEnabled(False)
        self.bal_label_6.setGeometry(QtCore.QRect(15, 45, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.bal_label_6.setFont(font)
        self.bal_label_6.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_label_6.setMaxLength(30)
        self.bal_label_6.setObjectName("bal_label_6")
        self.bal_onoff_6 = QtWidgets.QPushButton(self.bal_wi_6)
        self.bal_onoff_6.setGeometry(QtCore.QRect(160, 40, 91, 81))
        self.bal_onoff_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_onoff_6.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.bal_onoff_6.setText("")
        self.bal_onoff_6.setCheckable(True)
        self.bal_onoff_6.setChecked(False)
        self.bal_onoff_6.setObjectName("bal_onoff_6")
        self.bal_r_6 = QtWidgets.QLabel(self.bal_wi_6)
        self.bal_r_6.setGeometry(QtCore.QRect(55, 88, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_r_6.setFont(font)
        self.bal_r_6.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_r_6.setObjectName("bal_r_6")
        self.bal_b_6 = QtWidgets.QLabel(self.bal_wi_6)
        self.bal_b_6.setGeometry(QtCore.QRect(55, 129, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_b_6.setFont(font)
        self.bal_b_6.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_b_6.setObjectName("bal_b_6")
        self.bal_w_6 = QtWidgets.QLabel(self.bal_wi_6)
        self.bal_w_6.setGeometry(QtCore.QRect(55, 170, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_w_6.setFont(font)
        self.bal_w_6.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_w_6.setObjectName("bal_w_6")
        self.bal_su_6 = QtWidgets.QPushButton(self.bal_wi_6)
        self.bal_su_6.setGeometry(QtCore.QRect(185, 170, 31, 31))
        self.bal_su_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_su_6.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.bal_su_6.setText("")
        self.bal_su_6.setCheckable(True)
        self.bal_su_6.setObjectName("bal_su_6")
        self.bal_clo_6 = QtWidgets.QPushButton(self.bal_wi_6)
        self.bal_clo_6.setGeometry(QtCore.QRect(220, 170, 31, 31))
        self.bal_clo_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_clo_6.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.bal_clo_6.setText("")
        self.bal_clo_6.setCheckable(False)
        self.bal_clo_6.setObjectName("bal_clo_6")
        self.bal_r_6.raise_()
        self.bal_w_6.raise_()
        self.bal_b_6.raise_()
        self.bal_btn_6.raise_()
        self.bal_text_6.raise_()
        self.bal_label_6.raise_()
        self.bal_onoff_6.raise_()
        self.bal_su_6.raise_()
        self.bal_clo_6.raise_()
        self.gridLayout.addWidget(self.bal_wi_6, 1, 1, 1, 1)
        self.bal_wi_7 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.bal_wi_7.setEnabled(True)
        self.bal_wi_7.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.bal_wi_7.setObjectName("bal_wi_7")
        self.bal_text_7 = QtWidgets.QLineEdit(self.bal_wi_7)
        self.bal_text_7.setEnabled(False)
        self.bal_text_7.setGeometry(QtCore.QRect(15, 12, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.bal_text_7.setFont(font)
        self.bal_text_7.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_text_7.setMaxLength(30)
        self.bal_text_7.setObjectName("bal_text_7")
        self.bal_btn_7 = QtWidgets.QPushButton(self.bal_wi_7)
        self.bal_btn_7.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.bal_btn_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_btn_7.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.bal_btn_7.setText("")
        self.bal_btn_7.setObjectName("bal_btn_7")
        self.bal_label_7 = QtWidgets.QLineEdit(self.bal_wi_7)
        self.bal_label_7.setEnabled(False)
        self.bal_label_7.setGeometry(QtCore.QRect(15, 45, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.bal_label_7.setFont(font)
        self.bal_label_7.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_label_7.setMaxLength(30)
        self.bal_label_7.setObjectName("bal_label_7")
        self.bal_onoff_7 = QtWidgets.QPushButton(self.bal_wi_7)
        self.bal_onoff_7.setGeometry(QtCore.QRect(160, 40, 91, 81))
        self.bal_onoff_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_onoff_7.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.bal_onoff_7.setText("")
        self.bal_onoff_7.setCheckable(True)
        self.bal_onoff_7.setChecked(False)
        self.bal_onoff_7.setObjectName("bal_onoff_7")
        self.bal_r_7 = QtWidgets.QLabel(self.bal_wi_7)
        self.bal_r_7.setGeometry(QtCore.QRect(55, 88, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_r_7.setFont(font)
        self.bal_r_7.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_r_7.setObjectName("bal_r_7")
        self.bal_b_7 = QtWidgets.QLabel(self.bal_wi_7)
        self.bal_b_7.setGeometry(QtCore.QRect(55, 129, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_b_7.setFont(font)
        self.bal_b_7.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_b_7.setObjectName("bal_b_7")
        self.bal_w_7 = QtWidgets.QLabel(self.bal_wi_7)
        self.bal_w_7.setGeometry(QtCore.QRect(55, 170, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_w_7.setFont(font)
        self.bal_w_7.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_w_7.setObjectName("bal_w_7")
        self.bal_su_7 = QtWidgets.QPushButton(self.bal_wi_7)
        self.bal_su_7.setGeometry(QtCore.QRect(185, 170, 31, 31))
        self.bal_su_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_su_7.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.bal_su_7.setText("")
        self.bal_su_7.setCheckable(True)
        self.bal_su_7.setObjectName("bal_su_7")
        self.bal_clo_7 = QtWidgets.QPushButton(self.bal_wi_7)
        self.bal_clo_7.setGeometry(QtCore.QRect(220, 170, 31, 31))
        self.bal_clo_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_clo_7.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.bal_clo_7.setText("")
        self.bal_clo_7.setCheckable(False)
        self.bal_clo_7.setObjectName("bal_clo_7")
        self.bal_r_7.raise_()
        self.bal_b_7.raise_()
        self.bal_w_7.raise_()
        self.bal_btn_7.raise_()
        self.bal_text_7.raise_()
        self.bal_label_7.raise_()
        self.bal_onoff_7.raise_()
        self.bal_su_7.raise_()
        self.bal_clo_7.raise_()
        self.gridLayout.addWidget(self.bal_wi_7, 1, 2, 1, 1)
        self.bal_wi_8 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.bal_wi_8.setEnabled(True)
        self.bal_wi_8.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.bal_wi_8.setObjectName("bal_wi_8")
        self.bal_text_8 = QtWidgets.QLineEdit(self.bal_wi_8)
        self.bal_text_8.setEnabled(False)
        self.bal_text_8.setGeometry(QtCore.QRect(15, 12, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.bal_text_8.setFont(font)
        self.bal_text_8.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_text_8.setMaxLength(30)
        self.bal_text_8.setObjectName("bal_text_8")
        self.bal_btn_8 = QtWidgets.QPushButton(self.bal_wi_8)
        self.bal_btn_8.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.bal_btn_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_btn_8.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.bal_btn_8.setText("")
        self.bal_btn_8.setObjectName("bal_btn_8")
        self.bal_label_8 = QtWidgets.QLineEdit(self.bal_wi_8)
        self.bal_label_8.setEnabled(False)
        self.bal_label_8.setGeometry(QtCore.QRect(15, 45, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.bal_label_8.setFont(font)
        self.bal_label_8.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.bal_label_8.setMaxLength(30)
        self.bal_label_8.setObjectName("bal_label_8")
        self.bal_onoff_8 = QtWidgets.QPushButton(self.bal_wi_8)
        self.bal_onoff_8.setGeometry(QtCore.QRect(160, 40, 91, 81))
        self.bal_onoff_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_onoff_8.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.bal_onoff_8.setText("")
        self.bal_onoff_8.setCheckable(True)
        self.bal_onoff_8.setChecked(False)
        self.bal_onoff_8.setObjectName("bal_onoff_8")
        self.bal_r_8 = QtWidgets.QLabel(self.bal_wi_8)
        self.bal_r_8.setGeometry(QtCore.QRect(55, 88, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_r_8.setFont(font)
        self.bal_r_8.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_r_8.setObjectName("bal_r_8")
        self.bal_b_8 = QtWidgets.QLabel(self.bal_wi_8)
        self.bal_b_8.setGeometry(QtCore.QRect(55, 129, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_b_8.setFont(font)
        self.bal_b_8.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_b_8.setObjectName("bal_b_8")
        self.bal_w_8 = QtWidgets.QLabel(self.bal_wi_8)
        self.bal_w_8.setGeometry(QtCore.QRect(55, 170, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.bal_w_8.setFont(font)
        self.bal_w_8.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.bal_w_8.setObjectName("bal_w_8")
        self.bal_su_8 = QtWidgets.QPushButton(self.bal_wi_8)
        self.bal_su_8.setGeometry(QtCore.QRect(185, 170, 31, 31))
        self.bal_su_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_su_8.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.bal_su_8.setText("")
        self.bal_su_8.setCheckable(True)
        self.bal_su_8.setObjectName("bal_su_8")
        self.bal_clo_8 = QtWidgets.QPushButton(self.bal_wi_8)
        self.bal_clo_8.setGeometry(QtCore.QRect(220, 170, 31, 31))
        self.bal_clo_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_clo_8.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.bal_clo_8.setText("")
        self.bal_clo_8.setCheckable(False)
        self.bal_clo_8.setObjectName("bal_clo_8")
        self.bal_r_8.raise_()
        self.bal_b_8.raise_()
        self.bal_w_8.raise_()
        self.bal_btn_8.raise_()
        self.bal_text_8.raise_()
        self.bal_label_8.raise_()
        self.bal_onoff_8.raise_()
        self.bal_su_8.raise_()
        self.bal_clo_8.raise_()
        self.gridLayout.addWidget(self.bal_wi_8, 1, 3, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.balgi)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 480, 1411, 121))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_15 = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.widget_15.setStyleSheet("border-top : 2px solid rgb(217,217,217) ;")
        self.widget_15.setObjectName("widget_15")
        self.horizontalSlider_4 = QtWidgets.QSlider(self.widget_15)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(25, 55, 371, 51))
        self.horizontalSlider_4.setStyleSheet("\n"
"QSlider::groove:horizontal {\n"
"    height:4px;\n"
"    background: rgb(217,217,217);\n"
"\n"
"\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(./image/red_slide.png);\n"
"    width: 12px;\n"
"    height: 37px;\n"
"\n"
"    margin-top: -17px;\n"
"    margin-bottom: -16.5px;\n"
"\n"
"\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-image: url(./image/red_slide2.png);\n"
"    width: 12px;\n"
"    height: 37px;\n"
"    \n"
"    margin-top: -17px;\n"
"    margin-bottom: -16.5px;\n"
"\n"
"}\n"
"QSlider{\n"
"    border : 0px;\n"
"\n"
"}")
        self.horizontalSlider_4.setMaximum(100)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.label_9 = QtWidgets.QLabel(self.widget_15)
        self.label_9.setGeometry(QtCore.QRect(405, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("서울남산체 M")
        font.setPointSize(22)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border : 0px;")
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_15)
        self.pushButton_5.setGeometry(QtCore.QRect(395, 12, 71, 31))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton{image:url(./image/button_gray.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/button_red.png); border:0px;}\n"
"\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_10 = QtWidgets.QLabel(self.widget_15)
        self.label_10.setGeometry(QtCore.QRect(330, 8, 61, 41))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border : 0px;")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.widget_15)
        self.widget_14 = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.widget_14.setStyleSheet("border-top : 2px solid rgb(217,217,217) ;")
        self.widget_14.setObjectName("widget_14")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.widget_14)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(25, 55, 371, 51))
        self.horizontalSlider_3.setStyleSheet("\n"
"QSlider::groove:horizontal {\n"
"    height:4px;\n"
"    background: rgb(217,217,217);\n"
"\n"
"\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(./image/blue_slide.png);\n"
"    width: 12px;\n"
"    height: 37px;\n"
"\n"
"    margin-top: -17px;\n"
"    margin-bottom: -16.5px;\n"
"\n"
"\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-image: url(./image/blue_slide2.png);\n"
"    width: 12px;\n"
"    height: 37px;\n"
"    \n"
"    margin-top: -17px;\n"
"    margin-bottom: -16.5px;\n"
"\n"
"}\n"
"QSlider{\n"
"    border : 0px;\n"
"\n"
"}")
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.label_7 = QtWidgets.QLabel(self.widget_14)
        self.label_7.setGeometry(QtCore.QRect(405, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("서울남산체 M")
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border : 0px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_4.setGeometry(QtCore.QRect(395, 12, 71, 31))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{image:url(./image/button_gray.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/button_blue.png); border:0px;}\n"
"\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_8 = QtWidgets.QLabel(self.widget_14)
        self.label_8.setGeometry(QtCore.QRect(330, 8, 61, 41))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border : 0px;")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.widget_14)
        self.widget_13 = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.widget_13.setStyleSheet("border-top : 2px solid rgb(217,217,217) ;")
        self.widget_13.setObjectName("widget_13")
        self.horizontalSlider = QtWidgets.QSlider(self.widget_13)
        self.horizontalSlider.setGeometry(QtCore.QRect(25, 55, 371, 51))
        self.horizontalSlider.setStyleSheet("\n"
"QSlider::groove:horizontal {\n"
"    height:4px;\n"
"    background: rgb(217,217,217);\n"
"\n"
"\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(./image/black_slide.png);\n"
"    width: 12px;\n"
"    height: 37px;\n"
"\n"
"    margin-top: -17px;\n"
"    margin-bottom: -16.5px;\n"
"\n"
"\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-image: url(./image/black_slide2.png);\n"
"    width: 12px;\n"
"    height: 37px;\n"
"    \n"
"    margin-top: -17px;\n"
"    margin-bottom: -16.5px;\n"
"\n"
"}\n"
"QSlider{\n"
"    border : 0px;\n"
"\n"
"}")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_3 = QtWidgets.QLabel(self.widget_13)
        self.label_3.setGeometry(QtCore.QRect(405, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("서울남산체 M")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border : 0px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.widget_13)
        self.pushButton.setGeometry(QtCore.QRect(395, 12, 71, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{image:url(./image/button_gray.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/button_black.png); border:0px;}\n"
"\n"
"")
        self.pushButton.setText("")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.widget_13)
        self.label_4.setGeometry(QtCore.QRect(280, 8, 111, 41))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border : 0px;")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.widget_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.balgi)
        self.pushButton_14.setGeometry(QtCore.QRect(20, 210, 31, 61))
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet("QPushButton{image:url(./image/left_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/left_2.png); border:0px;}\n"
"")
        self.pushButton_14.setText("")
        self.pushButton_14.setCheckable(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.balgi)
        self.pushButton_15.setGeometry(QtCore.QRect(1360, 210, 31, 61))
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet("QPushButton{image:url(./image/right_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/right_2.png); border:0px;}\n"
"")
        self.pushButton_15.setText("")
        self.pushButton_15.setCheckable(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_29 = QtWidgets.QLabel(self.balgi)
        self.label_29.setGeometry(QtCore.QRect(40, 10, 41, 461))
        self.label_29.setStyleSheet("border : 0px;")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.gridLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.pushButton_15.raise_()
        self.label_29.raise_()
        self.pushButton_14.raise_()
        self.stackedWidget.addWidget(self.balgi)
        self.ondo = QtWidgets.QWidget()
        self.ondo.setObjectName("ondo")
        self.stackedWidget.addWidget(self.ondo)
        self.co2 = QtWidgets.QWidget()
        self.co2.setObjectName("co2")
        self.stackedWidget.addWidget(self.co2)
        self.yangak = QtWidgets.QWidget()
        self.yangak.setObjectName("yangak")
        self.stackedWidget.addWidget(self.yangak)
        self.kit_1 = QtWidgets.QWidget()
        self.kit_1.setObjectName("kit_1")
        self.pushButton_78 = QtWidgets.QPushButton(self.kit_1)
        self.pushButton_78.setGeometry(QtCore.QRect(20, 260, 31, 61))
        self.pushButton_78.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_78.setStyleSheet("QPushButton{image:url(./image/left_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/left_2.png); border:0px;}\n"
"")
        self.pushButton_78.setText("")
        self.pushButton_78.setCheckable(False)
        self.pushButton_78.setObjectName("pushButton_78")
        self.pushButton_79 = QtWidgets.QPushButton(self.kit_1)
        self.pushButton_79.setGeometry(QtCore.QRect(1360, 260, 31, 61))
        self.pushButton_79.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_79.setStyleSheet("QPushButton{image:url(./image/right_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/right_2.png); border:0px;}\n"
"")
        self.pushButton_79.setText("")
        self.pushButton_79.setCheckable(False)
        self.pushButton_79.setObjectName("pushButton_79")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.kit_1)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(60, 0, 1291, 591))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setContentsMargins(45, 10, 45, 10)
        self.gridLayout_5.setHorizontalSpacing(45)
        self.gridLayout_5.setVerticalSpacing(5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.w1_30 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.w1_30.setEnabled(True)
        self.w1_30.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_30.setObjectName("w1_30")
        self.lineEdit_61 = QtWidgets.QLineEdit(self.w1_30)
        self.lineEdit_61.setEnabled(False)
        self.lineEdit_61.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_61.setFont(font)
        self.lineEdit_61.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_61.setMaxLength(30)
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.pushButton_132 = QtWidgets.QPushButton(self.w1_30)
        self.pushButton_132.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_132.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_132.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_132.setText("")
        self.pushButton_132.setObjectName("pushButton_132")
        self.lineEdit_62 = QtWidgets.QLineEdit(self.w1_30)
        self.lineEdit_62.setEnabled(False)
        self.lineEdit_62.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_62.setFont(font)
        self.lineEdit_62.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_62.setMaxLength(30)
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.pushButton_133 = QtWidgets.QPushButton(self.w1_30)
        self.pushButton_133.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_133.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_133.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_133.setText("")
        self.pushButton_133.setCheckable(True)
        self.pushButton_133.setChecked(False)
        self.pushButton_133.setObjectName("pushButton_133")
        self.label_47 = QtWidgets.QLabel(self.w1_30)
        self.label_47.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_47.setObjectName("label_47")
        self.pushButton_134 = QtWidgets.QPushButton(self.w1_30)
        self.pushButton_134.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_134.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_134.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_134.setText("")
        self.pushButton_134.setCheckable(True)
        self.pushButton_134.setObjectName("pushButton_134")
        self.pushButton_135 = QtWidgets.QPushButton(self.w1_30)
        self.pushButton_135.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_135.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_135.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_135.setText("")
        self.pushButton_135.setCheckable(False)
        self.pushButton_135.setObjectName("pushButton_135")
        self.gridLayout_5.addWidget(self.w1_30, 0, 3, 1, 1)
        self.w1_31 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.w1_31.setEnabled(True)
        self.w1_31.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_31.setObjectName("w1_31")
        self.lineEdit_63 = QtWidgets.QLineEdit(self.w1_31)
        self.lineEdit_63.setEnabled(False)
        self.lineEdit_63.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_63.setFont(font)
        self.lineEdit_63.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_63.setMaxLength(30)
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.pushButton_136 = QtWidgets.QPushButton(self.w1_31)
        self.pushButton_136.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_136.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_136.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_136.setText("")
        self.pushButton_136.setObjectName("pushButton_136")
        self.lineEdit_64 = QtWidgets.QLineEdit(self.w1_31)
        self.lineEdit_64.setEnabled(False)
        self.lineEdit_64.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_64.setFont(font)
        self.lineEdit_64.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_64.setMaxLength(30)
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.pushButton_137 = QtWidgets.QPushButton(self.w1_31)
        self.pushButton_137.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_137.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_137.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_137.setText("")
        self.pushButton_137.setCheckable(True)
        self.pushButton_137.setChecked(False)
        self.pushButton_137.setObjectName("pushButton_137")
        self.label_48 = QtWidgets.QLabel(self.w1_31)
        self.label_48.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_48.setObjectName("label_48")
        self.pushButton_138 = QtWidgets.QPushButton(self.w1_31)
        self.pushButton_138.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_138.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_138.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_138.setText("")
        self.pushButton_138.setCheckable(True)
        self.pushButton_138.setObjectName("pushButton_138")
        self.pushButton_139 = QtWidgets.QPushButton(self.w1_31)
        self.pushButton_139.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_139.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_139.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_139.setText("")
        self.pushButton_139.setCheckable(False)
        self.pushButton_139.setObjectName("pushButton_139")
        self.gridLayout_5.addWidget(self.w1_31, 1, 3, 1, 1)
        self.w1_32 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.w1_32.setEnabled(True)
        self.w1_32.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_32.setObjectName("w1_32")
        self.lineEdit_65 = QtWidgets.QLineEdit(self.w1_32)
        self.lineEdit_65.setEnabled(False)
        self.lineEdit_65.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_65.setFont(font)
        self.lineEdit_65.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_65.setMaxLength(30)
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.pushButton_140 = QtWidgets.QPushButton(self.w1_32)
        self.pushButton_140.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_140.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_140.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_140.setText("")
        self.pushButton_140.setObjectName("pushButton_140")
        self.lineEdit_66 = QtWidgets.QLineEdit(self.w1_32)
        self.lineEdit_66.setEnabled(False)
        self.lineEdit_66.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_66.setFont(font)
        self.lineEdit_66.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_66.setMaxLength(30)
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.pushButton_141 = QtWidgets.QPushButton(self.w1_32)
        self.pushButton_141.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_141.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_141.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_141.setText("")
        self.pushButton_141.setCheckable(True)
        self.pushButton_141.setChecked(False)
        self.pushButton_141.setObjectName("pushButton_141")
        self.label_49 = QtWidgets.QLabel(self.w1_32)
        self.label_49.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_49.setObjectName("label_49")
        self.pushButton_142 = QtWidgets.QPushButton(self.w1_32)
        self.pushButton_142.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_142.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_142.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_142.setText("")
        self.pushButton_142.setCheckable(True)
        self.pushButton_142.setObjectName("pushButton_142")
        self.pushButton_143 = QtWidgets.QPushButton(self.w1_32)
        self.pushButton_143.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_143.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_143.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_143.setText("")
        self.pushButton_143.setCheckable(False)
        self.pushButton_143.setObjectName("pushButton_143")
        self.gridLayout_5.addWidget(self.w1_32, 0, 1, 1, 1)
        self.w1_25 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.w1_25.setEnabled(True)
        self.w1_25.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_25.setObjectName("w1_25")
        self.lineEdit_51 = QtWidgets.QLineEdit(self.w1_25)
        self.lineEdit_51.setEnabled(False)
        self.lineEdit_51.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_51.setFont(font)
        self.lineEdit_51.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_51.setMaxLength(30)
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.pushButton_112 = QtWidgets.QPushButton(self.w1_25)
        self.pushButton_112.setGeometry(QtCore.QRect(10, 0, 251, 181))
        self.pushButton_112.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_112.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_112.setText("")
        self.pushButton_112.setObjectName("pushButton_112")
        self.lineEdit_52 = QtWidgets.QLineEdit(self.w1_25)
        self.lineEdit_52.setEnabled(False)
        self.lineEdit_52.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_52.setFont(font)
        self.lineEdit_52.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_52.setMaxLength(30)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.pushButton_113 = QtWidgets.QPushButton(self.w1_25)
        self.pushButton_113.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pushButton_113.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_113.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_113.setText("")
        self.pushButton_113.setCheckable(True)
        self.pushButton_113.setChecked(False)
        self.pushButton_113.setObjectName("pushButton_113")
        self.label_41 = QtWidgets.QLabel(self.w1_25)
        self.label_41.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_41.setObjectName("label_41")
        self.pushButton_114 = QtWidgets.QPushButton(self.w1_25)
        self.pushButton_114.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pushButton_114.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_114.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_114.setText("")
        self.pushButton_114.setCheckable(True)
        self.pushButton_114.setObjectName("pushButton_114")
        self.pushButton_115 = QtWidgets.QPushButton(self.w1_25)
        self.pushButton_115.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pushButton_115.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_115.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_115.setText("")
        self.pushButton_115.setCheckable(False)
        self.pushButton_115.setObjectName("pushButton_115")
        self.label_42 = QtWidgets.QLabel(self.w1_25)
        self.label_42.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout_5.addWidget(self.w1_25, 0, 0, 1, 1)
        self.w1_34 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.w1_34.setEnabled(True)
        self.w1_34.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_34.setObjectName("w1_34")
        self.lineEdit_69 = QtWidgets.QLineEdit(self.w1_34)
        self.lineEdit_69.setEnabled(False)
        self.lineEdit_69.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_69.setFont(font)
        self.lineEdit_69.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_69.setMaxLength(30)
        self.lineEdit_69.setObjectName("lineEdit_69")
        self.pushButton_148 = QtWidgets.QPushButton(self.w1_34)
        self.pushButton_148.setGeometry(QtCore.QRect(10, 0, 251, 181))
        self.pushButton_148.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_148.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_148.setText("")
        self.pushButton_148.setObjectName("pushButton_148")
        self.lineEdit_70 = QtWidgets.QLineEdit(self.w1_34)
        self.lineEdit_70.setEnabled(False)
        self.lineEdit_70.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_70.setFont(font)
        self.lineEdit_70.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_70.setMaxLength(30)
        self.lineEdit_70.setObjectName("lineEdit_70")
        self.pushButton_149 = QtWidgets.QPushButton(self.w1_34)
        self.pushButton_149.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pushButton_149.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_149.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_149.setText("")
        self.pushButton_149.setCheckable(True)
        self.pushButton_149.setChecked(False)
        self.pushButton_149.setObjectName("pushButton_149")
        self.label_52 = QtWidgets.QLabel(self.w1_34)
        self.label_52.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_52.setObjectName("label_52")
        self.pushButton_150 = QtWidgets.QPushButton(self.w1_34)
        self.pushButton_150.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pushButton_150.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_150.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_150.setText("")
        self.pushButton_150.setCheckable(True)
        self.pushButton_150.setObjectName("pushButton_150")
        self.pushButton_151 = QtWidgets.QPushButton(self.w1_34)
        self.pushButton_151.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pushButton_151.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_151.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_151.setText("")
        self.pushButton_151.setCheckable(False)
        self.pushButton_151.setObjectName("pushButton_151")
        self.label_53 = QtWidgets.QLabel(self.w1_34)
        self.label_53.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.gridLayout_5.addWidget(self.w1_34, 2, 1, 1, 1)
        self.w1_26 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.w1_26.setEnabled(True)
        self.w1_26.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_26.setObjectName("w1_26")
        self.lineEdit_53 = QtWidgets.QLineEdit(self.w1_26)
        self.lineEdit_53.setEnabled(False)
        self.lineEdit_53.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_53.setFont(font)
        self.lineEdit_53.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_53.setMaxLength(30)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.pushButton_116 = QtWidgets.QPushButton(self.w1_26)
        self.pushButton_116.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_116.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_116.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_116.setText("")
        self.pushButton_116.setObjectName("pushButton_116")
        self.lineEdit_54 = QtWidgets.QLineEdit(self.w1_26)
        self.lineEdit_54.setEnabled(False)
        self.lineEdit_54.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_54.setFont(font)
        self.lineEdit_54.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_54.setMaxLength(30)
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.pushButton_117 = QtWidgets.QPushButton(self.w1_26)
        self.pushButton_117.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_117.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_117.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_117.setText("")
        self.pushButton_117.setCheckable(True)
        self.pushButton_117.setChecked(False)
        self.pushButton_117.setObjectName("pushButton_117")
        self.label_43 = QtWidgets.QLabel(self.w1_26)
        self.label_43.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_43.setObjectName("label_43")
        self.pushButton_118 = QtWidgets.QPushButton(self.w1_26)
        self.pushButton_118.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_118.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_118.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_118.setText("")
        self.pushButton_118.setCheckable(True)
        self.pushButton_118.setObjectName("pushButton_118")
        self.pushButton_119 = QtWidgets.QPushButton(self.w1_26)
        self.pushButton_119.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_119.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_119.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_119.setText("")
        self.pushButton_119.setCheckable(False)
        self.pushButton_119.setObjectName("pushButton_119")
        self.gridLayout_5.addWidget(self.w1_26, 0, 2, 1, 1)
        self.w1_27 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.w1_27.setEnabled(True)
        self.w1_27.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_27.setObjectName("w1_27")
        self.lineEdit_55 = QtWidgets.QLineEdit(self.w1_27)
        self.lineEdit_55.setEnabled(False)
        self.lineEdit_55.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_55.setFont(font)
        self.lineEdit_55.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_55.setMaxLength(30)
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.pushButton_120 = QtWidgets.QPushButton(self.w1_27)
        self.pushButton_120.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_120.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_120.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_120.setText("")
        self.pushButton_120.setObjectName("pushButton_120")
        self.lineEdit_56 = QtWidgets.QLineEdit(self.w1_27)
        self.lineEdit_56.setEnabled(False)
        self.lineEdit_56.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_56.setFont(font)
        self.lineEdit_56.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_56.setMaxLength(30)
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.pushButton_121 = QtWidgets.QPushButton(self.w1_27)
        self.pushButton_121.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_121.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_121.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_121.setText("")
        self.pushButton_121.setCheckable(True)
        self.pushButton_121.setChecked(False)
        self.pushButton_121.setObjectName("pushButton_121")
        self.label_44 = QtWidgets.QLabel(self.w1_27)
        self.label_44.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_44.setObjectName("label_44")
        self.pushButton_122 = QtWidgets.QPushButton(self.w1_27)
        self.pushButton_122.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_122.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_122.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_122.setText("")
        self.pushButton_122.setCheckable(True)
        self.pushButton_122.setObjectName("pushButton_122")
        self.pushButton_123 = QtWidgets.QPushButton(self.w1_27)
        self.pushButton_123.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_123.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_123.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_123.setText("")
        self.pushButton_123.setCheckable(False)
        self.pushButton_123.setObjectName("pushButton_123")
        self.gridLayout_5.addWidget(self.w1_27, 1, 0, 1, 1)
        self.w1_33 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.w1_33.setEnabled(True)
        self.w1_33.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_33.setObjectName("w1_33")
        self.lineEdit_67 = QtWidgets.QLineEdit(self.w1_33)
        self.lineEdit_67.setEnabled(False)
        self.lineEdit_67.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_67.setFont(font)
        self.lineEdit_67.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_67.setMaxLength(30)
        self.lineEdit_67.setObjectName("lineEdit_67")
        self.pushButton_144 = QtWidgets.QPushButton(self.w1_33)
        self.pushButton_144.setGeometry(QtCore.QRect(10, 0, 251, 181))
        self.pushButton_144.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_144.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_144.setText("")
        self.pushButton_144.setObjectName("pushButton_144")
        self.lineEdit_68 = QtWidgets.QLineEdit(self.w1_33)
        self.lineEdit_68.setEnabled(False)
        self.lineEdit_68.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_68.setFont(font)
        self.lineEdit_68.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_68.setMaxLength(30)
        self.lineEdit_68.setObjectName("lineEdit_68")
        self.pushButton_145 = QtWidgets.QPushButton(self.w1_33)
        self.pushButton_145.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pushButton_145.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_145.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_145.setText("")
        self.pushButton_145.setCheckable(True)
        self.pushButton_145.setChecked(False)
        self.pushButton_145.setObjectName("pushButton_145")
        self.label_50 = QtWidgets.QLabel(self.w1_33)
        self.label_50.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_50.setObjectName("label_50")
        self.pushButton_146 = QtWidgets.QPushButton(self.w1_33)
        self.pushButton_146.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pushButton_146.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_146.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_146.setText("")
        self.pushButton_146.setCheckable(True)
        self.pushButton_146.setObjectName("pushButton_146")
        self.pushButton_147 = QtWidgets.QPushButton(self.w1_33)
        self.pushButton_147.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pushButton_147.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_147.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_147.setText("")
        self.pushButton_147.setCheckable(False)
        self.pushButton_147.setObjectName("pushButton_147")
        self.label_51 = QtWidgets.QLabel(self.w1_33)
        self.label_51.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.gridLayout_5.addWidget(self.w1_33, 2, 0, 1, 1)
        self.w1_28 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.w1_28.setEnabled(True)
        self.w1_28.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_28.setObjectName("w1_28")
        self.lineEdit_57 = QtWidgets.QLineEdit(self.w1_28)
        self.lineEdit_57.setEnabled(False)
        self.lineEdit_57.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_57.setFont(font)
        self.lineEdit_57.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_57.setMaxLength(30)
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.pushButton_124 = QtWidgets.QPushButton(self.w1_28)
        self.pushButton_124.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_124.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_124.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_124.setText("")
        self.pushButton_124.setObjectName("pushButton_124")
        self.lineEdit_58 = QtWidgets.QLineEdit(self.w1_28)
        self.lineEdit_58.setEnabled(False)
        self.lineEdit_58.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_58.setFont(font)
        self.lineEdit_58.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_58.setMaxLength(30)
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.pushButton_125 = QtWidgets.QPushButton(self.w1_28)
        self.pushButton_125.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_125.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_125.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_125.setText("")
        self.pushButton_125.setCheckable(True)
        self.pushButton_125.setChecked(False)
        self.pushButton_125.setObjectName("pushButton_125")
        self.label_45 = QtWidgets.QLabel(self.w1_28)
        self.label_45.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_45.setObjectName("label_45")
        self.pushButton_126 = QtWidgets.QPushButton(self.w1_28)
        self.pushButton_126.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_126.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_126.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_126.setText("")
        self.pushButton_126.setCheckable(True)
        self.pushButton_126.setObjectName("pushButton_126")
        self.pushButton_127 = QtWidgets.QPushButton(self.w1_28)
        self.pushButton_127.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_127.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_127.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_127.setText("")
        self.pushButton_127.setCheckable(False)
        self.pushButton_127.setObjectName("pushButton_127")
        self.gridLayout_5.addWidget(self.w1_28, 1, 1, 1, 1)
        self.w1_29 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.w1_29.setEnabled(True)
        self.w1_29.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_29.setObjectName("w1_29")
        self.lineEdit_59 = QtWidgets.QLineEdit(self.w1_29)
        self.lineEdit_59.setEnabled(False)
        self.lineEdit_59.setGeometry(QtCore.QRect(15, 27, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_59.setFont(font)
        self.lineEdit_59.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_59.setMaxLength(30)
        self.lineEdit_59.setObjectName("lineEdit_59")
        self.pushButton_128 = QtWidgets.QPushButton(self.w1_29)
        self.pushButton_128.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.pushButton_128.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_128.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_128.setText("")
        self.pushButton_128.setObjectName("pushButton_128")
        self.lineEdit_60 = QtWidgets.QLineEdit(self.w1_29)
        self.lineEdit_60.setEnabled(False)
        self.lineEdit_60.setGeometry(QtCore.QRect(15, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_60.setFont(font)
        self.lineEdit_60.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_60.setMaxLength(30)
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.pushButton_129 = QtWidgets.QPushButton(self.w1_29)
        self.pushButton_129.setGeometry(QtCore.QRect(160, 50, 91, 81))
        self.pushButton_129.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_129.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_129.setText("")
        self.pushButton_129.setCheckable(True)
        self.pushButton_129.setChecked(False)
        self.pushButton_129.setObjectName("pushButton_129")
        self.label_46 = QtWidgets.QLabel(self.w1_29)
        self.label_46.setGeometry(QtCore.QRect(55, 107, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_46.setObjectName("label_46")
        self.pushButton_130 = QtWidgets.QPushButton(self.w1_29)
        self.pushButton_130.setGeometry(QtCore.QRect(185, 157, 31, 31))
        self.pushButton_130.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_130.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_130.setText("")
        self.pushButton_130.setCheckable(True)
        self.pushButton_130.setObjectName("pushButton_130")
        self.pushButton_131 = QtWidgets.QPushButton(self.w1_29)
        self.pushButton_131.setGeometry(QtCore.QRect(220, 157, 31, 31))
        self.pushButton_131.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_131.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_131.setText("")
        self.pushButton_131.setCheckable(False)
        self.pushButton_131.setObjectName("pushButton_131")
        self.gridLayout_5.addWidget(self.w1_29, 1, 2, 1, 1)
        self.w1_35 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.w1_35.setEnabled(True)
        self.w1_35.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_35.setObjectName("w1_35")
        self.lineEdit_71 = QtWidgets.QLineEdit(self.w1_35)
        self.lineEdit_71.setEnabled(False)
        self.lineEdit_71.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_71.setFont(font)
        self.lineEdit_71.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_71.setMaxLength(30)
        self.lineEdit_71.setObjectName("lineEdit_71")
        self.pushButton_152 = QtWidgets.QPushButton(self.w1_35)
        self.pushButton_152.setGeometry(QtCore.QRect(10, 0, 251, 181))
        self.pushButton_152.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_152.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_152.setText("")
        self.pushButton_152.setObjectName("pushButton_152")
        self.lineEdit_72 = QtWidgets.QLineEdit(self.w1_35)
        self.lineEdit_72.setEnabled(False)
        self.lineEdit_72.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_72.setFont(font)
        self.lineEdit_72.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_72.setMaxLength(30)
        self.lineEdit_72.setObjectName("lineEdit_72")
        self.pushButton_153 = QtWidgets.QPushButton(self.w1_35)
        self.pushButton_153.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pushButton_153.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_153.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_153.setText("")
        self.pushButton_153.setCheckable(True)
        self.pushButton_153.setChecked(False)
        self.pushButton_153.setObjectName("pushButton_153")
        self.label_54 = QtWidgets.QLabel(self.w1_35)
        self.label_54.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_54.setObjectName("label_54")
        self.pushButton_154 = QtWidgets.QPushButton(self.w1_35)
        self.pushButton_154.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pushButton_154.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_154.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_154.setText("")
        self.pushButton_154.setCheckable(True)
        self.pushButton_154.setObjectName("pushButton_154")
        self.pushButton_155 = QtWidgets.QPushButton(self.w1_35)
        self.pushButton_155.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pushButton_155.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_155.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_155.setText("")
        self.pushButton_155.setCheckable(False)
        self.pushButton_155.setObjectName("pushButton_155")
        self.label_55 = QtWidgets.QLabel(self.w1_35)
        self.label_55.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.gridLayout_5.addWidget(self.w1_35, 2, 2, 1, 1)
        self.w1_36 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.w1_36.setEnabled(True)
        self.w1_36.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.w1_36.setObjectName("w1_36")
        self.lineEdit_73 = QtWidgets.QLineEdit(self.w1_36)
        self.lineEdit_73.setEnabled(False)
        self.lineEdit_73.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.lineEdit_73.setFont(font)
        self.lineEdit_73.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_73.setMaxLength(30)
        self.lineEdit_73.setObjectName("lineEdit_73")
        self.pushButton_156 = QtWidgets.QPushButton(self.w1_36)
        self.pushButton_156.setGeometry(QtCore.QRect(10, 0, 251, 181))
        self.pushButton_156.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_156.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pushButton_156.setText("")
        self.pushButton_156.setObjectName("pushButton_156")
        self.lineEdit_74 = QtWidgets.QLineEdit(self.w1_36)
        self.lineEdit_74.setEnabled(False)
        self.lineEdit_74.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.lineEdit_74.setFont(font)
        self.lineEdit_74.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.lineEdit_74.setMaxLength(30)
        self.lineEdit_74.setObjectName("lineEdit_74")
        self.pushButton_157 = QtWidgets.QPushButton(self.w1_36)
        self.pushButton_157.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pushButton_157.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_157.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pushButton_157.setText("")
        self.pushButton_157.setCheckable(True)
        self.pushButton_157.setChecked(False)
        self.pushButton_157.setObjectName("pushButton_157")
        self.label_56 = QtWidgets.QLabel(self.w1_36)
        self.label_56.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.label_56.setObjectName("label_56")
        self.pushButton_158 = QtWidgets.QPushButton(self.w1_36)
        self.pushButton_158.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pushButton_158.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_158.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pushButton_158.setText("")
        self.pushButton_158.setCheckable(True)
        self.pushButton_158.setObjectName("pushButton_158")
        self.pushButton_159 = QtWidgets.QPushButton(self.w1_36)
        self.pushButton_159.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pushButton_159.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_159.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pushButton_159.setText("")
        self.pushButton_159.setCheckable(False)
        self.pushButton_159.setObjectName("pushButton_159")
        self.label_57 = QtWidgets.QLabel(self.w1_36)
        self.label_57.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.label_57.setAlignment(QtCore.Qt.AlignCenter)
        self.label_57.setObjectName("label_57")
        self.gridLayout_5.addWidget(self.w1_36, 2, 3, 1, 1)
        self.stackedWidget.addWidget(self.kit_1)
        self.kit_2 = QtWidgets.QWidget()
        self.kit_2.setObjectName("kit_2")
        self.stackedWidget.addWidget(self.kit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1460, 0, 311, 71))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border : 0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label.raise_()
        self.credit.raise_()
        self.set.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.stackedWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.horizontalSlider.valueChanged['int'].connect(self.label_3.setNum)
        self.horizontalSlider_4.sliderMoved['int'].connect(self.label_9.setNum)
        self.horizontalSlider_4.valueChanged['int'].connect(self.label_9.setNum)
        self.horizontalSlider_3.valueChanged['int'].connect(self.label_7.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chk_temp.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"69°"))
        self.chk_hum.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"74%"))
        self.chk_co2.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"58"))
        self.chk_ph2.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"82"))
        self.chk_tds.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"45"))
        self.chk_light.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"19"))
        self.label_12.setText(_translate("MainWindow", "100%"))
        self.lineEdit_3.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_4.setText(_translate("MainWindow", "L02"))
        self.label_13.setText(_translate("MainWindow", "100"))
        self.label_31.setText(_translate("MainWindow", "%"))
        self.lineEdit_13.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_14.setText(_translate("MainWindow", "L02"))
        self.label_18.setText(_translate("MainWindow", "100"))
        self.lineEdit_11.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_12.setText(_translate("MainWindow", "L02"))
        self.label_17.setText(_translate("MainWindow", "100"))
        self.lineEdit_9.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_10.setText(_translate("MainWindow", "L02"))
        self.label_16.setText(_translate("MainWindow", "100"))
        self.lineEdit_15.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_16.setText(_translate("MainWindow", "L02"))
        self.label_19.setText(_translate("MainWindow", "100"))
        self.lineEdit_17.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_18.setText(_translate("MainWindow", "L02"))
        self.label_20.setText(_translate("MainWindow", "100"))
        self.lineEdit_33.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_34.setText(_translate("MainWindow", "L02"))
        self.label_28.setText(_translate("MainWindow", "100"))
        self.lineEdit_7.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_8.setText(_translate("MainWindow", "L02"))
        self.label_15.setText(_translate("MainWindow", "100"))
        self.bal_text_1.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_1.setText(_translate("MainWindow", "L02"))
        self.bal_r_1.setText(_translate("MainWindow", "100"))
        self.bal_b_1.setText(_translate("MainWindow", "100"))
        self.bal_w_1.setText(_translate("MainWindow", "100"))
        self.bal_text_2.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_2.setText(_translate("MainWindow", "L02"))
        self.bal_r_2.setText(_translate("MainWindow", "100"))
        self.bal_b_2.setText(_translate("MainWindow", "100"))
        self.bal_w_2.setText(_translate("MainWindow", "100"))
        self.bal_text_3.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_3.setText(_translate("MainWindow", "L02"))
        self.bal_r_3.setText(_translate("MainWindow", "100"))
        self.bal_b_3.setText(_translate("MainWindow", "100"))
        self.bal_w_3.setText(_translate("MainWindow", "100"))
        self.bal_text_4.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_4.setText(_translate("MainWindow", "L02"))
        self.bal_r_4.setText(_translate("MainWindow", "100"))
        self.bal_b_4.setText(_translate("MainWindow", "100"))
        self.bal_w_4.setText(_translate("MainWindow", "100"))
        self.bal_text_5.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_5.setText(_translate("MainWindow", "L02"))
        self.bal_r_5.setText(_translate("MainWindow", "100"))
        self.bal_b_5.setText(_translate("MainWindow", "100"))
        self.bal_w_5.setText(_translate("MainWindow", "100"))
        self.bal_text_6.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_6.setText(_translate("MainWindow", "L02"))
        self.bal_r_6.setText(_translate("MainWindow", "100"))
        self.bal_b_6.setText(_translate("MainWindow", "100"))
        self.bal_w_6.setText(_translate("MainWindow", "100"))
        self.bal_text_7.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_7.setText(_translate("MainWindow", "L02"))
        self.bal_r_7.setText(_translate("MainWindow", "100"))
        self.bal_b_7.setText(_translate("MainWindow", "100"))
        self.bal_w_7.setText(_translate("MainWindow", "100"))
        self.bal_text_8.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_8.setText(_translate("MainWindow", "L02"))
        self.bal_r_8.setText(_translate("MainWindow", "100"))
        self.bal_b_8.setText(_translate("MainWindow", "100"))
        self.bal_w_8.setText(_translate("MainWindow", "100"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "RED"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "BLUE"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "WHITE"))
        self.lineEdit_61.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_62.setText(_translate("MainWindow", "L02"))
        self.label_47.setText(_translate("MainWindow", "100"))
        self.lineEdit_63.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_64.setText(_translate("MainWindow", "L02"))
        self.label_48.setText(_translate("MainWindow", "100"))
        self.lineEdit_65.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_66.setText(_translate("MainWindow", "L02"))
        self.label_49.setText(_translate("MainWindow", "100"))
        self.lineEdit_51.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_52.setText(_translate("MainWindow", "L02"))
        self.label_41.setText(_translate("MainWindow", "100"))
        self.label_42.setText(_translate("MainWindow", "%"))
        self.lineEdit_69.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_70.setText(_translate("MainWindow", "L02"))
        self.label_52.setText(_translate("MainWindow", "100"))
        self.label_53.setText(_translate("MainWindow", "%"))
        self.lineEdit_53.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_54.setText(_translate("MainWindow", "L02"))
        self.label_43.setText(_translate("MainWindow", "100"))
        self.lineEdit_55.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_56.setText(_translate("MainWindow", "L02"))
        self.label_44.setText(_translate("MainWindow", "100"))
        self.lineEdit_67.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_68.setText(_translate("MainWindow", "L02"))
        self.label_50.setText(_translate("MainWindow", "100"))
        self.label_51.setText(_translate("MainWindow", "%"))
        self.lineEdit_57.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_58.setText(_translate("MainWindow", "L02"))
        self.label_45.setText(_translate("MainWindow", "100"))
        self.lineEdit_59.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_60.setText(_translate("MainWindow", "L02"))
        self.label_46.setText(_translate("MainWindow", "100"))
        self.lineEdit_71.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_72.setText(_translate("MainWindow", "L02"))
        self.label_54.setText(_translate("MainWindow", "100"))
        self.label_55.setText(_translate("MainWindow", "%"))
        self.lineEdit_73.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.lineEdit_74.setText(_translate("MainWindow", "L02"))
        self.label_56.setText(_translate("MainWindow", "100"))
        self.label_57.setText(_translate("MainWindow", "%"))

