# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\graphtest\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import datetime

# class TimeAxisItem(pg.AxisItem):
#     def tickStrings(self, values, scale, spacing):
#         return [datetime.datetime.fromtimestamp(value).strftime("%H:%M") for value in values]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.graphicsView = PlotWidget(self.centralwidget,axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(140, 70, 491, 451))
        self.graphicsView.setObjectName("graphicsView")
        font = QtGui.QFont()
        font.setFamily("서울남산체 B")
        font.setPointSize(40)
        self.graphicsView.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

from pyqtgraph import PlotWidget
