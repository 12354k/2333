from PyQt5.QtCore import QObject
'''
游戏核心

'''
class GameCore(QObject):
    def __init__(self):
        super(GameCore, self).__init__()
        '''
        记录棋盘信息
        使用列表生成式创建二维表
        '''
        self.chessboard = [[None for i in range(19)] for j in range(19)]
    # 初始化棋盘信息
    def init_game(self):
        for i in range(19):
            for j in range(19):
                self.chessboard[i][j] = None
    # 是否可以悔棋(消除棋子记录)
    def regert(self, x, y):
        # 判断是否有棋子
        if self.chessboard[x][y] == None:
            return False
        else:
            self.chessboard[x][y] = None
            return True
    #判断输赢 判断八个方向的棋子
    def judge_win(self, x, y, color):
        '''
        :param x: 水平坐标
        :param y: 垂直坐标
        :param color: 棋子颜色
        :return:
        '''

        # 水平方向判断 y不变 x发生变化
        # 左边
        count = 1
        i = x - 1
        while i >= 0:
            if self.chessboard[y][i] == None or self.chessboard[y][i] != color:
                break
            count += 1
            i -= 1
        # 右边
        i = x + 1
        while i <= 18:
            if self.chessboard[y][i] == None or self.chessboard[y][i] != color:
                break
            count += 1
            i += 1

        if count > 4:
            return color

        # 上边
        count = 1
        j = y - 1
        while j >= 0:
            if self.chessboard[j][x] == None or self.chessboard[j][x] != color:
                break
            count += 1
            j -= 1

        # 下边
        j = y + 1
        while j <= 18:
            if self.chessboard[j][x] == None or self.chessboard[j][x] != color:
                break
            count += 1
            j += 1

        if count > 4:
            return color

        # 右上 x增加 y减少
        count = 1
        i = x + 1
        j = y - 1
        while i <= 18 and j >= 0:

            if self.chessboard[j][i] == None or self.chessboard[j][i] != color:
                break
            count += 1
            i += 1
            j -= 1

        # 左下
        i = x - 1
        j = y + 1
        while i >= 0 and j <= 18:
            if self.chessboard[j][i] == None or self.chessboard[j][i] != color:
                break
            count += 1
            i -= 1
            j += 1

        if count > 4:
            return color

        # 左上
        count = 1
        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0:
            if self.chessboard[j][i] == None or self.chessboard[j][i] != color:
                break
            count += 1
            j -= 1
            i -= 1

        # 右下 x增加 y增加
        i = x + 1
        j = y + 1
        while i <= 18 and j <= 18:
            if self.chessboard[j][i] == None or self.chessboard[j][i] != color:
                break
            count += 1
            j += 1
            i += 1

        if count > 4:
            return color

        return 'Down'

    # 落子
    def down_chessman(self, x, y, color):
        if self.chessboard[y][x] is not None:
            return None
        self.chessboard[y][x] = color
        return self.judge_win(x, y, color)


if __name__ == '__main__':
    gc = GameCore()
    print(gc.down_chessman(0, 0, 'white'))
    print(gc.down_chessman(0, 1, 'white'))
    print(gc.down_chessman(0, 2, 'white'))
    print(gc.down_chessman(0, 3, 'white'))
    print(gc.down_chessman(0, 4, 'white'))