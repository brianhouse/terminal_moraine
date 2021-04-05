#!/usr/bin/env python3

import time
import visualizer, sonifier
from tree import Tree
from util.osc import osc_out
from util import rescale, clip
from random import random

# osc is on port 5005
osc_out.log_osc = False


config = {
    # time
    'DAY': 1/30,                # length of day in seconds

    # limits
    'MAX_LEAVES': 32,           # hitting limits affects load, hence rate; better for it to hit the leaf limit
    'MAX_LIMBS': 64,            # with double branching, limbs will be twice the leaves, minus 1
    'MAX_ROOT_LENGTH': 100,

    # dynamics
    'LIMB_BRANCH_LENGTH': 10,       # length before branching, in "pixels"
    'LIMB_GROWTH_AMOUNT': 2, #1/4,         # growth per tick, in "pixels"
    'LIMB_GROWTH_VARIANCE': .1,     # additional difference in growth rate among branches
    }


gains = [0] * config['MAX_LIMBS']
rates = [0] * config['MAX_LIMBS']
phases = [0] * config['MAX_LIMBS']


def update_gains(tree, day):
    if day == 5:
        print("")
        print("activating")
        print("limbs", len(tree.limbs), "leaves", len(tree.leaves))

        for limb in tree.limbs:
            l = limb
            length = limb.length
            while l.parent is not None:
                l = l.parent
                length += l.length
            delay = length/100
            print(f"{limb.id+1} delay {delay:.2f} phase {phases[limb.id]:.2f} rate {rates[limb.id] * 4} depth {limb.depth}")
            def s(id):
                def f():
                    gains[id] = 1
                return f
            sonifier.add(s(limb.id), delay)

    elif day == 250:
        print("winter")
        for limb in tree.limbs:
            def s(id):
                def f():
                    gains[id] = 0
                return f
            sonifier.add(s(limb.id), 0)


def update_rates(tree, day):
    if day == 1:
        for limb in tree.limbs:
            load = max(limb.load, 1)    # prevent rate swoops from 0
            rate = config['MAX_LEAVES'] / load # current vs max possible load
            rate *= .25  # global rate adjustment vs original playback speed of sample
            rates[limb.id] = rate
        print("updated rates")


def sonify(tree, day):
    update_gains(tree, day)
    update_rates(tree, day)

    # move tree
    for limb in tree.limbs:

        gain = 1/16 * gains[limb.id]
        rate = rates[limb.id]

        # distribute and interleave the phasing
        phase = limb.id * (1 / config['MAX_LIMBS']) * .5
        if limb.id % 2:
            phase = 0.5 - phase
        phases[limb.id] = phase

        # y is up internally; swapping with z here
        pos_x = clip(rescale(limb.end[0], -250, 250, -1, 1), -1, 1)
        pos_y = clip(rescale(limb.end[2], -250, 250, 1, -1), -1, 1)
        pos_z = clip(rescale(limb.end[1], -250, 250, 1, -1), -1, 1)
        pos_z = 0   # dropping

        # shift ids to 1-index
        osc_out.send("limb/", [limb.id+1, rate, phase, gain, pos_x, pos_y, pos_z])


# reset synthesizer
def reset():
    for l in range(128):
        osc_out.send("limb/", [l+1, 0, 0, 0, 0, 0, 0])
reset()

# set up sonification callbacks
sonifier = sonifier.Sonifier()
sonifier.start()
def callback(tree, day):
    def f():
        sonify(tree, day)
    sonifier.add(f, 0)

# go
tree = Tree(config, callback)
try:
    visualizer.start(tree)
except KeyboardInterrupt:
    tree.stop()
    reset()
    time.sleep(.25)
