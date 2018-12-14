# coding:utf-8

HEIGHT = 2

class Bar:
    def __init__(self, x, y, length, pyxel, color=2):
        self.x, self.y = x, y
        self.length = length
        self.color = color
        self.pyxel = pyxel

    def draw(self):
        self.x = self.pyxel.mouse_x
        x1, x2 = self.x - self.length/2, self.x + self.length/2
        y1, y2 = self.y - HEIGHT/2, self.y + HEIGHT/2
        if x1 <= 0:
            x1 = 0
            x2 = self.length
        elif x2 >= self.pyxel.width-1:
            x2 = self.pyxel.width-1
            x1 = x2 - self.length
        self.pyxel.rect(x1, y1, x2, y2, self.color)

    def hit(self, li):
        for xy in li:
            x1, x2 = self.x -self.length/2, self.x + self.length/2
            if xy[1] > self.y:
                if x1 < xy[0] < x2:
                    return True
        return False
