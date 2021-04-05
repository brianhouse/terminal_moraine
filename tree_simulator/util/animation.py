#!/usr/bin/env python3

# https://github.com/brianhouse/housepy/blob/master/animation.py
# https://pyglet.readthedocs.io/en/latest/modules/shapes.html

import pyglet
import math
from random import random, randint


class Context():

    def __init__(self, width, height, title=""):
        self.width = width
        self.height = height
        config = pyglet.gl.Config(sample_buffers=1, samples=2, depth_size=0, double_buffer=True)
        style = pyglet.window.Window.WINDOW_STYLE_DEFAULT
        self.window = pyglet.window.Window(config=config, width=self.width, height=self.height, resizable=False, caption=title, style=style)
        self.objects = []
        self.labels = []
        pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)

    def start(self, draw_f):
        self.draw_f = draw_f
        self.window.on_draw = self.on_draw
        pyglet.clock.schedule(self.update)
        pyglet.app.run()

    def on_draw(self):
        self.window.clear()
        self.objects.clear()
        self.labels = []
        self.batch = pyglet.graphics.Batch()
        lines = self.draw_f()
        self.batch.draw()
        for label in self.labels:
            label.draw()
        fps = pyglet.clock.get_fps()

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

    def text(self, s, x, y, size=5, color=(0, 0, 0, 255)):
        y = self.height - y
        label = pyglet.text.Label(s, font_name='monospace', font_size=size, x=x, y=y, anchor_x='center', anchor_y='center', color=color)
        self.labels.append(label)

if __name__ == "__main__":
    ctx = Context(800, 600)
    def draw():
        lines = []
        for i in range(100):
            ctx.line(randint(0, ctx.width), randint(0, ctx.height), randint(0, ctx.width), randint(0, ctx.height), weight=randint(1, 10), color=(randint(0, 255), randint(0, 255), randint(0, 255)))
            ctx.circle(randint(0, ctx.width), randint(0, ctx.height), 10, (0, 0, 0))
    ctx.start(draw)
