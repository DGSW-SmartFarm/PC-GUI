import pymysql
import sys
from Ui_test import *
from bal_class import *
from kit_class import * 
from pen_class import * 
from grap import *
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QRect, QUrl, QTimer
from PyQt5.QtGui import QDesktopServices, QColor
import datetime, time
import threading

def buttonchange(self):
        btn = self.sender().checkedButton().objectName()

        if(btn == 'chk_temp'):
                ui.stackedWidget.setCurrentIndex(6)
                kit.kit_data_change('t','c')
                
        elif(btn == 'chk_tds'):
                ui.stackedWidget.setCurrentIndex(6)
                kit.kit_data_change('s','t')
                 
        elif(btn == 'chk_ph2'):
                ui.stackedWidget.setCurrentIndex(6)
                kit.kit_data_change('p','p')
 
        elif(btn == 'chk_light'):
                ui.stackedWidget.setCurrentIndex(6)
                kit.kit_data_change('i','%')
 
        elif(btn == 'chk_hum'):
                ui.stackedWidget.setCurrentIndex(6)
                kit.kit_data_change('h','%')
 
        elif(btn == 'chk_co2'):
                ui.stackedWidget.setCurrentIndex(6)
                kit.kit_data_change('c','c')
 
        elif(btn == 'see_grap'):
                ui.stackedWidget.setCurrentIndex(0)
 
        elif(btn == 'see_pen'):
                ui.stackedWidget.setCurrentIndex(1)
 
        elif(btn == 'see_co2'):
                ui.stackedWidget.setCurrentIndex(4)
 
        elif(btn == 'see_bal'):
                ui.stackedWidget.setCurrentIndex(2)
                bal.bal_data_change()
 
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

def grap_btn(self):
        global nowi

        btn = self.sender().checkedButton().objectName()
        grap_list = ['grap_temp','grap_hum','grap_co2','grap_light']
        grap_location = [QRect(350,70,61,5),QRect(560,70,61,5),QRect(770,70,61,5),QRect(980,70,61,5)]

        i = grap_list.index(btn)
        if nowi == i:
                return
        

        ui.anim = QPropertyAnimation(ui.grap_ch, b"geometry")
        ui.anim.setDuration(1000)
        ui.anim.setStartValue(grap_location[nowi])
        ui.anim.setEndValue(grap_location[i])
        ui.anim.setEasingCurve(QEasingCurve(QEasingCurve.InOutQuart))
        ui.anim.start()
        
        nowi = i


        graph_update(ui.graphicsView,x[nowi],y[nowi],strf="%H:%M:%S")

        


def data_update():
        while True:
                with lock:
                        curs.execute('select distinct label from data;')
                        row = curs.fetchall()

                for i in row:
                        message = ''.join(['\x02',str(i[0]),'TEMP?','\x03\x0A\x0D'])
                        ser.write(bytes(message.encode()))
                        print(message)
                        time.sleep(0.5)

                        while True:
                                rxdata = ser.readline().decode('utf-8')
                                print('rxdata =',rxdata)

                                if(rxdata):
                                        if(len(rxdata) > 5):
                                                if rxdata[0] == chr(13):
                                                        rxdata = rxdata[1:]
                                                if(rxdata[1:3] == i[0] and len(rxdata) == 23):
                                                        print('sql=in',rxdata[1:3])
                                                        with lock:
                                                                curs.execute(("insert into sensor values('0','%s','%s','%s','%s','%s','%f');") % (rxdata[1:3], rxdata[4:9], rxdata[10:12], rxdata[13:17],rxdata[18:21],time.time()))
                                                                conn.commit()

                                                        break
                                                

                                else:
                                        break
                        for j in range(2):
                                ser.readline()

                        

                kit.sensor_data_change()




def timer_ovf():
        
        
        chk_arr = [ui.chk_temp,ui.chk_hum,ui.chk_co2,ui.chk_light,ui.chk_ph2,ui.chk_tds]
        chk_s = ['t','h','c','i','p','s']
        chk_formet = ['%.1f°','%d%%','%d','%d%%','%d','%d']
        settime = time.time()
        for i in range(6):

                if chk_s[i] == 's' or chk_s[i] == 'p':
                        sqls = ("select *,basicv from data where id = '%s' and onoff = 1;") % (chk_s[i])
                else:
                        sqls = ("select d.*, ( select s.%s from sensor s where s.label = d.label order by s.no desc limit 1 ) from data d where d.id = '%s' and onoff = 1;") % (chk_s[i],chk_s[i])

                with lock:
                        curs.execute(sqls)
                        data = curs.fetchall()   

                sum = 0
                
                if (len(data) == 0):
                        gap = 0
                        chk_arr[i].setText(''.join(['\n\n\n',chk_formet[i] % gap]))
                else:    
                        cnt = 0
                        for j in data:
                                cnt = cnt + 1
                                if j[6] is None:
                                        sum = sum + j[4]
                                else:
                                        sum = sum + j[6]
                        
                        if cnt == 0:
                                gqp = 0
                        else:
                                gap = sum/cnt

                        chk_arr[i].setText(''.join(['\n\n\n',chk_formet[i] % gap]))
                if i < 4:
                        x[i].append(settime)
                        y[i].append(gap)
                
        graph_update(ui.graphicsView,x[nowi],y[nowi],strf="%H:%M:%S")

        
def exitexit(self):
        sys.exit(app.exec_())

# -------메인

ser = serial.Serial(port='COM14',
    				baudrate=115200,
        			parity=serial.PARITY_NONE,
        			stopbits=serial.STOPBITS_ONE,
        			bytesize=serial.EIGHTBITS,
    				timeout=1)



nowi = 0

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

MainWindow.showFullScreen()
MainWindow.dgsw = dgsw
MainWindow.exitexit = exitexit

ui = Ui_MainWindow()
ui.setupUi(MainWindow)




ui.buttonGroup.buttonClicked.connect(buttonchange)
ui.buttonGroup_2.buttonClicked.connect(grap_btn)

#mysql
conn = pymysql.connect(host='localhost', user='root', password='1234', db='smartfarm', charset='utf8')
curs = conn.cursor()
conn2 = pymysql.connect(host='localhost', user='root', password='1234', db='smartfarm', charset='utf8')


lock = threading.Lock()

#밝기조절 클래스

kit = Kit(ui,ser,conn,lock)
kit.kit_data_change('t','°')

bal = Balgi(ui,ser,conn2) 
bal.bal_data_change()

pen = Pen(ui,ser,conn2)
pen.pen_data_change()

time.sleep(9)

data_update_thread = threading.Thread(target=data_update)  #쓰레드 생성
data_update_thread.daemon = True
data_update_thread.start()


graph_init(ui.graphicsView)

x = [deque(maxlen=9) for i in range(4)]
y = [deque(maxlen=9) for i in range(4)]


ui.stackedWidget.setCurrentIndex(9)
ui.credit.setChecked(True)

timer = QTimer()
timer.timeout.connect(timer_ovf)
timer_ovf()
timer.start(10000)

app.exec_()
