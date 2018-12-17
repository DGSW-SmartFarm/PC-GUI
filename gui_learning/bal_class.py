
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import pymysql

class Balgi(QtWidgets.QMainWindow):

    test = 10
    ind = [0,1,2,3,4,5,6,7]
    nowchk = 0
    count = 0

    tmprbw = [0,0,0]



    originalstyle = 'QWidget{image:url(./image/kit_light.png); border:0px; background-color : rgba(0,0,0,0);}QWidget:hover{image:url(./image/kit_light2.png); border:0px; background-color : rgba(0,0,0,0);}'
    chkstyle = 'QWidget{image:url(./image/kit_light2.png); border:0px; background-color : rgba(0,0,0,0);}'






    def __init__(self,ui,ser,conn):
        super().__init__()

        self.ser = ser
        self.conn = conn
        self.curs = conn.cursor()
        

        self.ui = ui
        self.bal_wi = [self.ui.bal_wi_1,self.ui.bal_wi_2,self.ui.bal_wi_3,self.ui.bal_wi_4,self.ui.bal_wi_5,self.ui.bal_wi_6,self.ui.bal_wi_7,self.ui.bal_wi_8]
        self.bal_b = [self.ui.bal_b_1,self.ui.bal_b_2,self.ui.bal_b_3,self.ui.bal_b_4,self.ui.bal_b_5,self.ui.bal_b_6,self.ui.bal_b_7,self.ui.bal_b_8]
        self.bal_btn = [self.ui.bal_btn_1,self.ui.bal_btn_2,self.ui.bal_btn_3,self.ui.bal_btn_4,self.ui.bal_btn_5,self.ui.bal_btn_6,self.ui.bal_btn_7,self.ui.bal_btn_8]
        self.bal_clo = [self.ui.bal_clo_1,self.ui.bal_clo_2,self.ui.bal_clo_3,self.ui.bal_clo_4,self.ui.bal_clo_5,self.ui.bal_clo_6,self.ui.bal_clo_7,self.ui.bal_clo_8]
        self.bal_label = [self.ui.bal_label_1,self.ui.bal_label_2,self.ui.bal_label_3,self.ui.bal_label_4,self.ui.bal_label_5,self.ui.bal_label_6,self.ui.bal_label_7,self.ui.bal_label_8]
        self.bal_onoff = [self.ui.bal_onoff_1,self.ui.bal_onoff_2,self.ui.bal_onoff_3,self.ui.bal_onoff_4,self.ui.bal_onoff_5,self.ui.bal_onoff_6,self.ui.bal_onoff_7,self.ui.bal_onoff_8]
        self.bal_r = [self.ui.bal_r_1,self.ui.bal_r_2,self.ui.bal_r_3,self.ui.bal_r_4,self.ui.bal_r_5,self.ui.bal_r_6,self.ui.bal_r_7,self.ui.bal_r_8]
        self.bal_su = [self.ui.bal_su_1,self.ui.bal_su_2,self.ui.bal_su_3,self.ui.bal_su_4,self.ui.bal_su_5,self.ui.bal_su_6,self.ui.bal_su_7,self.ui.bal_su_8]
        self.bal_text = [self.ui.bal_text_1,self.ui.bal_text_2,self.ui.bal_text_3,self.ui.bal_text_4,self.ui.bal_text_5,self.ui.bal_text_6,self.ui.bal_text_7,self.ui.bal_text_8]
        self.bal_w = [self.ui.bal_w_1,self.ui.bal_w_2,self.ui.bal_w_3,self.ui.bal_w_4,self.ui.bal_w_5,self.ui.bal_w_6,self.ui.bal_w_7,self.ui.bal_w_8]

        for i in range(8):
            self.bal_btn[i].clicked.connect(self.bal_btn_event)
            self.bal_onoff[i].clicked.connect(self.bal_onoff_event)
            self.bal_su[i].clicked.connect(self.bal_su_event)
            self.bal_clo[i].clicked.connect(self.bal_clo_event)
            
        self.ui.bal_r_val.valueChanged.connect(self.bal_r_event)
        self.ui.bal_b_val.valueChanged.connect(self.bal_b_event)
        self.ui.bal_w_val.valueChanged.connect(self.bal_w_event)

        self.ui.bal_r_val.sliderReleased.connect(self.send_data)
        self.ui.bal_b_val.sliderReleased.connect(self.send_data)
        self.ui.bal_w_val.sliderReleased.connect(self.send_data)

        self.ui.bal_r_btn.clicked.connect(self.bal_r_btn_event)
        self.ui.bal_b_btn.clicked.connect(self.bal_b_btn_event)
        self.ui.bal_w_btn.clicked.connect(self.bal_w_btn_event)
        
        #self.bal_data_change([[1,2],[1,2],[1,2]]) #testdata



    def send_data(self):
        
        ID=self.bal_label[self.nowchk].text()
        P=str(self.pen_value[self.nowchk]+1000)[1:]
        R=str(int(self.bal_r[self.nowchk].text())+1000)[1:]
        B=str(int(self.bal_b[self.nowchk].text())+1000)[1:]
        W=str(int(self.bal_w[self.nowchk].text())+1000)[1:]
        
        
        self.curs.execute(('update bal set r = %s, b = %s, w = %s where no = %d') % (R,B,W,self.sql_in[self.nowchk]))
        print(('update bal set r = %s, b = %s, w = %s where no = %d') % (R,B,W,self.sql_in[self.nowchk]))
        self.conn.commit()

        if self.bal_onoff[self.nowchk].isChecked == False:
            return 
        #on/off 취소

        message = ''.join(['\x02',ID,'P',P,'R',R,'B',B,'W',W,'\x03'])
        self.ser.write(bytes(message.encode()))
        print(message)

    def update_kit(self):
        self.set_val_value()
        self.bal_r_event()
        self.bal_b_event()
        self.bal_w_event()

        self.tmprbw[0] = self.ui.bal_r_val.value()
        self.tmprbw[1] = self.ui.bal_b_val.value()
        self.tmprbw[2] = self.ui.bal_w_val.value()


    def set_val_value(self):
        self.ui.bal_r_val.setValue(int(self.bal_r[self.nowchk].text()))
        self.ui.bal_b_val.setValue(int(self.bal_b[self.nowchk].text()))
        self.ui.bal_w_val.setValue(int(self.bal_w[self.nowchk].text()))

    def get_index(self,txt):
        return int(txt.split('_')[2]) - 1

    def bal_btn_event(self):
        
        index = self.get_index(self.sender().objectName())
        self.chk_event(index)

    def chk_event(self,index):

        if(index > self.count - 1):
            return
        
        print(self.nowchk,index)

        self.bal_wi[self.nowchk].setStyleSheet(self.originalstyle)
        self.nowchk = index
        self.bal_wi[self.nowchk].setStyleSheet(self.chkstyle)
        self.update_kit()
    
    def bal_onoff_event(self):
        print('onoff')
    
    def bal_su_event(self):
        print('su')
    
    def bal_clo_event(self):
        print('clo')
        
    def bal_r_btn_event(self):
        self.bal_color_btn_event(self.ui.bal_r_val, self.bal_r[self.nowchk], 0)

    def bal_b_btn_event(self):
        self.bal_color_btn_event(self.ui.bal_b_val, self.bal_b[self.nowchk], 1)
        # val = self.ui.bal_b_val.value()


        # if(val == 0):
        #     self.ui.bal_b_val.setValue(max(1,self.tmpb))
        # else:
        #     self.tmpb = val
        #     self.ui.bal_b_val.setValue(0)
        # self.bal_b[self.nowchk].setNum(self.ui.bal_b_val.value())
        # self.send_data();

    def bal_w_btn_event(self):
        self.bal_color_btn_event(self.ui.bal_w_val, self.bal_w[self.nowchk], 2)

    def bal_color_btn_event(self, slider, bal_label, ti):
        val = slider.value()
        
        if(val == 0):
            slider.setValue(max(1,self.tmprbw[ti]))
        else:
            self.tmprbw[ti] = val
            slider.setValue(0)

        bal_label.setNum(slider.value())
        self.send_data();
    

    def bal_r_event(self):
        self.bal_event(self.ui.bal_r_num,self.ui.bal_r_btn,self.bal_r[self.nowchk],0)
        

    def bal_b_event(self):
        self.bal_event(self.ui.bal_b_num,self.ui.bal_b_btn,self.bal_b[self.nowchk],1)
        

    def bal_w_event(self):
        self.bal_event(self.ui.bal_w_num,self.ui.bal_w_btn,self.bal_w[self.nowchk],2)

        
    def bal_event(self,num,btn,label,ti):
        val = int(num.text())
        if(val > 0):
            btn.setChecked(True)
        else:
            btn.setChecked(False)
            #self.tmprbw[ti] = 0

        label.setNum(val)

    def bal_data_change(self):
        self.curs.execute("select * from bal;")
        data = self.curs.fetchall()
        
        i=0
        
        self.pen_value = [0 for i in range(len(data))]
        self.sql_in = [0 for i in range(len(data))]

        self.curs.execute("select * from pen")
        data_pen = self.curs.fetchall()

        for i in range(len(data)):
            self.bal_wi[i].setVisible(True)
            self.bal_btn[i].setStyleSheet('image : url(./);\nbackground-color : rgba(0,0,0,0);')
            self.bal_btn[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) 
            self.bal_label[i].setText(data[i][1])
            self.bal_text[i].setText(data[i][2])
            self.bal_r[i].setNum(data[i][3])
            self.bal_b[i].setNum(data[i][4])
            self.bal_w[i].setNum(data[i][5])
            self.bal_onoff[i].setChecked(data[i][6])
        
            self.bal_wi[i].setStyleSheet(self.originalstyle)
            
            self.sql_in[i] = data[i][0]

            for d in data_pen:
    
                if(data[i][1] == d[1]):
                    self.pen_value[i] = d[3]
            
        print(self.pen_value)
            


        for j in range(i+1,8):
            self.bal_btn[j].raise_()
            self.bal_btn[j].setStyleSheet('image : url(./); background-color : rgba(255,255,255);')
            self.bal_btn[j].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor)) 
        
        self.bal_wi[self.nowchk].setStyleSheet(self.chkstyle)
        
        self.count = len(data)

        self.update_kit()