from Ui_test import *

import sys


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.showFullScreen()



ui = Ui_MainWindow()
ui.setupUi(MainWindow)




app.exec_()
