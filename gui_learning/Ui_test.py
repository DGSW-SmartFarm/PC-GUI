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
"\n"
"\n"
"")
        self.credit_3.setText("")
        self.credit_3.setFlat(False)
        self.credit_3.setObjectName("credit_3")
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
"\n"
"\n"
"")
        self.credit_7.setText("")
        self.credit_7.setObjectName("credit_7")
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
"")
        self.credit_6.setText("")
        self.credit_6.setObjectName("credit_6")
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
"\n"
"\n"
"")
        self.credit_4.setText("")
        self.credit_4.setObjectName("credit_4")
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
"\n"
"\n"
"")
        self.credit_5.setText("")
        self.credit_5.setObjectName("credit_5")
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
"\n"
"\n"
"")
        self.credit_2.setText("")
        self.credit_2.setObjectName("credit_2")
        self.verticalLayout.addWidget(self.credit_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(507, 460, 1414, 621))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget.addTab(self.tab_12, "")
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
"\n"
"\n"
"\n"
"\n"
"")
        self.chk_temp.setObjectName("chk_temp")
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
"\n"
"\n"
"")
        self.chk_hum.setObjectName("chk_hum")
        self.chk_layout.addWidget(self.chk_hum)
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
"\n"
"\n"
"")
        self.chk_light.setObjectName("chk_light")
        self.chk_layout.addWidget(self.chk_light)
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
"\n"
"\n"
"")
        self.chk_co2.setObjectName("chk_co2")
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
"\n"
"")
        self.chk_ph2.setObjectName("chk_ph2")
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
"\n"
"\n"
"")
        self.chk_tds.setObjectName("chk_tds")
        self.chk_layout.addWidget(self.chk_tds)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "온도"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "습도"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "CO2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "PH"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "TDS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "조도"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "그래프 보기"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "온도 제어"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "밝기 제어"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "CO2 제어"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("MainWindow", "송풍기 제어"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("MainWindow", "양액 제어"))
        self.chk_temp.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"69°"))
        self.chk_hum.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"74%"))
        self.chk_light.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"19"))
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

