import pyxel
from ball import Ball

def draw():
    pyxel.cls(1)
    ball.draw()

def update():
    ball.move()
    hit(ball.hitPosition())

def hit(li):
    for xy in li:
        if not (0 < xy[0] < pyxel.width-1):
            ball.setSpeed(-ball.dx, ball.dy)
        if not (0 < xy[1] < pyxel.height-1):
            ball.setSpeed(ball.dx, -ball.dy)
        

pyxel.init(200, 200)
pyxel.cls(1)
ball = Ball(100, 110, pyxel)
pyxel.run(update, draw)
