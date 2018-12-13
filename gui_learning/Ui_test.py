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
        MainWindow.resize(1916, 1076)
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
        self.stackedWidget.setGeometry(QtCore.QRect(508, 485, 1411, 595))
        self.stackedWidget.setStyleSheet("border-left : 2px solid rgb(217,217,217) ;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.grape = QtWidgets.QWidget()
        self.grape.setObjectName("grape")
        self.stackedWidget.addWidget(self.grape)
        self.song = QtWidgets.QWidget()
        self.song.setObjectName("song")
        self.stackedWidget.addWidget(self.song)
        self.balgi = QtWidgets.QWidget()
        self.balgi.setObjectName("balgi")
        self.gridLayoutWidget = QtWidgets.QWidget(self.balgi)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(59, 9, 1291, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_3.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px;}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px;}\n"
"\n"
"\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_6.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px;}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px;}\n"
"\n"
"\n"
"")
        self.widget_6.setObjectName("widget_6")
        self.gridLayout.addWidget(self.widget_6, 0, 2, 1, 1)
        self.widget_8 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_8.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px;}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px;}\n"
"\n"
"\n"
"")
        self.widget_8.setObjectName("widget_8")
        self.gridLayout.addWidget(self.widget_8, 1, 2, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_5.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px;}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px;}\n"
"\n"
"\n"
"")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout.addWidget(self.widget_5, 0, 1, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_7.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px;}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px;}\n"
"\n"
"\n"
"")
        self.widget_7.setObjectName("widget_7")
        self.gridLayout.addWidget(self.widget_7, 0, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_4.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px;}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px;}\n"
"\n"
"\n"
"")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 1, 1, 1, 1)
        self.widget_9 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_9.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px;}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px;}\n"
"\n"
"\n"
"")
        self.widget_9.setObjectName("widget_9")
        self.gridLayout.addWidget(self.widget_9, 0, 3, 1, 1)
        self.widget_10 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_10.setStyleSheet("QWidget{image:url(./image/kit_light.png); border:0px;}\n"
"QWidget:hover{image:url(./image/kit_light2.png); border:0px;}\n"
"\n"
"\n"
"")
        self.widget_10.setObjectName("widget_10")
        self.gridLayout.addWidget(self.widget_10, 1, 3, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.balgi)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 480, 1411, 121))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
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
"QPushButton:checked{image:url(./image/button_red.png); border:0px;}\n"
"\n"
"")
        self.pushButton.setText("")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.widget_13)
        self.label_4.setGeometry(QtCore.QRect(330, 10, 61, 41))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border : 0px;")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.widget_13)
        self.widget_12 = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.widget_12.setStyleSheet("border-top : 2px solid rgb(217,217,217) ;")
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout.addWidget(self.widget_12)
        self.widget_11 = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.widget_11.setStyleSheet("border-top : 2px solid rgb(217,217,217) ;")
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout.addWidget(self.widget_11)
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
        self.stackedWidget.addWidget(self.kit_1)
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
        self.stackedWidget.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.horizontalSlider.valueChanged['int'].connect(self.label_3.setNum)
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
        self.label_3.setText(_translate("MainWindow", "10"))
        self.label_4.setText(_translate("MainWindow", "RED"))

