
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import pymysql
from time import sleep

class Balgi(QtWidgets.QMainWindow):

    test = 10
    ind = [0,1,2,3,4,5,6,7]
    nowchk = 0
    nowadd = 0

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
        
        self.ui.bal_left_btn.clicked.connect(self.bal_left_btn_event)
        self.ui.bal_right_btn.clicked.connect(self.bal_right_btn_event)

        self.curs.execute("select * from bal;")
        data = self.curs.fetchall()
        
        i=0
        
        self.pen_value = [0 for i in range(len(data))]
        self.sql_in = [0 for i in range(len(data))]

        self.curs.execute("select * from pen")
        data_pen = self.curs.fetchall()


        for i in range(len(data)):
            self.sql_in[i] = data[i][0]
            

            for d in data_pen:
    
                if(data[i][1] == d[1]):
                    self.pen_value[i] = d[3]

            message = ''.join(['\x02',data[i][1],'P',str(self.pen_value[i]).zfill(3),'R',str(data[i][3]).zfill(3),'B',str(data[i][4]).zfill(3),'W',str(data[i][5]).zfill(3),'\x03'])
            print(message)
            self.ser.write(bytes(message.encode()))
            sleep(0.7)


    def bal_left_btn_event(self):
        if self.nowadd > 0:
            self.nowadd = self.nowadd-2
            self.bal_data_change()

    def bal_right_btn_event(self):
        print('evnet')
        if self.nowadd + 7 + 2 <= len(self.sql_in)+1: 
            self.nowadd = self.nowadd + 2
            self.bal_data_change()

    def send_data(self):
        
        ID=self.bal_label[self.nowchk].text()
        P=str(self.pen_value[self.nowchk+self.nowadd]+1000)[1:]
        R=str(int(self.bal_r[self.nowchk].text())+1000)[1:]
        B=str(int(self.bal_b[self.nowchk].text())+1000)[1:]
        W=str(int(self.bal_w[self.nowchk].text())+1000)[1:]
        
        
        self.curs.execute(('update bal set r = %s, b = %s, w = %s where no = %d') % (R,B,W,self.sql_in[self.nowchk+self.nowadd]))
        print(('update bal set r = %s, b = %s, w = %s where no = %d') % (R,B,W,self.sql_in[self.nowchk+self.nowadd]))
        self.conn.commit()

        if self.bal_onoff[self.nowchk].isChecked() == True:
            message = ''.join(['\x02',ID,'P',P,'R',R,'B',B,'W',W,'\x03'])
        else: 
            message = ''.join(['\x02',ID,'P',P,'R','000','B','000','W','000','\x03'])
        

        
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
        if index == len(self.sql_in) - self.nowadd:
            self.curs.execute(("insert into bal values(0,'식별번호','이름',0,0,0,true);"))
            self.conn.commit()
            self.bal_data_change()

        else:    
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
        index = self.get_index(self.sender().objectName())
        self.chk_event(index)

        self.curs.execute(("update bal set onoff = '%d' where no = '%d' ") % (int(self.bal_onoff[index].isChecked()), self.sql_in[self.nowchk+self.nowadd] ))
        self.conn.commit()

        self.send_data()
    
    def bal_su_event(self):
        index = self.get_index(self.sender().objectName())
        self.chk_event(index)
        
        if(self.bal_su[index].isChecked()):
            self.bal_text[index].setEnabled(True)
            self.bal_label[index].setEnabled(True) 
        else:
            self.bal_text[index].setEnabled(False)
            self.bal_label[index].setEnabled(False)
            self.curs.execute(("update bal set text = '%s', label = '%s' where no = '%d' ") % (self.bal_text[index].text(),self.bal_label[index].text(), self.sql_in[index+self.nowadd] ))
            self.conn.commit()
            
        
        


    def bal_clo_event(self):
        print('clo')
        index = self.get_index(self.sender().objectName())
        self.chk_event(index)

        quit_msg = "정말 삭제하시겠습니까?"
        reply = QtWidgets.QMessageBox.question(self, '확인', 
                        quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        
        if reply == QtWidgets.QMessageBox.Yes:
            self.curs.execute(("delete from bal where no = '%d' ") % (self.sql_in[index+self.nowadd]) )
            self.conn.commit()
            self.bal_data_change()

        else:
            print('no')
        
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
            self.sql_in[i] = data[i][0]
            

            for d in data_pen:
    
                if(data[i][1] == d[1]):
                    self.pen_value[i] = d[3]


        lt = len(data)
        
        print('lt=',lt)
        if(lt != 0):
            for i in range(min(8,lt-self.nowadd)):
                self.bal_btn[i].lower()
                self.bal_wi[i].setVisible(True)
                self.bal_btn[i].setStyleSheet('image : url(./);\nbackground-color : rgba(0,0,0,0);')
                self.bal_btn[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) 
                self.bal_label[i].setText(data[i+self.nowadd][1])
                self.bal_text[i].setText(data[i+self.nowadd][2])
                self.bal_r[i].setNum(data[i+self.nowadd][3])
                self.bal_b[i].setNum(data[i+self.nowadd][4])
                self.bal_w[i].setNum(data[i+self.nowadd][5])
                self.bal_onoff[i].setChecked(data[i+self.nowadd][6])
            
                self.bal_wi[i].setStyleSheet(self.originalstyle)
        else:
            i = -1    

        print(self.pen_value)

        self.nowchk = 0    

        

        for j in range(i+1,8):
            self.bal_btn[j].raise_()
            self.bal_btn[j].setStyleSheet('image : url(./); background-color : rgba(255,255,255);')
            self.bal_btn[j].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor)) 
        
        self.bal_wi[self.nowchk].setStyleSheet(self.chkstyle)
        
        if(not(i == 7)):
            self.bal_btn[i+1].setStyleSheet('QPushButton{image:url(./image/add_btn.png); border:0px; background-color : rgba(255,255,255);} QPushButton:hover{image:url(./image/add_btn2.png); border:0px; background-color : rgba(255,255,255);}')
            self.bal_btn[i+1].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) 
            

        self.count = len(data)

        

        self.update_kit()