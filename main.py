#!/usr/bin/env python3

import time, threading
import visualizer
from random import random, randint
from util import *

TICK_DURATION = 1/60 # hz
TICKS_PER_YEAR = 50
MAX_LEAVES = 128
GROWTH_RATE = .25

WIDTH, HEIGHT = 1000, 700
ORIGIN = 500, 700

BRANCH_MIN_SIZE = 10
BRANCH_PROB = .75

leaves = []


class Leaf():

    number = 0

    def __init__(self, limb):
        self.id = Leaf.number
        leaves.append(self)
        Leaf.number += 1
        self.limb = limb
        self.intensity = 0
        # play note on creation
        # midi_out.send_note(1, randint(1, 127), 127)  # channel, note, velocity

    @property
    def position(self):
        return self.limb.end

    def move(self, limb):
        self.limb = limb
        return self


class Limb():

    def __init__(self, parent=None, angle=-90, leaf=None):
        self.parent = parent
        self.children = []
        self.leaf = Leaf(self) if not leaf else leaf.move(self)
        self.size = 0
        self.angle = angle
        self.start = self.parent.end if self.parent else ORIGIN
        self.end = self.start

    def grow(self, day):
        if self.leaf:
            self.leaf.intensity = leaf_function(day, self.leaf.id)
        if len(leaves) < MAX_LEAVES:
            self.start = self.parent.end if self.parent else ORIGIN
            self.size += growth_function(day) * GROWTH_RATE
            self.end = get_point(self.start, self.angle, self.size)
            if  self.leaf and \
                self.size > BRANCH_MIN_SIZE and \
                random() > BRANCH_PROB:
                self.branch()
        for child in self.children:
            child.grow(day)

    ## TREE STRUCTURE IS DEFINED HERE ##
    def branch(self):
        if random() > 1/4:
            a = Limb(self, self.angle + randint(-30, -20), self.leaf)
            b = Limb(self, self.angle + randint(40, 50))
            self.children = [a, b]
        else:
            a = Limb(self, self.angle + randint(-50, -40), self.leaf)
            self.children = [a]
        self.leaf = None



class Tree(threading.Thread):

    def __init__(self):
        super(Tree, self).__init__()
        self.daemon = True
        self.root = Limb()
        self.start()

    ## MAIN TIMER ##
    def run(self):
        start_t = time.time()
        ticks = 0
        while True:
            self.update(int((ticks / TICKS_PER_YEAR) * 365))
            ticks = (ticks + 1) % TICKS_PER_YEAR
            time.sleep(TICK_DURATION)
            stop_t = time.time()
            elapsed = stop_t - start_t
            delta = abs(elapsed - TICK_DURATION)
            if delta > 1/60:
                print(f"whoops, perceptible latency: {int(delta * 1000)}ms")
            start_t = stop_t


    ## MAIN LOOP ##
    def update(self, day):

        self.root.grow(day)

        for leaf in leaves:
            x, y, v = *leaf.position, leaf.intensity
            x = int((x / WIDTH) * 127)
            y = int((y / HEIGHT) * 127)
            v = int(v)

            # channel, control number, control value
            #
            # proposal:
            # midi can only have 16 channels (true?)
            # so channel 1 sends x values, channel 2 sends y values, and channel 3 sends intensity values
            # each leaf is a control number (0-127)
            #
            # midi_out.send_control(1, leaf.id, x)
            # midi_out.send_control(2, leaf.id, y)
            # midi_out.send_control(3, leaf.id, v)

            # midi_out.send_control(127, 127, 127)


def growth_function(day):
    if day > 150 and day < 215:
        return 1
    elif day > 50 and day < 315:
        return 1/2
    else:
        return 0

def leaf_function(day, n):
    if n % 2:
        n = MAX_LEAVES - n
    if day < 50:
        return 0
    elif day > 315 + ((n / MAX_LEAVES) * 100):
        return 0
    else:
        return (day - 50) / 200



tree = Tree()
visualizer.start(tree.root)
