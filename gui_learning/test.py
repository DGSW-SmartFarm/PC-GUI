import pymysql
import sys
from Ui_test import *
from bal_class import *
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QRect, QUrl, QTimer
from PyQt5.QtGui import QDesktopServices, QColor

def buttonchange(self):
        btn = self.sender().checkedButton().objectName()

        if(btn == 'chk_temp'):
                pass
                
        elif(btn == 'chk_tds'):
                pass
                 
        elif(btn == 'chk_ph2'):
                pass
 
        elif(btn == 'chk_light'):
                pass
 
        elif(btn == 'chk_hum'):
                pass
 
        elif(btn == 'chk_co2'):
                pass
 
        elif(btn == 'see_grap'):
                ui.stackedWidget.setCurrentIndex(0)
 
        elif(btn == 'see_pen'):
                ui.stackedWidget.setCurrentIndex(1)
 
        elif(btn == 'see_co2'):
                ui.stackedWidget.setCurrentIndex(4)
 
        elif(btn == 'see_bal'):
                ui.stackedWidget.setCurrentIndex(2)
 
        elif(btn == 'see_temp'):
                ui.stackedWidget.setCurrentIndex(3)

        elif(btn == 'see_yang'):
                ui.stackedWidget.setCurrentIndex(5)

        elif(btn == 'set'):
                ui.stackedWidget.setCurrentIndex(8)

        elif(btn == 'credit'):
                ui.stackedWidget.setCurrentIndex(9)

def dgsw(self):
        QDesktopServices.openUrl(QUrl("www.dgsw.hs.kr"))

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
MainWindow.dgsw = dgsw


ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.stackedWidget.setCurrentIndex(2)



ui.buttonGroup.buttonClicked.connect(buttonchange)


#mysql
conn = pymysql.connect(host='localhost', user='root', password='1234', db='smartfarm', charset='utf8')





#밝기조절 클래스


bal = Balgi(ui,ser,conn) 
bal.bal_data_change()

app.exec_()
