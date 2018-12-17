class Balgi:
    test = 10

    def __init__(self,ui):
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
            self.bal_clo[i].clicked.connect(self.bal_bal_event)
            
    def bal_btn_event(self):
        print('event',self.test)

    def bal_onoff_event():
        print('onoff')
    
    def bal_su_event():
        print('su')
    
    def bal_clo_event():
        print('clo')