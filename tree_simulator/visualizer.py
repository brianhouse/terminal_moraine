from util.animation import Context
from util import rescale, clip

ctx = Context(1200, 600, "GROWTH")

def draw_side(limb):
    size = limb.load
    x1, y1 = limb.start[:2]
    x2, y2 = limb.end[:2]
    x1 += 300
    x2 += 300
    y1 += 300 + 300
    y2 += 300 + 300
    if limb.leaf:
        x, y = limb.leaf.position[:2]
        x += 300
        y += 300 + 300
        ctx.circle(x, y, 5, (0, 150, 20))
    ctx.line(x1, y1, x2, y2, min(size / 2, 20), (50, 0, 0))
    ctx.circle(x2, y2, min(size / 4, 10), (50, 0, 0))
    for child in limb.children:
        draw_side(child)

def draw_top(limb):
    size = limb.load
    x1, y1 = limb.start[::2]
    x2, y2 = limb.end[::2]
    x1 += 300 + 600
    x2 += 300 + 600
    y1 += 300
    y2 += 300
    if limb.leaf:
        x, y = limb.leaf.position[::2]
        x += 300 + 600
        y += 300
        ctx.circle(x, y, 5, (0, 150, 20))
    ctx.line(x1, y1, x2, y2, min(size / 2, 20), (50, 0, 0))
    ctx.circle(x2, y2, min(size / 4, 10), (50, 0, 0))
    pan_x = clip(rescale(limb.end[0], -250, 250, -1, 1), -1, 1)
    pan_y = clip(rescale(limb.end[2], -250, 250, 1, -1), -1, 1)
    ctx.text(f"{pan_x:.2f} {pan_y:.2f}", x2, y2)
    for child in limb.children:
        draw_top(child)

def start(tree):
    def loop():
        ctx.line(650, 50, 1150, 50, 1, (100, 100, 100))
        ctx.line(650, 550, 1150, 550, 1, (100, 100, 100))
        ctx.line(650, 50, 650, 550, 1, (100, 100, 100))
        ctx.line(1150, 50, 1150, 550, 1, (100, 100, 100))
        draw_top(tree.root)
        draw_side(tree.root)
    ctx.start(loop)
