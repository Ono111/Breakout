# coding:utf-8
import math

class Ball:
    def __init__(self, x, y, pyxel, color=0):
        """円の中心(x, y)、pyxel、色は初期値0(黒)"""
        self.x = x
        self.y = y
        self.pyxel = pyxel
        self.color = color
        self.dx = 2
        self.dy = 2
        self.r = 3

    def move(self):
        # 円の位置を移動させる。
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        # 円を描画する。
        self.pyxel.circ(self.x, self.y, self.r, self.color)

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

    def hitPosition(self):
        # 当たり判定に用いるリストの作成。
        li = []
        for a in range(8):
            a = a / 4
            x = self.x + self.r * math.cos(a * math.pi)
            y = self.y + self.r * math.sin(a * math.pi)
            li.append([x, y])
        return li