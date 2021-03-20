#!/usr/bin/env python3

import visualizer
from tree import Tree
from util.osc import osc_out
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
    'WIDTH': 1000,
    'HEIGHT': 700,
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
            # print("limb", limb.id, limb.water, limb.percent)
            load = max(limb.load, 1)    # prevent rate swoops from 0
            rate = 20 / load # current vs max possible load
            # rate *= 1.5                 # master pitch adjust
            phase = limb.id * (1 / config['MAX_LIMBS']) # distribute the phasing
            gain = limb.load / config['MAX_LIMBS']      # keep total gain below unity
            # pos_x = (limb.end[0] - config['ORIGIN'][0]) / (config['WIDTH'] / 2)
            # pos_y = (limb.end[1] - config['ORIGIN'][1]) / (config['HEIGHT'] / 2)
            pan = ((limb.id / (config['MAX_LIMBS'] - 1)) * 2) - 1

            x, y, z = limb.end
            # print(l, "\t", int(x), int(y), int(z))
            # osc_out.send("limb/", [l, rate, phase, gain, pos_x, pos_y])
        else:
            # zero out all uncreated limbs to avoid having to hit reset
            # osc_out.send("limb/", [l, 0, 0, 0, 0, 0])
            pass

visualizer.start(Tree(config, sonify))
