from Ui_test import *

import sys


def slot1():
    print('test')



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()



MainWindow.slot1 = slot1

MainWindow.showFullScreen()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)

ui.stackedWidget.setCurrentIndex(2)

app.exec_()
