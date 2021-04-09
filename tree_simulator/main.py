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
    'DAY': 1/10,                # length of day in seconds

    # limits
    'MAX_LEAVES': 36,           # hitting limits affects load, hence rate; better for it to hit the leaf limit
    'MAX_LIMBS': 64,            # with double branching, limbs will be twice the leaves, minus 1
    'MAX_ROOT_LENGTH': 100,
    'MAX_DEPTH': 5,

    # dynamics
    'LIMB_BRANCH_LENGTH': 10,       # length before branching, in "pixels"
    'LIMB_GROWTH_AMOUNT': 1/8,      # growth per tick, in "pixels"
    'LIMB_GROWTH_VARIANCE': .1,     # additional difference in growth rate among branches
    }


gains = [0] * 127
rates = [0] * 127
phases = [0] * 127

# harmonies = [0, 1/8, 1/4, 1/3, 1/2, 2/3, 7/8]
# harmonies = [1 + 1/4, 1 + 1/3, 1 + 1/2, 1 + 2/3] # + leaves
# harmonies = [1/4, 1/3, 1/2, 2+2/3, 8] # + leaves
harmonies = [1/4, 1/2, 2/3, 1, 8]
gain_adj = [1, .7, .5, 1/4, 1/16]
delay_adj = .15
n_limbs = 0


def update_params(tree, day):
    if day == 5:
        print("")
        print("activating")
        print("depth", tree.depth)
        print("limbs", len(tree.limbs), "leaves", len(tree.leaves))
        global n_limbs
        n_limbs = len(tree.limbs)
        for limb in tree.limbs:

            d = tree.depth - limb.depth
            rate = harmonies[-d]
            rates[limb.id] = rate

            l = limb
            # length = limb.length
            length = 0  # discounting own length
            while l.parent is not None:
                l = l.parent
                length += l.length
            delay = length/20 + (delay_adj / rate) # + (4 * random()) #(limb.id / 10)

            def s(id, d):
                def f():
                    gains[id] = gain_adj[-d]
                return f
            sonifier.add(s(limb.id, d), delay)

            print(f"{limb.id+1} depth {limb.depth} length {length:.2f} delay {delay:.2f} phase {phases[limb.id]:.2f} rate {rates[limb.id]:.3f} gain {gain_adj[limb.depth]:.3f}")

    elif day == 250:
        print("winter")
        for limb in tree.limbs:
            def s(id):
                def f():
                    gains[id] = 0
                return f
            sonifier.add(s(limb.id), random() * 4)


def sonify(tree, day):
    global n_limbs
    update_params(tree, day)

    # move tree
    for l, limb in enumerate(tree.limbs):


        # hack for emerging leaves
        if day > 5 and day < 250:
            if l >= n_limbs:
                # print("BONUS LIMB")
                rates[limb.id] = harmonies[-1]
                gains[limb.id] = gain_adj[-1]
                n_limbs += 1

        rate = rates[limb.id]
        # if rate != 8:
        #     continue


        siblings = [id for (id, r) in enumerate(rates) if r == rate]
        index = siblings.index(limb.id)
        phase = index * (1 / len(siblings)) * .5
        phase = 1 - phase if index % 2 else phase
        print(siblings, index, phase)


        rate *= 2

        gain = gains[limb.id]

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
def reset_synth():
    for l in range(128):
        osc_out.send("limb/", [l+1, 0, 0, 0, 0, 0, 0])
reset_synth()

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
    reset_synth()
    time.sleep(.25)
