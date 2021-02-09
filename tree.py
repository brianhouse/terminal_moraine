import time, threading, math
from random import random, randint


class Leaf():

    number = 0

    def __init__(self, tree, limb):
        self.id = Leaf.number
        Leaf.number += 1
        self.tree = tree
        self.limb = limb
        self.intensity = 0
        self.tree.leaves.append(self)

    @property
    def position(self):
        return self.limb.end

    def move(self, limb):
        self.limb = limb
        return self


class Limb():

    number = 0

    def __init__(self, tree, parent=None, angle=-90, leaf=None):
        self.id = Limb.number
        Limb.number += 1
        self.tree = tree
        self.parent = parent
        self.children = []
        self.leaf = Leaf(tree, self) if not leaf else leaf.move(self)
        self.size = 0
        self.angle = angle
        self.start = self.parent.end if self.parent else Tree.ORIGIN
        self.end = self.start
        self.water = 0
        self.tree.limbs.append(self)

    def grow(self, day):
        if self.leaf:
            self.leaf.intensity = leaf_function(day, self.leaf.id)
        if self.tree.root.size < Tree.MAX_ROOT_SIZE:
            self.start = self.parent.end if self.parent else Tree.ORIGIN
            self.size += growth_function(day) * Tree.GROWTH_RATE
            self.end = get_point(self.start, self.angle, self.size)
            if  len(self.tree.leaves) < Tree.MAX_LEAVES and \
                len(self.tree.limbs) < Tree.MAX_LIMBS and \
                self.leaf and \
                self.size > Tree.BRANCH_MIN_SIZE and \
                random() > Tree.BRANCH_PROB:
                self.branch()
        for child in self.children:
            child.grow(day)


    ## TREE STRUCTURE IS DEFINED HERE ##
    def branch(self):
        if random() > 1/4:
            a = Limb(self.tree, self, self.angle + randint(-30, -20), self.leaf)
            b = Limb(self.tree, self, self.angle + randint(40, 50))
            self.children = [a, b]
        else:
            a = Limb(self.tree, self, self.angle + randint(-50, -40), self.leaf)
            self.children = [a]
        self.leaf = None



class Tree(threading.Thread):

    def __init__(self, config, callback=None):
        super(Tree, self).__init__()
        self.daemon = True
        for key, value in config.items():
            setattr(Tree, key, value)
        self.callback = callback
        self.leaves = []
        self.limbs = []
        self.root = Limb(self)
        self.start()

    def run(self):
        start_t = time.time()
        ticks = 0
        while True:
            self.update(int((ticks / Tree.TICKS_PER_YEAR) * 365))
            ticks = (ticks + 1) % Tree.TICKS_PER_YEAR
            time.sleep(Tree.TICK_DURATION)
            stop_t = time.time()
            elapsed = stop_t - start_t
            delta = abs(elapsed - Tree.TICK_DURATION)
            if delta > 1/60:
                print(f"whoops, perceptible latency: {int(delta * 1000)}ms")
            start_t = stop_t

    def update(self, day):

        # grow the tree
        self.root.grow(day)

        # calculate water distribution in all the limbs
        for limb in self.limbs:
            limb.water = 0
        for leaf in self.leaves:
            limb = leaf.limb
            while limb:
                limb.water += 1
                limb = limb.parent
        root_water = self.root.water
        for limb in self.limbs:
            limb.water /= root_water

        # call sonification function
        if self.callback:
            self.callback(self)


def growth_function(day):
    if day > 150 and day < 215:
        return 1
    elif day > 50 and day < 315:
        return 1/2
    else:
        return 0

def leaf_function(day, n):
    if n % 2:
        n = Tree.MAX_LEAVES - n
    if day < 50:
        return 0
    elif day > 315 + ((n / Tree.MAX_LEAVES) * 100):
        return 0
    else:
        return (day - 50) / 200

def get_point(start_point, angle, distance):
    x, y = start_point
    return x + (distance * math.cos(math.radians(angle))), y + (distance * math.sin(math.radians(angle)))
