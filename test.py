import pyxel
from ball import Ball

def draw():
    pyxel.cls(1)
    b.draw()

def update():
    b.move()

pyxel.init(200, 200)
pyxel.cls(1)
b = Ball(10, 10, pyxel)
pyxel.run(update, draw)
