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
        self.credit = QtWidgets.QPushButton(self.centralwidget)
        self.credit.setGeometry(QtCore.QRect(1790, 20, 40, 40))
        self.credit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credit.setStyleSheet("QPushButton{image:url(./image/credit.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/credit2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/credit2.png); border:0px;}\n"
"")
        self.credit.setText("")
        self.credit.setCheckable(True)
        self.credit.setObjectName("credit")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.credit)
        self.set = QtWidgets.QPushButton(self.centralwidget)
        self.set.setGeometry(QtCore.QRect(1850, 20, 40, 40))
        self.set.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set.setStyleSheet("QPushButton{image:url(./image/set.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/set2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/set2.png); border:0px;}\n"
"\n"
"\n"
"")
        self.set.setText("")
        self.set.setCheckable(True)
        self.set.setObjectName("set")
        self.buttonGroup.addButton(self.set)
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
        self.see_grap = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.see_grap.sizePolicy().hasHeightForWidth())
        self.see_grap.setSizePolicy(sizePolicy)
        self.see_grap.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.see_grap.setStyleSheet("QPushButton{image:url(./image/mon_graph.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/mon_graph2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/mon_graph2.png); border:0px;}\n"
"")
        self.see_grap.setText("")
        self.see_grap.setCheckable(True)
        self.see_grap.setChecked(False)
        self.see_grap.setFlat(False)
        self.see_grap.setObjectName("see_grap")
        self.buttonGroup.addButton(self.see_grap)
        self.verticalLayout.addWidget(self.see_grap)
        self.see_pen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.see_pen.sizePolicy().hasHeightForWidth())
        self.see_pen.setSizePolicy(sizePolicy)
        self.see_pen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.see_pen.setStyleSheet("QPushButton{image:url(./image/mon_pen.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/mon_pen2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/mon_pen2.png); border:0px;}\n"
"\n"
"")
        self.see_pen.setText("")
        self.see_pen.setCheckable(True)
        self.see_pen.setObjectName("see_pen")
        self.buttonGroup.addButton(self.see_pen)
        self.verticalLayout.addWidget(self.see_pen)
        self.see_bal = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.see_bal.sizePolicy().hasHeightForWidth())
        self.see_bal.setSizePolicy(sizePolicy)
        self.see_bal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.see_bal.setStyleSheet("QPushButton{image:url(./image/mon_light.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/mon_light2.png); border:0px;}\n"
"\n"
"\n"
"QPushButton:checked{image:url(./image/mon_light2.png); border:0px;}")
        self.see_bal.setText("")
        self.see_bal.setCheckable(True)
        self.see_bal.setObjectName("see_bal")
        self.buttonGroup.addButton(self.see_bal)
        self.verticalLayout.addWidget(self.see_bal)
        self.see_temp = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.see_temp.sizePolicy().hasHeightForWidth())
        self.see_temp.setSizePolicy(sizePolicy)
        self.see_temp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.see_temp.setStyleSheet("QPushButton{image:url(./image/mon_temp.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/mon_temp2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/mon_temp2.png); border:0px;}\n"
"\n"
"")
        self.see_temp.setText("")
        self.see_temp.setCheckable(True)
        self.see_temp.setObjectName("see_temp")
        self.buttonGroup.addButton(self.see_temp)
        self.verticalLayout.addWidget(self.see_temp)
        self.see_co2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.see_co2.sizePolicy().hasHeightForWidth())
        self.see_co2.setSizePolicy(sizePolicy)
        self.see_co2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.see_co2.setStyleSheet("QPushButton{image:url(./image/mon_co2.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/mon_co22.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/mon_co22.png); border:0px;}\n"
"\n"
"")
        self.see_co2.setText("")
        self.see_co2.setCheckable(True)
        self.see_co2.setObjectName("see_co2")
        self.buttonGroup.addButton(self.see_co2)
        self.verticalLayout.addWidget(self.see_co2)
        self.see_yang = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.see_yang.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.see_yang.sizePolicy().hasHeightForWidth())
        self.see_yang.setSizePolicy(sizePolicy)
        self.see_yang.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.see_yang.setStyleSheet("QPushButton{image:url(./image/mon_nutri.png); border:0px;}\n"
"QPushButton:hover{image:url(./image/mon_nutri2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/mon_nutri2.png); border:0px;}\n"
"\n"
"")
        self.see_yang.setText("")
        self.see_yang.setCheckable(True)
        self.see_yang.setObjectName("see_yang")
        self.buttonGroup.addButton(self.see_yang)
        self.verticalLayout.addWidget(self.see_yang)
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
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(507, 485, 1411, 595))
        self.stackedWidget.setStyleSheet("border-left : 2px solid rgb(217,217,217);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.grape = QtWidgets.QWidget()
        self.grape.setObjectName("grape")
        self.graphicsView = PlotWidget(self.grape)
        self.graphicsView.setGeometry(QtCore.QRect(35, 121, 1341, 451))
        self.graphicsView.setObjectName("graphicsView")
        self.grap_temp = QtWidgets.QPushButton(self.grape)
        self.grap_temp.setGeometry(QtCore.QRect(350, 30, 61, 40))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.grap_temp.setFont(font)
        self.grap_temp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.grap_temp.setStyleSheet("QPushButton{color : rgb(166,166,166);  border:0px;}\n"
"QPushButton:hover{color : rgb(0,176,80); border:0px;}\n"
"QPushButton:checked{color : rgb(0,176,80); border:0px;}\n"
"")
        self.grap_temp.setCheckable(True)
        self.grap_temp.setChecked(True)
        self.grap_temp.setObjectName("grap_temp")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.grap_temp)
        self.grap_hum = QtWidgets.QPushButton(self.grape)
        self.grap_hum.setGeometry(QtCore.QRect(560, 30, 61, 40))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.grap_hum.setFont(font)
        self.grap_hum.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.grap_hum.setStyleSheet("QPushButton{color : rgb(166,166,166);  border:0px;}\n"
"QPushButton:hover{color : rgb(0,176,80); border:0px;}\n"
"QPushButton:checked{color : rgb(0,176,80); border:0px;}\n"
"")
        self.grap_hum.setCheckable(True)
        self.grap_hum.setChecked(False)
        self.grap_hum.setObjectName("grap_hum")
        self.buttonGroup_2.addButton(self.grap_hum)
        self.grap_co2 = QtWidgets.QPushButton(self.grape)
        self.grap_co2.setGeometry(QtCore.QRect(770, 30, 61, 40))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.grap_co2.setFont(font)
        self.grap_co2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.grap_co2.setStyleSheet("QPushButton{color : rgb(166,166,166);  border:0px;}\n"
"QPushButton:hover{color : rgb(0,176,80); border:0px;}\n"
"QPushButton:checked{color : rgb(0,176,80); border:0px;}\n"
"")
        self.grap_co2.setCheckable(True)
        self.grap_co2.setChecked(False)
        self.grap_co2.setObjectName("grap_co2")
        self.buttonGroup_2.addButton(self.grap_co2)
        self.grap_light = QtWidgets.QPushButton(self.grape)
        self.grap_light.setGeometry(QtCore.QRect(980, 30, 61, 40))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.grap_light.setFont(font)
        self.grap_light.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.grap_light.setStyleSheet("QPushButton{color : rgb(166,166,166);  border:0px;}\n"
"QPushButton:hover{color : rgb(0,176,80); border:0px;}\n"
"QPushButton:checked{color : rgb(0,176,80); border:0px;}\n"
"")
        self.grap_light.setCheckable(True)
        self.grap_light.setChecked(False)
        self.grap_light.setObjectName("grap_light")
        self.buttonGroup_2.addButton(self.grap_light)
        self.grap_ch = QtWidgets.QLabel(self.grape)
        self.grap_ch.setGeometry(QtCore.QRect(350, 70, 61, 5))
        self.grap_ch.setStyleSheet("border : 0ox;\n"
"background-color : rgb(0,178,80);")
        self.grap_ch.setText("")
        self.grap_ch.setObjectName("grap_ch")
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
        self.pen_slider = QtWidgets.QSlider(self.song)
        self.pen_slider.setGeometry(QtCore.QRect(150, 450, 1071, 121))
        self.pen_slider.setStyleSheet("\n"
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
        self.pen_slider.setMaximum(100)
        self.pen_slider.setOrientation(QtCore.Qt.Horizontal)
        self.pen_slider.setObjectName("pen_slider")
        self.pen_value_label = QtWidgets.QLabel(self.song)
        self.pen_value_label.setGeometry(QtCore.QRect(1240, 480, 91, 61))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.pen_value_label.setFont(font)
        self.pen_value_label.setStyleSheet("border : 0px;\n"
"color : rgb(0,112,192);")
        self.pen_value_label.setTextFormat(QtCore.Qt.AutoText)
        self.pen_value_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pen_value_label.setObjectName("pen_value_label")
        self.pen_onoff_btn = QtWidgets.QPushButton(self.song)
        self.pen_onoff_btn.setGeometry(QtCore.QRect(10, 450, 131, 111))
        self.pen_onoff_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_onoff_btn.setStyleSheet("QPushButton{image:url(./image/off_big_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_big_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_big_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_big_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pen_onoff_btn.setText("")
        self.pen_onoff_btn.setCheckable(True)
        self.pen_onoff_btn.setChecked(False)
        self.pen_onoff_btn.setObjectName("pen_onoff_btn")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.song)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 10, 1291, 411))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(45, 10, 45, 10)
        self.gridLayout_2.setHorizontalSpacing(45)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pen_wi_1 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.pen_wi_1.setEnabled(True)
        self.pen_wi_1.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.pen_wi_1.setObjectName("pen_wi_1")
        self.pen_text_1 = QtWidgets.QLineEdit(self.pen_wi_1)
        self.pen_text_1.setEnabled(False)
        self.pen_text_1.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.pen_text_1.setFont(font)
        self.pen_text_1.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_text_1.setMaxLength(30)
        self.pen_text_1.setObjectName("pen_text_1")
        self.pen_btn_1 = QtWidgets.QPushButton(self.pen_wi_1)
        self.pen_btn_1.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.pen_btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_btn_1.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pen_btn_1.setText("")
        self.pen_btn_1.setObjectName("pen_btn_1")
        self.pen_label_1 = QtWidgets.QLineEdit(self.pen_wi_1)
        self.pen_label_1.setEnabled(False)
        self.pen_label_1.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.pen_label_1.setFont(font)
        self.pen_label_1.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_label_1.setMaxLength(30)
        self.pen_label_1.setObjectName("pen_label_1")
        self.pen_onoff_1 = QtWidgets.QPushButton(self.pen_wi_1)
        self.pen_onoff_1.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pen_onoff_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_onoff_1.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pen_onoff_1.setText("")
        self.pen_onoff_1.setCheckable(True)
        self.pen_onoff_1.setChecked(False)
        self.pen_onoff_1.setObjectName("pen_onoff_1")
        self.pen_value_1 = QtWidgets.QLabel(self.pen_wi_1)
        self.pen_value_1.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.pen_value_1.setFont(font)
        self.pen_value_1.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.pen_value_1.setObjectName("pen_value_1")
        self.pen_su_1 = QtWidgets.QPushButton(self.pen_wi_1)
        self.pen_su_1.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pen_su_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_su_1.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pen_su_1.setText("")
        self.pen_su_1.setCheckable(True)
        self.pen_su_1.setObjectName("pen_su_1")
        self.pen_clo_1 = QtWidgets.QPushButton(self.pen_wi_1)
        self.pen_clo_1.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pen_clo_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_clo_1.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pen_clo_1.setText("")
        self.pen_clo_1.setCheckable(False)
        self.pen_clo_1.setObjectName("pen_clo_1")
        self.pen_per_1 = QtWidgets.QLabel(self.pen_wi_1)
        self.pen_per_1.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.pen_per_1.setFont(font)
        self.pen_per_1.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.pen_per_1.setAlignment(QtCore.Qt.AlignCenter)
        self.pen_per_1.setObjectName("pen_per_1")
        self.pen_per_1.raise_()
        self.pen_value_1.raise_()
        self.pen_btn_1.raise_()
        self.pen_text_1.raise_()
        self.pen_label_1.raise_()
        self.pen_onoff_1.raise_()
        self.pen_su_1.raise_()
        self.pen_clo_1.raise_()
        self.gridLayout_2.addWidget(self.pen_wi_1, 0, 0, 1, 1)
        self.pen_wi_2 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.pen_wi_2.setEnabled(True)
        self.pen_wi_2.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.pen_wi_2.setObjectName("pen_wi_2")
        self.pen_text_2 = QtWidgets.QLineEdit(self.pen_wi_2)
        self.pen_text_2.setEnabled(False)
        self.pen_text_2.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.pen_text_2.setFont(font)
        self.pen_text_2.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_text_2.setMaxLength(30)
        self.pen_text_2.setObjectName("pen_text_2")
        self.pen_btn_2 = QtWidgets.QPushButton(self.pen_wi_2)
        self.pen_btn_2.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.pen_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_btn_2.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pen_btn_2.setText("")
        self.pen_btn_2.setObjectName("pen_btn_2")
        self.pen_label_2 = QtWidgets.QLineEdit(self.pen_wi_2)
        self.pen_label_2.setEnabled(False)
        self.pen_label_2.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.pen_label_2.setFont(font)
        self.pen_label_2.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_label_2.setMaxLength(30)
        self.pen_label_2.setObjectName("pen_label_2")
        self.pen_onoff_2 = QtWidgets.QPushButton(self.pen_wi_2)
        self.pen_onoff_2.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pen_onoff_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_onoff_2.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pen_onoff_2.setText("")
        self.pen_onoff_2.setCheckable(True)
        self.pen_onoff_2.setChecked(False)
        self.pen_onoff_2.setObjectName("pen_onoff_2")
        self.pen_value_2 = QtWidgets.QLabel(self.pen_wi_2)
        self.pen_value_2.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.pen_value_2.setFont(font)
        self.pen_value_2.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.pen_value_2.setObjectName("pen_value_2")
        self.pen_su_2 = QtWidgets.QPushButton(self.pen_wi_2)
        self.pen_su_2.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pen_su_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_su_2.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pen_su_2.setText("")
        self.pen_su_2.setCheckable(True)
        self.pen_su_2.setObjectName("pen_su_2")
        self.pen_clo_2 = QtWidgets.QPushButton(self.pen_wi_2)
        self.pen_clo_2.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pen_clo_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_clo_2.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pen_clo_2.setText("")
        self.pen_clo_2.setCheckable(False)
        self.pen_clo_2.setObjectName("pen_clo_2")
        self.pen_per_2 = QtWidgets.QLabel(self.pen_wi_2)
        self.pen_per_2.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.pen_per_2.setFont(font)
        self.pen_per_2.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.pen_per_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pen_per_2.setObjectName("pen_per_2")
        self.pen_value_2.raise_()
        self.pen_per_2.raise_()
        self.pen_text_2.raise_()
        self.pen_btn_2.raise_()
        self.pen_label_2.raise_()
        self.pen_onoff_2.raise_()
        self.pen_su_2.raise_()
        self.pen_clo_2.raise_()
        self.gridLayout_2.addWidget(self.pen_wi_2, 1, 0, 1, 1)
        self.pen_wi_5 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.pen_wi_5.setEnabled(True)
        self.pen_wi_5.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.pen_wi_5.setObjectName("pen_wi_5")
        self.pen_text_5 = QtWidgets.QLineEdit(self.pen_wi_5)
        self.pen_text_5.setEnabled(False)
        self.pen_text_5.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.pen_text_5.setFont(font)
        self.pen_text_5.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_text_5.setMaxLength(30)
        self.pen_text_5.setObjectName("pen_text_5")
        self.pen_btn_5 = QtWidgets.QPushButton(self.pen_wi_5)
        self.pen_btn_5.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.pen_btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_btn_5.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pen_btn_5.setText("")
        self.pen_btn_5.setObjectName("pen_btn_5")
        self.pen_label_5 = QtWidgets.QLineEdit(self.pen_wi_5)
        self.pen_label_5.setEnabled(False)
        self.pen_label_5.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.pen_label_5.setFont(font)
        self.pen_label_5.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_label_5.setMaxLength(30)
        self.pen_label_5.setObjectName("pen_label_5")
        self.pen_onoff_5 = QtWidgets.QPushButton(self.pen_wi_5)
        self.pen_onoff_5.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pen_onoff_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_onoff_5.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pen_onoff_5.setText("")
        self.pen_onoff_5.setCheckable(True)
        self.pen_onoff_5.setChecked(False)
        self.pen_onoff_5.setObjectName("pen_onoff_5")
        self.pen_value_5 = QtWidgets.QLabel(self.pen_wi_5)
        self.pen_value_5.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.pen_value_5.setFont(font)
        self.pen_value_5.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.pen_value_5.setObjectName("pen_value_5")
        self.pen_su_5 = QtWidgets.QPushButton(self.pen_wi_5)
        self.pen_su_5.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pen_su_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_su_5.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pen_su_5.setText("")
        self.pen_su_5.setCheckable(True)
        self.pen_su_5.setObjectName("pen_su_5")
        self.pen_clo_5 = QtWidgets.QPushButton(self.pen_wi_5)
        self.pen_clo_5.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pen_clo_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_clo_5.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pen_clo_5.setText("")
        self.pen_clo_5.setCheckable(False)
        self.pen_clo_5.setObjectName("pen_clo_5")
        self.pen_per_5 = QtWidgets.QLabel(self.pen_wi_5)
        self.pen_per_5.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.pen_per_5.setFont(font)
        self.pen_per_5.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.pen_per_5.setAlignment(QtCore.Qt.AlignCenter)
        self.pen_per_5.setObjectName("pen_per_5")
        self.pen_per_5.raise_()
        self.pen_value_5.raise_()
        self.pen_text_5.raise_()
        self.pen_btn_5.raise_()
        self.pen_label_5.raise_()
        self.pen_onoff_5.raise_()
        self.pen_su_5.raise_()
        self.pen_clo_5.raise_()
        self.gridLayout_2.addWidget(self.pen_wi_5, 0, 2, 1, 1)
        self.pen_wi_3 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.pen_wi_3.setEnabled(True)
        self.pen_wi_3.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.pen_wi_3.setObjectName("pen_wi_3")
        self.pen_text_3 = QtWidgets.QLineEdit(self.pen_wi_3)
        self.pen_text_3.setEnabled(False)
        self.pen_text_3.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.pen_text_3.setFont(font)
        self.pen_text_3.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_text_3.setMaxLength(30)
        self.pen_text_3.setObjectName("pen_text_3")
        self.pen_btn_3 = QtWidgets.QPushButton(self.pen_wi_3)
        self.pen_btn_3.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.pen_btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_btn_3.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pen_btn_3.setText("")
        self.pen_btn_3.setObjectName("pen_btn_3")
        self.pen_label_3 = QtWidgets.QLineEdit(self.pen_wi_3)
        self.pen_label_3.setEnabled(False)
        self.pen_label_3.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.pen_label_3.setFont(font)
        self.pen_label_3.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_label_3.setMaxLength(30)
        self.pen_label_3.setObjectName("pen_label_3")
        self.pen_onoff_3 = QtWidgets.QPushButton(self.pen_wi_3)
        self.pen_onoff_3.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pen_onoff_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_onoff_3.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pen_onoff_3.setText("")
        self.pen_onoff_3.setCheckable(True)
        self.pen_onoff_3.setChecked(False)
        self.pen_onoff_3.setObjectName("pen_onoff_3")
        self.pen_value_3 = QtWidgets.QLabel(self.pen_wi_3)
        self.pen_value_3.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.pen_value_3.setFont(font)
        self.pen_value_3.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.pen_value_3.setObjectName("pen_value_3")
        self.pen_su_3 = QtWidgets.QPushButton(self.pen_wi_3)
        self.pen_su_3.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pen_su_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_su_3.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pen_su_3.setText("")
        self.pen_su_3.setCheckable(True)
        self.pen_su_3.setObjectName("pen_su_3")
        self.pen_clo_3 = QtWidgets.QPushButton(self.pen_wi_3)
        self.pen_clo_3.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pen_clo_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_clo_3.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pen_clo_3.setText("")
        self.pen_clo_3.setCheckable(False)
        self.pen_clo_3.setObjectName("pen_clo_3")
        self.pen_per_3 = QtWidgets.QLabel(self.pen_wi_3)
        self.pen_per_3.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.pen_per_3.setFont(font)
        self.pen_per_3.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.pen_per_3.setAlignment(QtCore.Qt.AlignCenter)
        self.pen_per_3.setObjectName("pen_per_3")
        self.pen_per_3.raise_()
        self.pen_value_3.raise_()
        self.pen_text_3.raise_()
        self.pen_btn_3.raise_()
        self.pen_label_3.raise_()
        self.pen_onoff_3.raise_()
        self.pen_su_3.raise_()
        self.pen_clo_3.raise_()
        self.gridLayout_2.addWidget(self.pen_wi_3, 0, 1, 1, 1)
        self.pen_wi_4 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.pen_wi_4.setEnabled(True)
        self.pen_wi_4.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.pen_wi_4.setObjectName("pen_wi_4")
        self.pen_text_4 = QtWidgets.QLineEdit(self.pen_wi_4)
        self.pen_text_4.setEnabled(False)
        self.pen_text_4.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.pen_text_4.setFont(font)
        self.pen_text_4.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_text_4.setMaxLength(30)
        self.pen_text_4.setObjectName("pen_text_4")
        self.pen_btn_4 = QtWidgets.QPushButton(self.pen_wi_4)
        self.pen_btn_4.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.pen_btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_btn_4.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pen_btn_4.setText("")
        self.pen_btn_4.setObjectName("pen_btn_4")
        self.pen_label_4 = QtWidgets.QLineEdit(self.pen_wi_4)
        self.pen_label_4.setEnabled(False)
        self.pen_label_4.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.pen_label_4.setFont(font)
        self.pen_label_4.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_label_4.setMaxLength(30)
        self.pen_label_4.setObjectName("pen_label_4")
        self.pen_onoff_4 = QtWidgets.QPushButton(self.pen_wi_4)
        self.pen_onoff_4.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pen_onoff_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_onoff_4.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pen_onoff_4.setText("")
        self.pen_onoff_4.setCheckable(True)
        self.pen_onoff_4.setChecked(False)
        self.pen_onoff_4.setObjectName("pen_onoff_4")
        self.pen_value_4 = QtWidgets.QLabel(self.pen_wi_4)
        self.pen_value_4.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.pen_value_4.setFont(font)
        self.pen_value_4.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.pen_value_4.setObjectName("pen_value_4")
        self.pen_su_4 = QtWidgets.QPushButton(self.pen_wi_4)
        self.pen_su_4.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pen_su_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_su_4.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pen_su_4.setText("")
        self.pen_su_4.setCheckable(True)
        self.pen_su_4.setObjectName("pen_su_4")
        self.pen_clo_4 = QtWidgets.QPushButton(self.pen_wi_4)
        self.pen_clo_4.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pen_clo_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_clo_4.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pen_clo_4.setText("")
        self.pen_clo_4.setCheckable(False)
        self.pen_clo_4.setObjectName("pen_clo_4")
        self.pen_per_4 = QtWidgets.QLabel(self.pen_wi_4)
        self.pen_per_4.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.pen_per_4.setFont(font)
        self.pen_per_4.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.pen_per_4.setAlignment(QtCore.Qt.AlignCenter)
        self.pen_per_4.setObjectName("pen_per_4")
        self.pen_per_4.raise_()
        self.pen_value_4.raise_()
        self.pen_text_4.raise_()
        self.pen_btn_4.raise_()
        self.pen_label_4.raise_()
        self.pen_onoff_4.raise_()
        self.pen_su_4.raise_()
        self.pen_clo_4.raise_()
        self.gridLayout_2.addWidget(self.pen_wi_4, 1, 1, 1, 1)
        self.pen_wi_6 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.pen_wi_6.setEnabled(True)
        self.pen_wi_6.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.pen_wi_6.setObjectName("pen_wi_6")
        self.pen_text_6 = QtWidgets.QLineEdit(self.pen_wi_6)
        self.pen_text_6.setEnabled(False)
        self.pen_text_6.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.pen_text_6.setFont(font)
        self.pen_text_6.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_text_6.setMaxLength(30)
        self.pen_text_6.setObjectName("pen_text_6")
        self.pen_btn_6 = QtWidgets.QPushButton(self.pen_wi_6)
        self.pen_btn_6.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.pen_btn_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_btn_6.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pen_btn_6.setText("")
        self.pen_btn_6.setObjectName("pen_btn_6")
        self.pen_label_6 = QtWidgets.QLineEdit(self.pen_wi_6)
        self.pen_label_6.setEnabled(False)
        self.pen_label_6.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.pen_label_6.setFont(font)
        self.pen_label_6.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_label_6.setMaxLength(30)
        self.pen_label_6.setObjectName("pen_label_6")
        self.pen_onoff_6 = QtWidgets.QPushButton(self.pen_wi_6)
        self.pen_onoff_6.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pen_onoff_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_onoff_6.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pen_onoff_6.setText("")
        self.pen_onoff_6.setCheckable(True)
        self.pen_onoff_6.setChecked(False)
        self.pen_onoff_6.setObjectName("pen_onoff_6")
        self.pen_value_6 = QtWidgets.QLabel(self.pen_wi_6)
        self.pen_value_6.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.pen_value_6.setFont(font)
        self.pen_value_6.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.pen_value_6.setObjectName("pen_value_6")
        self.pen_su_6 = QtWidgets.QPushButton(self.pen_wi_6)
        self.pen_su_6.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pen_su_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_su_6.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pen_su_6.setText("")
        self.pen_su_6.setCheckable(True)
        self.pen_su_6.setObjectName("pen_su_6")
        self.pen_clo_6 = QtWidgets.QPushButton(self.pen_wi_6)
        self.pen_clo_6.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pen_clo_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_clo_6.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pen_clo_6.setText("")
        self.pen_clo_6.setCheckable(False)
        self.pen_clo_6.setObjectName("pen_clo_6")
        self.pen_per_6 = QtWidgets.QLabel(self.pen_wi_6)
        self.pen_per_6.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.pen_per_6.setFont(font)
        self.pen_per_6.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.pen_per_6.setAlignment(QtCore.Qt.AlignCenter)
        self.pen_per_6.setObjectName("pen_per_6")
        self.pen_per_6.raise_()
        self.pen_value_6.raise_()
        self.pen_text_6.raise_()
        self.pen_btn_6.raise_()
        self.pen_label_6.raise_()
        self.pen_onoff_6.raise_()
        self.pen_su_6.raise_()
        self.pen_clo_6.raise_()
        self.gridLayout_2.addWidget(self.pen_wi_6, 1, 2, 1, 1)
        self.pen_wi_7 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.pen_wi_7.setEnabled(True)
        self.pen_wi_7.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.pen_wi_7.setObjectName("pen_wi_7")
        self.pen_text_7 = QtWidgets.QLineEdit(self.pen_wi_7)
        self.pen_text_7.setEnabled(False)
        self.pen_text_7.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.pen_text_7.setFont(font)
        self.pen_text_7.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_text_7.setMaxLength(30)
        self.pen_text_7.setObjectName("pen_text_7")
        self.pen_btn_7 = QtWidgets.QPushButton(self.pen_wi_7)
        self.pen_btn_7.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.pen_btn_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_btn_7.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pen_btn_7.setText("")
        self.pen_btn_7.setObjectName("pen_btn_7")
        self.pen_label_7 = QtWidgets.QLineEdit(self.pen_wi_7)
        self.pen_label_7.setEnabled(False)
        self.pen_label_7.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.pen_label_7.setFont(font)
        self.pen_label_7.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_label_7.setMaxLength(30)
        self.pen_label_7.setObjectName("pen_label_7")
        self.pen_onoff_7 = QtWidgets.QPushButton(self.pen_wi_7)
        self.pen_onoff_7.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pen_onoff_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_onoff_7.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pen_onoff_7.setText("")
        self.pen_onoff_7.setCheckable(True)
        self.pen_onoff_7.setChecked(False)
        self.pen_onoff_7.setObjectName("pen_onoff_7")
        self.pen_value_7 = QtWidgets.QLabel(self.pen_wi_7)
        self.pen_value_7.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.pen_value_7.setFont(font)
        self.pen_value_7.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.pen_value_7.setObjectName("pen_value_7")
        self.pen_su_7 = QtWidgets.QPushButton(self.pen_wi_7)
        self.pen_su_7.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pen_su_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_su_7.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pen_su_7.setText("")
        self.pen_su_7.setCheckable(True)
        self.pen_su_7.setObjectName("pen_su_7")
        self.pen_clo_7 = QtWidgets.QPushButton(self.pen_wi_7)
        self.pen_clo_7.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pen_clo_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_clo_7.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pen_clo_7.setText("")
        self.pen_clo_7.setCheckable(False)
        self.pen_clo_7.setObjectName("pen_clo_7")
        self.pen_per_7 = QtWidgets.QLabel(self.pen_wi_7)
        self.pen_per_7.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.pen_per_7.setFont(font)
        self.pen_per_7.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.pen_per_7.setAlignment(QtCore.Qt.AlignCenter)
        self.pen_per_7.setObjectName("pen_per_7")
        self.pen_value_7.raise_()
        self.pen_per_7.raise_()
        self.pen_text_7.raise_()
        self.pen_btn_7.raise_()
        self.pen_label_7.raise_()
        self.pen_onoff_7.raise_()
        self.pen_su_7.raise_()
        self.pen_clo_7.raise_()
        self.gridLayout_2.addWidget(self.pen_wi_7, 0, 3, 1, 1)
        self.pen_wi_8 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.pen_wi_8.setEnabled(True)
        self.pen_wi_8.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.pen_wi_8.setObjectName("pen_wi_8")
        self.pen_text_8 = QtWidgets.QLineEdit(self.pen_wi_8)
        self.pen_text_8.setEnabled(False)
        self.pen_text_8.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.pen_text_8.setFont(font)
        self.pen_text_8.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_text_8.setMaxLength(30)
        self.pen_text_8.setObjectName("pen_text_8")
        self.pen_btn_8 = QtWidgets.QPushButton(self.pen_wi_8)
        self.pen_btn_8.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.pen_btn_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_btn_8.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.pen_btn_8.setText("")
        self.pen_btn_8.setObjectName("pen_btn_8")
        self.pen_label_8 = QtWidgets.QLineEdit(self.pen_wi_8)
        self.pen_label_8.setEnabled(False)
        self.pen_label_8.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.pen_label_8.setFont(font)
        self.pen_label_8.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.pen_label_8.setMaxLength(30)
        self.pen_label_8.setObjectName("pen_label_8")
        self.pen_onoff_8 = QtWidgets.QPushButton(self.pen_wi_8)
        self.pen_onoff_8.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.pen_onoff_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_onoff_8.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.pen_onoff_8.setText("")
        self.pen_onoff_8.setCheckable(True)
        self.pen_onoff_8.setChecked(False)
        self.pen_onoff_8.setObjectName("pen_onoff_8")
        self.pen_value_8 = QtWidgets.QLabel(self.pen_wi_8)
        self.pen_value_8.setGeometry(QtCore.QRect(55, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.pen_value_8.setFont(font)
        self.pen_value_8.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"")
        self.pen_value_8.setObjectName("pen_value_8")
        self.pen_su_8 = QtWidgets.QPushButton(self.pen_wi_8)
        self.pen_su_8.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.pen_su_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_su_8.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.pen_su_8.setText("")
        self.pen_su_8.setCheckable(True)
        self.pen_su_8.setObjectName("pen_su_8")
        self.pen_clo_8 = QtWidgets.QPushButton(self.pen_wi_8)
        self.pen_clo_8.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.pen_clo_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_clo_8.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.pen_clo_8.setText("")
        self.pen_clo_8.setCheckable(False)
        self.pen_clo_8.setObjectName("pen_clo_8")
        self.pen_per_8 = QtWidgets.QLabel(self.pen_wi_8)
        self.pen_per_8.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.pen_per_8.setFont(font)
        self.pen_per_8.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.pen_per_8.setAlignment(QtCore.Qt.AlignCenter)
        self.pen_per_8.setObjectName("pen_per_8")
        self.pen_value_8.raise_()
        self.pen_per_8.raise_()
        self.pen_text_8.raise_()
        self.pen_btn_8.raise_()
        self.pen_label_8.raise_()
        self.pen_onoff_8.raise_()
        self.pen_su_8.raise_()
        self.pen_clo_8.raise_()
        self.gridLayout_2.addWidget(self.pen_wi_8, 1, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.song)
        self.label_30.setGeometry(QtCore.QRect(30, 0, 41, 421))
        self.label_30.setStyleSheet("border : 0px;")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.pen_right_btn = QtWidgets.QPushButton(self.song)
        self.pen_right_btn.setGeometry(QtCore.QRect(1360, 180, 31, 61))
        self.pen_right_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_right_btn.setStyleSheet("QPushButton{image:url(./image/right_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/right_2.png); border:0px;}\n"
"")
        self.pen_right_btn.setText("")
        self.pen_right_btn.setCheckable(False)
        self.pen_right_btn.setObjectName("pen_right_btn")
        self.pen_left_btn = QtWidgets.QPushButton(self.song)
        self.pen_left_btn.setGeometry(QtCore.QRect(20, 180, 31, 61))
        self.pen_left_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pen_left_btn.setStyleSheet("QPushButton{image:url(./image/left_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/left_2.png); border:0px;}\n"
"")
        self.pen_left_btn.setText("")
        self.pen_left_btn.setCheckable(False)
        self.pen_left_btn.setObjectName("pen_left_btn")
        self.pen_value_label_2 = QtWidgets.QLabel(self.song)
        self.pen_value_label_2.setGeometry(QtCore.QRect(1334, 480, 91, 61))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(36)
        self.pen_value_label_2.setFont(font)
        self.pen_value_label_2.setStyleSheet("border : 0px;\n"
"color : rgb(0,112,192);")
        self.pen_value_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.pen_value_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pen_value_label_2.setObjectName("pen_value_label_2")
        self.stackedWidget.addWidget(self.song)
        self.balgi = QtWidgets.QWidget()
        self.balgi.setObjectName("balgi")
        self.gridLayoutWidget = QtWidgets.QWidget(self.balgi)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(79, 9, 1251, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.bal_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.bal_layout.setContentsMargins(25, 12, 25, 12)
        self.bal_layout.setHorizontalSpacing(45)
        self.bal_layout.setVerticalSpacing(10)
        self.bal_layout.setObjectName("bal_layout")
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
        self.bal_btn_1.setGeometry(QtCore.QRect(0, 0, 261, 211))
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
        self.bal_layout.addWidget(self.bal_wi_1, 0, 0, 1, 1)
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
        self.bal_btn_6.setGeometry(QtCore.QRect(0, 0, 261, 211))
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
        self.bal_layout.addWidget(self.bal_wi_6, 1, 2, 1, 1)
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
        self.bal_btn_8.setGeometry(QtCore.QRect(0, 0, 261, 211))
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
        self.bal_layout.addWidget(self.bal_wi_8, 1, 4, 1, 1)
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
        self.bal_btn_3.setGeometry(QtCore.QRect(0, 0, 261, 211))
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
        self.bal_layout.addWidget(self.bal_wi_3, 0, 1, 1, 1)
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
        self.bal_btn_5.setGeometry(QtCore.QRect(0, 0, 261, 211))
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
        self.bal_layout.addWidget(self.bal_wi_5, 0, 2, 1, 1)
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
        self.bal_btn_2.setGeometry(QtCore.QRect(0, 0, 261, 211))
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
        self.bal_layout.addWidget(self.bal_wi_2, 1, 0, 1, 1)
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
        self.bal_btn_4.setGeometry(QtCore.QRect(0, 0, 261, 211))
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
        self.bal_layout.addWidget(self.bal_wi_4, 1, 1, 1, 1)
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
        self.bal_btn_7.setGeometry(QtCore.QRect(0, 0, 261, 211))
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
        self.bal_layout.addWidget(self.bal_wi_7, 0, 4, 1, 1)
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
        self.bal_r_val = QtWidgets.QSlider(self.widget_15)
        self.bal_r_val.setGeometry(QtCore.QRect(25, 55, 371, 51))
        self.bal_r_val.setStyleSheet("\n"
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
        self.bal_r_val.setMaximum(255)
        self.bal_r_val.setOrientation(QtCore.Qt.Horizontal)
        self.bal_r_val.setObjectName("bal_r_val")
        self.bal_r_num = QtWidgets.QLabel(self.widget_15)
        self.bal_r_num.setGeometry(QtCore.QRect(405, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("서울남산체 M")
        font.setPointSize(22)
        self.bal_r_num.setFont(font)
        self.bal_r_num.setStyleSheet("border : 0px;")
        self.bal_r_num.setTextFormat(QtCore.Qt.AutoText)
        self.bal_r_num.setAlignment(QtCore.Qt.AlignCenter)
        self.bal_r_num.setObjectName("bal_r_num")
        self.bal_r_btn = QtWidgets.QPushButton(self.widget_15)
        self.bal_r_btn.setGeometry(QtCore.QRect(395, 12, 71, 31))
        self.bal_r_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_r_btn.setStyleSheet("QPushButton{image:url(./image/button_gray.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/button_red.png); border:0px;}\n"
"\n"
"")
        self.bal_r_btn.setText("")
        self.bal_r_btn.setCheckable(True)
        self.bal_r_btn.setChecked(False)
        self.bal_r_btn.setObjectName("bal_r_btn")
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
        self.bal_b_val = QtWidgets.QSlider(self.widget_14)
        self.bal_b_val.setGeometry(QtCore.QRect(25, 55, 371, 51))
        self.bal_b_val.setStyleSheet("\n"
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
        self.bal_b_val.setMaximum(255)
        self.bal_b_val.setOrientation(QtCore.Qt.Horizontal)
        self.bal_b_val.setObjectName("bal_b_val")
        self.bal_b_num = QtWidgets.QLabel(self.widget_14)
        self.bal_b_num.setGeometry(QtCore.QRect(405, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("서울남산체 M")
        font.setPointSize(22)
        self.bal_b_num.setFont(font)
        self.bal_b_num.setStyleSheet("border : 0px;")
        self.bal_b_num.setAlignment(QtCore.Qt.AlignCenter)
        self.bal_b_num.setObjectName("bal_b_num")
        self.bal_b_btn = QtWidgets.QPushButton(self.widget_14)
        self.bal_b_btn.setGeometry(QtCore.QRect(395, 12, 71, 31))
        self.bal_b_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_b_btn.setStyleSheet("QPushButton{image:url(./image/button_gray.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/button_blue.png); border:0px;}\n"
"\n"
"")
        self.bal_b_btn.setText("")
        self.bal_b_btn.setCheckable(True)
        self.bal_b_btn.setChecked(False)
        self.bal_b_btn.setObjectName("bal_b_btn")
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
        self.bal_w_val = QtWidgets.QSlider(self.widget_13)
        self.bal_w_val.setGeometry(QtCore.QRect(25, 55, 371, 51))
        self.bal_w_val.setStyleSheet("\n"
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
        self.bal_w_val.setMaximum(255)
        self.bal_w_val.setOrientation(QtCore.Qt.Horizontal)
        self.bal_w_val.setObjectName("bal_w_val")
        self.bal_w_num = QtWidgets.QLabel(self.widget_13)
        self.bal_w_num.setGeometry(QtCore.QRect(405, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("서울남산체 M")
        font.setPointSize(22)
        self.bal_w_num.setFont(font)
        self.bal_w_num.setStyleSheet("border : 0px;")
        self.bal_w_num.setAlignment(QtCore.Qt.AlignCenter)
        self.bal_w_num.setObjectName("bal_w_num")
        self.bal_w_btn = QtWidgets.QPushButton(self.widget_13)
        self.bal_w_btn.setGeometry(QtCore.QRect(395, 12, 71, 31))
        self.bal_w_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_w_btn.setStyleSheet("QPushButton{image:url(./image/button_gray.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/button_black.png); border:0px;}\n"
"\n"
"")
        self.bal_w_btn.setText("")
        self.bal_w_btn.setCheckable(True)
        self.bal_w_btn.setChecked(False)
        self.bal_w_btn.setObjectName("bal_w_btn")
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
        self.bal_left_btn = QtWidgets.QPushButton(self.balgi)
        self.bal_left_btn.setGeometry(QtCore.QRect(30, 210, 31, 61))
        self.bal_left_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_left_btn.setStyleSheet("QPushButton{image:url(./image/left_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/left_2.png); border:0px;}\n"
"")
        self.bal_left_btn.setText("")
        self.bal_left_btn.setCheckable(False)
        self.bal_left_btn.setObjectName("bal_left_btn")
        self.bal_right_btn = QtWidgets.QPushButton(self.balgi)
        self.bal_right_btn.setGeometry(QtCore.QRect(1350, 210, 31, 61))
        self.bal_right_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal_right_btn.setStyleSheet("QPushButton{image:url(./image/right_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/right_2.png); border:0px;}\n"
"")
        self.bal_right_btn.setText("")
        self.bal_right_btn.setCheckable(False)
        self.bal_right_btn.setObjectName("bal_right_btn")
        self.label_29 = QtWidgets.QLabel(self.balgi)
        self.label_29.setGeometry(QtCore.QRect(40, 10, 41, 461))
        self.label_29.setStyleSheet("border : 0px;")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.gridLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.bal_right_btn.raise_()
        self.label_29.raise_()
        self.bal_left_btn.raise_()
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
        self.kit = QtWidgets.QWidget()
        self.kit.setObjectName("kit")
        self.kit_left_btn = QtWidgets.QPushButton(self.kit)
        self.kit_left_btn.setGeometry(QtCore.QRect(40, 260, 31, 61))
        self.kit_left_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_left_btn.setStyleSheet("QPushButton{image:url(./image/left_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/left_2.png); border:0px;}\n"
"")
        self.kit_left_btn.setText("")
        self.kit_left_btn.setCheckable(False)
        self.kit_left_btn.setObjectName("kit_left_btn")
        self.kit_right_btn = QtWidgets.QPushButton(self.kit)
        self.kit_right_btn.setGeometry(QtCore.QRect(1340, 260, 31, 61))
        self.kit_right_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_right_btn.setStyleSheet("QPushButton{image:url(./image/right_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/right_2.png); border:0px;}\n"
"")
        self.kit_right_btn.setText("")
        self.kit_right_btn.setCheckable(False)
        self.kit_right_btn.setObjectName("kit_right_btn")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.kit)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(60, 0, 1291, 591))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.kit_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.kit_layout.setContentsMargins(45, 10, 45, 10)
        self.kit_layout.setHorizontalSpacing(45)
        self.kit_layout.setVerticalSpacing(5)
        self.kit_layout.setObjectName("kit_layout")
        self.kit_wi_4 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.kit_wi_4.setEnabled(True)
        self.kit_wi_4.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.kit_wi_4.setObjectName("kit_wi_4")
        self.kit_text_4 = QtWidgets.QLineEdit(self.kit_wi_4)
        self.kit_text_4.setEnabled(False)
        self.kit_text_4.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.kit_text_4.setFont(font)
        self.kit_text_4.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_text_4.setMaxLength(30)
        self.kit_text_4.setObjectName("kit_text_4")
        self.kit_btn_4 = QtWidgets.QPushButton(self.kit_wi_4)
        self.kit_btn_4.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.kit_btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_btn_4.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.kit_btn_4.setText("")
        self.kit_btn_4.setObjectName("kit_btn_4")
        self.kit_label_4 = QtWidgets.QLineEdit(self.kit_wi_4)
        self.kit_label_4.setEnabled(False)
        self.kit_label_4.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.kit_label_4.setFont(font)
        self.kit_label_4.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_label_4.setMaxLength(30)
        self.kit_label_4.setObjectName("kit_label_4")
        self.kit_onoff_4 = QtWidgets.QPushButton(self.kit_wi_4)
        self.kit_onoff_4.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.kit_onoff_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_onoff_4.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.kit_onoff_4.setText("")
        self.kit_onoff_4.setCheckable(True)
        self.kit_onoff_4.setChecked(False)
        self.kit_onoff_4.setObjectName("kit_onoff_4")
        self.kit_su_4 = QtWidgets.QPushButton(self.kit_wi_4)
        self.kit_su_4.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.kit_su_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_su_4.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.kit_su_4.setText("")
        self.kit_su_4.setCheckable(True)
        self.kit_su_4.setObjectName("kit_su_4")
        self.kit_clo_4 = QtWidgets.QPushButton(self.kit_wi_4)
        self.kit_clo_4.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.kit_clo_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_clo_4.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.kit_clo_4.setText("")
        self.kit_clo_4.setCheckable(False)
        self.kit_clo_4.setObjectName("kit_clo_4")
        self.kit_icon_4 = QtWidgets.QLabel(self.kit_wi_4)
        self.kit_icon_4.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.kit_icon_4.setFont(font)
        self.kit_icon_4.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.kit_icon_4.setAlignment(QtCore.Qt.AlignCenter)
        self.kit_icon_4.setObjectName("kit_icon_4")
        self.kit_value_4 = QtWidgets.QLineEdit(self.kit_wi_4)
        self.kit_value_4.setEnabled(False)
        self.kit_value_4.setGeometry(QtCore.QRect(55, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.kit_value_4.setFont(font)
        self.kit_value_4.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}")
        self.kit_value_4.setMaxLength(10)
        self.kit_value_4.setObjectName("kit_value_4")
        self.kit_layout.addWidget(self.kit_wi_4, 0, 1, 1, 1)
        self.kit_wi_1 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.kit_wi_1.setEnabled(True)
        self.kit_wi_1.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.kit_wi_1.setObjectName("kit_wi_1")
        self.kit_text_1 = QtWidgets.QLineEdit(self.kit_wi_1)
        self.kit_text_1.setEnabled(False)
        self.kit_text_1.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.kit_text_1.setFont(font)
        self.kit_text_1.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_text_1.setMaxLength(30)
        self.kit_text_1.setObjectName("kit_text_1")
        self.kit_btn_1 = QtWidgets.QPushButton(self.kit_wi_1)
        self.kit_btn_1.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.kit_btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_btn_1.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.kit_btn_1.setText("")
        self.kit_btn_1.setObjectName("kit_btn_1")
        self.kit_label_1 = QtWidgets.QLineEdit(self.kit_wi_1)
        self.kit_label_1.setEnabled(False)
        self.kit_label_1.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.kit_label_1.setFont(font)
        self.kit_label_1.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_label_1.setMaxLength(30)
        self.kit_label_1.setObjectName("kit_label_1")
        self.kit_onoff_1 = QtWidgets.QPushButton(self.kit_wi_1)
        self.kit_onoff_1.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.kit_onoff_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_onoff_1.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.kit_onoff_1.setText("")
        self.kit_onoff_1.setCheckable(True)
        self.kit_onoff_1.setChecked(False)
        self.kit_onoff_1.setObjectName("kit_onoff_1")
        self.kit_su_1 = QtWidgets.QPushButton(self.kit_wi_1)
        self.kit_su_1.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.kit_su_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_su_1.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.kit_su_1.setText("")
        self.kit_su_1.setCheckable(True)
        self.kit_su_1.setObjectName("kit_su_1")
        self.kit_clo_1 = QtWidgets.QPushButton(self.kit_wi_1)
        self.kit_clo_1.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.kit_clo_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_clo_1.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.kit_clo_1.setText("")
        self.kit_clo_1.setCheckable(False)
        self.kit_clo_1.setObjectName("kit_clo_1")
        self.kit_icon_1 = QtWidgets.QLabel(self.kit_wi_1)
        self.kit_icon_1.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.kit_icon_1.setFont(font)
        self.kit_icon_1.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.kit_icon_1.setAlignment(QtCore.Qt.AlignCenter)
        self.kit_icon_1.setObjectName("kit_icon_1")
        self.kit_value_1 = QtWidgets.QLineEdit(self.kit_wi_1)
        self.kit_value_1.setEnabled(False)
        self.kit_value_1.setGeometry(QtCore.QRect(55, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.kit_value_1.setFont(font)
        self.kit_value_1.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}")
        self.kit_value_1.setMaxLength(10)
        self.kit_value_1.setObjectName("kit_value_1")
        self.kit_btn_1.raise_()
        self.kit_text_1.raise_()
        self.kit_label_1.raise_()
        self.kit_onoff_1.raise_()
        self.kit_su_1.raise_()
        self.kit_clo_1.raise_()
        self.kit_icon_1.raise_()
        self.kit_value_1.raise_()
        self.kit_layout.addWidget(self.kit_wi_1, 0, 0, 1, 1)
        self.kit_wi_2 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.kit_wi_2.setEnabled(True)
        self.kit_wi_2.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.kit_wi_2.setObjectName("kit_wi_2")
        self.kit_text_2 = QtWidgets.QLineEdit(self.kit_wi_2)
        self.kit_text_2.setEnabled(False)
        self.kit_text_2.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.kit_text_2.setFont(font)
        self.kit_text_2.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_text_2.setMaxLength(30)
        self.kit_text_2.setObjectName("kit_text_2")
        self.kit_btn_2 = QtWidgets.QPushButton(self.kit_wi_2)
        self.kit_btn_2.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.kit_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_btn_2.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.kit_btn_2.setText("")
        self.kit_btn_2.setObjectName("kit_btn_2")
        self.kit_label_2 = QtWidgets.QLineEdit(self.kit_wi_2)
        self.kit_label_2.setEnabled(False)
        self.kit_label_2.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.kit_label_2.setFont(font)
        self.kit_label_2.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_label_2.setMaxLength(30)
        self.kit_label_2.setObjectName("kit_label_2")
        self.kit_onoff_2 = QtWidgets.QPushButton(self.kit_wi_2)
        self.kit_onoff_2.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.kit_onoff_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_onoff_2.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.kit_onoff_2.setText("")
        self.kit_onoff_2.setCheckable(True)
        self.kit_onoff_2.setChecked(False)
        self.kit_onoff_2.setObjectName("kit_onoff_2")
        self.kit_su_2 = QtWidgets.QPushButton(self.kit_wi_2)
        self.kit_su_2.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.kit_su_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_su_2.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.kit_su_2.setText("")
        self.kit_su_2.setCheckable(True)
        self.kit_su_2.setObjectName("kit_su_2")
        self.kit_clo_2 = QtWidgets.QPushButton(self.kit_wi_2)
        self.kit_clo_2.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.kit_clo_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_clo_2.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.kit_clo_2.setText("")
        self.kit_clo_2.setCheckable(False)
        self.kit_clo_2.setObjectName("kit_clo_2")
        self.kit_icon_2 = QtWidgets.QLabel(self.kit_wi_2)
        self.kit_icon_2.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.kit_icon_2.setFont(font)
        self.kit_icon_2.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.kit_icon_2.setAlignment(QtCore.Qt.AlignCenter)
        self.kit_icon_2.setObjectName("kit_icon_2")
        self.kit_value_2 = QtWidgets.QLineEdit(self.kit_wi_2)
        self.kit_value_2.setEnabled(False)
        self.kit_value_2.setGeometry(QtCore.QRect(55, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.kit_value_2.setFont(font)
        self.kit_value_2.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}")
        self.kit_value_2.setMaxLength(10)
        self.kit_value_2.setObjectName("kit_value_2")
        self.kit_text_2.raise_()
        self.kit_btn_2.raise_()
        self.kit_label_2.raise_()
        self.kit_onoff_2.raise_()
        self.kit_su_2.raise_()
        self.kit_clo_2.raise_()
        self.kit_value_2.raise_()
        self.kit_icon_2.raise_()
        self.kit_layout.addWidget(self.kit_wi_2, 1, 0, 1, 1)
        self.kit_wi_3 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.kit_wi_3.setEnabled(True)
        self.kit_wi_3.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.kit_wi_3.setObjectName("kit_wi_3")
        self.kit_text_3 = QtWidgets.QLineEdit(self.kit_wi_3)
        self.kit_text_3.setEnabled(False)
        self.kit_text_3.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.kit_text_3.setFont(font)
        self.kit_text_3.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_text_3.setMaxLength(30)
        self.kit_text_3.setObjectName("kit_text_3")
        self.kit_btn_3 = QtWidgets.QPushButton(self.kit_wi_3)
        self.kit_btn_3.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.kit_btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_btn_3.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.kit_btn_3.setText("")
        self.kit_btn_3.setObjectName("kit_btn_3")
        self.kit_label_3 = QtWidgets.QLineEdit(self.kit_wi_3)
        self.kit_label_3.setEnabled(False)
        self.kit_label_3.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.kit_label_3.setFont(font)
        self.kit_label_3.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_label_3.setMaxLength(30)
        self.kit_label_3.setObjectName("kit_label_3")
        self.kit_onoff_3 = QtWidgets.QPushButton(self.kit_wi_3)
        self.kit_onoff_3.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.kit_onoff_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_onoff_3.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.kit_onoff_3.setText("")
        self.kit_onoff_3.setCheckable(True)
        self.kit_onoff_3.setChecked(False)
        self.kit_onoff_3.setObjectName("kit_onoff_3")
        self.kit_su_3 = QtWidgets.QPushButton(self.kit_wi_3)
        self.kit_su_3.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.kit_su_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_su_3.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.kit_su_3.setText("")
        self.kit_su_3.setCheckable(True)
        self.kit_su_3.setObjectName("kit_su_3")
        self.kit_clo_3 = QtWidgets.QPushButton(self.kit_wi_3)
        self.kit_clo_3.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.kit_clo_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_clo_3.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.kit_clo_3.setText("")
        self.kit_clo_3.setCheckable(False)
        self.kit_clo_3.setObjectName("kit_clo_3")
        self.kit_icon_3 = QtWidgets.QLabel(self.kit_wi_3)
        self.kit_icon_3.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.kit_icon_3.setFont(font)
        self.kit_icon_3.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.kit_icon_3.setAlignment(QtCore.Qt.AlignCenter)
        self.kit_icon_3.setObjectName("kit_icon_3")
        self.kit_value_3 = QtWidgets.QLineEdit(self.kit_wi_3)
        self.kit_value_3.setEnabled(False)
        self.kit_value_3.setGeometry(QtCore.QRect(55, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.kit_value_3.setFont(font)
        self.kit_value_3.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}")
        self.kit_value_3.setMaxLength(10)
        self.kit_value_3.setObjectName("kit_value_3")
        self.kit_layout.addWidget(self.kit_wi_3, 2, 0, 1, 1)
        self.kit_wi_5 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.kit_wi_5.setEnabled(True)
        self.kit_wi_5.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.kit_wi_5.setObjectName("kit_wi_5")
        self.kit_text_5 = QtWidgets.QLineEdit(self.kit_wi_5)
        self.kit_text_5.setEnabled(False)
        self.kit_text_5.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.kit_text_5.setFont(font)
        self.kit_text_5.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_text_5.setMaxLength(30)
        self.kit_text_5.setObjectName("kit_text_5")
        self.kit_btn_5 = QtWidgets.QPushButton(self.kit_wi_5)
        self.kit_btn_5.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.kit_btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_btn_5.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.kit_btn_5.setText("")
        self.kit_btn_5.setObjectName("kit_btn_5")
        self.kit_label_5 = QtWidgets.QLineEdit(self.kit_wi_5)
        self.kit_label_5.setEnabled(False)
        self.kit_label_5.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.kit_label_5.setFont(font)
        self.kit_label_5.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_label_5.setMaxLength(30)
        self.kit_label_5.setObjectName("kit_label_5")
        self.kit_onoff_5 = QtWidgets.QPushButton(self.kit_wi_5)
        self.kit_onoff_5.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.kit_onoff_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_onoff_5.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.kit_onoff_5.setText("")
        self.kit_onoff_5.setCheckable(True)
        self.kit_onoff_5.setChecked(False)
        self.kit_onoff_5.setObjectName("kit_onoff_5")
        self.kit_su_5 = QtWidgets.QPushButton(self.kit_wi_5)
        self.kit_su_5.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.kit_su_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_su_5.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.kit_su_5.setText("")
        self.kit_su_5.setCheckable(True)
        self.kit_su_5.setObjectName("kit_su_5")
        self.kit_clo_5 = QtWidgets.QPushButton(self.kit_wi_5)
        self.kit_clo_5.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.kit_clo_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_clo_5.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.kit_clo_5.setText("")
        self.kit_clo_5.setCheckable(False)
        self.kit_clo_5.setObjectName("kit_clo_5")
        self.kit_icon_5 = QtWidgets.QLabel(self.kit_wi_5)
        self.kit_icon_5.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.kit_icon_5.setFont(font)
        self.kit_icon_5.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.kit_icon_5.setAlignment(QtCore.Qt.AlignCenter)
        self.kit_icon_5.setObjectName("kit_icon_5")
        self.kit_value_5 = QtWidgets.QLineEdit(self.kit_wi_5)
        self.kit_value_5.setEnabled(False)
        self.kit_value_5.setGeometry(QtCore.QRect(55, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.kit_value_5.setFont(font)
        self.kit_value_5.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}")
        self.kit_value_5.setMaxLength(10)
        self.kit_value_5.setObjectName("kit_value_5")
        self.kit_layout.addWidget(self.kit_wi_5, 1, 1, 1, 1)
        self.kit_wi_6 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.kit_wi_6.setEnabled(True)
        self.kit_wi_6.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.kit_wi_6.setObjectName("kit_wi_6")
        self.kit_text_6 = QtWidgets.QLineEdit(self.kit_wi_6)
        self.kit_text_6.setEnabled(False)
        self.kit_text_6.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.kit_text_6.setFont(font)
        self.kit_text_6.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_text_6.setMaxLength(30)
        self.kit_text_6.setObjectName("kit_text_6")
        self.kit_btn_6 = QtWidgets.QPushButton(self.kit_wi_6)
        self.kit_btn_6.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.kit_btn_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_btn_6.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.kit_btn_6.setText("")
        self.kit_btn_6.setObjectName("kit_btn_6")
        self.kit_label_6 = QtWidgets.QLineEdit(self.kit_wi_6)
        self.kit_label_6.setEnabled(False)
        self.kit_label_6.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.kit_label_6.setFont(font)
        self.kit_label_6.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_label_6.setMaxLength(30)
        self.kit_label_6.setObjectName("kit_label_6")
        self.kit_onoff_6 = QtWidgets.QPushButton(self.kit_wi_6)
        self.kit_onoff_6.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.kit_onoff_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_onoff_6.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.kit_onoff_6.setText("")
        self.kit_onoff_6.setCheckable(True)
        self.kit_onoff_6.setChecked(False)
        self.kit_onoff_6.setObjectName("kit_onoff_6")
        self.kit_su_6 = QtWidgets.QPushButton(self.kit_wi_6)
        self.kit_su_6.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.kit_su_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_su_6.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.kit_su_6.setText("")
        self.kit_su_6.setCheckable(True)
        self.kit_su_6.setObjectName("kit_su_6")
        self.kit_clo_6 = QtWidgets.QPushButton(self.kit_wi_6)
        self.kit_clo_6.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.kit_clo_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_clo_6.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.kit_clo_6.setText("")
        self.kit_clo_6.setCheckable(False)
        self.kit_clo_6.setObjectName("kit_clo_6")
        self.kit_icon_6 = QtWidgets.QLabel(self.kit_wi_6)
        self.kit_icon_6.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.kit_icon_6.setFont(font)
        self.kit_icon_6.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.kit_icon_6.setAlignment(QtCore.Qt.AlignCenter)
        self.kit_icon_6.setObjectName("kit_icon_6")
        self.kit_value_6 = QtWidgets.QLineEdit(self.kit_wi_6)
        self.kit_value_6.setEnabled(False)
        self.kit_value_6.setGeometry(QtCore.QRect(55, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.kit_value_6.setFont(font)
        self.kit_value_6.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}")
        self.kit_value_6.setMaxLength(10)
        self.kit_value_6.setObjectName("kit_value_6")
        self.kit_text_6.raise_()
        self.kit_btn_6.raise_()
        self.kit_label_6.raise_()
        self.kit_onoff_6.raise_()
        self.kit_su_6.raise_()
        self.kit_clo_6.raise_()
        self.kit_value_6.raise_()
        self.kit_icon_6.raise_()
        self.kit_layout.addWidget(self.kit_wi_6, 2, 1, 1, 1)
        self.kit_wi_8 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.kit_wi_8.setEnabled(True)
        self.kit_wi_8.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.kit_wi_8.setObjectName("kit_wi_8")
        self.kit_text_8 = QtWidgets.QLineEdit(self.kit_wi_8)
        self.kit_text_8.setEnabled(False)
        self.kit_text_8.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.kit_text_8.setFont(font)
        self.kit_text_8.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_text_8.setMaxLength(30)
        self.kit_text_8.setObjectName("kit_text_8")
        self.kit_btn_8 = QtWidgets.QPushButton(self.kit_wi_8)
        self.kit_btn_8.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.kit_btn_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_btn_8.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.kit_btn_8.setText("")
        self.kit_btn_8.setObjectName("kit_btn_8")
        self.kit_label_8 = QtWidgets.QLineEdit(self.kit_wi_8)
        self.kit_label_8.setEnabled(False)
        self.kit_label_8.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.kit_label_8.setFont(font)
        self.kit_label_8.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_label_8.setMaxLength(30)
        self.kit_label_8.setObjectName("kit_label_8")
        self.kit_onoff_8 = QtWidgets.QPushButton(self.kit_wi_8)
        self.kit_onoff_8.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.kit_onoff_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_onoff_8.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.kit_onoff_8.setText("")
        self.kit_onoff_8.setCheckable(True)
        self.kit_onoff_8.setChecked(False)
        self.kit_onoff_8.setObjectName("kit_onoff_8")
        self.kit_su_8 = QtWidgets.QPushButton(self.kit_wi_8)
        self.kit_su_8.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.kit_su_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_su_8.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.kit_su_8.setText("")
        self.kit_su_8.setCheckable(True)
        self.kit_su_8.setObjectName("kit_su_8")
        self.kit_clo_8 = QtWidgets.QPushButton(self.kit_wi_8)
        self.kit_clo_8.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.kit_clo_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_clo_8.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.kit_clo_8.setText("")
        self.kit_clo_8.setCheckable(False)
        self.kit_clo_8.setObjectName("kit_clo_8")
        self.kit_icon_8 = QtWidgets.QLabel(self.kit_wi_8)
        self.kit_icon_8.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.kit_icon_8.setFont(font)
        self.kit_icon_8.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.kit_icon_8.setAlignment(QtCore.Qt.AlignCenter)
        self.kit_icon_8.setObjectName("kit_icon_8")
        self.kit_value_8 = QtWidgets.QLineEdit(self.kit_wi_8)
        self.kit_value_8.setEnabled(False)
        self.kit_value_8.setGeometry(QtCore.QRect(55, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.kit_value_8.setFont(font)
        self.kit_value_8.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}")
        self.kit_value_8.setMaxLength(10)
        self.kit_value_8.setObjectName("kit_value_8")
        self.kit_layout.addWidget(self.kit_wi_8, 1, 2, 1, 1)
        self.kit_wi_7 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.kit_wi_7.setEnabled(True)
        self.kit_wi_7.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.kit_wi_7.setObjectName("kit_wi_7")
        self.kit_text_7 = QtWidgets.QLineEdit(self.kit_wi_7)
        self.kit_text_7.setEnabled(False)
        self.kit_text_7.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.kit_text_7.setFont(font)
        self.kit_text_7.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_text_7.setMaxLength(30)
        self.kit_text_7.setObjectName("kit_text_7")
        self.kit_btn_7 = QtWidgets.QPushButton(self.kit_wi_7)
        self.kit_btn_7.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.kit_btn_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_btn_7.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.kit_btn_7.setText("")
        self.kit_btn_7.setObjectName("kit_btn_7")
        self.kit_label_7 = QtWidgets.QLineEdit(self.kit_wi_7)
        self.kit_label_7.setEnabled(False)
        self.kit_label_7.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.kit_label_7.setFont(font)
        self.kit_label_7.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_label_7.setMaxLength(30)
        self.kit_label_7.setObjectName("kit_label_7")
        self.kit_onoff_7 = QtWidgets.QPushButton(self.kit_wi_7)
        self.kit_onoff_7.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.kit_onoff_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_onoff_7.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.kit_onoff_7.setText("")
        self.kit_onoff_7.setCheckable(True)
        self.kit_onoff_7.setChecked(False)
        self.kit_onoff_7.setObjectName("kit_onoff_7")
        self.kit_su_7 = QtWidgets.QPushButton(self.kit_wi_7)
        self.kit_su_7.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.kit_su_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_su_7.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.kit_su_7.setText("")
        self.kit_su_7.setCheckable(True)
        self.kit_su_7.setObjectName("kit_su_7")
        self.kit_clo_7 = QtWidgets.QPushButton(self.kit_wi_7)
        self.kit_clo_7.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.kit_clo_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_clo_7.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.kit_clo_7.setText("")
        self.kit_clo_7.setCheckable(False)
        self.kit_clo_7.setObjectName("kit_clo_7")
        self.kit_icon_7 = QtWidgets.QLabel(self.kit_wi_7)
        self.kit_icon_7.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.kit_icon_7.setFont(font)
        self.kit_icon_7.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.kit_icon_7.setAlignment(QtCore.Qt.AlignCenter)
        self.kit_icon_7.setObjectName("kit_icon_7")
        self.kit_value_7 = QtWidgets.QLineEdit(self.kit_wi_7)
        self.kit_value_7.setEnabled(False)
        self.kit_value_7.setGeometry(QtCore.QRect(55, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.kit_value_7.setFont(font)
        self.kit_value_7.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}")
        self.kit_value_7.setMaxLength(10)
        self.kit_value_7.setObjectName("kit_value_7")
        self.kit_text_7.raise_()
        self.kit_btn_7.raise_()
        self.kit_label_7.raise_()
        self.kit_onoff_7.raise_()
        self.kit_su_7.raise_()
        self.kit_clo_7.raise_()
        self.kit_value_7.raise_()
        self.kit_icon_7.raise_()
        self.kit_layout.addWidget(self.kit_wi_7, 0, 2, 1, 1)
        self.kit_wi_9 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.kit_wi_9.setEnabled(True)
        self.kit_wi_9.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.kit_wi_9.setObjectName("kit_wi_9")
        self.kit_text_9 = QtWidgets.QLineEdit(self.kit_wi_9)
        self.kit_text_9.setEnabled(False)
        self.kit_text_9.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.kit_text_9.setFont(font)
        self.kit_text_9.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_text_9.setMaxLength(30)
        self.kit_text_9.setObjectName("kit_text_9")
        self.kit_btn_9 = QtWidgets.QPushButton(self.kit_wi_9)
        self.kit_btn_9.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.kit_btn_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_btn_9.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.kit_btn_9.setText("")
        self.kit_btn_9.setObjectName("kit_btn_9")
        self.kit_label_9 = QtWidgets.QLineEdit(self.kit_wi_9)
        self.kit_label_9.setEnabled(False)
        self.kit_label_9.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.kit_label_9.setFont(font)
        self.kit_label_9.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_label_9.setMaxLength(30)
        self.kit_label_9.setObjectName("kit_label_9")
        self.kit_onoff_9 = QtWidgets.QPushButton(self.kit_wi_9)
        self.kit_onoff_9.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.kit_onoff_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_onoff_9.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.kit_onoff_9.setText("")
        self.kit_onoff_9.setCheckable(True)
        self.kit_onoff_9.setChecked(False)
        self.kit_onoff_9.setObjectName("kit_onoff_9")
        self.kit_su_9 = QtWidgets.QPushButton(self.kit_wi_9)
        self.kit_su_9.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.kit_su_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_su_9.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.kit_su_9.setText("")
        self.kit_su_9.setCheckable(True)
        self.kit_su_9.setObjectName("kit_su_9")
        self.kit_clo_9 = QtWidgets.QPushButton(self.kit_wi_9)
        self.kit_clo_9.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.kit_clo_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_clo_9.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.kit_clo_9.setText("")
        self.kit_clo_9.setCheckable(False)
        self.kit_clo_9.setObjectName("kit_clo_9")
        self.kit_icon_9 = QtWidgets.QLabel(self.kit_wi_9)
        self.kit_icon_9.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.kit_icon_9.setFont(font)
        self.kit_icon_9.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.kit_icon_9.setAlignment(QtCore.Qt.AlignCenter)
        self.kit_icon_9.setObjectName("kit_icon_9")
        self.kit_value_9 = QtWidgets.QLineEdit(self.kit_wi_9)
        self.kit_value_9.setEnabled(False)
        self.kit_value_9.setGeometry(QtCore.QRect(55, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.kit_value_9.setFont(font)
        self.kit_value_9.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}")
        self.kit_value_9.setMaxLength(10)
        self.kit_value_9.setObjectName("kit_value_9")
        self.kit_text_9.raise_()
        self.kit_btn_9.raise_()
        self.kit_label_9.raise_()
        self.kit_onoff_9.raise_()
        self.kit_su_9.raise_()
        self.kit_clo_9.raise_()
        self.kit_value_9.raise_()
        self.kit_icon_9.raise_()
        self.kit_layout.addWidget(self.kit_wi_9, 2, 2, 1, 1)
        self.kit_wi_10 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.kit_wi_10.setEnabled(True)
        self.kit_wi_10.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.kit_wi_10.setObjectName("kit_wi_10")
        self.kit_text_10 = QtWidgets.QLineEdit(self.kit_wi_10)
        self.kit_text_10.setEnabled(False)
        self.kit_text_10.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.kit_text_10.setFont(font)
        self.kit_text_10.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_text_10.setMaxLength(30)
        self.kit_text_10.setObjectName("kit_text_10")
        self.kit_btn_10 = QtWidgets.QPushButton(self.kit_wi_10)
        self.kit_btn_10.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.kit_btn_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_btn_10.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.kit_btn_10.setText("")
        self.kit_btn_10.setObjectName("kit_btn_10")
        self.kit_label_10 = QtWidgets.QLineEdit(self.kit_wi_10)
        self.kit_label_10.setEnabled(False)
        self.kit_label_10.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.kit_label_10.setFont(font)
        self.kit_label_10.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_label_10.setMaxLength(30)
        self.kit_label_10.setObjectName("kit_label_10")
        self.kit_onoff_10 = QtWidgets.QPushButton(self.kit_wi_10)
        self.kit_onoff_10.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.kit_onoff_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_onoff_10.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.kit_onoff_10.setText("")
        self.kit_onoff_10.setCheckable(True)
        self.kit_onoff_10.setChecked(False)
        self.kit_onoff_10.setObjectName("kit_onoff_10")
        self.kit_su_10 = QtWidgets.QPushButton(self.kit_wi_10)
        self.kit_su_10.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.kit_su_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_su_10.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.kit_su_10.setText("")
        self.kit_su_10.setCheckable(True)
        self.kit_su_10.setObjectName("kit_su_10")
        self.kit_clo_10 = QtWidgets.QPushButton(self.kit_wi_10)
        self.kit_clo_10.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.kit_clo_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_clo_10.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.kit_clo_10.setText("")
        self.kit_clo_10.setCheckable(False)
        self.kit_clo_10.setObjectName("kit_clo_10")
        self.kit_icon_10 = QtWidgets.QLabel(self.kit_wi_10)
        self.kit_icon_10.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.kit_icon_10.setFont(font)
        self.kit_icon_10.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.kit_icon_10.setAlignment(QtCore.Qt.AlignCenter)
        self.kit_icon_10.setObjectName("kit_icon_10")
        self.kit_value_10 = QtWidgets.QLineEdit(self.kit_wi_10)
        self.kit_value_10.setEnabled(False)
        self.kit_value_10.setGeometry(QtCore.QRect(55, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.kit_value_10.setFont(font)
        self.kit_value_10.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}")
        self.kit_value_10.setMaxLength(10)
        self.kit_value_10.setObjectName("kit_value_10")
        self.kit_layout.addWidget(self.kit_wi_10, 0, 3, 1, 1)
        self.kit_wi_11 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.kit_wi_11.setEnabled(True)
        self.kit_wi_11.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.kit_wi_11.setObjectName("kit_wi_11")
        self.kit_text_11 = QtWidgets.QLineEdit(self.kit_wi_11)
        self.kit_text_11.setEnabled(False)
        self.kit_text_11.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.kit_text_11.setFont(font)
        self.kit_text_11.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_text_11.setMaxLength(30)
        self.kit_text_11.setObjectName("kit_text_11")
        self.kit_btn_11 = QtWidgets.QPushButton(self.kit_wi_11)
        self.kit_btn_11.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.kit_btn_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_btn_11.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.kit_btn_11.setText("")
        self.kit_btn_11.setObjectName("kit_btn_11")
        self.kit_label_11 = QtWidgets.QLineEdit(self.kit_wi_11)
        self.kit_label_11.setEnabled(False)
        self.kit_label_11.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.kit_label_11.setFont(font)
        self.kit_label_11.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_label_11.setMaxLength(30)
        self.kit_label_11.setObjectName("kit_label_11")
        self.kit_onoff_11 = QtWidgets.QPushButton(self.kit_wi_11)
        self.kit_onoff_11.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.kit_onoff_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_onoff_11.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.kit_onoff_11.setText("")
        self.kit_onoff_11.setCheckable(True)
        self.kit_onoff_11.setChecked(False)
        self.kit_onoff_11.setObjectName("kit_onoff_11")
        self.kit_su_11 = QtWidgets.QPushButton(self.kit_wi_11)
        self.kit_su_11.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.kit_su_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_su_11.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.kit_su_11.setText("")
        self.kit_su_11.setCheckable(True)
        self.kit_su_11.setObjectName("kit_su_11")
        self.kit_clo_11 = QtWidgets.QPushButton(self.kit_wi_11)
        self.kit_clo_11.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.kit_clo_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_clo_11.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.kit_clo_11.setText("")
        self.kit_clo_11.setCheckable(False)
        self.kit_clo_11.setObjectName("kit_clo_11")
        self.kit_icon_11 = QtWidgets.QLabel(self.kit_wi_11)
        self.kit_icon_11.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.kit_icon_11.setFont(font)
        self.kit_icon_11.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.kit_icon_11.setAlignment(QtCore.Qt.AlignCenter)
        self.kit_icon_11.setObjectName("kit_icon_11")
        self.kit_value_11 = QtWidgets.QLineEdit(self.kit_wi_11)
        self.kit_value_11.setEnabled(False)
        self.kit_value_11.setGeometry(QtCore.QRect(55, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.kit_value_11.setFont(font)
        self.kit_value_11.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}")
        self.kit_value_11.setMaxLength(10)
        self.kit_value_11.setObjectName("kit_value_11")
        self.kit_text_11.raise_()
        self.kit_btn_11.raise_()
        self.kit_label_11.raise_()
        self.kit_onoff_11.raise_()
        self.kit_su_11.raise_()
        self.kit_clo_11.raise_()
        self.kit_value_11.raise_()
        self.kit_icon_11.raise_()
        self.kit_layout.addWidget(self.kit_wi_11, 1, 3, 1, 1)
        self.kit_wi_12 = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.kit_wi_12.setEnabled(True)
        self.kit_wi_12.setStyleSheet("QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"\n"
"\n"
"")
        self.kit_wi_12.setObjectName("kit_wi_12")
        self.kit_text_12 = QtWidgets.QLineEdit(self.kit_wi_12)
        self.kit_text_12.setEnabled(False)
        self.kit_text_12.setGeometry(QtCore.QRect(15, 17, 241, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.kit_text_12.setFont(font)
        self.kit_text_12.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_text_12.setMaxLength(30)
        self.kit_text_12.setObjectName("kit_text_12")
        self.kit_btn_12 = QtWidgets.QPushButton(self.kit_wi_12)
        self.kit_btn_12.setGeometry(QtCore.QRect(0, 0, 261, 185))
        self.kit_btn_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_btn_12.setStyleSheet("image : url(./);\n"
"background-color : rgba(0,0,0,0);")
        self.kit_btn_12.setText("")
        self.kit_btn_12.setObjectName("kit_btn_12")
        self.kit_label_12 = QtWidgets.QLineEdit(self.kit_wi_12)
        self.kit_label_12.setEnabled(False)
        self.kit_label_12.setGeometry(QtCore.QRect(15, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(14)
        self.kit_label_12.setFont(font)
        self.kit_label_12.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(255,255,255);\n"
"image : NULL;\n"
"}")
        self.kit_label_12.setMaxLength(30)
        self.kit_label_12.setObjectName("kit_label_12")
        self.kit_onoff_12 = QtWidgets.QPushButton(self.kit_wi_12)
        self.kit_onoff_12.setGeometry(QtCore.QRect(160, 42, 91, 81))
        self.kit_onoff_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_onoff_12.setStyleSheet("QPushButton{image:url(./image/off_1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/off_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/on_1.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked:hover{image:url(./image/on_2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"")
        self.kit_onoff_12.setText("")
        self.kit_onoff_12.setCheckable(True)
        self.kit_onoff_12.setChecked(False)
        self.kit_onoff_12.setObjectName("kit_onoff_12")
        self.kit_su_12 = QtWidgets.QPushButton(self.kit_wi_12)
        self.kit_su_12.setGeometry(QtCore.QRect(185, 145, 31, 31))
        self.kit_su_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_su_12.setStyleSheet("QPushButton{image:url(./image/su_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/su_2.png); border:0px;}\n"
"QPushButton:checked{image:url(./image/ck_1.png); border:0px;}\n"
"QPushButton:checked:hover{image:url(./image/ck_2.png); border:0px;}\n"
"\n"
"")
        self.kit_su_12.setText("")
        self.kit_su_12.setCheckable(True)
        self.kit_su_12.setObjectName("kit_su_12")
        self.kit_clo_12 = QtWidgets.QPushButton(self.kit_wi_12)
        self.kit_clo_12.setGeometry(QtCore.QRect(220, 145, 31, 31))
        self.kit_clo_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kit_clo_12.setStyleSheet("QPushButton{image:url(./image/close_1.png); border:0px;color:}\n"
"QPushButton:hover{image:url(./image/close_2.png); border:0px;}\n"
"")
        self.kit_clo_12.setText("")
        self.kit_clo_12.setCheckable(False)
        self.kit_clo_12.setObjectName("kit_clo_12")
        self.kit_icon_12 = QtWidgets.QLabel(self.kit_wi_12)
        self.kit_icon_12.setGeometry(QtCore.QRect(5, 97, 56, 30))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(18)
        self.kit_icon_12.setFont(font)
        self.kit_icon_12.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"image : url(./);\n"
"color : rgb(255,255,255);")
        self.kit_icon_12.setAlignment(QtCore.Qt.AlignCenter)
        self.kit_icon_12.setObjectName("kit_icon_12")
        self.kit_value_12 = QtWidgets.QLineEdit(self.kit_wi_12)
        self.kit_value_12.setEnabled(False)
        self.kit_value_12.setGeometry(QtCore.QRect(55, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(20)
        self.kit_value_12.setFont(font)
        self.kit_value_12.setStyleSheet("QLineEdit:Enabled{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}\n"
"QLineEdit{\n"
"background-color : rgba(0,0,0,0);\n"
"color : rgb(0,0,0);\n"
"image : NULL;\n"
"}")
        self.kit_value_12.setMaxLength(10)
        self.kit_value_12.setObjectName("kit_value_12")
        self.kit_text_12.raise_()
        self.kit_btn_12.raise_()
        self.kit_label_12.raise_()
        self.kit_onoff_12.raise_()
        self.kit_su_12.raise_()
        self.kit_clo_12.raise_()
        self.kit_value_12.raise_()
        self.kit_icon_12.raise_()
        self.kit_layout.addWidget(self.kit_wi_12, 2, 3, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.kit)
        self.label_31.setGeometry(QtCore.QRect(40, 0, 41, 591))
        self.label_31.setStyleSheet("border : 0px;")
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.kit_right_btn.raise_()
        self.gridLayoutWidget_3.raise_()
        self.label_31.raise_()
        self.kit_left_btn.raise_()
        self.stackedWidget.addWidget(self.kit)
        self.kit_2 = QtWidgets.QWidget()
        self.kit_2.setObjectName("kit_2")
        self.stackedWidget.addWidget(self.kit_2)
        self.set_page = QtWidgets.QWidget()
        self.set_page.setObjectName("set_page")
        self.close_btn = QtWidgets.QPushButton(self.set_page)
        self.close_btn.setGeometry(QtCore.QRect(470, 240, 509, 99))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("서울한강체 EB")
        font.setPointSize(36)
        self.close_btn.setFont(font)
        self.close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_btn.setStyleSheet("QPushButton{image:url(./); border:2px solid rgb(225,225,225); background-color : rgb(255,255,255)}\n"
"QPushButton:hover{image:url(./); border:2px; background-color : rgb(225,225,225)}\n"
"\n"
"\n"
"")
        self.close_btn.setCheckable(True)
        self.close_btn.setObjectName("close_btn")
        self.stackedWidget.addWidget(self.set_page)
        self.credit_page = QtWidgets.QWidget()
        self.credit_page.setObjectName("credit_page")
        self.label_3 = QtWidgets.QLabel(self.credit_page)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 1401, 571))
        self.label_3.setStyleSheet("border : 0px;\n"
"image:url(./image/credit_image.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.credit_page)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1460, 0, 311, 71))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border : 0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-20, -20, 1960, 120))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("image/north_bar.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.credit.raise_()
        self.set.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.stackedWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(9)
        self.pushButton_2.clicked.connect(MainWindow.dgsw)
        self.bal_r_val.sliderMoved['int'].connect(self.bal_r_num.setNum)
        self.bal_r_val.valueChanged['int'].connect(self.bal_r_num.setNum)
        self.bal_b_val.valueChanged['int'].connect(self.bal_b_num.setNum)
        self.bal_w_val.valueChanged['int'].connect(self.bal_w_num.setNum)
        self.pen_slider.valueChanged['int'].connect(self.pen_value_label.setNum)
        self.close_btn.clicked.connect(MainWindow.exitexit)
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
        self.chk_light.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"19"))
        self.chk_ph2.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"82"))
        self.chk_tds.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"45"))
        self.grap_temp.setText(_translate("MainWindow", "온도"))
        self.grap_hum.setText(_translate("MainWindow", "습도"))
        self.grap_co2.setText(_translate("MainWindow", "CO2"))
        self.grap_light.setText(_translate("MainWindow", "조도"))
        self.pen_value_label.setText(_translate("MainWindow", "100"))
        self.pen_text_1.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.pen_label_1.setText(_translate("MainWindow", "L02"))
        self.pen_value_1.setText(_translate("MainWindow", "100"))
        self.pen_per_1.setText(_translate("MainWindow", "%"))
        self.pen_text_2.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.pen_label_2.setText(_translate("MainWindow", "L02"))
        self.pen_value_2.setText(_translate("MainWindow", "100"))
        self.pen_per_2.setText(_translate("MainWindow", "%"))
        self.pen_text_5.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.pen_label_5.setText(_translate("MainWindow", "L02"))
        self.pen_value_5.setText(_translate("MainWindow", "100"))
        self.pen_per_5.setText(_translate("MainWindow", "%"))
        self.pen_text_3.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.pen_label_3.setText(_translate("MainWindow", "L02"))
        self.pen_value_3.setText(_translate("MainWindow", "100"))
        self.pen_per_3.setText(_translate("MainWindow", "%"))
        self.pen_text_4.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.pen_label_4.setText(_translate("MainWindow", "L02"))
        self.pen_value_4.setText(_translate("MainWindow", "100"))
        self.pen_per_4.setText(_translate("MainWindow", "%"))
        self.pen_text_6.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.pen_label_6.setText(_translate("MainWindow", "L02"))
        self.pen_value_6.setText(_translate("MainWindow", "100"))
        self.pen_per_6.setText(_translate("MainWindow", "%"))
        self.pen_text_7.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.pen_label_7.setText(_translate("MainWindow", "L02"))
        self.pen_value_7.setText(_translate("MainWindow", "100"))
        self.pen_per_7.setText(_translate("MainWindow", "%"))
        self.pen_text_8.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.pen_label_8.setText(_translate("MainWindow", "L02"))
        self.pen_value_8.setText(_translate("MainWindow", "100"))
        self.pen_per_8.setText(_translate("MainWindow", "%"))
        self.pen_value_label_2.setText(_translate("MainWindow", "%"))
        self.bal_text_1.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_1.setText(_translate("MainWindow", "L02"))
        self.bal_r_1.setText(_translate("MainWindow", "100"))
        self.bal_b_1.setText(_translate("MainWindow", "100"))
        self.bal_w_1.setText(_translate("MainWindow", "100"))
        self.bal_text_6.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_6.setText(_translate("MainWindow", "L02"))
        self.bal_r_6.setText(_translate("MainWindow", "100"))
        self.bal_b_6.setText(_translate("MainWindow", "100"))
        self.bal_w_6.setText(_translate("MainWindow", "100"))
        self.bal_text_8.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_8.setText(_translate("MainWindow", "L02"))
        self.bal_r_8.setText(_translate("MainWindow", "100"))
        self.bal_b_8.setText(_translate("MainWindow", "100"))
        self.bal_w_8.setText(_translate("MainWindow", "100"))
        self.bal_text_3.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_3.setText(_translate("MainWindow", "L02"))
        self.bal_r_3.setText(_translate("MainWindow", "100"))
        self.bal_b_3.setText(_translate("MainWindow", "100"))
        self.bal_w_3.setText(_translate("MainWindow", "100"))
        self.bal_text_5.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_5.setText(_translate("MainWindow", "L02"))
        self.bal_r_5.setText(_translate("MainWindow", "100"))
        self.bal_b_5.setText(_translate("MainWindow", "100"))
        self.bal_w_5.setText(_translate("MainWindow", "100"))
        self.bal_text_2.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_2.setText(_translate("MainWindow", "L02"))
        self.bal_r_2.setText(_translate("MainWindow", "100"))
        self.bal_b_2.setText(_translate("MainWindow", "100"))
        self.bal_w_2.setText(_translate("MainWindow", "100"))
        self.bal_text_4.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_4.setText(_translate("MainWindow", "L02"))
        self.bal_r_4.setText(_translate("MainWindow", "100"))
        self.bal_b_4.setText(_translate("MainWindow", "100"))
        self.bal_w_4.setText(_translate("MainWindow", "100"))
        self.bal_text_7.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.bal_label_7.setText(_translate("MainWindow", "L02"))
        self.bal_r_7.setText(_translate("MainWindow", "100"))
        self.bal_b_7.setText(_translate("MainWindow", "100"))
        self.bal_w_7.setText(_translate("MainWindow", "100"))
        self.bal_r_num.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "RED"))
        self.bal_b_num.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "BLUE"))
        self.bal_w_num.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "WHITE"))
        self.kit_text_4.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.kit_label_4.setText(_translate("MainWindow", "L02"))
        self.kit_icon_4.setText(_translate("MainWindow", "%"))
        self.kit_value_4.setText(_translate("MainWindow", "100"))
        self.kit_text_1.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.kit_label_1.setText(_translate("MainWindow", "L02"))
        self.kit_icon_1.setText(_translate("MainWindow", "%"))
        self.kit_value_1.setText(_translate("MainWindow", "100"))
        self.kit_text_2.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.kit_label_2.setText(_translate("MainWindow", "L02"))
        self.kit_icon_2.setText(_translate("MainWindow", "%"))
        self.kit_value_2.setText(_translate("MainWindow", "100"))
        self.kit_text_3.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.kit_label_3.setText(_translate("MainWindow", "L02"))
        self.kit_icon_3.setText(_translate("MainWindow", "%"))
        self.kit_value_3.setText(_translate("MainWindow", "100"))
        self.kit_text_5.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.kit_label_5.setText(_translate("MainWindow", "L02"))
        self.kit_icon_5.setText(_translate("MainWindow", "%"))
        self.kit_value_5.setText(_translate("MainWindow", "100"))
        self.kit_text_6.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.kit_label_6.setText(_translate("MainWindow", "L02"))
        self.kit_icon_6.setText(_translate("MainWindow", "%"))
        self.kit_value_6.setText(_translate("MainWindow", "100"))
        self.kit_text_8.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.kit_label_8.setText(_translate("MainWindow", "L02"))
        self.kit_icon_8.setText(_translate("MainWindow", "%"))
        self.kit_value_8.setText(_translate("MainWindow", "100"))
        self.kit_text_7.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.kit_label_7.setText(_translate("MainWindow", "L02"))
        self.kit_icon_7.setText(_translate("MainWindow", "%"))
        self.kit_value_7.setText(_translate("MainWindow", "100"))
        self.kit_text_9.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.kit_label_9.setText(_translate("MainWindow", "L02"))
        self.kit_icon_9.setText(_translate("MainWindow", "%"))
        self.kit_value_9.setText(_translate("MainWindow", "100"))
        self.kit_text_10.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.kit_label_10.setText(_translate("MainWindow", "L02"))
        self.kit_icon_10.setText(_translate("MainWindow", "%"))
        self.kit_value_10.setText(_translate("MainWindow", "100"))
        self.kit_text_11.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.kit_label_11.setText(_translate("MainWindow", "L02"))
        self.kit_icon_11.setText(_translate("MainWindow", "%"))
        self.kit_value_11.setText(_translate("MainWindow", "100"))
        self.kit_text_12.setText(_translate("MainWindow", "왼쪽 위 led"))
        self.kit_label_12.setText(_translate("MainWindow", "L02"))
        self.kit_icon_12.setText(_translate("MainWindow", "%"))
        self.kit_value_12.setText(_translate("MainWindow", "100"))
        self.close_btn.setText(_translate("MainWindow", "종료"))

from pyqtgraph import PlotWidget
