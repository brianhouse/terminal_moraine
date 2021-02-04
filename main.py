#!/usr/bin/env python3

import time, threading
import visualizer
from random import random, randint
from util.midi import midi_out

TICK_DURATION = 1/16 # 1/32 note at 120bpm
MAX_LEAVES = 128

midi_out.log_midi = True


class Leaf():

    number = 0

    def __init__(self, limb):
        self.channel = Leaf.number + 1
        self.limb = limb
        Leaf.number += 1

        midi_out.send_note(1, randint(1, 127), 127)  # channel, note, velocity



class Limb():

    def __init__(self, parent=None, angle=0, leaf=None):
        self.parent = parent
        self.children = []
        self.age = 0
        self.angle = angle
        self.leaf = leaf or Leaf(self)

    @property
    def has_leaf(self):
        return self.leaf != None

    def grow(self):
        if Leaf.number < MAX_LEAVES:
            self.age += 1
            for child in self.children:
                child.grow()
            if self.has_leaf:
                self.branch()

    def branch(self):
        if Leaf.number < MAX_LEAVES and self.age >= 10 and random() > .75:
            if random() > 1/4:
                self.children.append(Limb(self, randint(-30, -20), self.leaf))
                self.children.append(Limb(self, randint(40, 50)))
            else:
                self.children.append(Limb(self, randint(-50, -40), self.leaf))
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
        while True:
            self.root.grow()
            time.sleep(TICK_DURATION)
            stop_t = time.time()
            elapsed = stop_t - start_t
            delta = abs(elapsed - TICK_DURATION)
            if delta > 1/60:
                print(f"bad timing: {int(delta * 1000)}ms")
            start_t = stop_t



tree = Tree()
visualizer.start(tree.root)
