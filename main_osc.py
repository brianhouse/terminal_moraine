#!/usr/bin/env python3

import visualizer
from tree import Tree
from util.osc import osc_out

osc_out.log_osc = True
# receive OSC on port 23232
# format:
# osc_out.send(address, message)


config = {
    'TICK_DURATION': 1/60,
    'TICKS_PER_YEAR': 50,
    'GROWTH_RATE': .25,

    'MAX_LEAVES': 128,
    'MAX_LIMBS': 8,
    'MAX_ROOT_SIZE': 100,

    'WIDTH': 1000,
    'HEIGHT': 700,

    'ORIGIN': (500, 700),

    'BRANCH_MIN_SIZE': 10,
    'BRANCH_PROB': .75,
    }


def sonify(tree):
    for limb in tree.limbs:
        # print("limb", limb.id, limb.size, limb.water)
        osc_out.send("limb/", [limb.id, limb.size, limb.water])


visualizer.start(Tree(config, sonify))
