from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

#创建窗口
class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setWindowTitle('爷的窗口') #标题
       # labal = QLabel('使用爷的QT窗口')    #标签
       # # 标签显示窗口中央
       # labal.setAlignment(Qt.AlignCenter)
       # self.setCentralWidget(labal)
        #设置大小
        self.resize(600,500)

        #创建布局
        layout = QVBoxLayout()
        #创建按钮
        for i in range(5):
            button = QPushButton(str(i))
            #绑定槽函数
            button.pressed.connect(lambda x=i: self.myButton(x))
            #将按钮添加到布局里面
            layout.addWidget(button)
        #创建部件
        weight = QWidget()
        #将布局添加到部件里面
        weight.setLayout(layout)
        #将部件添加到窗口
        self.setCentralWidget(weight)

    #槽函数
    def myButton(self, n):
            print(f'这是第{n}个按钮')

#创建应用实例 通过SYS.argv 传入命令行参数
app = QApplication(sys.argv)
#创建窗口
window = mainWindow()
#显示窗口
window.show()
#执行应用 进入事件循环
app.exec_()
