import time, threading, math
from random import random, randint, choice


class Leaf():

    number = 0

    def __init__(self, tree, limb):
        self.id = Leaf.number
        Leaf.number += 1
        self.tree = tree
        self.limb = limb
        self.tree.leaves.append(self)

    @property
    def position(self):
        return self.limb.end

    def move(self, limb):
        self.limb = limb
        return self


class Limb():

    number = 0

    def __init__(self, tree, parent=None, rotation=0, pitch=-90, leaf=None):
        self.id = Limb.number
        Limb.number += 1
        self.tree = tree            # ref to tree object
        self.parent = parent        # ref to parent limb
        self.children = []          # ref to children limbs
        self.leaf = Leaf(tree, self) if not leaf else leaf.move(self) # ref to leaf
        self.start = self.parent.end if self.parent else (0, 0, 0)    # coords of start point
        self.end = self.start       # coords of end point
        self.length = 0             # length of limb

        self.rotation = rotation    # rotation around y axis (y is up)
        self.pitch = pitch          # angle above horiztonal

        self.load = 0               # number of leaves supported by this limb or its children
        self.depth = 0
        parent = self.parent
        while parent is not None:
            self.depth += 1
            parent = parent.parent
        self.tree.limbs.append(self)

    def grow(self, day):
        self.start = self.parent.end if self.parent else (0, 0, 0)
        if self.length < length_f(self.depth) + (random() * .1):
            self.length += growth_f(day)# + (random() * .1)
        self.end = get_point(self.start, self.rotation, self.pitch, self.length)
        for child in self.children:
            child.grow(day)
        if self.leaf and \
            len(self.tree.limbs) < Tree.MAX_LIMBS - 2 and \
            self.depth < Tree.MAX_DEPTH and \
            self.length >= Tree.LIMB_BRANCH_LENGTH:
            self.branch()


    ## TREE STRUCTURE IS DEFINED HERE ##
    def branch(self):
        self.children = []
        if self.leaf.id == 0:
            self.children.append(Limb(self.tree, self, randint(0, 360), self.pitch + randint(-10, 10), self.leaf)) # keep trunk relatively straight
            pitch = randint(60, 90)
            rotation = self.tree.core_rotation
            self.children.append(Limb(self.tree, self, rotation, self.pitch + pitch))
            rotation += randint(100, 140)
            rotation %= 360
            self.children.append(Limb(self.tree, self, rotation, self.pitch + pitch))
            rotation += randint(100, 140)
            rotation %= 360
            self.children.append(Limb(self.tree, self, rotation, self.pitch + pitch))
            rotation += randint(100, 140)
            rotation %= 360
            self.tree.core_rotation += rotation
        else:
            pitch = randint(-50, 20)
            self.children.append(Limb(self.tree, self, self.rotation + randint(10, 60), pitch, self.leaf if self.leaf.id != 0 else None))
            self.children.append(Limb(self.tree, self, self.rotation + randint(-60, -10), pitch))
        self.leaf = None



class Tree(threading.Thread):

    def __init__(self, config, callback=None):
        super(Tree, self).__init__()
        self.daemon = True
        for key, value in config.items():
            setattr(Tree, key, value)
        self.callback = callback
        self.running = True
        self.leaves = []
        self.limbs = []
        self.root = Limb(self)
        self.age = 0                    # age of tree in years
        self.core_rotation = randint(0, 360)
        self.start()

    def run(self):
        start_t = time.perf_counter()
        day = 0
        while self.running:
            day += 1
            day_of_year = day % 365
            self.update(day_of_year)
            self.age = day // 365
            if day_of_year == 1:
                print(f"tree is {self.age} years old")
            time.sleep(Tree.YEAR_TIME / 365)
            stop_t = time.perf_counter()
            elapsed = stop_t - start_t
            delta = abs(elapsed - (Tree.YEAR_TIME / 365))
            if delta > 1/60:
                print(f"whoops, perceptible latency in tree: {int(delta * 1000)}ms")
            start_t = stop_t

    def stop(self):
        self.running = False

    def update(self, day):

        # grow the tree
        self.root.grow(day)

        # calculate leaf load
        for limb in self.limbs:
            limb.load = 0
        for leaf in self.leaves:
            limb = leaf.limb
            while limb:
                limb.load += 1
                limb = limb.parent

        # call sonification function
        if self.callback:
            self.callback(self, day)

    @property
    def depth(self):
        depth = 0
        parent = self.leaves[0].limb
        while parent is not None:
            depth += 1
            parent = parent.parent
        return depth

    @property
    def length(self):
        limb = self.leaves[0].limb
        length = limb.length
        while limb.parent is not None:
            limb = limb.parent
            length += limb.length
        return length if length > 0 else 0.001


golden = (1 + 5**0.5) / 2
def length_f(depth):
    depth /= 4
    return Tree.MAX_ROOT_LENGTH / golden**depth

def growth_f(day):
    if day >= 50 and day < 250: # 200 days
        return Tree.GROWTH_PER_YEAR / 200
    else:
        return 0

def get_point(start_point, rotation, pitch, length):
    x, y, z = start_point
    rotation, pitch = math.radians(rotation), math.radians(pitch)
    x += length * math.cos(pitch) * math.cos(rotation)
    y += length * math.sin(pitch)
    z += length * math.cos(pitch) * math.sin(-rotation)
    return x, y, z
