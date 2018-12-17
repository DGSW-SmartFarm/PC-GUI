from Ui_kit_1 import *

import sys
import copy

def slot1(self):
    print('test')
    



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()



MainWindow.slot1 = slot1

MainWindow.show()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

#ui.push3 = ui.pushButton_2
#ui.push3.setObjectName("push3")
#ui.push3.setGeometry(QtCore.QRect(0, 0, 75, 23))

app.exec_()
