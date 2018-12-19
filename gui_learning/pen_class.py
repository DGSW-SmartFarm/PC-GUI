
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import pymysql
from time import sleep

class Pen(QtWidgets.QMainWindow):

    test = 10
    ind = [0,1,2,3,4,5,6,7]
    nowchk = 0
    nowadd = 0

    count = 0

    tmp = 0



    originalstyle = 'QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}'
    chkstyle = 'QWidget{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}'


    



    def __init__(self,ui,ser,conn):
        super().__init__()

        self.ser = ser
        self.conn = conn
        self.curs = conn.cursor()
        

        self.ui = ui
        self.pen_wi = [self.ui.pen_wi_1,self.ui.pen_wi_2,self.ui.pen_wi_3,self.ui.pen_wi_4,self.ui.pen_wi_5,self.ui.pen_wi_6,self.ui.pen_wi_7,self.ui.pen_wi_8]
        self.pen_btn = [self.ui.pen_btn_1,self.ui.pen_btn_2,self.ui.pen_btn_3,self.ui.pen_btn_4,self.ui.pen_btn_5,self.ui.pen_btn_6,self.ui.pen_btn_7,self.ui.pen_btn_8]
        self.pen_clo = [self.ui.pen_clo_1,self.ui.pen_clo_2,self.ui.pen_clo_3,self.ui.pen_clo_4,self.ui.pen_clo_5,self.ui.pen_clo_6,self.ui.pen_clo_7,self.ui.pen_clo_8]
        self.pen_label = [self.ui.pen_label_1,self.ui.pen_label_2,self.ui.pen_label_3,self.ui.pen_label_4,self.ui.pen_label_5,self.ui.pen_label_6,self.ui.pen_label_7,self.ui.pen_label_8]
        self.pen_onoff = [self.ui.pen_onoff_1,self.ui.pen_onoff_2,self.ui.pen_onoff_3,self.ui.pen_onoff_4,self.ui.pen_onoff_5,self.ui.pen_onoff_6,self.ui.pen_onoff_7,self.ui.pen_onoff_8]
        self.pen_value = [self.ui.pen_value_1,self.ui.pen_value_2,self.ui.pen_value_3,self.ui.pen_value_4,self.ui.pen_value_5,self.ui.pen_value_6,self.ui.pen_value_7,self.ui.pen_value_8]
        self.pen_su = [self.ui.pen_su_1,self.ui.pen_su_2,self.ui.pen_su_3,self.ui.pen_su_4,self.ui.pen_su_5,self.ui.pen_su_6,self.ui.pen_su_7,self.ui.pen_su_8]
        self.pen_text = [self.ui.pen_text_1,self.ui.pen_text_2,self.ui.pen_text_3,self.ui.pen_text_4,self.ui.pen_text_5,self.ui.pen_text_6,self.ui.pen_text_7,self.ui.pen_text_8]
        
        for i in range(8):
            self.pen_btn[i].clicked.connect(self.pen_btn_event)
            self.pen_onoff[i].clicked.connect(self.pen_onoff_event)
            self.pen_su[i].clicked.connect(self.pen_su_event)
            self.pen_clo[i].clicked.connect(self.pen_clo_event)
            
        self.ui.pen_slider.valueChanged.connect(self.pen_event)


        self.ui.pen_slider.sliderReleased.connect(self.send_data)


        self.ui.pen_onoff_btn.clicked.connect(self.pen_slider_btn_event)

        
        self.ui.pen_left_btn.clicked.connect(self.pen_left_btn_event)
        self.ui.pen_right_btn.clicked.connect(self.pen_right_btn_event)


        self.curs.execute("select * from pen;")
        data = self.curs.fetchall()
        
        i=0
        
        self.bal_value = [[0 for j in range(3)] for i in range(len(data))]
        self.sql_in = [0 for i in range(len(data))]

        self.curs.execute("select * from bal")
        data_bal = self.curs.fetchall()


        for i in range(len(data)):
            self.sql_in[i] = data[i][0]
            

            for d in data_bal:
    
                if(data[i][1] == d[1]):
                    self.bal_value[i][0] = d[3]
                    self.bal_value[i][1] = d[4]
                    self.bal_value[i][2] = d[5]

            message = ''.join(['\x02',data[i][1],'P',str(data[i][3]).zfill(3),'R',str(self.bal_value[i][0]).zfill(3),'B',str(self.bal_value[i][1]).zfill(3),'W',str(self.bal_value[i][2]).zfill(3),'\x03'])
            print(message)
            self.ser.write(bytes(message.encode()))
            sleep(0.7)


    def pen_left_btn_event(self):
        if self.nowadd > 0:
            self.nowadd = self.nowadd-2
            self.pen_data_change()

    def pen_right_btn_event(self):
        print('evnet')
        if self.nowadd + 7 + 2 <= len(self.sql_in)+1: 
            self.nowadd = self.nowadd + 2
            self.pen_data_change()

    def send_data(self):
        
        ID=self.pen_label[self.nowchk].text()
        P=str(int(self.pen_value[self.nowchk].text())+1000)[1:]
        R=str(self.bal_value[self.nowchk+self.nowadd][0]+1000)[1:]
        B=str(self.bal_value[self.nowchk+self.nowadd][1]+1000)[1:]
        W=str(self.bal_value[self.nowchk+self.nowadd][2]+1000)[1:]
        
        
        self.curs.execute(('update pen set val = %s where no = %d') % (P, self.sql_in[self.nowchk+self.nowadd]))
        self.conn.commit()

        if self.pen_onoff[self.nowchk].isChecked() == True:
            message = ''.join(['\x02',ID,'P',P,'R',R,'B',B,'W',W,'\x03'])
        else: 
            message = ''.join(['\x02',ID,'P','000','R',R,'B',B,'W',W,'\x03'])
        

        
        self.ser.write(bytes(message.encode()))
        print(message)

    def update_kit(self):
        self.set_val_value()
        self.pen_event()

        self.tmp = self.ui.pen_slider.value()



    def set_val_value(self):
        self.ui.pen_slider.setValue(int(self.pen_value[self.nowchk].text()))

    def get_index(self,txt):
        return int(txt.split('_')[2]) - 1

    def pen_btn_event(self):
        
        index = self.get_index(self.sender().objectName())
        self.chk_event(index)
        if index == len(self.sql_in) - self.nowadd:
            self.curs.execute(("insert into pen values(0,'식별번호','이름',0,true);"))
            self.conn.commit()
            self.pen_data_change()

        else:    
            self.chk_event(index)

    def chk_event(self,index):

        if(index > self.count - 1):
            return
        
        print(self.nowchk,index)

        self.pen_wi[self.nowchk].setStyleSheet(self.originalstyle)
        self.nowchk = index
        self.pen_wi[self.nowchk].setStyleSheet(self.chkstyle)
        self.update_kit()
    
    def pen_onoff_event(self):
        index = self.get_index(self.sender().objectName())
        self.chk_event(index)

        self.curs.execute(("update pen set onoff = '%d' where no = '%d' ") % (int(self.pen_onoff[index].isChecked()), self.sql_in[self.nowchk+self.nowadd] ))
        self.conn.commit()

        self.send_data()
    
    def pen_su_event(self):
        index = self.get_index(self.sender().objectName())
        self.chk_event(index)
        
        if(self.pen_su[index].isChecked()):
            self.pen_text[index].setEnabled(True)
            self.pen_label[index].setEnabled(True) 
        else:
            self.pen_text[index].setEnabled(False)
            self.pen_label[index].setEnabled(False)
            self.curs.execute(("update pen set text = '%s', label = '%s' where no = '%d' ") % (self.pen_text[index].text(),self.pen_label[index].text(), self.sql_in[index+self.nowadd] ))
            self.conn.commit()
            
        
        


    def pen_clo_event(self):
        print('clo')
        index = self.get_index(self.sender().objectName())
        self.chk_event(index)

        quit_msg = "정말 삭제하시겠습니까?"
        reply = QtWidgets.QMessageBox.question(self, '확인', 
                        quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        
        if reply == QtWidgets.QMessageBox.Yes:
            self.curs.execute(("delete from pen where no = '%d' ") % (self.sql_in[index+self.nowadd]) )
            self.conn.commit()
            self.pen_data_change()

        else:
            print('no')
    

    
    def pen_slider_btn_event(self):
        val = self.ui.pen_slider.value()
        
        if(val == 0):
            self.ui.pen_slider.setValue(max(1,self.tmp))
        else:
            self.tmp = val
            self.ui.pen_slider.setValue(0)

        self.pen_value[self.nowchk].setNum(self.ui.pen_slider.value())
        self.send_data();
    
  
    def pen_event(self):

        val = int(self.ui.pen_value_label.text())
        if(val > 0):
            self.ui.pen_onoff_btn.setChecked(True)
        else:
            self.ui.pen_onoff_btn.setChecked(False)

        self.pen_value[self.nowchk].setNum(val)

    def pen_data_change(self):
        self.curs.execute("select * from pen;")
        data = self.curs.fetchall()
        
        i=0
        
        self.bal_value = [[0 for j in range(3)] for i in range(len(data))]
        self.sql_in = [0 for i in range(len(data))]

        self.curs.execute("select * from bal")
        data_bal = self.curs.fetchall()


        for i in range(len(data)):
            self.sql_in[i] = data[i][0]
            

            for d in data_bal:
    
                if(data[i][1] == d[1]):
                    self.bal_value[i][0] = d[3]
                    self.bal_value[i][1] = d[4]
                    self.bal_value[i][2] = d[5]



        lt = len(data)
        
        print('lt=',lt)
        
        if(lt != 0):
            for i in range(min(8,lt-self.nowadd)):
                self.pen_btn[i].lower()
                self.pen_wi[i].setVisible(True)
                self.pen_btn[i].setStyleSheet('image : url(./);\nbackground-color : rgba(0,0,0,0);')
                self.pen_btn[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) 
                self.pen_label[i].setText(data[i+self.nowadd][1])
                self.pen_text[i].setText(data[i+self.nowadd][2])
                self.pen_value[i].setNum(data[i+self.nowadd][3])
                self.pen_onoff[i].setChecked(data[i+self.nowadd][4])
            
                self.pen_wi[i].setStyleSheet(self.originalstyle)
        else:
            i = -1     

        print(self.bal_value)

        self.nowchk = 0    

        

        for j in range(i+1,8):
            self.pen_btn[j].raise_()
            self.pen_btn[j].setStyleSheet('image : url(./); background-color : rgba(255,255,255,255); border : 0px;')
            self.pen_btn[j].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor)) 
        
        self.pen_wi[self.nowchk].setStyleSheet(self.chkstyle)
        
        if(not(i == 7)):
            self.pen_btn[i+1].setStyleSheet('QPushButton{image:url(./image/add_smbtn.png); border:0px; background-color : rgba(255,255,255);} QPushButton:hover{image:url(./image/add_smbtn2.png); border:0px; background-color : rgba(255,255,255);}')
            self.pen_btn[i+1].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) 
            

        self.count = len(data)

        

        self.update_kit()