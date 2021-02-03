import math
from util.animation import Context

class Turtle():

    def __init__(self, width, height, title=""):
        self.ctx = Context(width, height, title)
        self.width = 1
        self.color = 0, 0, 0
        self.start = self.ctx.start
        self.reset()

    def reset(self):
        self.x, self.y = self.ctx.width / 2, self.ctx.height / 2
        self.a = -90

    def jump(self, x, y):
        self.x, self.y = x, y

    def forward(self, d):
        x, y = self.x + (d * math.cos(math.radians(self.a))), self.y + (d * math.sin(math.radians(self.a)))
        self.ctx.line(self.x, self.y, x, y, self.width, self.color)
        self.x, self.y = x, y

    def circle(self, r):
        self.ctx.circle(self.x, self.y, r, self.color)

    def face(self, a):
        self.a = a

    def right(self, a):
        self.a += a
        self.a %= 360

    def left(self, a):
        self.a -= a
        self.a %= 360
