import sys

from MenuWidget import MenuWidget
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from DoublePlayer import DoublePlayer
from SinglePlayer import SinglePlayer
'''
主控程序
'''
class Main(QObject):
    def __init__(self):
        super(Main, self).__init__()
        # 初始化菜单界面
        self.menu_widget = MenuWidget()
        # 指定双人对战
        self.double_player = DoublePlayer()
        self.menu_widget.double_clicked.connect(self.start_double_player)
        # 游戏退出 展示菜单界面
        self.double_player.exit_clicked.connect(self.menu_widget.show)

        # 人机 初始化
        self.singleplayer = SinglePlayer()
        self.menu_widget.single_clicked.connect(self.start_singleplayer)
        self.singleplayer.exit_clicked.connect(self.menu_widget.show)


    # 游戏启动方法
    def start_programe(self):
        self.menu_widget.show()

    # 双人
    def start_double_player(self):
        # 启动游戏界面
        self.double_player.start_game()
        # 隐藏菜单
        self.menu_widget.hide()
    # 人机
    def start_singleplayer(self):
        self.singleplayer.start_game()
        self.menu_widget.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.start_programe()
    sys.exit(app.exec_())
