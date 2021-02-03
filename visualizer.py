#!/usr/bin/env python3

# https://github.com/brianhouse/housepy/blob/master/animation.py
# https://pyglet.readthedocs.io/en/latest/modules/shapes.html

import pyglet
import math
from random import random, randint


class Context():

    def __init__(self, width, height, title="", framerate=None):
        self.width = width
        self.height = height
        self.framerate = framerate
        config = pyglet.gl.Config(sample_buffers=1, samples=2, depth_size=0, double_buffer=True)
        style = pyglet.window.Window.WINDOW_STYLE_DEFAULT
        self.window = pyglet.window.Window(config=config, width=self.width, height=self.height, resizable=False, caption=title, style=style)
        self.objects = []
        pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)

    def start(self, draw_f):
        self.draw_f = draw_f
        self.window.on_draw = self.on_draw
        if self.framerate is None:
            pyglet.clock.schedule(self.update)
        else:
            pyglet.clock.schedule_interval(self.update, 1/self.framerate)
        pyglet.app.run()

    def on_draw(self):
        self.window.clear()
        self.objects.clear()
        self.batch = pyglet.graphics.Batch()
        lines = self.draw_f()
        self.batch.draw()
        fps = pyglet.clock.get_fps()
        # if (self.framerate and fps < self.framerate - 1) or (not self.framerate and fps < 30):
        #     print(f"low fps ({int(fps)})")

    def update(self, dt):
        pass

    def line(self, x1, y1, x2, y2, weight, color=(0, 0, 0)):
        y1 = self.height - y1
        y2 = self.height - y2
        self.objects.append(pyglet.shapes.Line(x1, y1, x2, y2, width=weight, color=color, batch=self.batch))

    def circle(self, x, y, radius, color=(0, 0, 0), segments=None):
        y = self.height - y
        if segments is None:
            segments = int(math.pi * radius)   # 1/2 the number of points on the circumference, just a heuristic
            segments = max(segments, 1)
        self.objects.append(pyglet.shapes.Circle(x, y, radius, segments=segments, color=color, batch=self.batch))



class Turtle():

    def __init__(self, width, height, title="", framerate=None):
        self.ctx = Context(width, height, title, framerate)
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


def test_ctx():
    ctx = Context(800, 600)
    def draw():
        lines = []
        for i in range(100):
            ctx.line(randint(0, ctx.width), randint(0, ctx.height), randint(0, ctx.width), randint(0, ctx.height), weight=randint(1, 10), color=(randint(0, 255), randint(0, 255), randint(0, 255)))
            ctx.circle(randint(0, ctx.width), randint(0, ctx.height), 10, (0, 0, 0))
    ctx.start(draw)


def test_turtle():
    t = Turtle(800, 600)
    def draw():
        t.forward(100)
    t.start(draw)


# test_ctx()
# test_turtle()
