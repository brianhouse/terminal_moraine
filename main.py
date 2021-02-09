#!/usr/bin/env python3

import visualizer
from tree import Tree
from util.midi import midi_out

midi_out.log_midi = False
# format:
# midi_out.send_control(channel, control, value)
# midi_out.send_note(channel, pitch, velocity)


config = {
    # time
    'TICK_DURATION': 1/60,
    'TICKS_PER_YEAR': 50,
    'GROWTH_RATE': .25,     # not sure what the units are here

    # size
    'MAX_LEAVES': 128,
    'MAX_LIMBS': 128,
    'MAX_ROOT_LENGTH': 100,

    # canvas
    'WIDTH': 1000,
    'HEIGHT': 700,
    'ORIGIN': (500, 700),

    # dynamics
    'BRANCH_MIN_LENGTH': 10,    # min length before branching
    'BRANCH_PROB': .75,
    }


## sonify is called every tick

# this one sends control values for the x, y of each leaf
# the "channel" is 1 for x, 2 for y, the "control" is the leaf.id
# also a control for leaf intensity
# prints out branch structure below the leaf, not sure how to send it
def sonify(tree):
    for leaf in tree.leaves:

        x, y = leaf.position
        x = int((x / config['WIDTH']) * 127)
        y = int((y / config['HEIGHT']) * 127)
        intensity = int((leaf.intensity / 5) * 127)
        midi_out.send_control(1, leaf.id, x)
        midi_out.send_control(2, leaf.id, y)
        midi_out.send_control(3, leaf.id, intensity)

        structure = []
        limb = leaf.limb
        while limb:
            structure.append(limb.id)
            limb = limb.parent
        structure.reverse()

        print("leaf", leaf.id, structure, leaf.intensity)

    # show "water" distributed through limbs
    # for limb in tree.limbs:
    #     print("limb", limb.id, limb.length, limb.water, limb.percentage)



visualizer.start(Tree(config, sonify))
