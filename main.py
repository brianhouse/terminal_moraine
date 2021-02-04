#!/usr/bin/env python3

import time, threading
import visualizer
from random import random, randint
from util.midi import midi_out

TICK_DURATION = 1/16 # 1/32 note at 120bpm
MAX_BRANCH_AGE = 125

midi_out.log_midi = True

class Branch():

    def __init__(self, parent=None, angle=0):
        self.parent = parent
        self.children = []
        self.age = 0
        self.angle = angle

    @property
    def has_leaf(self):
        return len(self.children) == 0

    def grow(self):
        if self.age < MAX_BRANCH_AGE:
            self.age += 1
            for child in self.children:
                child.grow()
            if self.has_leaf:
                self.split()

    ## BRANCH STRUCTURE ##
    def split(self):

        if self.age >= 10 and random() > .75:

            midi_out.send_note(1, randint(1, 127), 127)  # channel, note, velocity

            if random() > 1/4:
                self.children.append(Branch(self, randint(-30, -20)))
                self.children.append(Branch(self, randint(40, 50)))
            else:
                self.children.append(Branch(self, randint(-50, -40)))


class Tree(threading.Thread):

    def __init__(self):
        super(Tree, self).__init__()
        self.daemon = True
        self.root = Branch()
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
