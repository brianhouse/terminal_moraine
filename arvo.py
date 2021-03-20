#!/usr/bin/env python3

import visualizer
from tree import Tree
from util.osc import osc_out
from util import rescale, clip
from random import random

# osc is on port 5005
osc_out.log_osc = False


config = {
    # time
    'TICK_DURATION': 1/60,
    'TICKS_PER_YEAR': 50,
    'GROWTH_RATE': 1/4,     # not sure what the units are here

    # size
    'MAX_LEAVES': 127,
    'MAX_LIMBS': 127,
    'MAX_ROOT_LENGTH': 100,

    # canvas
    'WIDTH': 600,
    'HEIGHT': 600,
    'DEPTH': 600,
    'ORIGIN': (300, 300, 300),

    # dynamics
    'BRANCH_MIN_LENGTH': 10,    # min length before branching
    'BRANCH_PROB': .75,
    'BUD_SPEED': 1/10,
    }




def sonify(tree):
    for l in range(config['MAX_LIMBS']):
        if l < len(tree.limbs):
            limb = tree.limbs[l]
            load = max(limb.load, 1)    # prevent rate swoops from 0
            rate = 20 / load # current vs max possible load
            # rate *= 1.5                 # master pitch adjust
            phase = limb.id * (1 / config['MAX_LIMBS']) # distribute the phasing
            gain = limb.load / config['MAX_LIMBS']      # keep total gain below unity

            # y is up internally; swapping with z here
            pos_x = clip(rescale(limb.end[0], 50, 550, -1, 1), -1, 1)
            pos_y = clip(rescale(limb.end[2], 50, 550, 1, -1), -1, 1)
            pos_z = clip(rescale(limb.end[1], 50, 550, 1, -1), -1, 1)

            osc_out.send("limb/", [l, rate, phase, gain, pos_x, pos_y, pos_z])
        else:
            # zero out all uncreated limbs to avoid having to hit reset
            osc_out.send("limb/", [l, 0, 0, 0, 0, 0])

visualizer.start(Tree(config, sonify))
