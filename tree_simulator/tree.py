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

    def __init__(self, tree, parent=None, angle=-90, zangle=90, leaf=None):
        self.id = Limb.number
        Limb.number += 1
        self.tree = tree            # ref to tree object
        self.parent = parent        # ref to parent limb
        self.children = []          # ref to children limbs
        self.leaf = Leaf(tree, self) if not leaf else leaf.move(self) # ref to leaf
        self.start = self.parent.end if self.parent else (0, 0, 0)    # coords of start point
        self.end = self.start   # coords of end point
        self.length = 0             # length of limb
        self.angle = angle          # x-y angle of limb (y is up)
        self.zangle = zangle        # x-z angle of limb (z is out)
        self.load = 0   # number of leaves supported by this limb or its children
        self.depth = 0
        parent = self.parent
        while parent is not None:
            self.depth += 1
            parent = parent.parent
        self.growth_variance = random() * Tree.LIMB_GROWTH_VARIANCE
        self.tree.limbs.append(self)

    def grow(self, day):
        # if self.tree.root.length >= Tree.MAX_ROOT_LENGTH:
        #     return
        self.start = self.parent.end if self.parent else (0, 0, 0)
        if self.length < length_f(self.depth):
            self.length += (growth_f(day) + self.growth_variance) * Tree.LIMB_GROWTH_AMOUNT
        self.end = get_point(self.start, self.angle, self.zangle, self.length)
         # ... note that it might create more than 1
        for child in self.children:
            child.grow(day)
        if self.leaf and \
            len(self.tree.leaves) < Tree.MAX_LEAVES and \
            len(self.tree.limbs) < Tree.MAX_LIMBS and \
            self.length >= Tree.LIMB_BRANCH_LENGTH:
            self.branch()


    ## TREE STRUCTURE IS DEFINED HERE ##
    def branch(self):
        self.children = []
        if self.leaf.id == 0:
            self.children.append(Limb(self.tree, self, self.angle + randint(-20, 20), self.zangle + randint(-10, 10), self.leaf)) # keep trunk relatively straight

        axis = randint(-10, 10)
        spread = randint(10, 100)
        angle_1 = axis - spread/2
        angle_2 = axis + spread/2

        zaxis = randint(-10, 10)
        zspread = randint(10, 100)
        zangle_1 = zaxis - zspread/2
        zangle_2 = zaxis + zspread/2

        self.children.append(Limb(self.tree, self, self.angle + angle_1, self.zangle + zangle_1, self.leaf if self.leaf.id != 0 else None))
        self.children.append(Limb(self.tree, self, self.angle + angle_2, self.zangle + zangle_2))
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
            time.sleep(Tree.DAY)
            stop_t = time.perf_counter()
            elapsed = stop_t - start_t
            delta = abs(elapsed - Tree.DAY)
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


golden = (1 + 5**0.5) / 2
def length_f(depth):
    depth /= 2
    return Tree.MAX_ROOT_LENGTH / golden**depth

def growth_f(day):
    if day > 150 and day < 215:
        return 7/8
    elif day > 50 and day < 315:
        return 1/8
    else:
        return 0

def get_point(start_point, angle, zangle, length):
    x, y, z = start_point
    angle, zangle = math.radians(angle), math.radians(zangle)
    x += length * math.sin(zangle) * math.cos(angle)
    y += length * math.sin(zangle) * math.sin(angle)
    z += length * math.cos(zangle)
    return x, y, z
