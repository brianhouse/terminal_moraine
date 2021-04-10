#!/usr/bin/env python3

import time, sys
import visualizer, sonifier
from tree import Tree
from util.osc import OSCIn

TEST_MODE = len(sys.argv) > 1

config = {
    # time
    'YEAR_TIME': 30,                # length of year in seconds
    'AGE': 10,                      # stop after this age tree

    # dynamics
    'GROWTH_PER_YEAR': 15,          # growth per year, in "pixels"
    'LIMB_BRANCH_LENGTH': 10,       # length before branching, in "pixels"

    # limits
    'MAX_LIMBS': 64,                # with double branching, limbs will be twice the leaves, minus 1
    'MAX_ROOT_LENGTH': 100,
    'MAX_DEPTH': 5,

    }


start = False
stop = False
tree = None

def receive(address, *args):
    global start, stop
    if address.strip("/") == "start":
        start = True
        config['YEAR_TIME'] = float(args[0]) or config['YEAR_TIME']
        config['AGE'] = int(args[1]) or config['AGE']
    if address.strip("/") == "stop":
        stop = True
osc_in = OSCIn(6006, receive)   # sends on port 5005 / receives on port 6006
osc_in.log_osc = True


if TEST_MODE:
    tree = Tree(config, sonifier.callback)
    try:
        visualizer.start(tree)
    except KeyboardInterrupt:
        tree.stop()
        sonifier.reset_synth()
        time.sleep(.25)
else:
    while True:
        if start:
            print(f"Starting with {config['YEAR_TIME']}s per year until age {config['AGE']}...")
            sonifier.reset_synth()
            time.sleep(.25)
            tree = Tree(config, sonifier.callback)
            start = False
        if stop:
            print("Stopping...")
            tree.stop()
            sonifier.reset_synth()
            time.sleep(.25)
            stop = False
        if tree is not None and tree.running and tree.age > config['AGE']:
            stop = True
        time.sleep(1/8)
