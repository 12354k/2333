from PyQt5.QtCore import QObject, pyqtSignal
from GameWight import GameWight
from gamecore import GameCore

from GoBangAlgorithm import GoBangAlgorithm
'''
人机对战 游戏逻辑控制
'''

class SinglePlayer(QObject):
    exit_clicked = pyqtSignal()

    def __init__(self):
        super(SinglePlayer, self).__init__()
        # 游戏界面
        self.game_widget = GameWight()

        # 游戏核心对象
        self.game_core = GameCore()

        # 默认先手颜色
        self.current_color = 'black'

        # 定义状态 判断是否可以落子
        self.is_active = False

        # 定义落子位置坐标
        self.history = []

        # 连接信号 槽函数
        self.game_widget.goback_clicked.connect(self.stop_game)
        self.game_widget.start_clicked.connect(self.start_game)
        self.game_widget.regret_clicked.connect(self.regret)
        self.game_widget.lose_clicked.connect(self.lose_game)
        self.game_widget.position_clicked.connect(self.down_chess)

    # 切换棋子颜色
    def get_reverse_color(self, color):
        if color == 'black':
            return 'white'
        else:
            return 'black'

    # 落子逻辑控制
    def down_chess(self, position):
        # 判断胜利状态 已有输赢 无法继续下棋
        if not self.is_active:
            return
        # 判断当前位置是否已经落子
        res = self.game_core.down_chessman(position[0], position[1], self.current_color)
        if res is None:
            return
        # 落子
        self.game_widget.downchess(position, self.current_color)

        # 记录落子位置
        self.history.append(position)

        # 切换颜色
        self.current_color=self.get_reverse_color(self.current_color)

        # 判断输赢状态
        if res != 'Down':
            self.game_widget.show_win(res)
            # 重置状态
            self.is_active = False

        # 电脑落子
        self.computer_down_chess()

    # 电脑落子方法
    def computer_down_chess(self):
        # 判断电脑能否落子
        if not self.is_active:
            return
        # 核心逻辑 落子操作 改变chessboard
        # 获取电脑落子交点坐标
        # 人机算法返回的最大分数的坐标位置
        position = GoBangAlgorithm(self.game_core.chessboard).get_point()
        res = self.game_core.down_chessman(position[0], position[1], self.current_color)

        if res is None:
            return
        # 落子操作
        self.game_widget.downchess(position, self.current_color)
        # 改变history
        self.history.append(position)
        # 改变颜色
        self.current_color = self.get_reverse_color(self.current_color)
        # 判断输赢
        if res != 'Down':
            self.game_widget.show_win(res)
            self.is_active = False

    # 悔棋
    def regret(self):
        if not self.is_active:
            return
        # 判断棋盘中有没有棋子
        if len(self.history) <= 0:
            return
        if not self.game_core.regert(*self.history.pop()):
            return
        self.game_widget.goback()

        if not self.game_core.regert(*self.history.pop()):
            return
        self.game_widget.goback()



    # 认输
    def lose_game(self):
        self.game_widget.show_win(self.get_reverse_color(self.current_color))
        # 重置状态
        self.is_active = False

    # 游戏初始化
    def init_game(self):
        self.current_color = 'black'
        self.game_widget.reset()
        self.game_core.init_game()
        self.history.clear()

    # 开始游戏
    def start_game(self):
        # 展示游戏界面
        self.game_widget.show()
        self.init_game()
        self.is_active = True

    # 退出游戏
    def stop_game(self):
        # 发射退出信号
        print('退出')
        self.exit_clicked.emit()
        self.game_widget.close()

