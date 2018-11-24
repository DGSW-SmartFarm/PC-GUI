from Ui_test import *

import sys


def slot1():
    print('test')



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.showFullScreen()


MainWindow.slot1 = slot1

ui = Ui_MainWindow()
ui.setupUi(MainWindow)





app.exec_()
