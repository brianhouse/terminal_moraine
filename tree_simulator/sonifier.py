import time, threading, queue
from util import rescale, clip
from random import random, choice, randint
from util.osc import OSCOut
from tree import Tree

osc_out = OSCOut(5005)
osc_out.log_osc = False


harmonies = [1/2, 1, 4/3, 2, 2+2/3], [16, 4/3 * 2**4, 2/3 * 2**4]  # limbs, leaf
gain_adj = [1, .7, .5, 1/4, 1/5], 1/32      # limbs, leaf


def update_params(tree, day):
    if day == 5:
        print("summer: ", "depth_i", tree.depth, "length", tree.length, "limbs", len(tree.limbs), "leaves", len(tree.leaves))
        global n_limbs
        n_limbs = len(tree.limbs)
        for limb in tree.limbs:

            d = tree.depth - limb.depth
            if limb.leaf:
                rate = choice(harmonies[1])
            else:
                rate = harmonies[0][-d]
            rates[limb.id] = rate

            l = limb
            length = limb.length
            while l.parent is not None:
                l = l.parent
                length += l.length
            length -= tree.root.length
            progress = tree.depth / Tree.MAX_DEPTH
            delay = (Tree.YEAR_TIME/3) * progress * (length / (tree.length - tree.root.length))
            delay += random() * choice([.2, -.2])   # give some wiggle for equal length branches

            def s(id, g):
                def f():
                    gains[id] = g
                return f
            g = gain_adj[0][-d] if not limb.leaf else gain_adj[1]
            scheduler.add(s(limb.id, g), delay)

            print(f"{limb.id+1} depth {limb.depth} length {length:.2f} delay {delay:.2f} phase {phases[limb.id]:.2f} rate {rates[limb.id]:.3f} gain {g:.3f} leaf {limb.leaf is not None}")


    elif day == 250:
        print("winter")
        print("")
        print("")
        for limb in tree.limbs:
            def s(id):
                def f():
                    gains[id] = 0
                return f
            scheduler.add(s(limb.id), random() * 4)


def sonify(tree, day):
    global n_limbs
    update_params(tree, day)

    # move tree
    for l, limb in enumerate(tree.limbs):

        # account for emerging leaves
        if day > 5 and day < 250:
            if l >= n_limbs:
                print("...new leaf sprouted")
                rates[limb.id] = choice(harmonies[1])
                gains[limb.id] = gain_adj[1]
                n_limbs += 1

        rate = rates[limb.id]

        # distribute and interleave the phasing
        siblings = [id for (id, r) in enumerate(rates) if r == rate]
        index = siblings.index(limb.id)
        phase = index * (1 / len(siblings)) * .5
        phase = .5 - phase if index % 2 else phase
        phases[limb.id] = phase

        # set gain
        gain = gains[limb.id]

        # y is up internally; swapping with z here
        pos_x = clip(rescale(limb.end[0], -250, 250, -1, 1), -1, 1)
        pos_y = clip(rescale(limb.end[2], -250, 250, 1, -1), -1, 1)
        pos_z = clip(rescale(limb.end[1], -250, 250, 1, -1), -1, 1)
        pos_z = 0   # dropping

        # shift ids to 1-index
        osc_out.send("limb/", [limb.id+1, rate, phase, gain, pos_x, pos_y, pos_z])


class Scheduler(threading.Thread):

    def __init__(self):
        super(Scheduler, self).__init__()
        self.daemon = True
        self.queue = queue.Queue()

    def add(self, f, delay):
        self.queue.put([time.perf_counter() + delay, f])

    def run(self):
        while True:
            remaining_tasks = []
            try:
                while True:
                    task = self.queue.get_nowait()
                    if task[0] <= time.perf_counter():
                        task[1]()
                    else:
                        remaining_tasks.append(task)
            except queue.Empty:
                pass
            for task in remaining_tasks:
                self.queue.put(task)
            time.sleep(1/60)

    def clear(self):
        try:
            while True:
                self.queue.get_nowait()
        except queue.Empty:
            pass

# placeholders
gains = [0] * 500
rates = [0] * 500
phases = [0] * 500
n_limbs = 0

# reset synthesizer
def reset_synth():
    for l in range(500):
        osc_out.send("limb/", [l+1, 0, 0, 0, 0, 0, 0])
reset_synth()

# set up sonification callbacks
scheduler = Scheduler()
scheduler.start()
def callback(tree, day):
    def f():
        sonify(tree, day)
    scheduler.add(f, 0)
