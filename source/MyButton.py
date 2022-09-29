from  PyQt5.QtGui import *
from  PyQt5.QtCore import *
from  PyQt5.QtWidgets import *
import sys
from  PyQt5 import QtGui , QtCore

class MyButton(QLabel):

    click_signal = pyqtSignal()  # 定义信号
    def __init__(self,*args,parent = None):
        # parent 父类窗口 初始化
        super(MyButton, self).__init__(parent)
        self.hoverpixmap = QPixmap(args[0])   # QPixmap 加载图片 悬浮图片
        self.normalpixmap = QPixmap(args[1])  # 正常
        self.presspixmap = QPixmap(args[2])   # 按压

        # 鼠标状态 True: 按钮上方 False: 未接触按钮
        self.enterstate = False
        # 图片默认是正常状态
        self.setPixmap(self.normalpixmap)
        self.setFixedSize(self.normalpixmap.size())

    #鼠标释放按钮
    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent):
        print('鼠标释放')
        if self.enterstate:
            self.setPixmap(self.hoverpixmap)
        else:
            self.setPixmap(self.normalpixmap)
        self.click_signal.emit() #发射信号

    #鼠标按下
    def mousePressEvent(self, event):
        print('鼠标按下')
        self.setPixmap(self.presspixmap)

    #鼠标进入
    def enterEvent(self, a0: QtCore.QEvent):
        print('鼠标进入')
        self.setPixmap(self.hoverpixmap)
        self.enterstate = True

    #鼠标离开
    def leaveEvent(self, a0: QtCore.QEvent):
        print('鼠标离开')
        self.setPixmap(self.normalpixmap)
        self.enterstate = False

import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    mybtn = MyButton('source/人机对战_hover.png',
                     'source/人机对战_normal.png',
                     'source/人机对战_press.png', parent=window)
    mybtn.click_signal.connect(window.close)
    window.show()
    app.exit(app.exec_())


