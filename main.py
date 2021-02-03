#!/usr/bin/env python3

import random, time
from visualizer import Turtle


class Branch():

    def __init__(self, parent=None, angle=0):
        self.parent = parent
        self.children = []
        self.age = 0
        self.angle = angle

    @property
    def has_leaf(self):
        return len(self.children) == 0


    ## the character of the tree is defined by this method ##
    def split(self):
        if self.age >= 10 and random.random() > .75:
            if random.random() > 1/4:
                self.children.append(Branch(self, random.randint(-30, -20)))
                self.children.append(Branch(self, random.randint(40, 50)))
            else:
                self.children.append(Branch(self, random.randint(-50, -40)))



def grow(branch):
    if branch.age < 125:
        branch.age += 1
        for child in branch.children:
            grow(child)
        if branch.has_leaf:
            branch.split()


def draw(branch, angle=0):
    t.right(branch.angle)
    t.width = branch.age / 4
    t.color = 50, 0, 0
    t.forward(branch.age)
    t.circle(t.width / 2)
    if branch.has_leaf:
        t.color = 0, 150, 20
        t.circle(5)
    else:
        x, y = t.x, t.y
        angle = t.a
        for c, child in enumerate(branch.children):
            draw(child)
            t.jump(x, y)
            t.face(angle)


t = Turtle(1000, 700, "GROWTH")
root = Branch()
def run():
    t.reset()
    t.jump(500, 700)
    draw(root)
    grow(root)
t.start(run)
