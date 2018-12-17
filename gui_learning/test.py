from Ui_test import *
from bal_class import *

import pymysql
import sys



def bal_r_event():
    bal.bal_r_event()

def bal_b_event():
    bal.bal_b_event()

def bal_w_event():
    bal.bal_w_event()



def bal_btn():
    print('test')

def test_event():
    print('test')


def bal_signals():
    for i in range(8):
        bal_btn[i].clicked.connect(bal_btn)


# -------메인

ser = serial.Serial(port='COM14',
    				baudrate=115200,
        			parity=serial.PARITY_NONE,
        			stopbits=serial.STOPBITS_ONE,
        			bytesize=serial.EIGHTBITS,
    				timeout=1)



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

MainWindow.showFullScreen()

MainWindow.bal_r_event = bal_r_event
MainWindow.bal_b_event = bal_b_event
MainWindow.bal_w_event = bal_w_event

ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.stackedWidget.setCurrentIndex(2)


#mysql
conn = pymysql.connect(host='localhost', user='root', password='1234', db='smartfarm', charset='utf8')





#밝기조절 클래스


bal = Balgi(ui,ser,conn) 
bal.bal_data_change()

app.exec_()
