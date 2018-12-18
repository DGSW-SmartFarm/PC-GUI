

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QRect, QUrl,  QTimer
from PyQt5.QtGui import QDesktopServices, QColor
from pyqtgraph import mkPen,AxisItem,TextItem
import Ui_untitled
import datetime, time
import pyqtgraph
from collections import deque
import sys
import random


def graph_init(graph,  bg_color = QColor(255,255,255), y_grid=True, x_grid=False, mouse_enable = False):
    graph.setBackground(bg_color)
    graph.showGrid(x = x_grid, y= y_grid) #눈금선 주기 
    if mouse_enable is False:
        graph.setMouseEnabled(x=False,y=False) # 스크롤 및 드래그 가능여부
    
    

def graph_update(graph, x, y, pen_color = QColor(91,155,213),pen_width=2, symbol_color = QColor(91,155,213), symbol = 'o', symbolSize = 10, strf = "%H:%M"):
    graph.plot(
            #값 설정
            x,
            y,
            #펜 설정
            pen=mkPen(pen_color, width=2), #pen QColor 
           #symbol 설정
            symbol=symbol, # o, s, t, d, +, x 등등 하나 (동그라미, 팔각형,육각형 ,마름모,십자가)
            symbolBrush=symbol_color,  #symbol
            symbolSize = symbolSize,
           #기타
            antialias= True, #안티앨리어싱
            clear = True
            )
    time_axis = [ (ts,datetime.datetime.fromtimestamp(ts).strftime(strf)) for ts in x]
    graph.getAxis('bottom').setTicks([time_axis,[]])


def timer_ovf():
    x.append(time.time())
    y.append(random.randrange(0,100))
    graph_update(ui.graphicsView,x,y,strf="%H:%M")


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
MainWindow.show()


ui = Ui_untitled.Ui_MainWindow()
ui.setupUi(MainWindow)

graph_init(ui.graphicsView)

x = deque(maxlen=9)
y = deque(maxlen=9)

timer = QTimer()
timer.timeout.connect(timer_ovf)
timer.start(1000)








app.exec_()
