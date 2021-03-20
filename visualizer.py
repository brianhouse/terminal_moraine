from util.animation import Context

ctx = Context(1200, 600, "GROWTH")

def draw_side(limb):
    size = limb.load
    x1, y1 = limb.start[:2]
    x2, y2 = limb.end[:2]
    y1 += 300
    y2 += 300
    ctx.line(x1, y1, x2, y2, min(size / 2, 20), (50, 0, 0))
    ctx.circle(x2, y2, min(size / 4, 10), (50, 0, 0))
    for child in limb.children:
        draw_side(child)
    if limb.leaf:
        x, y = limb.leaf.position[:2]
        y += 300
        ctx.circle(x, y, 5 * limb.leaf.maturity, (0, 150, 20))

def draw_top(limb):
    size = limb.load
    x1, y1 = limb.start[::2]
    x2, y2 = limb.end[::2]
    x1 += 600
    x2 += 600
    ctx.line(x1, y1, x2, y2, min(size / 2, 20), (50, 0, 0))
    ctx.circle(x2, y2, min(size / 4, 10), (50, 0, 0))
    for child in limb.children:
        draw_top(child)
    if limb.leaf:
        x, y = limb.leaf.position[::2]
        x += 600
        ctx.circle(x, y, 5 * limb.leaf.maturity, (0, 150, 20))

def start(tree):
    def loop():
        draw_top(tree.root)
        draw_side(tree.root)
    ctx.start(loop)


"""
x is left-right
y is up-down
z is out

angle is the amount of y along the x-axis; greater the distance from -90, the more the bend side to side
-> rotation around the z axis

zangle is the amount y along the y-axis; greater the distance from -90, the more the bend toward or away
-> rotation around the x axis

on the overhead view:
- using angle only, should see a line along the x-axis
- using zangle only, should see a line along the z-axis

"""
