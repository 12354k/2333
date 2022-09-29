'''
人机算法
'''
class GoBangAlgorithm(object):
    def __init__(self, chessboard):
        self.chessboard = chessboard
    # 计算坐标点的对应棋子颜色的分数
    def get_point_score(self, x, y, color):
        '''
        :param x: 
        :param y: 
        :param color: 
        :return:  得分
        '''

        # 计算周围5子以内，空白和同色的分数
        blank_score = 0
        color_score = 0

        # 记录每个方向的棋子分数
        # 水平 垂直 正斜线 反斜线
        blank_score_plus = [0, 0, 0, 0]
        color_score_plus = [0, 0, 0, 0]

        # 水平方向
        # 右侧
        i = x   # 横坐标
        j = y   # 纵坐标
        while i <= 18:
            if self.chessboard[j][i] == None:
                blank_score += 1
                blank_score_plus[0] += 1
            elif self.chessboard[j][i] == color:
                color_score += 1
                color_score_plus[0] += 1
            else:
                break
            if i >= x + 4:
                break
            i += 1

        # 左侧
        i = x  # 横坐标
        j = y  # 纵坐标
        while i >= 0:
            if self.chessboard[j][i] == None:
                blank_score += 1
                blank_score_plus[0] += 1
            elif self.chessboard[j][i] == color:
                color_score += 1
                color_score_plus[0] += 1
            else:
                break
            if i <= x - 4:
                break
            i -= 1

        # 垂直方向
        # 下面
        i = x  # 横坐标
        j = y  # 纵坐标
        while j <= 18:
            if self.chessboard[j][i] == None:
                blank_score += 1
                blank_score_plus[1] += 1
            elif self.chessboard[j][i] == color:
                color_score += 1
                color_score_plus[1] += 1
            else:
                break
            if j >= y + 4:
                break
            j += 1

        # 上面
        i = x  # 横坐标
        j = y  # 纵坐标
        while j >= 0:
            if self.chessboard[j][i] == None:
                blank_score += 1
                blank_score_plus[1] += 1
            elif self.chessboard[j][i] == color:
                color_score += 1
                color_score_plus[1] += 1
            else:
                break
            if j <= y - 4:
                break
            j -= 1

        # 正斜线
        # 右上
        i = x
        j = y
        while i < 19 and j >= 0:
            if self.chessboard[j][i] == None:
                blank_score += 1
                blank_score_plus[2] += 1
            elif self.chessboard[j][i] == color:
                color_score += 1
                color_score_plus[2] += 1
            else:
                break
            if i >= x + 4:
                break
            i += 1
            j -= 1
        # 左下
        i = x
        j = y
        while i >= 0 and j < 19:
            if self.chessboard[j][i] == None:
                blank_score += 1
                blank_score_plus[2] += 1
            elif self.chessboard[j][i] == color:
                color_score += 1
                color_score_plus[2] += 1
            else:
                break
            if j >= y + 4:
                break
            i -= 1
            j += 1

        # 反斜线
        # 左上
        i = x
        j = y
        while i >= 0 and j >= 0:
            if self.chessboard[j][i] == None:
                blank_score += 1
                blank_score_plus[3] += 1
            elif self.chessboard[j][i] == color:
                color_score += 1
                color_score_plus[3] += 1
            else:
                break
            if i <= x - 4:
                break
            i -= 1
            j -= 1

        # 右下
        i = x
        j = y
        while i < 19 and j < 19:
            if self.chessboard[j][i] == None:
                blank_score += 1
                blank_score_plus[3] += 1
            elif self.chessboard[j][i] == color:
                color_score += 1
                color_score_plus[3] += 1
            else:
                break
            if j >= y + 4:
                break
            i += 1
            j += 1

        for k in range(4):
            # 判断每个方向的同色棋子 >= 5
            if color_score_plus[k] >= 5:
                return 100
        # 获取指定位置 每条线上的总分 (同色 + 空白)
        return max([x+y for x, y in zip(color_score_plus, blank_score_plus)])

    # 获取位置坐标并返回
    def get_point(self):
        '''
        返回落子位置
        :return:

        [
            [0, 3, 4, 1, 5],
            [1, 2, 0, 5],
            []
        ]
        '''

        # 初始化二维列表
        # 存储黑棋,白棋每个坐标点的分数
        # 白棋每个坐标点的分数
        white_score = [[0 for i in range(19)] for j in range(19)]
        # 黑棋每个坐标点的分数
        black_score = [[0 for i in range(19)] for j in range(19)]
        # 测试落子 存储分数
        for i in range(19):
            for j in range(19):
                # 判断当前位置是否有棋子 无棋子 None 黑棋子 black 白棋子 white
                if self.chessboard[i][j] != None:
                    continue
                # 模拟落子 获得当前位置得分
                # 测试白棋落子
                self.chessboard[i][j] = 'white'
                white_score[i][j] = self.get_point_score(j, i, 'white')
                self.chessboard[i][j] = None
                # 测试黑棋落子
                self.chessboard[i][j] = 'black'
                white_score[i][j] = self.get_point_score(j, i, 'black')
                self.chessboard[i][j] = None

        # 将二维坐标转化为一维坐标
        r_white_score=[]
        r_black_score=[]
        # 列表的扩展
        for i in white_score:
            r_white_score.extend(i)
        for i in black_score:
            r_black_score.extend(i)
        print(r_white_score)
        print(r_black_score)
        # zip(r_white_score, r_black_score) +> [(0, 0),(2, 1).......]
        score = [max(x, y) for x, y in zip(r_white_score, r_black_score)]
        print(score)
        # 找出最大值下标
        chess_index = score.index(max(score))
        # 输出x坐标 y坐标  x取余 y取整
        x = chess_index % 19
        y = chess_index // 19
        return (x, y)


