#!/usr/bin/env python3

import visualizer
from tree import Tree

config = {
    'TICK_DURATION': 1/60,
    'TICKS_PER_YEAR': 50,
    'MAX_LEAVES': 128,
    'GROWTH_RATE': .25,

    'WIDTH': 1000,
    'HEIGHT': 700,

    'ORIGIN': (500, 700),

    'BRANCH_MIN_SIZE': 10,
    'BRANCH_PROB': .75,
    }

tree = Tree(config)


def traverse(limb):
    for child in limb.children:
        traverse(child)
    if limb.leaf:
        pass

def start(root):
    def loop():
        traverse(tree.root)




visualizer.start(tree.root)
