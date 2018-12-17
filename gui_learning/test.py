from Ui_test import *
from bal_class import *

import sys




def bal_btn():
    print('test')

def bal_signals():
    for i in range(8):
        bal_btn[i].clicked.connect(bal_btn)


# -------메인

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()





MainWindow.showFullScreen()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.stackedWidget.setCurrentIndex(2)


bal = Balgi(ui) #밝기조절 클래스


app.exec_()
