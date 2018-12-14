import pyxel
from ball import Ball
from bar import Bar

def draw():
    pyxel.cls(1)
    ball.draw()
    bar.draw()

def update():
    ball.move()
    hitwindow(ball.hitPosition())
    if bar.hit(ball.hitPosition()):
        ball.setSpeed(ball.dx, -ball.dy)

def hitWindow(li):
    for xy in li:
        if not (0 < xy[0] < pyxel.width-1):
            # ボールがウィンドウ左右に当たったとき
            ball.setSpeed(-ball.dx, ball.dy)
        if not (0 < xy[1]):
            # ボールがウィンドウ上部に当たったとき
            ball.setSpeed(ball.dx, -ball.dy)
        if xy[1] > pyxel.height-1:
            # ボールがウィンドウ下部に当たったとき
            ball.setSpeed(ball.dx, -ball.dy) 
        

pyxel.init(200, 200)
pyxel.cls(1)
ball = Ball(100, 110, pyxel)
bar = Bar(100, 180, 20, pyxel)
pyxel.run(update, draw)
