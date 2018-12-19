from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import pymysql

class Kit(QtWidgets.QMainWindow):

    test = 10
    ind = [0,1,2,3,4,5,6,7]
    nowchk = 0
    nowadd = 0

    count = 0

    tmprbw = [0,0,0]



    originalstyle = 'QWidget{image:url(./image/kit2_light.png); border:0px; background-color : rgba(0,0,0,0);}QWidget:hover{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}'
    chkstyle = 'QWidget{image:url(./image/kit2_light2.png); border:0px; background-color : rgba(0,0,0,0);}'





    def __init__(self,ui,ser,conn,lock):
        super().__init__()

        self.ser = ser
        self.conn = conn
        self.curs = conn.cursor()
        self.lock = lock

        self.ui = ui
        self.kit_wi = [self.ui.kit_wi_1,self.ui.kit_wi_2,self.ui.kit_wi_3,self.ui.kit_wi_4,self.ui.kit_wi_5,self.ui.kit_wi_6,self.ui.kit_wi_7,self.ui.kit_wi_8,self.ui.kit_wi_9,self.ui.kit_wi_10,self.ui.kit_wi_11,self.ui.kit_wi_12]
        self.kit_value = [self.ui.kit_value_1,self.ui.kit_value_2,self.ui.kit_value_3,self.ui.kit_value_4,self.ui.kit_value_5,self.ui.kit_value_6,self.ui.kit_value_7,self.ui.kit_value_8,self.ui.kit_value_9,self.ui.kit_value_10,self.ui.kit_value_11,self.ui.kit_value_12]
        self.kit_btn = [self.ui.kit_btn_1,self.ui.kit_btn_2,self.ui.kit_btn_3,self.ui.kit_btn_4,self.ui.kit_btn_5,self.ui.kit_btn_6,self.ui.kit_btn_7,self.ui.kit_btn_8,self.ui.kit_btn_9,self.ui.kit_btn_10,self.ui.kit_btn_11,self.ui.kit_btn_12]
        self.kit_clo = [self.ui.kit_clo_1,self.ui.kit_clo_2,self.ui.kit_clo_3,self.ui.kit_clo_4,self.ui.kit_clo_5,self.ui.kit_clo_6,self.ui.kit_clo_7,self.ui.kit_clo_8,self.ui.kit_clo_9,self.ui.kit_clo_10,self.ui.kit_clo_11,self.ui.kit_clo_12]
        self.kit_label = [self.ui.kit_label_1,self.ui.kit_label_2,self.ui.kit_label_3,self.ui.kit_label_4,self.ui.kit_label_5,self.ui.kit_label_6,self.ui.kit_label_7,self.ui.kit_label_8,self.ui.kit_label_9,self.ui.kit_label_10,self.ui.kit_label_11,self.ui.kit_label_12]
        self.kit_onoff = [self.ui.kit_onoff_1,self.ui.kit_onoff_2,self.ui.kit_onoff_3,self.ui.kit_onoff_4,self.ui.kit_onoff_5,self.ui.kit_onoff_6,self.ui.kit_onoff_7,self.ui.kit_onoff_8,self.ui.kit_onoff_9,self.ui.kit_onoff_10,self.ui.kit_onoff_11,self.ui.kit_onoff_12]
        self.kit_su = [self.ui.kit_su_1,self.ui.kit_su_2,self.ui.kit_su_3,self.ui.kit_su_4,self.ui.kit_su_5,self.ui.kit_su_6,self.ui.kit_su_7,self.ui.kit_su_8,self.ui.kit_su_9,self.ui.kit_su_10,self.ui.kit_su_11,self.ui.kit_su_12]
        self.kit_text = [self.ui.kit_text_1,self.ui.kit_text_2,self.ui.kit_text_3,self.ui.kit_text_4,self.ui.kit_text_5,self.ui.kit_text_6,self.ui.kit_text_7,self.ui.kit_text_8,self.ui.kit_text_9,self.ui.kit_text_10,self.ui.kit_text_11,self.ui.kit_text_12]
        self.kit_icon = [self.ui.kit_icon_1,self.ui.kit_icon_2,self.ui.kit_icon_3,self.ui.kit_icon_4,self.ui.kit_icon_5,self.ui.kit_icon_6,self.ui.kit_icon_7,self.ui.kit_icon_8,self.ui.kit_icon_9,self.ui.kit_icon_10,self.ui.kit_icon_11,self.ui.kit_icon_12]
      
        for i in range(12):
            self.kit_btn[i].clicked.connect(self.kit_btn_event)
            self.kit_onoff[i].clicked.connect(self.kit_onoff_event)
            self.kit_su[i].clicked.connect(self.kit_su_event)
            self.kit_clo[i].clicked.connect(self.kit_clo_event)
            
        
        self.ui.kit_left_btn.clicked.connect(self.kit_left_btn_event)
        self.ui.kit_right_btn.clicked.connect(self.kit_right_btn_event)



    
    def kit_left_btn_event(self):
        if self.nowadd > 0:
            self.kit_data_change(self.did,self.dicon,self.nowadd-3)

    def kit_right_btn_event(self):
        
        if self.nowadd + 11 + 3 <= len(self.sql_in)+2: 
            print('evnet')
            self.kit_data_change(self.did,self.dicon,self.nowadd + 3)



    def get_index(self,txt):
        return int(txt.split('_')[2]) - 1

    def kit_btn_event(self):
        print('btn')
        index = self.get_index(self.sender().objectName())
        if index == len(self.sql_in) - self.nowadd:
            with self.lock:
                self.curs.execute(("insert into data values(0,'%s','식별번호','이름',0,true);") % (self.did))
                self.conn.commit()
            self.kit_data_change(self.did,self.dicon)

        else:    
            self.chk_event(index)

    def chk_event(self,index):

        if(index > self.count - 1):
            return
        
        print(self.nowchk,index)

        self.kit_wi[self.nowchk].setStyleSheet(self.originalstyle)
        self.nowchk = index
        self.kit_wi[self.nowchk].setStyleSheet(self.chkstyle)
    
    def kit_onoff_event(self):
        print('onoff')
        index = self.get_index(self.sender().objectName())
        self.chk_event(index)

        with self.lock:
            self.curs.execute(("update data set onoff = '%d' where no = '%d' ") % (int(self.kit_onoff[index].isChecked()), self.sql_in[self.nowchk+self.nowadd] ))
            self.conn.commit()

        
    
    def kit_su_event(self):
        print('su')
        index = self.get_index(self.sender().objectName())
        self.chk_event(index)
        
        if(self.kit_su[index].isChecked()):
            self.kit_text[index].setEnabled(True)
            self.kit_label[index].setEnabled(True)
            self.kit_value[index].setEnabled(True) 
        else:
            self.kit_text[index].setEnabled(False)
            self.kit_label[index].setEnabled(False)
            self.kit_value[index].setEnabled(False)


            with self.lock:
                self.curs.execute(("update data set text = '%s', label = '%s', basicv = '%s' where no = '%s' ") % (self.kit_text[index].text(),self.kit_label[index].text(),self.kit_value[index].text(), self.sql_in[index+self.nowadd]))
                self.conn.commit()
            
        
        


    def kit_clo_event(self):
        print('clo')
        index = self.get_index(self.sender().objectName())
        self.chk_event(index)

        quit_msg = "정말 삭제하시겠습니까?"
        reply = QtWidgets.QMessageBox.question(self, '확인', 
                        quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        
        if reply == QtWidgets.QMessageBox.Yes:
            with self.lock:
                self.curs.execute(("delete from data where no = '%d' ") % (self.sql_in[index+self.nowadd]) )
                self.conn.commit()
            
            self.kit_data_change(self.did,self.dicon)

      
    
    def sensor_data_change(self):
        if self.did == 's' or self.did == 'p':
            return;
        with self.lock:
            self.curs.execute(("select d.*, ( select s.%s from sensor s where s.label = d.label order by s.no desc limit 1 ) from data d where d.id = '%s';") % (self.did,self.did))
            data2 = self.curs.fetchall()
        
        lt = len(data2)
        

        for i in range(min(12,lt-self.nowadd)):
            print('get_data = ',data2[i][6])
            if data2[i][6] is None:
                self.kit_value[i].setText(str(data2[i+self.nowadd][4]))
            else:
                self.kit_value[i].setText(str(data2[i+self.nowadd][6]))
            


    def kit_data_change(self,did,dicon,nowadd = 0):
        self.did = did
        self.dicon = dicon
        self.nowadd = nowadd

        print(("select d.*, ( select s.%s from sensor s where s.label = d.label order by s.no desc limit 1 ) from data d where d.id = '%s';") % (self.did,self.did))
        

        if did == 's' or did == 'p':
            sqls = ("select *,basicv from data where id = '%s';") % (did)
        else:
            sqls = ("select d.*, ( select s.%s from sensor s where s.label = d.label order by s.no desc limit 1 ) from data d where d.id = '%s';") % (self.did,self.did)

        with self.lock:
            self.curs.execute(sqls)
            data = self.curs.fetchall()

        print(did,'\n',data)
        i=0
        
        self.sql_in = [0 for i in range(len(data))]

        lt = len(data)
        
        print('lt=',lt)
        
        for i in range(len(data)):
            self.sql_in[i] = data[i][0]
        

        if(lt != 0):
            for i in range(min(12,lt-self.nowadd)):
                self.kit_btn[i].lower()
                self.kit_wi[i].setVisible(True)
                self.kit_btn[i].setStyleSheet('image : url(./);\nbackground-color : rgba(0,0,0,0);')
                self.kit_btn[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) 
                self.kit_label[i].setText(data[i+self.nowadd][2])
                self.kit_text[i].setText(data[i+self.nowadd][3])
                
                if data[i][6] is None:
                    self.kit_value[i].setText(str(data[i+self.nowadd][4]))
                else:
                    self.kit_value[i].setText(str(data[i+self.nowadd][6]))
                
                self.kit_onoff[i].setChecked(data[i+self.nowadd][5])
                self.kit_icon[i].setText(self.dicon)
                self.kit_wi[i].setStyleSheet(self.originalstyle)
        else:
            i = -1         

        self.nowchk = 0    

        for j in range(i+1,12):
            self.kit_btn[j].raise_()
            self.kit_btn[j].setStyleSheet('image : url(./); background-color : rgba(255,255,255,255); border : 0px;')
            self.kit_btn[j].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor)) 
        
        self.kit_wi[self.nowchk].setStyleSheet(self.chkstyle)
        
        if(not(i == 11)):
            self.kit_btn[i+1].setStyleSheet('QPushButton{image:url(./image/add_smbtn.png); border:0px; background-color : rgba(255,255,255);} QPushButton:hover{image:url(./image/add_smbtn2.png); border:0px; background-color : rgba(255,255,255);}')
            self.kit_btn[i+1].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) 
            

        self.count = len(data)

