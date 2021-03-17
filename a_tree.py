#!/usr/bin/env python3

import visualizer
from tree import Tree
# from util.osc import osc_out
from util.osc import OSCOut
from random import random
from braid import *


osc_out = OSCOut(5005)

oscST = OSCOut(4002)

osc_out.log_osc = True
oscST.log_osc = True
# receive OSC on port 23232
# format:
# osc_out.send(address, message)

config = {
    # time
    'TICK_DURATION': 1/60,
    'TICKS_PER_YEAR': 50,
    'GROWTH_RATE': 1/16,     # not sure what the units are here

    # size
    'MAX_LEAVES': 128,
    'MAX_LIMBS': 16,
    'MAX_ROOT_LENGTH': 100,

    # canvas
    'WIDTH': 1000,
    'HEIGHT': 700,
    'ORIGIN': (500, 700),

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
            rate = load / min(config['MAX_LIMBS'], config['MAX_LEAVES']) # current vs max possible load
            rate *= 1.5                 # master pitch adjust
            # phase = limb.id * (1 / config['MAX_LIMBS']) # distribute the phasing
            phase = limb.id * (1 / len(tree.limbs))
            gain = limb.load / config['MAX_LIMBS']      # keep total gain below unity
            # pos_x = (limb.end[0] - config['ORIGIN'][0]) / (config['WIDTH'] / 2)
            # pos_y = (limb.end[1] - config['ORIGIN'][1]) / (config['HEIGHT'] / 2)
            # pan = ((limb.id / (config['MAX_LIMBS'] - 1)) * 2) - 1
            pos_x = (500 - limb.end[0]) / 100.0
            pos_y = (700 - limb.end[1]) / 100.0
            # print(f'{limb.end=}')
            pos_z = (2 - 2 * (limb.id * (1 / len(tree.limbs)))) # -100 to 100

            # id, rate, phase, gain, pos_x, pos_y, pos_z
            # osc_out.send("limb/", [l, rate, phase, gain, pos_x, pos_y, pos_z])
            # osc_out.send("limb/", [7, rate, phase, gain, pos_x, pos_y, pos_z])
            # port 4002
            q = random()
            ST_coords = f"aed {q*40.0} 50. 90.0"
            oscST.send("/7/coord/", ST_coords)
            # print(ST_coords)
        else:
            pass
            # zero out all uncreated limbs to avoid having to hit reset
            # osc_out.send("limb/", [l, 0, 0, 0, 0, 0, 0])





visualizer.start(Tree(config, sonify))
