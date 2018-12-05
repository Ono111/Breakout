# coding:utf-8

class Ball:
    def __init__(self, x, y, pyxel, color=0):
        """円の中心(x, y)、pyxel、色は初期値0(黒)"""
        self.x = x
        self.y = y
        self.pyxel = pyxel
        self.color = color
        self.dx = 2
        self.dy = 2
        self.r = 5

    def move(self):
        # 円の位置を移動させる。
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        # 円を描画する。
        self.pyxel.circ(self.x, self.y, self.r, 0)

    def setSpeed(self, x, y):
        # x方向、y方向への1フレームごとの移動量を設定する。
        self.dx = x
        self.dy = y

    def setColor(self, color):
        # 円の色を設定する。
        self.color = color

    def changeSize(self, r):
        # 円の半径を設定する。
        self.r = r